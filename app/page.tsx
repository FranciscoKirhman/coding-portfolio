import { ArrowUpRight, Code2, GitFork, Sparkles } from 'lucide-react';

type Project = {
  title: string;
  year: string;
  eyebrow: string;
  description: string;
  tags: string[];
  repo: string;
  demo?: string;
  accent: string;
};

const projects: Project[] = [
  { title: 'KOL Radar', year: '2026', eyebrow: 'Scientific intelligence', description: 'A Chile-focused research radar for specialists, centres, and public evidence to support Medical Affairs work.', tags: ['Health', 'Data', 'Product'], repo: 'https://github.com/FranciscoKirhman/kol-radar', demo: 'https://franciscokirhman.github.io/kol-radar/', accent: 'from-cyan-300 via-teal-300 to-lime-200' },
  { title: 'Job Tracker', year: '2026', eyebrow: 'Automation toolkit', description: 'A self-contained application tracker with command-line tools that keep structured posting data in sync.', tags: ['HTML / JS', 'CLI', 'Automation'], repo: 'https://github.com/FranciscoKirhman/job-tracker', accent: 'from-violet-400 via-fuchsia-400 to-rose-300' },
  { title: 'Training Dashboard', year: '2026', eyebrow: 'Personal analytics', description: 'An interactive training dashboard generated from structured profiles, routines, progress, and history.', tags: ['Dashboard', 'Python', 'Data'], repo: 'https://github.com/FranciscoKirhman/entrenamiento-dashboard', demo: 'https://franciscokirhman.github.io/entrenamiento-dashboard/', accent: 'from-amber-300 via-orange-300 to-red-300' },
  { title: 'JobFinder', year: '2026', eyebrow: 'Monitoring bot', description: 'A web-monitoring bot built to check for new opportunities on a recurring schedule.', tags: ['Automation', 'Monitoring'], repo: 'https://github.com/FranciscoKirhman/JobFinder', accent: 'from-lime-300 via-emerald-300 to-cyan-300' },
  { title: 'ChiliNews', year: '2025', eyebrow: 'News experience', description: 'A web-based news site for Chile with a focused, dark editorial presentation.', tags: ['HTML', 'Web'], repo: 'https://github.com/FranciscoKirhman/ChiliNews', demo: 'https://franciscokirhman.github.io/ChiliNews/', accent: 'from-sky-300 via-blue-400 to-indigo-400' },
  { title: 'PlantFinder', year: '2024', eyebrow: 'Science utility', description: 'A web interface for querying a database of Chilean plant species.', tags: ['HTML', 'Database', 'Science'], repo: 'https://github.com/FranciscoKirhman/PlantFinder', accent: 'from-green-300 via-emerald-400 to-teal-400' },
  { title: 'NutriCal', year: '2024', eyebrow: 'Web project', description: 'A public HTML project kept as part of the project archive.', tags: ['HTML', 'Archive'], repo: 'https://github.com/FranciscoKirhman/NutriCal', accent: 'from-yellow-200 via-amber-300 to-orange-300' },
  { title: 'BiopREL', year: '2023', eyebrow: 'Research analysis', description: 'Data analysis for GelMA hydrogel research, exploring material behaviour and release profiles.', tags: ['Python', 'Research', 'Data'], repo: 'https://github.com/FranciscoKirhman/BiopREL', accent: 'from-pink-300 via-fuchsia-300 to-purple-400' },
];

export default function Home() {
  return (
    <main className="min-h-screen overflow-hidden bg-[#06141d] text-[#eaf3f4]">
      <div className="pointer-events-none absolute inset-0 opacity-50 [background-image:linear-gradient(rgba(155,255,209,.06)_1px,transparent_1px),linear-gradient(90deg,rgba(155,255,209,.06)_1px,transparent_1px)] [background-size:36px_36px]" />
      <div className="pointer-events-none absolute -right-28 top-24 h-96 w-96 rounded-full bg-cyan-400/15 blur-[120px]" />
      <div className="pointer-events-none absolute -left-28 top-[36rem] h-96 w-96 rounded-full bg-fuchsia-500/10 blur-[120px]" />
      <div className="relative mx-auto max-w-7xl px-5 pb-16 pt-6 sm:px-8 lg:px-12">
        <header className="flex items-center justify-between border-b border-white/10 pb-5">
          <a href="#projects" className="flex items-center gap-3 font-mono text-sm font-bold tracking-tight"><span className="grid h-9 w-9 place-items-center rounded-lg bg-[#b7ff79] text-[#06141d]">FK</span>FRANCISCO KIRHMAN</a>
          <a href="https://github.com/FranciscoKirhman" target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 text-sm text-[#a9c0c5] transition hover:text-[#b7ff79]"><GitFork className="h-4 w-4" />GitHub</a>
        </header>
        <section className="grid gap-10 py-16 md:grid-cols-[1.45fr_.55fr] md:py-24">
          <div>
            <p className="mb-5 flex items-center gap-2 font-mono text-xs font-bold uppercase tracking-[0.2em] text-[#b7ff79]"><Sparkles className="h-4 w-4" />Public work / 2023–2026</p>
            <h1 className="max-w-4xl text-5xl font-semibold leading-[.96] tracking-[-.065em] text-white sm:text-7xl lg:text-8xl">Tools for real-world questions.</h1>
            <p className="mt-7 max-w-xl text-lg leading-8 text-[#b8cbd0]">A growing collection of scientific tools, practical automations, and interactive web experiences.</p>
          </div>
          <aside className="self-end border-l border-[#b7ff79]/50 pl-5 font-mono text-sm leading-6 text-[#a9c0c5]"><p className="text-[#b7ff79]">08 PUBLIC PROJECTS</p><p className="mt-3">Built across research, data, automation, and the web.</p></aside>
        </section>
        <section id="projects" aria-labelledby="projects-heading">
          <div className="mb-7 flex items-end justify-between gap-4"><div><p className="font-mono text-xs uppercase tracking-[0.18em] text-[#7e9ba2]">Project index</p><h2 id="projects-heading" className="mt-2 text-2xl font-semibold tracking-tight text-white">Selected public work</h2></div><p className="hidden font-mono text-xs text-[#7e9ba2] sm:block">Scroll to explore ↓</p></div>
          <div className="grid gap-4 md:grid-cols-2">
            {projects.map((project, index) => <article key={project.title} className="group relative isolate overflow-hidden rounded-2xl border border-white/10 bg-[#0a202b]/85 p-6 transition duration-300 hover:-translate-y-1 hover:border-[#b7ff79]/50 hover:bg-[#0d2631] sm:p-7">
              <div className={`absolute inset-x-0 top-0 h-1 bg-gradient-to-r ${project.accent}`} />
              <div className="flex items-start justify-between gap-4"><span className="font-mono text-xs text-[#7e9ba2]">0{index + 1} / {project.year}</span><Code2 className="h-5 w-5 text-[#b7ff79]" aria-hidden="true" /></div>
              <p className="mt-9 font-mono text-xs font-semibold uppercase tracking-[0.16em] text-[#b7ff79]">{project.eyebrow}</p><h3 className="mt-3 text-3xl font-semibold tracking-[-.04em] text-white">{project.title}</h3><p className="mt-3 max-w-lg text-base leading-7 text-[#b8cbd0]">{project.description}</p>
              <div className="mt-5 flex flex-wrap gap-2">{project.tags.map((tag) => <span key={tag} className="rounded-full border border-white/10 bg-white/5 px-2.5 py-1 font-mono text-[11px] text-[#a9c0c5]">{tag}</span>)}</div>
              <div className="mt-7 flex items-center gap-5"><a href={project.repo} target="_blank" rel="noreferrer" className="inline-flex items-center gap-1.5 text-sm font-semibold text-white transition hover:text-[#b7ff79]">Repository <ArrowUpRight className="h-4 w-4" /></a>{project.demo && <a href={project.demo} target="_blank" rel="noreferrer" className="text-sm font-semibold text-[#b7ff79] transition hover:text-white">Live demo</a>}</div>
            </article>)}
          </div>
        </section>
        <footer className="mt-20 flex flex-col gap-5 border-t border-white/10 pt-7 font-mono text-xs text-[#7e9ba2] sm:flex-row sm:items-center sm:justify-between"><p>Each card links directly to its public source repository.</p><a href="https://github.com/FranciscoKirhman" target="_blank" rel="noreferrer" className="text-[#b7ff79] transition hover:text-white">github.com/FranciscoKirhman ↗</a></footer>
      </div>
    </main>
  );
}
