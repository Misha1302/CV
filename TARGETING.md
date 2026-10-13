# Targeting guide — role-specific CV suite

## Primary profiles

1. `Software Engineer — Systems & Architecture` — default broad profile for software, systems, infrastructure, platform, and architecture-heavy engineering roles. Compiler/runtime work is used as evidence of depth rather than as an exclusive specialization. This is intentionally not titled `Software Architect`: multi-team/enterprise architecture authority is not claimed.
2. `C++ / LLVM Systems` — systems, low-level infrastructure, performance, and C++-heavy roles.
3. `.NET Backend / Platform Engineer — State & Reliability` — backend/platform roles where payments, idempotency, recovery, migrations, and release correctness dominate.
4. `Compiler Infrastructure / Language Tooling Engineer` — language infrastructure, compiler platforms, extensible DSL/language tooling, deterministic composition, and runtime/toolchain roles.
5. `Compiler & Program Analysis Engineer — LLVM · C++ · Static Analysis` — compiler, LLVM, static/program-analysis, compiler-backend, and adjacent code-intelligence roles.

## Secondary profiles

- `Compiler Backend / Code Generation Engineer` — LLVM/backend, native codegen, register allocation, and low-level compiler roles.
- `Static Analysis / Program Analysis Engineer` — Roslyn/LLVM data-flow and conservative program-analysis roles.
- `C++ / LLVM Systems` — systems, performance, low-level infrastructure, and HFT-adjacent applications.
- `Quant Developer / Research Engineer` and `Quant Research Candidate` — selective roles where algorithmic experimentation and reproducible validation are central.
- `Compiler / Software Protection Engineer` — selective / evidence-limited; use only for directly relevant roles.

## Systems & Architecture profile evidence order

`UniversalToolchain -> botay! -> VpnMediator`. The profile proves architecture through a verified semantic-plan boundary, a user-facing offline web/Android product, and payment/access recovery semantics—not through design-pattern vocabulary or a seniority title. x86-64 codegen remains the stronger flagship for compiler-backend and systems vacancies.

All profiles share canonical facts from `data/site.json`; they differ only in evidence ordering and role-specific vocabulary.

## Evidence-led revision — 2026-10-11

- **Broad systems/architecture:** UniversalToolchain → botay! → VpnMediator; product and offline architecture are now visible.
- **Backend/platform:** VpnMediator → botay! → CompilationLabLMS. Do not claim production readiness or green CI for VPN/LMS.
- **Compiler infrastructure:** UniversalToolchain → PlanFuzz → LLVM Global-IV; lead with semantic planning and independent verification.
- **Compiler/program analysis:** LLVM Global-IV → UniversalToolchain → x86-64 backend; correctness/legal transformations first.
- **Static/program analysis:** LLVM Global-IV → PS-form → Roslyn, reflecting three independent analysis styles.
- **C++/systems:** LLVM Global-IV → x86-64 backend → PS-form; strongly scoped low-level technical depth.
- **LangDev:** delivered on 9 Oct 2026, not merely accepted.
- **External adoption:** botay! release proof exists; independent external-user counts do not.

See [the claim matrix and before/after analysis](knowledge/cv-transformation-report-2026-10-11.md).

## Age privacy and evidence retention (public CV policy)

- Never publish age, date of birth, a school name, or an explicit school-age status in application CVs or PDFs.
- **Do retain real years of professional experience, competitions and historical software projects.** Their timelines are credible evidence and should not be deleted just to obscure a possible age inference.
- **Do retain the original names and verified scope of youth competitions** (including MEPhI Junior / «Юниор» and Vysshaya Proba / «Высшая проба»). These are achievements, not a statement of the applicant's age; do not mislabel or invent results.
- **HSE University is the exception:** give the institution and Software Engineering program **without enrollment, attendance, or expected graduation years** in RU/EN public CVs.
- Preserve the stronger engineering-oriented Quant Research summary rather than foregrounding a student's age/status.
- Continue using a neutral `MR` identity mark instead of a portrait; the applicant asked to restore years and awards, not a personal photo.
- `tools/validate_cv.py` protects against explicit age disclosures and years in the public HSE education field while allowing historical project years and genuine competition names in source, all generated HTML and PDF text layers. External linked pages and Git history are outside this public-CV guarantee.


## Universal positioning revision — 2026-10-13

The canonical broad CV remains `Software Engineer — Systems & Architecture`.
The landing hero now leads with professional experience (ISP RAS/MCST),
end-to-end projects and the delivered LangDev talk, rather than internal
compiler planning terminology or an isolated test count.

Four discoverable specialist routes are shown on the landing page:
.NET Backend / Reliability; C++ / Systems; Compiler Infrastructure;
Static / Program Analysis. All other role-specific URLs remain unchanged.
The language toggle from the Russian landing must point to
`en-architecture.html`, not the narrow compiler-infrastructure `en.html`.

The universal one-page PDFs drop compiler-only chronology and retain
three distinct projects: UniversalToolchain, botay!, VpnMediator.
Employer, selection and talk claims preserve their underlying evidence
boundaries. Compiler-only, quant and protection variants remain available
for targeted applications rather than being advertised as equal expertise.

No unsupported production scale, formal verification, senior/staff
architecture authority, or broad finance specialism has been introduced.
