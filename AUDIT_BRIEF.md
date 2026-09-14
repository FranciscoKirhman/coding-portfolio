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
| `docs/index.html` | The portfolio. One self-contained file: HTML, CSS, JSON-LD and the interactive scripts inline. | Yes |
| `docs/portrait.jpg` | Portrait, 800×800 JPEG; also the social preview image. | Yes |
| `docs/Francisco_Kirhman_MSL_CV.pdf` | Public web copy of the MSL CV. Identical to the application CV except that the phone number is removed. | Yes |
| `docs/kol-preview.json` | Anonymized KOL Radar network (types, degrees, positions, sample totals; no names). | Yes |
| `docs/job-tracker/` | Public copy of a job application tracker, opened with fictional demo data. | Yes |
| `docs/training-dashboard/` | Public copy of a strength-training dashboard, opened with a fictional demo athlete. | Yes |
| `scripts/build_public_tools.py` | Generates the two `docs/` tools from private source repositories: empties every data block, removes private integrations and fails if any string value from the source data survives, or if an expected replacement no longer matches. | No (run locally) |
| `scripts/build_kol_preview.py` | Generates `docs/kol-preview.json` from the public KOL Radar sample and fails if any entity name appears in the output. | No (run locally) |
| `scripts/demo_data.py` | The fictional demo records for both tools. Every company name ends in "(demo)". | No |
| `README.md`, `AUDIT_BRIEF.md` | Repository documentation. | No |
| branch `legacy-nextjs` | The earlier Next.js (vinext) version of the site, removed from `main`. | No |

## 3. The portfolio page (`docs/index.html`)

Approximate line map (it drifts with edits):

| Lines | Part |
|---|---|
| 5–73 | Canonical URL, Open Graph, Twitter card and JSON-LD (`Person` plus three `ScholarlyArticle`). |
| 75–291 | CSS. A deliberate light-only theme with explicit colors (see §5). |
| 310–338 | Hero: headline, quantified lede, CTAs, the helix `<canvas>`, the mutation panel (`#onco`) and the base key. |
| 340–357 | About: text column and a large portrait (a small circle on mobile). |
| 359–370 | Experience: five roles. |
| 372–431 | Publications: date, peer-review badge, journal, authors, plain-language summary, tags, DOI and an interactive illustration per article. |
| 433–464 | Credentials: education, clinical research certifications, languages. |
| 466–531 | Tools: KOL Radar feature (copy, sample counts, network preview), BiopREL, and a collapsed "Other builds" with the two utilities. |
| 534–540 | Footer and contact. |
| 542–end | Scripts: shared `animator` helper, helix (≈572), sequencing depth (≈838), hydrogel press (≈894), membrane vesicles (≈948), KOL Radar network (≈1001). |

### Visual references (chosen by Francisco)
- **Arc Institute** (arcinstitute.org): white ground, blue serif headline, a DNA helix made of dots as the only hero visual.
- **Distill** (distill.pub): a dated publication list with a peer-review badge and a figure beside each entry.
- **Ana Rebeka Kamšek** (kamsekar.github.io): a sober single column, a circular portrait and plain-language publication summaries.

### The interactive helix
- The model is a double helix with 44 base pairs and 10.5 bp per turn. The two strands are offset by 0.78π to suggest major and minor grooves. Depth is shown through dot size and opacity, and dots come from a reused object pool and are depth-sorted each frame.
- Each base pair is seeded with the reference base of one of 11 documented somatic hotspots, with the coding change in HGVS c. notation: KRAS G12D and G12C, BRAF V600E, EGFR L858R and T790M, TP53 R175H, PIK3CA H1047R, IDH1 R132H, JAK2 V617F, ESR1 Y537S and KIT D816V.
- **Hover (mouse or pen), tap (touch, under 8 px of movement) or Enter on the focused canvas** introduces one hotspot on **one strand only**. The opposite strand keeps the original complement, so the pair becomes a mismatch with broken hydrogen bonds. At most two mismatches exist at once, and hover mutations are at least 1.4 s apart.
- The `#onco` panel (`aria-live`) names the gene and protein change, the c. change, what the mutation does, where it is seen, and approved targeted therapy where one exists. These statements need medical accuracy review.
- **No controls.** After 1.6 s, an idle MSH2–MSH6 protein seeks the mismatch, works for 1.8 s and restores the original base. The panel then explains that a failed repair becomes permanent in dividing cells. The page introduces one example by itself after 2.6 s without interaction.
- Base identity is lettered next to open or mutated pairs, so it never depends on color alone.
- **Performance:** idle frames are capped near 30 fps, and animation stops when the canvas is offscreen or the tab is hidden. With `prefers-reduced-motion: reduce` there is no rotation or drift, and frames render only while a mismatch is pending.

### Publication illustrations (not data from the papers)
- **Sequencing depth:** a log slider from 10× to 10,000× samples 40 positions. One position carries an assumed 2% variant and all positions carry an assumed 0.5% error rate. A 3-SD noise band shows when the variant becomes distinguishable. Hovering a bar reads its counts.
- **Hydrogel press:** a slider sets the porcine gelatin fraction. Stiffness rises and swelling falls with it, following the reported qualitative trend; the page shows no numeric moduli. Hovering or dragging down presses the gel.
- **Membrane vesicles:** hovering or tapping releases vesicles, some linked in chains, as the abstract describes. It is animated only while hovered on devices with hover.

### KOL Radar feature
- The statistics are the totals of the public sample (`docs/kol-preview.json`, sample dated 10 Sep 2026): 77 specialists, 61 institutions, 579 clinical trials with a site in Chile, and 1,198 sourced links.
- The network shows the 150 most connected entities with a force-directed layout computed offline. Hovering a node shows its type and link count, and the type filters are toggle buttons with `aria-pressed`.

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
5. **Publication illustrations** are interactive, schematic and use assumed or qualitative values, not figures or data from the papers. Each caption says so.
6. **Tools are public with fictional data.** The tracker and dashboard are shared as reusable utilities, and every demo record is marked as demo in the UI.
7. **KOL Radar is the featured project**, by Francisco's choice. It is a beta that organizes public research signals about Chilean specialists; its own disclaimer says it is not KOL designation. The preview on this page is anonymized. How a pharma Medical Affairs or compliance reader perceives a public tool of this kind is a legitimate audit question.
8. **The helix runs without controls.** Repair is automatic, and there is one unprompted example.
9. **Section order:** About, Experience, Publications, Credentials, Tools.
10. **DiGenoma dates:** the role ran April 2024 to January 2025, so "2024–2025" is correct on the page. The canonical record carries the month-level dates.

## 6. What to audit

Rank findings by impact on the page's one job (§1).

1. **Claim accuracy:** every sentence against the CV and the DOIs (§4). Check dates, author positions, journal names and the degree title.
2. **MSL hiring effectiveness:** what a Medical Affairs director learns in 30 seconds, what is missing or buried, whether publications and medical education are framed for that reader, and whether anything reads as a gap confession or as overclaiming.
3. **Accessibility (WCAG 2.2 AA):**
   - Contrast of every text and color pair, including mono labels on `#eef2fe`, the base colors A `#2143d6`, T `#0b7a53`, G `#8a3fc7` and C `#0d1526`, and the mutation color `#d23a1b`.
   - Keyboard access to all controls and a visible focus indicator.
   - Heading order and landmarks.
   - The canvas alternatives: the helix `aria-label`, the `#onco` live panel and Enter to mutate; the slider labels and live readouts; the KOL Radar filter buttons.
   - Reduced motion and target sizes.
4. **Interactive code quality (lines 542–end):**
   - Correctness: the mismatch and repair state machine, protein assignment, `ResizeObserver` feedback loops and division by zero.
   - Performance: work per frame, behavior on low-end phones, battery use while idle, and whether the `animator` truly stops offscreen.
   - Touch: tap versus scroll on the helix and on the sliders and canvases.
   - **Medical and scientific accuracy:** every hotspot statement in the `HOT` array (c. notation, mechanism, tumor types, therapies), and whether the illustrations stay honest about assumed values.
5. **Responsive layout:** 320, 375, 768, 1024 and 1440 px widths. Check for horizontal overflow, the hero stacking order, whether the legend fits, and portrait cropping.
6. **Performance and SEO:**
   - Page weight and render-blocking font CSS.
   - Validity of the Open Graph and Twitter tags, the canonical URL and the JSON-LD (`Person`, `ScholarlyArticle`).
   - Whether `<title>` and `description` fit recruiter searches.
7. **Privacy and security of what is public:**
   - The public CV copy must not contain a phone number.
   - External links use `rel="noopener"`.
   - The two tool copies and `kol-preview.json` must contain no real personal data. Review `scripts/build_public_tools.py` and `scripts/build_kol_preview.py` for gaps in their leak checks.
8. **Repository hygiene:** the README, `.gitignore`, the homepage field, and whether anything else should move to `legacy-nextjs`.

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
