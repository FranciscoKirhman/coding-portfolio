import {
  ArrowUpRight,
  BarChart3,
  BookOpenCheck,
  Database,
  ExternalLink,
  GitFork,
  Microscope,
  Network,
  ShieldCheck,
} from 'lucide-react';

type Project = {
  title: string;
  year: string;
  description: string;
  tags: string[];
  repo: string;
  demo?: string;
};

const scientificProjects: Project[] = [
  {
    title: 'KOL Radar',
    year: '2026',
    description:
      'A Chile focused scientific intelligence tool for specialists, institutions, and public evidence.',
    tags: ['Medical Affairs', 'Evidence'],
    repo: 'https://github.com/FranciscoKirhman/kol-radar',
    demo: 'https://franciscokirhman.github.io/kol-radar/web/index.html',
  },
  {
    title: 'BiopREL',
    year: '2023',
    description:
      'GelMA hydrogel analysis and Young’s modulus visualization across formulations.',
    tags: ['Python', 'Tableau'],
    repo: 'https://github.com/FranciscoKirhman/BiopREL',
    demo: 'https://public.tableau.com/app/profile/francisco.kirhman.osorio/vizzes',
  },
  {
    title: 'PlantFinder',
    year: '2024',
    description:
      'A Chilean plant species query tool for species, distribution, and type.',
    tags: ['Node.js', 'Oracle'],
    repo: 'https://github.com/FranciscoKirhman/PlantFinder',
  },
  {
    title: 'NutriCal',
    year: '2024',
    description:
      'A macro and micronutrient calculator for dietary guidelines and portions.',
    tags: ['Node.js', 'Oracle'],
    repo: 'https://github.com/FranciscoKirhman/NutriCal',
  },
];

const otherProjects: Project[] = [
  {
    title: 'Job Tracker',
    year: '2026',
    description:
      'A self contained application tracker with structured data and automation utilities.',
    tags: ['HTML / JS', 'Automation'],
    repo: 'https://github.com/FranciscoKirhman/job-tracker',
  },
  {
    title: 'JobFinder',
    year: '2026',
    description: 'A recurring web monitoring bot for new opportunities.',
    tags: ['Automation', 'Monitoring'],
    repo: 'https://github.com/FranciscoKirhman/JobFinder',
  },
  {
    title: 'Training Dashboard',
    year: '2026',
    description:
      'An interactive dashboard generated from structured profiles, routines, and progress history.',
    tags: ['Dashboard', 'Python'],
    repo: 'https://github.com/FranciscoKirhman/entrenamiento-dashboard',
    demo: 'https://franciscokirhman.github.io/entrenamiento-dashboard/',
  },
  {
    title: 'ChiliNews',
    year: '2025',
    description: 'A web based news experience focused on Chile.',
    tags: ['HTML', 'Web'],
    repo: 'https://github.com/FranciscoKirhman/ChiliNews',
    demo: 'https://franciscokirhman.github.io/ChiliNews/',
  },
];

const foundation = [
  {
    icon: BookOpenCheck,
    label: 'Medical education',
    title: 'Professional Education Specialist',
    detail: 'Johnson & Johnson MedTech | 2025 to 2026',
    copy: 'Coordinated 10 national medical education programs across orthopaedic specialties, engaging HCPs under HCC and HCBI compliance frameworks.',
  },
  {
    icon: ShieldCheck,
    label: 'Clinical research',
    title: 'Clinical Research Intern',
    detail: 'Clínica Indisa | 2024 to 2025',
    copy: 'Reviewed clinical research protocols against GCP and regulatory requirements during a clinical research internship.',
  },
  {
    icon: Microscope,
    label: 'Scientific research',
    title: 'Cancer genomics and biomaterials',
    detail: 'UOH | Universidad de los Andes | PUC Chile',
    copy: 'Research across genomic bioinformatics, biomaterials, microbiology, and reproducible analysis, with two peer reviewed publications and one bioRxiv preprint.',
  },
];

function TagList({ tags }: { tags: string[] }) {
  return (
    <ul aria-label="Project technologies" className="mt-3 flex flex-wrap gap-2">
      {tags.map((tag) => (
        <li
          key={tag}
          className="rounded-full border border-white/10 px-2 py-1 font-mono text-[10px] text-[#9fb7b4]"
        >
          {tag}
        </li>
      ))}
    </ul>
  );
}

function ProjectRow({ project }: { project: Project }) {
  return (
    <article className="grid gap-4 py-6 md:grid-cols-[74px_1fr_auto] md:items-center">
      <p className="font-mono text-xs text-[#7fa29b]">{project.year}</p>
      <div>
        <h3 className="text-xl font-semibold text-white">{project.title}</h3>
        <p className="mt-2 max-w-2xl leading-6 text-[#b8c9c4]">
          {project.description}
        </p>
        <TagList tags={project.tags} />
      </div>
      <div className="flex gap-4 text-sm font-semibold">
        <a
          href={project.repo}
          target="_blank"
          rel="noreferrer"
          aria-label={`View ${project.title} source code`}
          className="inline-flex items-center gap-1.5 text-white transition hover:text-[#b8f28b] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]"
        >
          Source <GitFork aria-hidden="true" className="h-3.5 w-3.5" />
        </a>
        {project.demo && (
          <a
            href={project.demo}
            target="_blank"
            rel="noreferrer"
            aria-label={`View ${project.title}`}
            className="inline-flex items-center gap-1.5 text-[#b8f28b] transition hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]"
          >
            View <ExternalLink aria-hidden="true" className="h-3.5 w-3.5" />
          </a>
        )}
      </div>
    </article>
  );
}

export default function Home() {
  return (
    <main id="top" className="min-h-screen bg-[#071920] text-[#e8f2ee]">
      <a
        href="#main-content"
        className="sr-only absolute left-4 top-4 z-50 rounded bg-[#b8f28b] px-4 py-2 font-mono text-sm font-bold text-[#071920] focus:not-sr-only"
      >
        Skip to content
      </a>
      <div className="pointer-events-none fixed inset-0 opacity-40 [background-image:linear-gradient(rgba(187,255,190,.045)_1px,transparent_1px),linear-gradient(90deg,rgba(187,255,190,.045)_1px,transparent_1px)] [background-size:40px_40px]" />
      <div className="pointer-events-none fixed -right-40 top-12 h-[34rem] w-[34rem] rounded-full bg-[#75e5c4]/12 blur-[140px]" />
      <div className="relative mx-auto max-w-7xl px-5 pb-20 sm:px-8 lg:px-12">
        <header className="flex items-center justify-between border-b border-white/10 py-5">
          <a
            href="#top"
            className="flex items-center gap-3 font-mono text-xs font-bold tracking-[.12em] text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]"
          >
            <span aria-hidden="true" className="grid h-9 w-9 place-items-center rounded-lg bg-[#b8f28b] text-[#071920]">FK</span>
            <span>FRANCISCO KIRHMAN</span>
          </a>
          <nav aria-label="Primary" className="hidden items-center gap-6 font-mono text-xs text-[#9fb7b4] md:flex">
            <a className="transition hover:text-[#b8f28b] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]" href="#profile">Profile</a>
            <a className="transition hover:text-[#b8f28b] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]" href="#evidence">Evidence</a>
            <a className="transition hover:text-[#b8f28b] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]" href="#projects">Projects</a>
            <a className="transition hover:text-[#b8f28b] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]" href="#connect">Connect</a>
          </nav>
          <a
            href="https://www.linkedin.com/in/franciscokirhman/"
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-2 font-mono text-xs text-[#b8f28b] transition hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]"
          >
            LinkedIn <ArrowUpRight aria-hidden="true" className="h-3.5 w-3.5" />
          </a>
        </header>

        <main id="main-content">
          <section className="grid gap-10 py-16 md:grid-cols-[1.3fr_.7fr] md:py-24">
            <div>
              <p className="mb-5 font-mono text-xs font-bold uppercase tracking-[.2em] text-[#b8f28b]">Scientific portfolio | Chile</p>
              <h1 className="max-w-4xl text-5xl font-semibold leading-[.94] tracking-[-.065em] text-white sm:text-7xl lg:text-8xl">Medical science starts with evidence.</h1>
              <p className="mt-8 max-w-2xl text-lg leading-8 text-[#b8c9c4]">Molecular Biotechnology Engineer building toward Medical Science Liaison and Medical Affairs work through cancer genomics research, clinical research experience, HCP education coordination, and evidence led tools.</p>
            </div>
            <aside className="self-end rounded-2xl border border-[#b8f28b]/25 bg-[#0b252c]/80 p-6">
              <p className="font-mono text-xs uppercase tracking-[.16em] text-[#b8f28b]">Scientific foundation</p>
              <p className="mt-4 text-xl font-medium leading-7 text-white">Medical education | clinical research | cancer genomics | data communication</p>
              <div className="mt-7 grid grid-cols-2 gap-4 border-t border-white/10 pt-5 font-mono text-xs text-[#9fb7b4]">
                <p><strong className="block text-2xl font-semibold text-white">10</strong>national programs</p>
                <p><strong className="block text-2xl font-semibold text-white">2</strong>peer reviewed publications</p>
              </div>
            </aside>
          </section>

          <section id="profile" aria-labelledby="profile-heading" className="border-y border-white/10 py-14 md:py-18">
            <div className="max-w-3xl">
              <p className="font-mono text-xs uppercase tracking-[.18em] text-[#7fa29b]">Scientific profile</p>
              <h2 id="profile-heading" className="mt-3 text-3xl font-semibold tracking-[-.04em] text-white sm:text-4xl">A foundation for Medical Affairs</h2>
              <p className="mt-4 text-base leading-7 text-[#b8c9c4]">Molecular Biotechnology Engineer with research in cancer genomics, biomaterials, and microbiology; dual GCP certification; CITI Human Subjects Research training; a PUC Chile Diploma in Clinical Study Management; and HCP education coordination in a multinational MedTech setting.</p>
            </div>
            <div className="mt-10 grid gap-4 lg:grid-cols-3">
              {foundation.map(({ icon: Icon, label, title, detail, copy }) => (
                <article key={title} className="rounded-2xl border border-white/10 bg-[#0a2229]/80 p-6">
                  <Icon aria-hidden="true" className="h-5 w-5 text-[#b8f28b]" />
                  <p className="mt-7 font-mono text-xs font-semibold uppercase tracking-[.15em] text-[#b8f28b]">{label}</p>
                  <h3 className="mt-3 text-xl font-semibold text-white">{title}</h3>
                  <p className="mt-1 font-mono text-xs text-[#7fa29b]">{detail}</p>
                  <p className="mt-5 leading-7 text-[#b8c9c4]">{copy}</p>
                </article>
              ))}
            </div>
          </section>

          <section id="evidence" aria-labelledby="evidence-heading" className="py-16 md:py-24">
            <div className="grid gap-8 md:grid-cols-[1fr_.75fr] md:items-end">
              <div>
                <p className="font-mono text-xs uppercase tracking-[.18em] text-[#7fa29b]">Selected evidence</p>
                <h2 id="evidence-heading" className="mt-3 text-3xl font-semibold tracking-[-.04em] text-white sm:text-4xl">Scientific communication through tools and publications</h2>
              </div>
              <p className="text-base leading-7 text-[#b8c9c4]">Published work includes <em>Designing Tunable GelMA Hydrogels by Integrating Mammalian and Non Mammalian Gelatins</em>, published in <em>Gels</em> in 2026.</p>
            </div>
            <div className="mt-10 grid gap-4 md:grid-cols-2">
              <article className="group flex min-h-80 flex-col rounded-2xl border border-white/10 bg-[#0b252c] p-6 transition hover:-translate-y-1 hover:border-[#b8f28b]/45">
                <Network aria-hidden="true" className="h-6 w-6 text-[#b8f28b]" />
                <h3 className="mt-10 text-2xl font-semibold tracking-[-.035em] text-white">KOL Radar</h3>
                <p className="mt-4 leading-7 text-[#b8c9c4]">A transparent research workspace for comparing Chilean specialists, institutions, and public scientific signals. It supports research prioritization, not automatic KOL designation or outreach decisions.</p>
                <a href="https://franciscokirhman.github.io/kol-radar/web/index.html" target="_blank" rel="noreferrer" className="mt-auto inline-flex items-center gap-2 pt-8 text-sm font-semibold text-[#b8f28b] transition group-hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]">Open KOL Radar <ArrowUpRight aria-hidden="true" className="h-4 w-4" /></a>
              </article>
              <article className="group flex min-h-80 flex-col rounded-2xl border border-white/10 bg-[#0b252c] p-6 transition hover:-translate-y-1 hover:border-[#b8f28b]/45">
                <BarChart3 aria-hidden="true" className="h-6 w-6 text-[#b8f28b]" />
                <h3 className="mt-10 text-2xl font-semibold tracking-[-.035em] text-white">BiopREL analysis</h3>
                <p className="mt-4 leading-7 text-[#b8c9c4]">Data analysis and visualization for GelMA hydrogel research, translating compressive data comparisons into inspectable dashboards and figures.</p>
                <a href="https://public.tableau.com/app/profile/francisco.kirhman.osorio/vizzes" target="_blank" rel="noreferrer" className="mt-auto inline-flex items-center gap-2 pt-8 text-sm font-semibold text-[#b8f28b] transition group-hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]">View BiopREL dashboard <ArrowUpRight aria-hidden="true" className="h-4 w-4" /></a>
              </article>
            </div>
          </section>

          <section id="projects" aria-labelledby="projects-heading" className="border-t border-white/10 pt-14">
            <div className="flex items-end justify-between gap-5">
              <div>
                <p className="font-mono text-xs uppercase tracking-[.18em] text-[#7fa29b]">Scientific and technical projects</p>
                <h2 id="projects-heading" className="mt-3 text-3xl font-semibold tracking-[-.04em] text-white sm:text-4xl">Selected projects</h2>
              </div>
              <Database aria-hidden="true" className="h-8 w-8 text-[#b8f28b]" />
            </div>
            <div className="mt-8 divide-y divide-white/10 border-y border-white/10">
              {scientificProjects.map((project) => <ProjectRow key={project.title} project={project} />)}
            </div>
            <div className="mt-14">
              <p className="font-mono text-xs uppercase tracking-[.18em] text-[#7fa29b]">Other public builds</p>
              <h2 className="mt-3 text-2xl font-semibold tracking-[-.04em] text-white">Personal and web projects</h2>
              <div className="mt-6 divide-y divide-white/10 border-y border-white/10">
                {otherProjects.map((project) => <ProjectRow key={project.title} project={project} />)}
              </div>
            </div>
          </section>
        </main>

        <footer id="connect" className="mt-16 flex flex-col gap-5 border-t border-white/10 pt-7 font-mono text-xs text-[#7fa29b] sm:flex-row sm:items-center sm:justify-between">
          <p>Scientific portfolio | Santiago, Chile | Updated September 2026</p>
          <div className="flex flex-wrap gap-x-5 gap-y-2">
            <a href="https://www.linkedin.com/in/franciscokirhman/" target="_blank" rel="noreferrer" className="transition hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]">LinkedIn <span aria-hidden="true">↗</span></a>
            <a href="https://www.kaggle.com/franciscokirhman" target="_blank" rel="noreferrer" className="transition hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]">Kaggle <span aria-hidden="true">↗</span></a>
            <a href="https://public.tableau.com/app/profile/francisco.kirhman.osorio/vizzes" target="_blank" rel="noreferrer" className="transition hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]">Tableau <span aria-hidden="true">↗</span></a>
            <a href="https://github.com/FranciscoKirhman" target="_blank" rel="noreferrer" className="text-[#b8f28b] transition hover:text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#b8f28b]">GitHub <span aria-hidden="true">↗</span></a>
          </div>
        </footer>
      </div>
    </main>
  );
}
