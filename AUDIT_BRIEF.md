# Audit brief: Francisco Kirhman Osorio portfolio

Paste this whole file into the auditing model, or point it at the repository. It explains what the project is, how it is built, which decisions are deliberate, and exactly how to report findings.

## 1. What this is

A personal portfolio for **Medical Science Liaison (MSL) and Medical Affairs** roles in Chile and Latin America. Its readers are hiring managers, Medical Affairs directors and recruiters at pharmaceutical, biotech, MedTech and CRO companies. Its one job is to get Francisco a conversation, by making his published research, clinical research training and medical education experience verifiable in under two minutes.

- Live site: https://franciscokirhman.github.io/coding-portfolio/
- Repository: https://github.com/FranciscoKirhman/coding-portfolio (branch `main`)
- Hosting: GitHub Pages, serving the `docs/` folder. There is no build step for the portfolio page.

## 2. What is deployed and what is not

| Path | Role | Deployed |
|---|---|---|
| `docs/index.html` | The portfolio. One self-contained file: HTML, CSS and the helix script inline. | Yes |
| `docs/portrait.jpg` | Portrait, 640×800 JPEG. | Yes |
| `docs/Francisco_Kirhman_MSL_CV.pdf` | The MSL CV linked from the page. | Yes |
| `docs/job-tracker/` | Public copy of a job application tracker, opened with fictional demo data. | Yes |
| `docs/training-dashboard/` | Public copy of a strength-training dashboard, opened with a fictional demo athlete. | Yes |
| `scripts/build_public_tools.py` | Generates the two `docs/` tools from private source repositories: empties every data block, removes private integrations and fails if any term from the source data survives. | No (run locally) |
| `scripts/demo_data.py` | The fictional demo records for both tools. Every company name ends in "(demo)". | No |
| `app/`, `components/`, `hooks/`, `lib/`, `public/`, `package.json`, `vite.config.ts`, `next.config.ts` | An earlier Next.js (vinext) version of the site. **Not deployed and not used by Pages.** | No |
| `design-options/` | Local design drafts (untracked). | No |

## 3. The portfolio page (`docs/index.html`)

Approximate line map (it drifts with edits):

| Lines | Part |
|---|---|
| 12–170 | CSS. A deliberate light-only theme with explicit colors (see §5). |
| 173–195 | Hero: headline, lede, CTAs, the helix `<canvas>` and its legend and buttons. |
| 197–211 | About: a single column with a circular portrait. |
| 213–289 | Publications: three peer-reviewed articles, each with date, peer-review badge, journal, authors (Francisco in bold), plain-language summary, tags, DOI and an SVG illustration. |
| 291–302 | Experience: five roles. |
| 304–338 | Tools: KOL Radar, BiopREL, application tracker, training dashboard. |
| 340–372 | Credentials: education, clinical research certifications, languages. |
| 374–380 | Footer and contact. |
| 382–end | Helix script (Canvas 2D, no libraries). |

### Visual references (chosen by Francisco)
- **Arc Institute** (arcinstitute.org): white ground, blue serif headline, a DNA helix made of dots as the only hero visual.
- **Distill** (distill.pub): a dated publication list with a peer-review badge and a figure beside each entry.
- **Ana Rebeka Kamšek** (kamsekar.github.io): a sober single column, a circular portrait and plain-language publication summaries.

### The interactive helix
- The model is a double helix with 46 base pairs and 10.5 bp per turn. The two strands are offset by 0.78π to suggest major and minor grooves. Depth is shown through dot size and opacity, and dots are depth-sorted every frame.
- **Pointer over the helix:** nearby base pairs "heat up". The strands open and the hydrogen-bond rungs break. A fast pass mutates hot pairs, with transitions (A↔G, C↔T) at twice the probability of transversions. Each variant shows a label in genome-position notation (for example `A23403G`) and increments the "Variants" counter. The counter uses `aria-live`.
- **Click on the helix:** mutates the nearest pair. Clicking elsewhere, or the **Proofread** button, sends an enzyme along the axis that restores original bases. **Add a variant** is the keyboard and touch equivalent.
- **Binding proteins:** they drift, and dock beside existing variants.
- **Performance and accessibility:** the canvas scales to devicePixelRatio (capped at 2), redraws through ResizeObserver, pauses when offscreen (IntersectionObserver) or when the tab is hidden, and freezes all motion under `prefers-reduced-motion: reduce`.

## 4. Source of truth for every claim

**The MSL CV PDF in `docs/` is the authority for anything the page says about Francisco.** A page claim that is broader or stronger than the CV wording is a defect, even if it sounds reasonable for an MSL profile. Compare verbs and scope sentence by sentence (for example "coordinated", "reviewed", "developed"); a page verb must not be stronger than the CV's.

Verifiable externally:
- Publications: resolve each DOI (or query `https://api.crossref.org/works/<DOI>`) and check the title, journal, date, full author list and Francisco's author position.
  - `10.1038/s41598-026-59521-8`: *Scientific Reports*, 31 Aug 2026, 2nd of 8. The peer-reviewed version of bioRxiv `10.64898/2026.01.15.699801`.
  - `10.3390/gels12060540`: *Gels*, Jun 2026, 4th of 5.
  - `10.3389/fmicb.2023.1331363`: *Frontiers in Microbiology*, Jan 2024, 5th of 10.
- The plain-language summaries must stay faithful to each abstract. For the *Scientific Reports* article, only the preprint abstract was checked, so avoid preprint-only numbers.
- Degree title: **Engineer in Molecular Biotechnology** (Spanish: Ingeniero en Biotecnología Molecular). It is not "Civil Engineer" and must never be rendered as such.

Do not suggest adding experience, metrics, therapeutic areas or credentials that are not in the CV. Suggest wording or structure instead.

## 5. Deliberate decisions (challenge them only with evidence)

1. **Single static HTML file, no framework, no build.** The page is content, not an app; Pages serves it directly.
2. **Light-only theme** that mirrors a journal page. Colors are explicit, and there is no dark mode on purpose.
3. **English page** for regional and global Medical Affairs audiences. A Spanish version is an open question, not an oversight.
4. **Fonts** come from Google Fonts: Newsreader, Public Sans and IBM Plex Mono, with system fallbacks.
5. **SVG publication illustrations** are schematic motifs, not figures from the papers. Each has an `aria-label` that says "Illustration".
6. **Tools are public with fictional data.** The tracker and dashboard are shared as reusable utilities, and every demo record is marked as demo in the UI.
7. **KOL Radar** is linked as a beta that organizes public research signals about Chilean specialists; its own disclaimer says it is not KOL designation. How a pharma Medical Affairs or compliance reader perceives a public tool of this kind is a legitimate audit question.

## 6. What to audit

Rank findings by impact on the page's one job (§1).

1. **Claim accuracy:** every sentence against the CV and the DOIs (§4). Check dates, author positions, journal names and the degree title.
2. **MSL hiring effectiveness:** what a Medical Affairs director learns in 30 seconds, what is missing or buried, whether publications and medical education are framed for that reader, and whether anything reads as a gap confession or as overclaiming.
3. **Accessibility (WCAG 2.2 AA):**
   - Contrast of every text and color pair, including mono labels on `#eef2fe` and the coral `#c93a17` counter.
   - Keyboard access to all controls and a visible focus indicator.
   - Heading order and landmarks.
   - The canvas alternative: are the buttons, `aria-label` and `aria-live` enough?
   - Reduced motion and target sizes.
4. **Helix code quality (lines 382–end):**
   - Correctness: listener cleanup, `ResizeObserver` feedback loops, and division by zero when the pointer sits exactly on a dot.
   - Performance: allocations per frame (the dots array is rebuilt and sorted each frame, about 600 items), behavior on low-end phones, battery use while idle, and whether `IntersectionObserver` actually stops work.
   - Touch: `touch-action: pan-y` and scroll conflicts.
   - Clarity: whether the scientific metaphor is accurate enough not to embarrass a molecular biologist.
5. **Responsive layout:** 320, 375, 768, 1024 and 1440 px widths. Check for horizontal overflow, the hero stacking order, whether the legend fits, and portrait cropping.
6. **Performance and SEO:**
   - Page weight and render-blocking font CSS.
   - Missing Open Graph and Twitter meta tags, canonical URL and structured data (`Person`, `ScholarlyArticle`).
   - Whether `<title>` and `description` fit recruiter searches.
7. **Privacy and security of what is public:**
   - The CV PDF contains a phone number. Is that acceptable on a public site?
   - External links use `rel="noopener"`.
   - The two tool copies must contain no real personal data. Review `scripts/build_public_tools.py` for gaps in its leak check: it compares output against company names, job IDs, folder paths and CV file names from the source data, plus fixed personal terms.
8. **Repository hygiene:** the unused Next.js scaffold at the root (§2), whether anything should be deleted, the README, and whether the Pages source setting is documented.

## 7. How to report

Return a table, most severe first, then short notes:

| # | Severity (Critical / High / Medium / Low) | Area (§6 number) | File:line or URL | Finding | Evidence | Concrete fix |
|---|---|---|---|---|---|---|

Rules:
- Every finding needs evidence: a quoted line, a measured contrast ratio, a Crossref field, a viewport width. No generic advice.
- Separate **defects** (wrong, broken, inaccessible) from **opinions** (taste, positioning).
- For copy fixes, give the replacement sentence, and keep it within the CV's wording.
- Say explicitly when you could not verify something: for example, if you could not run the page, if a DOI did not resolve, or if an abstract was paywalled.

## 8. Ready-to-paste prompt

> You are auditing a personal portfolio website for Medical Science Liaison (MSL) and Medical Affairs job applications. Read the attached AUDIT_BRIEF.md first and follow it exactly. The live site is https://franciscokirhman.github.io/coding-portfolio/ and the source is https://github.com/FranciscoKirhman/coding-portfolio (the deployed page is `docs/index.html`). Treat the MSL CV PDF in `docs/` as the only source of truth for claims about the person, and verify the three DOIs. Audit the eight areas in section 6, respect the deliberate decisions in section 5 unless you have evidence against them, and report in the table format from section 7, most severe first, with evidence for every finding. Do not invent experience or credentials.
