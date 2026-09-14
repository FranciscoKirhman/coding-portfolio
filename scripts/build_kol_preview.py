#!/usr/bin/env python3
"""Genera docs/kol-preview.json: una vista anonimizada de la muestra publica de KOL Radar.

    python3 scripts/build_kol_preview.py [ruta_o_url_de_perfiles-muestra.json]

Guarda solo tipo de entidad, grado y posicion de las entidades mas conectadas, mas los
vinculos entre ellas y los totales de la muestra. Ningun nombre, ciudad ni identificador
sale de este script: los detalles viven en la herramienta.
"""
import json, math, os, random, sys, urllib.request
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = "https://franciscokirhman.github.io/kol-radar/data/sample/perfiles-muestra.json"
TOP = 150
TYPES = {"persona": "p", "institucion": "i", "ensayo_clinico": "t"}


def load(src):
    if src.startswith("http"):
        with urllib.request.urlopen(src, timeout=60) as r:
            return json.load(r)
    return json.load(open(src, encoding="utf-8"))


def layout(n, edges, iters=400, seed=7):
    rnd = random.Random(seed)
    pos = [[rnd.uniform(-1, 1), rnd.uniform(-1, 1)] for _ in range(n)]
    k = math.sqrt(4.0 / n)
    temp = 0.1
    for it in range(iters):
        disp = [[0.0, 0.0] for _ in range(n)]
        for a in range(n):
            ax, ay = pos[a]
            for b in range(a + 1, n):
                dx, dy = ax - pos[b][0], ay - pos[b][1]
                d2 = dx * dx + dy * dy + 1e-9
                f = k * k / d2
                disp[a][0] += dx * f; disp[a][1] += dy * f
                disp[b][0] -= dx * f; disp[b][1] -= dy * f
        for a, b in edges:
            dx, dy = pos[a][0] - pos[b][0], pos[a][1] - pos[b][1]
            d = math.sqrt(dx * dx + dy * dy) + 1e-9
            f = d / k
            disp[a][0] -= dx * f; disp[a][1] -= dy * f
            disp[b][0] += dx * f; disp[b][1] += dy * f
        for a in range(n):
            # gentle pull to the centre keeps disconnected nodes on screen
            disp[a][0] -= pos[a][0] * 0.6; disp[a][1] -= pos[a][1] * 0.6
            dx, dy = disp[a]
            d = math.sqrt(dx * dx + dy * dy) + 1e-9
            step = min(d, temp)
            pos[a][0] += dx / d * step; pos[a][1] += dy / d * step
        temp = max(0.004, temp * 0.985)
    # scale to the 8th-92nd percentile so a few peripheral nodes do not squeeze the core
    def span(vals):
        v = sorted(vals)
        return v[int(len(v) * .08)], v[int(len(v) * .92) - 1]
    (x0, x1), (y0, y1) = span([p[0] for p in pos]), span([p[1] for p in pos])
    squash = lambda t: 0.5 + 0.5 * math.tanh(2.1 * (t - 0.5))   # outliers approach the edge without piling on it
    return [[round(squash((p[0] - x0) / (x1 - x0 or 1)), 4), round(squash((p[1] - y0) / (y1 - y0 or 1)), 4)] for p in pos]


def main():
    data = load(sys.argv[1] if len(sys.argv) > 1 else SOURCE)
    ents = {e["id"]: e for e in data["entidades"]}
    links = [(v["origen"], v["destino"]) for v in data["vinculos"] if v["origen"] in ents and v["destino"] in ents]
    degree = Counter()
    for a, b in links:
        degree[a] += 1; degree[b] += 1
    top = [i for i, _ in degree.most_common(TOP)]
    index = {eid: n for n, eid in enumerate(top)}
    edges = sorted({tuple(sorted((index[a], index[b]))) for a, b in links if a in index and b in index and a != b})
    pos = layout(len(top), edges)
    out = {
        "sample": {
            "updated": data.get("actualizado", ""),
            "area": data.get("especialidad_muestra", ""),
            "counts": dict(Counter(TYPES.get(e["tipo"], "o") for e in data["entidades"])),
            "links": len(data["vinculos"]),
        },
        "nodes": [[pos[n][0], pos[n][1], TYPES.get(ents[eid]["tipo"], "o"), degree[eid]] for n, eid in enumerate(top)],
        "edges": edges,
    }
    path = os.path.join(ROOT, "docs", "kol-preview.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    text = open(path, encoding="utf-8").read()
    leaks = [e["nombre"] for e in data["entidades"] if e.get("nombre") and len(e["nombre"]) > 4 and e["nombre"] in text]
    if leaks:
        raise SystemExit(f"ERROR: names leaked into preview: {leaks[:5]}")
    print(f"kol-preview.json: {len(top)} nodes, {len(edges)} edges, {os.path.getsize(path):,} bytes; counts {out['sample']['counts']}")


if __name__ == "__main__":
    main()
