#!/usr/bin/env python3
"""Genera las versiones publicas, sin datos, del tracker de postulaciones y del tablero
de entrenamiento, dentro de docs/ para GitHub Pages.

    python3 scripts/build_public_tools.py \
        --tracker ~/Documents/Career/job-tracker-repo \
        --dashboard /ruta/a/entrenamiento-dashboard   # si se omite, se clona de GitHub

Los datos personales nunca se copian: se vacian los bloques de datos, se borra el DOM
pre-renderizado que el tracker guarda dentro de si mismo, se quitan las integraciones
privadas (relay, sync movil, rutas locales) y al final se busca en la salida cualquier
nombre de empresa, ruta o secreto que venga de los datos de origen. Si algo aparece,
el script falla y no escribe nada.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import demo_data

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")


def fail(msg):
    raise SystemExit("ERROR: " + msg)


def literal_end(s, start):
    """Indice justo despues del literal JS ([...] o {...}) que empieza en s[start]."""
    open_ch = s[start]
    assert open_ch in "[{", s[start:start + 20]
    depth, i, n = 0, start, len(s)
    while i < n:
        c = s[i]
        if c in "\"'`":
            q = c
            i += 1
            while i < n and s[i] != q:
                i += 2 if s[i] == "\\" else 1
        elif c in "[{":
            depth += 1
        elif c in "]}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    fail("literal sin cerrar")


def const_span(s, name):
    m = re.search(r"\bconst\s+" + name + r"\s*=\s*", s)
    if not m:
        fail("no encontre const " + name)
    j = m.end()
    if s[j] in "[{":
        return m.start(), j, literal_end(s, j)
    k = s.index(";", j)
    return m.start(), j, k


def blank(v):
    if isinstance(v, dict):
        return {k: blank(x) for k, x in v.items()}
    if isinstance(v, list):
        return []
    if isinstance(v, bool):
        return False
    if isinstance(v, (int, float)):
        return 0
    if isinstance(v, str):
        return ""
    return v


def empty_element(s, el_id):
    """Vacia el contenido del elemento con ese id, respetando anidamiento del mismo tag."""
    m = re.search(r'<([a-zA-Z0-9]+)\b[^>]*\bid="' + re.escape(el_id) + r'"[^>]*>', s)
    if not m:
        return s, False
    tag, inner_start = m.group(1).lower(), m.end()
    if tag in ("input", "img", "br", "meta", "link"):
        return s, False
    pat = re.compile(r"<(/?)" + tag + r"\b[^>]*>", re.I)
    depth = 1
    for t in pat.finditer(s, inner_start):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return s[:inner_start] + s[t.start():], True
    fail("sin cierre para #" + el_id)


def leak_terms_from_tracker(src):
    terms = set()
    for name in ("SAVED_DATA", "MARKET_HISTORY", "DISCARDED_POSTINGS", "NEW_JOB_RECOMMENDATIONS",
                 "ADJACENT_OPPORTUNITIES", "MAIL_SIGNALS", "LINKEDIN_MAIL_SIGNALS"):
        _, a, b = const_span(src, name)
        try:
            rows = json.loads(src[a:b])
        except json.JSONDecodeError:
            continue
        for r in rows:
            for key in ("company", "jobId", "folderPath", "cvVersion", "coverLetter"):
                v = r.get(key) if isinstance(r, dict) else None
                if isinstance(v, str) and len(v.strip()) >= 5:
                    terms.add(v.strip())
    _, a, b = const_span(src, "MOBILE_SYNC_SECRET")
    secret = src[a:b].strip().strip("'\"")
    if secret:
        terms.add(secret)
    return terms


# ---------------------------------------------------------------- tracker
TRACKER_ARRAYS = ["MARKET_HISTORY", "MAIL_SIGNALS", "NEW_JOB_RECOMMENDATIONS", "ADJACENT_OPPORTUNITIES",
                  "REVIEWED_SOURCES", "FAILED_SOURCES", "LINKEDIN_SAVED_SEARCHES", "LINKEDIN_MAIL_SIGNALS"]
TRACKER_CONTAINERS = [
    "navMoreLive", "homeAlertStrip", "homeMetrics", "homePriorityList", "homePipeline", "sankeyTotal",
    "sankeyTiming", "jobs3AutomationFeedGrid", "statCards", "pipeBar", "pipeLeg", "secStats", "timGrid",
    "staleSub", "staleList", "cFLeg", "cSLeg", "tBody", "historyCount", "historyList", "highFitAlert",
    "weeklyFitList", "internationalList", "swipeStack", "newFilterResult", "newJobsList", "calendarGrid",
    "calendarAgenda", "interestJobsList", "radarSummary", "companyRadarList", "failedSourcesList",
    "linkedinDiscoveryPanel", "savedSearchesList", "linkedinMailSignalsList", "reviewedSourcesList",
    "mailList", "aiAreaLive", "aiArea", "aiArea2", "aiMetaLive", "aiMeta", "aiMeta2", "ivList", "ppBody",
    "sourceReviewAnalysis", "jobs3ChatMessages", "mailAuditLine", "mailRelevantTotal", "mailNewTotal",
    "mailConfirmedTotal", "mailActionTotal",
]
# selects cuyas opciones salen de los datos: se deja solo la opcion "todas"
TRACKER_SELECTS = ["fCompany", "newCompany"]
# palabras de la interfaz que tambien aparecen como valor en algun registro
GENERIC_WORDS = {"LinkedIn", "empresa"}


def build_tracker(repo):
    src_path = os.path.join(repo, "francisco-job-tracker-2026.html")
    src = open(src_path, encoding="utf-8").read()
    leaks = leak_terms_from_tracker(src)
    s = src

    s = re.sub(r"// TRACKER_DATA_START[\s\S]*?// TRACKER_DATA_END",
               "// TRACKER_DATA_START\nconst SAVED_DATA = [];\n// TRACKER_DATA_END\n"
               + "const DEMO_JOBS = " + json.dumps(demo_data.tracker_jobs(), ensure_ascii=False).replace("\\", "\\\\")
               + ";" + demo_data.TRACKER_JS.replace("\\", "\\\\"), s, count=1)
    s = re.sub(r"// DISCARDED_START[\s\S]*?// DISCARDED_END",
               "// DISCARDED_START\nconst DISCARDED_POSTINGS = [];\n// DISCARDED_END", s, count=1)
    s = re.sub(r"// LAST_LOCAL_SYNC_START[\s\S]*?// LAST_LOCAL_SYNC_END",
               '// LAST_LOCAL_SYNC_START\nconst LAST_LOCAL_SYNC_AT = "";\n// LAST_LOCAL_SYNC_END', s, count=1)
    for name in TRACKER_ARRAYS:
        _, a, b = const_span(s, name)
        s = s[:a] + "[]" + s[b:]
    for name in ("CHILE_MONITOR_SUMMARY", "MAIL_AUDIT"):
        _, a, b = const_span(s, name)
        s = s[:a] + json.dumps(blank(json.loads(s[a:b])), ensure_ascii=False) + s[b:]
    for name in ("MOBILE_SYNC_URL", "MOBILE_SYNC_SECRET"):
        _, a, b = const_span(s, name)
        s = s[:a] + "''" + s[b:]

    # integraciones privadas y rutas locales
    s = re.sub(r"connect-src 'self'[^;]*;", "connect-src 'self';", s, count=1)
    m = re.search(r"function cvEvidenceFor\(j\)\{", s)
    s = s[:m.end()] + "return '';" + s[literal_end(s, m.end() - 1) - 1:]
    replacements = {
        '"/Users/franciscokirhman/Documents/Career/Job Search Workflow/tools/tracker_context.py"': '"tools/tracker_context.py"',
        '"/Users/franciscokirhman/Documents/francisco-job-tracker-2026.html"': '"job-tracker.html"',
        "Hola Francisco.": "Hola.",
        "Buenos días Francisco.": "Buenos días.",
        "Da los buenos días a Francisco y resume": "Da los buenos días y resume",
        "'francisco-job-tracker-2026.html'": "'job-tracker.html'",
        "La búsqueda parte del Master CV": "La búsqueda parte de tu CV maestro",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)

    # DOM pre-renderizado guardado dentro del archivo
    for el_id in TRACKER_CONTAINERS:
        s, _ = empty_element(s, el_id)
    for el_id in TRACKER_SELECTS:
        m = re.search(r'(<select\b[^>]*\bid="' + el_id + r'"[^>]*>)(<option value="">[^<]*</option>)[\s\S]*?(</select>)', s)
        if not m:
            fail("no encontre el select #" + el_id)
        s = s[:m.start()] + m.group(1) + m.group(2) + m.group(3) + s[m.end():]
    s, n = re.subn(r'<div class="mail-summary">[\s\S]*?</div>\s*</div>',
                   '<div class="mail-summary">'
                   '<div class="mail-summary-card"><b>0</b><span>envíos confirmados</span></div>'
                   '<div class="mail-summary-card"><b>0</b><span>procesos por revisar</span></div>'
                   '<div class="mail-summary-card"><b>0</b><span>cambios de tracker autorizados</span></div>'
                   '</div>', s, count=1)
    if n != 1:
        fail("no encontre el resumen de correo")
    # el asistente depende de un servidor local que la copia publica no tiene
    s = s.replace("</style>", "#jobs3ChatLauncher,#jobs3ChatPanel{display:none!important}</style>", 1)
    bridge = "return fetch(JOBS3_CHAT_URL+path,{...options,headers,cache:'no-store'});"
    if s.count(bridge) != 1:
        fail("no encontre la llamada al servidor local del asistente")
    s = s.replace(bridge, "return Promise.reject(new Error('offline'));")
    s = s.replace('placeholder="e.g. Roche"', 'placeholder="e.g. Acme Pharma"')
    s = s.replace('placeholder="e.g. CL_Roche_MedicalLead.pdf"', 'placeholder="e.g. CL_Acme_MedicalLead.pdf"')

    # demo: sin datos propios ni borrador en el navegador, se cargan los registros ficticios
    for a, b in [("const embedded=parseStored(SAVED_DATA);",
                  "const embedded=parseStored(SAVED_DATA.length?SAVED_DATA:(localStorage.getItem(SK)===null?demoJobs():[]));"),
                 ('<div class="hdr">', demo_data.TRACKER_BANNER + '<div class="hdr">'),
                 ("</body></html>", demo_data.TRACKER_TAIL + "</body></html>")]:
        if s.count(a) != 1:
            fail(f"tracker demo: se esperaba 1 aparicion de {a[:50]!r}")
        s = s.replace(a, b)
    s = s.replace("</style>", demo_data.TRACKER_BANNER_CSS + "</style>", 1)

    out_dir = os.path.join(DOCS, "job-tracker")
    os.makedirs(os.path.join(out_dir, "tracker-assets"), exist_ok=True)
    # canonicalCompanyName normaliza grafias de empresas conocidas; es codigo, no un registro
    m = re.search(r"function canonicalCompanyName\(value\)\{", s)
    scan = s[:m.start()] + s[literal_end(s, m.end() - 1):]
    check_leaks("job-tracker", scan, (leaks - GENERIC_WORDS) | {"franciscokirhman", "Francisco", "Kirhman",
                                                               "franckirhman", "ug.uchile", "6218 2752", "Johnson"})
    open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(s)
    shutil.copyfile(os.path.join(repo, "tracker-assets", "chart.umd.js"),
                    os.path.join(out_dir, "tracker-assets", "chart.umd.js"))
    print(f"job-tracker: {len(src):,} -> {len(s):,} bytes, {len(leaks)} terminos verificados")


# ---------------------------------------------------------------- dashboard
LOADER_HTML = """
      <div class="cargador" id="cargador">
        <button type="button" class="temabtn" id="btnCargar">Cargar profiles.json</button>
        <button type="button" class="temabtn" id="btnBorrar" hidden>Quitar mis datos</button>
        <a class="cargador-ayuda" href="https://github.com/FranciscoKirhman/coding-portfolio/tree/main/docs/training-dashboard#formato" target="_blank" rel="noopener">Formato</a>
        <input type="file" id="archivoPerfiles" accept="application/json,.json" hidden>
      </div>"""

LOADER_JS = """
  // ---------------- datos del usuario (solo en este navegador) ----------------
  (function(){
    var input = document.getElementById('archivoPerfiles');
    var borrar = document.getElementById('btnBorrar');
    try{ if(localStorage.getItem(CLAVE_PERFILES)) borrar.hidden = false; }catch(e){}
    document.getElementById('btnCargar').addEventListener('click', function(){ input.click(); });
    input.addEventListener('change', function(){
      var f = input.files && input.files[0]; if(!f) return;
      var r = new FileReader();
      r.onload = function(){
        try{
          var data = JSON.parse(r.result);
          if(!data || typeof data !== 'object' || Array.isArray(data) || !Object.keys(data).length) throw new Error('vacio');
          localStorage.setItem(CLAVE_PERFILES, JSON.stringify(data));
          location.reload();
        }catch(e){ alert('No se pudo leer el archivo: tiene que ser un objeto JSON con al menos un perfil.'); }
      };
      r.readAsText(f);
    });
    borrar.addEventListener('click', function(){
      try{ localStorage.removeItem(CLAVE_PERFILES); }catch(e){}
      location.reload();
    });
  })();
"""

def build_dashboard(repo):
    src = os.path.join(repo, "src")
    tpl = open(os.path.join(src, "dashboard.template.html"), encoding="utf-8").read()
    fonts = {"OSWALD_600": "oswald-600", "OSWALD_700": "oswald-700", "PLEXSANS_400": "plexsans-400",
             "PLEXSANS_500": "plexsans-500", "PLEXSANS_600": "plexsans-600", "PLEXMONO_400": "plexmono-400",
             "PLEXMONO_500": "plexmono-500"}
    for key, slug in fonts.items():
        tpl = tpl.replace("{{" + key + "}}", open(os.path.join(src, "fonts", slug + ".b64")).read().strip())
    bodypaths = json.load(open(os.path.join(src, "bodypaths.json"), encoding="utf-8"))
    tpl = tpl.replace("__BODYPATHS_JSON__", json.dumps(bodypaths, ensure_ascii=False, separators=(",", ":")))

    profiles_js = ("(function(){ try{ var u = JSON.parse(localStorage.getItem(CLAVE_PERFILES) || 'null');"
                   " if(u && typeof u === 'object' && !Array.isArray(u) && Object.keys(u).length) return u; }catch(e){}"
                   " ES_DEMO = true; return moverDemo(" + json.dumps(demo_data.dashboard_profile(), ensure_ascii=False) + "); })()")
    edits = [
        ("var PROFILES = __PROFILES_JSON__;", "var CLAVE_PERFILES = 'tablero_perfiles_v1', ES_DEMO = false;"
         + demo_data.DASHBOARD_SHIFT_JS.replace("__DEMO_MONDAY__", demo_data.demo_monday())
         + "\n  var PROFILES = " + profiles_js + ";\n  if(!ES_DEMO){ var av = document.getElementById('demoAviso'); if(av) av.style.display = 'none'; }"),
        ('<p class="eyebrow">Coach adaptativo · basado en registro Hevy</p>',
         '<p class="demo-aviso" id="demoAviso"><b>DEMO</b> Datos ficticios de una persona que no existe. Carga tu profiles.json para ver los tuyos.</p>\n      '
         '<p class="eyebrow">Coach adaptativo · basado en registro Hevy</p>'),
        ("var BODY_GENERO = {mopo:'male', mipi:'female'};",
         "var BODY_GENERO = {}; Object.keys(PROFILES).forEach(function(k){ BODY_GENERO[k] = PROFILES[k].bodyType === 'female' ? 'female' : 'male'; });"),
        ("renderProfile('mopo');", "renderProfile(Object.keys(PROFILES)[0]);" + LOADER_JS),
        ("Pásame el registro y lo armo igual que el de Mopo", "Carga tu profiles.json con el botón de arriba"),
        (" va a aparecer acá, buscable igual que el de Mopo", " va a aparecer acá, buscable por fecha y ejercicio"),
        ("<link rel=\"manifest\" href=\"manifest.webmanifest\">\n", ""),
        ('<div class="profile-switch" id="profileSwitch"></div>',
         '<div class="profile-switch" id="profileSwitch"></div>' + LOADER_HTML),
        ("'Registro_historico_consolidado.md'", "'profiles.json'"),
    ]
    for a, b in edits:
        if tpl.count(a) != 1:
            fail(f"dashboard: se esperaba 1 aparicion de {a[:60]!r}, hay {tpl.count(a)}")
        tpl = tpl.replace(a, b)
    # sin version.json ni service worker: la copia publica no se instala como PWA
    tpl = re.sub(r"\n  // -{16} ¿estoy viendo una copia vieja\? -{16}[\s\S]*?\n  if\('serviceWorker' in navigator\)\{[\s\S]*?\n  \}\n",
                 "\n  var VERSION = 'publica';\n", tpl, count=1)
    tpl = tpl.replace("</style>", ".cargador{display:flex;gap:8px;align-items:center;flex-wrap:wrap}"
                                   ".cargador-ayuda{font-size:.8rem;color:inherit;opacity:.75}"
                                   ".demo-aviso{display:inline-flex;gap:.6rem;align-items:baseline;margin:0 0 .8rem;padding:.35rem .7rem;"
                                   "border:1px solid currentColor;border-radius:999px;font-size:.8rem;opacity:.9}"
                                   ".demo-aviso b{letter-spacing:.12em}</style>", 1)
    if "{{" in tpl or "__PROFILES_JSON__" in tpl or "__BODYPATHS_JSON__" in tpl or "serviceWorker" in tpl:
        fail("dashboard: quedaron marcadores o service worker")

    profiles = json.load(open(os.path.join(src, "profiles.json"), encoding="utf-8"))
    leaks = {"Mopo", "Mipi", "mopo", "mipi", "Paloma", "franciscokirhman"}
    for p in profiles.values():
        for ses in p.get("SESSIONS_FULL", [])[:400]:
            for k in ("com", "title"):
                v = ses.get(k)
                if isinstance(v, str) and len(v) >= 25:
                    leaks.add(v[:40])
        for k in ("weekNote", "weekTodo", "note"):
            if isinstance(p.get(k), str) and len(p[k]) >= 25:
                leaks.add(p[k][:40])
    out_dir = os.path.join(DOCS, "training-dashboard")
    os.makedirs(out_dir, exist_ok=True)
    check_leaks("training-dashboard", tpl, leaks)
    open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(tpl)
    print(f"training-dashboard: {len(tpl):,} bytes, {len(leaks)} terminos verificados")


def check_leaks(label, text, terms):
    found = [(t, text.count(t)) for t in sorted(terms) if t and t in text]
    if found:
        for t, n in found[:40]:
            i = text.find(t)
            print(f"  [{label}] {n}x {t[:50]!r}  ...{text[max(0, i - 80):i + 60]!r}")
        fail(f"{label}: {len(found)} terminos de los datos de origen siguen en la salida")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tracker", default=os.path.expanduser("~/Documents/Career/job-tracker-repo"))
    ap.add_argument("--dashboard", default=None)
    args = ap.parse_args()
    build_tracker(args.tracker)
    if args.dashboard:
        build_dashboard(args.dashboard)
    else:
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["git", "clone", "-q", "--depth", "1",
                            "https://github.com/FranciscoKirhman/entrenamiento-dashboard.git", tmp + "/d"], check=True)
            build_dashboard(tmp + "/d")


if __name__ == "__main__":
    main()
