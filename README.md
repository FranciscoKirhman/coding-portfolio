# Francisco Kirhman Osorio · Medical Affairs portfolio

Live site: **https://franciscokirhman.github.io/coding-portfolio/**

A static portfolio for Medical Science Liaison and Medical Affairs roles. GitHub Pages serves the `docs/` folder of `main`; there is no build step for the page itself.

## Layout

| Path | What it is |
|---|---|
| `docs/index.html` | The portfolio: one file with HTML, CSS and the interactive scripts (DNA helix, publication illustrations, KOL Radar network preview). |
| `docs/portrait.jpg` | Portrait used on the page and as the social preview image. |
| `docs/Francisco_Kirhman_MSL_CV.pdf` | Public copy of the MSL CV (without phone number). |
| `docs/kol-preview.json` | Anonymized network preview of the KOL Radar sample. Generated. |
| `docs/job-tracker/`, `docs/training-dashboard/` | Public copies of two personal tools, opened with fictional demo data. Generated. |
| `scripts/build_kol_preview.py` | Rebuilds `docs/kol-preview.json` from the public KOL Radar sample; fails if any name leaks. |
| `scripts/build_public_tools.py` | Rebuilds the two tool copies from their private source repositories; fails if any source string survives. |
| `scripts/demo_data.py` | The fictional demo records used by the tool copies. |
| `AUDIT_BRIEF.md` | Instructions for external reviewers. |

## Updating

- Edit `docs/index.html` directly and push to `main`. Pages redeploys in about a minute.
- KOL Radar preview: `python3 scripts/build_kol_preview.py`
- Tool copies: `python3 scripts/build_public_tools.py --tracker <tracker repo> [--dashboard <dashboard repo>]`

The earlier Next.js version of the site is preserved on the `legacy-nextjs` branch.
