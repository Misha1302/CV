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

## Age privacy (mandatory for every public CV)

- Do not disclose birth date, age, school/pupil status, or expected graduation years in the public website, any RU/EN profile, or the generated PDFs.
- Use an age-neutral `MR` monogram instead of a personal portrait on public CV pages: facial appearance can reveal approximate age even when prose does not.
- Avoid youth-only competition names and dated school-age distinctions in public CV copy. Preserve their exact historical evidence in the research knowledge base, not in the application document.
- Present HSE Software Engineering without attendance/graduation years; present professional roles with real dates (ISP RAS starts October 2026), since actual employment timing is legitimate evidence.
- Describe earlier compiler/runtime engineering by technical progression, not a dated childhood timeline.
- Keep technical accomplishments and independently supportable adult/professional recognitions (MCST, LangDev, HSE open-source, Baltic diploma) prominent; never fabricate or rename a specific award to disguise its nature.
- The `tools/validate_cv.py` age-privacy gate checks canonical public data, all rendered HTML pages, and all 20 PDF text layers. A check cannot guarantee that an outside linked repository or an external result page does not reveal personal context.
