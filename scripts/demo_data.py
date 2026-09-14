"""Datos ficticios para las copias publicas del tracker y del tablero.

Todas las empresas llevan "(demo)" en el nombre y ninguna existe. Las fechas no se
guardan como fechas: el tracker recibe dias relativos a hoy y el tablero semanas
relativas a una semana ancla, y el JavaScript de cada pagina las convierte al abrirla,
asi la demo nunca se ve vieja.
"""
from datetime import date, timedelta

# ---------------------------------------------------------------- tracker
_JOB = dict(appliedDate="", category="", company="", companyType="", coverLetter="", createdAt=0, cvVersion="",
            deadline="", fitScore=0, folderPath="", gaps=[], id="", interviewDate="", interviews=[],
            jobDescription="", jobId="", keywords=[], links="", location="", myMatch=[], posted=0, priority="MEDIUM",
            rejectedDate="", replyDate="", requirements=[], responsibilities=[], role="", status="todo",
            strategicNotes="Registro de demostración con datos ficticios.")

_ROWS = [
    # company, role, category, type, location, status, priority, fit, posted, applied, reply, rejected, interviews
    ("Acme Pharma (demo)", "Medical Science Liaison", "Medical Affairs / Medical Science Liaison", "Pharmaceutical",
     "Santiago, Chile", "interview", "HIGH", 8.6, -34, -30, -21, "", [(1, -14, "Llamada inicial", "Conversación de 30 minutos con talento (ejemplo)."),
                                                                  (2, 3, "Videollamada", "Entrevista con la gerencia médica (ejemplo).")]),
    ("Contoso Salud (demo)", "Medical Advisor", "Medical Affairs", "Pharmaceutical", "Santiago, Chile",
     "applied", "HIGH", 8.1, -12, -10, "", "", []),
    ("Globex Biotech (demo)", "Clinical Research Associate", "Clinical Trial Management", "CRO / Clinical Research",
     "Remoto · LatAm", "offer", "HIGH", 8.9, -60, -55, -48, "", [(1, -40, "Llamada inicial", "Filtro de idioma (ejemplo)."),
                                                              (2, -31, "Videollamada", "Caso práctico de monitoreo (ejemplo)."),
                                                              (3, -20, "Presencial", "Panel final (ejemplo).")]),
    ("Initech Diagnósticos (demo)", "Field Application Specialist", "Clinical Applications / Medical Devices",
     "Diagnostics", "Santiago, Chile", "rejected", "MEDIUM", 6.4, -70, -66, -45, -45, []),
    ("Laboratorio Ejemplo (demo)", "Regulatory Affairs Analyst", "Regulatory Affairs", "Pharmaceutical",
     "Santiago, Chile", "applied", "MEDIUM", 7.2, -25, -22, "", "", []),
    ("BioDemo Andes (demo)", "Study Start-Up Specialist", "Regulatory Affairs", "CRO", "Lima, Perú",
     "interview", "MEDIUM", 7.7, -28, -24, -15, "", [(1, -9, "Video asíncrono", "Tres preguntas grabadas (ejemplo).")]),
    ("Farmacéutica Ficticia (demo)", "Medical Information Specialist", "Medical Affairs", "Pharmaceutical",
     "Bogotá, Colombia", "rejected", "LOW", 5.8, -90, -85, "", -52, []),
    ("Umbra CRO (demo)", "Clinical Trial Coordinator", "Clinical Trial Management", "CRO", "Santiago, Chile",
     "applied", "MEDIUM", 7.0, -8, -6, "", "", []),
    ("Ejemplo MedTech (demo)", "Medical Education Manager", "Medical Affairs", "Medical Devices",
     "Ciudad de México, México", "todo", "HIGH", 8.3, -3, "", "", "", []),
    ("Northwind Health (demo)", "Scientific Communications Associate", "Medical Affairs", "Communications agency",
     "Remoto · LatAm", "todo", "MEDIUM", 7.4, -2, "", "", "", []),
    ("Demo Genomics (demo)", "Clinical Data Analyst", "Clinical Trial Management", "Biotechnology",
     "Santiago, Chile", "withdrawn", "LOW", 6.1, -45, -41, "", "", []),
    ("Vértice Pharma (demo)", "Site Activation Specialist", "Regulatory Affairs", "CRO / Clinical Research",
     "Santiago, Chile", "todo", "MEDIUM", 7.1, -1, "", "", "", []),
]


def tracker_jobs():
    """Registros con fechas como enteros (dias desde hoy) o "" si no aplica."""
    jobs = []
    for n, (company, role, category, ctype, loc, status, prio, fit, posted, applied, reply, rejected, ivs) in enumerate(_ROWS, 1):
        j = dict(_JOB)
        j.update(id=f"DEMO_{n:02d}", jobId=f"DEMO-{n:03d}", company=company, role=role, category=category,
                 companyType=ctype, location=loc, status=status, priority=prio, fitScore=fit, posted=posted,
                 createdAt=posted if applied == "" else applied, appliedDate=applied, replyDate=reply,
                 rejectedDate=rejected, deadline=posted + 30,
                 interviews=[dict(round=r, date=d, type=t, notes=x) for r, d, t, x in ivs],
                 interviewDate=(ivs[-1][1] if ivs else ""),
                 links=f"https://example.com/empleos/demo-{n:02d}", cvVersion="CV_demo.pdf",
                 jobDescription=f"Aviso ficticio de {role} para mostrar el tracker. La empresa no existe.",
                 requirements=["Requisito de ejemplo 1", "Requisito de ejemplo 2"],
                 responsibilities=["Responsabilidad de ejemplo"], keywords=["demo", "ejemplo"],
                 myMatch=["Coincidencia de ejemplo"], gaps=(["Brecha de ejemplo"] if fit < 7 else []))
        jobs.append(j)
    return jobs


TRACKER_JS = r"""
// DEMO: las fechas vienen como dias relativos a hoy
function demoJobs(){
  const hoy=new Date();
  const iso=o=>{if(o===''||o==null)return'';const d=new Date(hoy.getFullYear(),hoy.getMonth(),hoy.getDate()+o);return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');};
  const F=['appliedDate','createdAt','deadline','interviewDate','posted','rejectedDate','replyDate'];
  return DEMO_JOBS.map(j=>{const c=JSON.parse(JSON.stringify(j));F.forEach(k=>c[k]=iso(c[k]));c.interviews=c.interviews.map(v=>({...v,date:iso(v.date)}));return c;});
}
"""

TRACKER_BANNER = ('<div class="demo-banner" id="demoBanner"><strong>DEMO</strong><span>Datos ficticios: las empresas '
                  'marcadas "(demo)" no existen. Lo que agregues se guarda solo en tu navegador.</span>'
                  '<button type="button" class="btn btn-ghost" onclick="clearDemoJobs()">Borrar datos de demo</button></div>\n')

TRACKER_BANNER_CSS = (".demo-banner{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:14px 0 0;padding:10px 14px;"
                      "border-radius:12px;border:1px solid rgba(251,191,36,.35);background:rgba(251,191,36,.10);color:#fde68a;font-size:.8rem}"
                      ".demo-banner strong{letter-spacing:.12em;color:#fbbf24}.demo-banner span{flex:1;min-width:220px}"
                      ".demo-banner.off{display:none!important}")

TRACKER_TAIL = r"""<script>
function updateDemoBanner(){const b=document.getElementById('demoBanner');if(b)b.classList.toggle('off',!S.jobs.some(j=>String(j.id).startsWith('DEMO_')));}
function clearDemoJobs(){S.jobs=S.jobs.filter(j=>!String(j.id).startsWith('DEMO_'));save();renderAll();}
const _renderAllDemo=renderAll;renderAll=function(){_renderAllDemo();updateDemoBanner();};
updateDemoBanner();
</script>
"""


# ---------------------------------------------------------------- tablero
ANCHOR = date(2026, 1, 5)          # lunes de la semana 0
CURRENT_WEEK = 8                   # la semana que el visitante ve como "esta semana"
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]

PLAN = {
    0: ("Tren inferior A", [("Sentadilla (barra)", 60, 8), ("Peso muerto rumano (barra)", 50, 10),
                            ("Prensa de piernas", 110, 12), ("Curl femoral sentado", 35, 12)]),
    1: ("Tren superior A", [("Press banca (barra)", 50, 8), ("Remo con barra", 45, 10),
                            ("Press militar (mancuernas)", 14, 10), ("Jalón al pecho", 45, 12)]),
    3: ("Tren inferior B", [("Hip thrust (barra)", 70, 10), ("Sentadilla búlgara", 12, 10),
                            ("Extensión de cuádriceps", 35, 12), ("Crunch en polea", 25, 15)]),
    5: ("Tren superior B", [("Press inclinado (mancuernas)", 18, 10), ("Remo sentado en polea", 45, 12),
                            ("Elevación lateral (mancuernas)", 7, 15), ("Curl bíceps (mancuernas)", 10, 12)]),
}
WARMUP = [dict(name="Bicicleta 5 minutos, ritmo conversable", how="Solo para subir la temperatura. Debes poder hablar frases completas."),
          dict(name="Movilidad de cadera y tobillo", how="Dos vueltas de 8 repeticiones lentas por lado."),
          dict(name="Serie de aproximación", how="El primer ejercicio con la mitad de la carga, 8 repeticiones.")]
STRETCH = [dict(name="Estiramiento de isquiotibiales", how="30 segundos por lado, sin rebotes."),
           dict(name="Estiramiento de pecho en marco de puerta", how="30 segundos, respiración lenta."),
           dict(name="Postura del niño", how="45 segundos, relajando la espalda baja.")]
MUSCLES = [("Cuádriceps", 12, 10, 16), ("Femoral", 5, 6, 10), ("Glúteo / cadera", 9, 8, 14), ("Espalda", 13, 10, 18),
           ("Pecho", 8, 8, 14), ("Hombro (empuje)", 6, 6, 12), ("Bíceps", 4, 6, 10), ("Tríceps", 3, 6, 10),
           ("Aductor / abductor", 2, 4, 8), ("Core", 7, 6, 12)]


def _load(base, week):
    # progresion simple de 2,5% por semana con una semana plana cada cuatro
    steps = week - week // 4
    v = base * (1.025 ** steps)
    return round(v * 2) / 2 if base >= 20 else round(v)


def _d(week, day):
    return ANCHOR + timedelta(days=7 * week + day)


def dashboard_profile():
    sessions = []
    for week in range(CURRENT_WEEK):
        for day, (focus, exs) in PLAN.items():
            d = _d(week, day)
            rows = []
            for name, base, reps in exs:
                w = _load(base, week)
                for s in range(3):
                    rows.append(dict(ej=name, carga=f"{w:g}", reps=str(reps), rpe=str(7 + s)))
            vol = sum(float(r["carga"]) * int(r["reps"]) for r in rows)
            sessions.append(dict(date=d.isoformat(), dlabel=f"{d.day:02d} {MESES[d.month - 1]}", title=f"{focus} (demo)",
                                 hora="19:00", dur="1h 05m", vol=f"{vol:,.0f}".replace(",", "."), com=None, rec=None,
                                 exercises=rows))
    sessions.reverse()

    weekdays = []
    for week in (CURRENT_WEEK, CURRENT_WEEK + 1):
        for day in range(7):
            d = _d(week, day)
            base = dict(date=d.isoformat(), day=f"{DIAS[day]} {d.day}")
            if day in PLAN:
                focus, exs = PLAN[day]
                exercises = []
                for name, b, reps in exs:
                    w = _load(b, week)
                    exercises.append(dict(name=name, sets=[dict(serie=str(i + 1), carga=f"{w:g} kg", reps=str(reps), rir="2",
                                                                descanso="2 min") for i in range(3)],
                                          cue="**Demo:** indicación de técnica de ejemplo. Controla la bajada y mantén el RIR indicado."))
                base.update(tag="entreno", focus=focus, cardio="Caminata 15 minutos en pendiente suave.",
                            rationale="Sesión de **ejemplo** generada con datos ficticios para mostrar cómo se ve el plan.",
                            warmup=WARMUP, stretch=STRETCH, exercises=exercises)
            else:
                base.update(tag="descanso", focus="Descanso", cardio="", warmup=[], stretch=[], exercises=[],
                            rationale="Día libre en la rutina de demostración.")
            weekdays.append(base)

    charts = []
    for day, (focus, exs) in PLAN.items():
        for name, b, reps in exs[:2]:
            data = [dict(iso=_d(w, day).isoformat(), d="", w=float(_load(b, w))) for w in range(CURRENT_WEEK)]
            ws = [p["w"] for p in data]
            charts.append(dict(name=name, data=data, pattern="ascendente_claro", lo=min(ws), hi=max(ws),
                               change="Ejemplo: seguir subiendo en pasos pequeños mientras el RIR se mantenga en 2.",
                               rationale="Serie ficticia con progresión lineal de 2,5% semanal y una semana plana cada cuatro."))

    muscles = []
    for name, recent, lo, hi in MUSCLES:
        tier = "critical" if recent < lo * 0.6 else ("warning" if recent < lo else "good")
        muscles.append(dict(name=name, recent=float(recent), hist=float(recent) - 0.5, lo=lo, hi=hi, tier=tier,
                            trend=0.5 if tier == "good" else -1.0, note="Valor de demostración.",
                            ex="Ejercicios del plan de ejemplo"))

    return {"demo": dict(
        displayName="Atleta demo", bodyType="male", hasData=True,
        chips=[dict(k="Demo", v="datos ficticios"), dict(k="Nivel", v="intermedio"), dict(k="Frecuencia", v="4 días")],
        MUSCLES=muscles, WEEKDAYS=weekdays, CHARTS=charts, SESSIONS_FULL=sessions,
        cycle=dict(badge="Semana 3 de 4 · demo", detail="Mesociclo ficticio de 4 semanas con descarga en la cuarta.",
                   meso=dict(semana=3, total=4, deload=4, inicio=_d(CURRENT_WEEK - 2, 0).isoformat(),
                             nota="Datos de **demostración**: nada de esto corresponde a una persona real.")),
        fuente="demo (datos ficticios)",
        weekNote="**Demo con datos ficticios.** Carga tu profiles.json para ver los tuyos.",
        weekTodo="")}


DASHBOARD_SHIFT_JS = r"""
  // DEMO: mueve las fechas de la demo para que "esta semana" sea la semana actual
  function moverDemo(p){
    var DIAS=['Dom','Lun','Mar','Mié','Jue','Vie','Sáb'], MESES=['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
    var hoy=new Date(); hoy.setHours(12,0,0,0);
    var lunes=new Date(hoy); lunes.setDate(hoy.getDate()-((hoy.getDay()+6)%7));
    var ancla=new Date('__DEMO_MONDAY__T12:00:00');
    var delta=Math.round((lunes-ancla)/86400000);
    function mover(iso){ var d=new Date(iso+'T12:00:00'); d.setDate(d.getDate()+delta); return d; }
    function fmt(d){ return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'); }
    Object.keys(p).forEach(function(k){
      var x=p[k];
      x.WEEKDAYS.forEach(function(w){ var d=mover(w.date); w.date=fmt(d); w.day=DIAS[d.getDay()]+' '+d.getDate(); });
      x.SESSIONS_FULL.forEach(function(s){ var d=mover(s.date); s.date=fmt(d); s.dlabel=String(d.getDate()).padStart(2,'0')+' '+MESES[d.getMonth()]; });
      x.CHARTS.forEach(function(c){ c.data.forEach(function(pt){ var d=mover(pt.iso); pt.d=String(d.getDate()).padStart(2,'0')+' '+MESES[d.getMonth()]; }); });
      if(x.cycle && x.cycle.meso && x.cycle.meso.inicio) x.cycle.meso.inicio=fmt(mover(x.cycle.meso.inicio));
    });
    return p;
  }
"""


def demo_monday():
    return (ANCHOR + timedelta(days=7 * CURRENT_WEEK)).isoformat()
