# CV Evidence-First Rebuild — Research Report

Date: 2026-09-13

## Executive decision

Primary positioning: **Compiler & Program Analysis Engineer**.

This is the strongest narrative because the most independently inspectable evidence is concentrated in:

- professional LLVM work at MCST;
- current static-analysis work at ISP RAS / SharpChecker;
- public LLVM legality/transformation work with verifier, regression and differential-execution checks;
- Roslyn fixed-point data-flow analysis;
- x86-64 code generation and register allocation;
- language/toolchain architecture in UniversalToolchain;
- real stateful production-system ownership that proves reliability/security maturity without turning the compiler CV into a backend CV.

The strongest competing narrative is **Compiler / Static Analysis / Software Protection Engineer**. The market is real and commercially attractive, especially for LLVM-based hardening, but the currently accessible evidence does not establish enough specific personal ownership of obfuscation / anti-tamper transformations to publish a dedicated software-protection CV without overclaiming.

A **Systems / Platform Engineer with compiler specialization** narrative is also credible, but it weakens the most differentiating signal: industrial compiler/program-analysis work plus independently inspectable compiler projects.

---

## A. Evidence inventory

| Claim / experience | Evidence inspected | Status | CV value | Recommended use |
|---|---|---:|---:|---|
| ISP RAS / SharpChecker employment, C#/.NET static analysis | Current CV source/history; ISP RAS recruiting email; public SharpChecker materials | VERIFIED / USER_REPORTED boundary | Very high | First experience item |
| Current work involves symbolic computations / symbolic execution | User-provided current fact; compatible with SharpChecker architecture; no accessible personal commit/task proving exact component | USER_REPORTED | High | Bounded bullet only; no claim of owning symbolic engine |
| DEREF_AFTER_NULL Roslyn detector task in ISP RAS hiring process | ISP RAS email explicitly assigned the detector task | VERIFIED | Medium | Supporting provenance; do not present hiring task as current production ownership |
| LLVM LICM at MCST | Public repository/code and existing audited CV materials | VERIFIED | Very high | MCST bullet |
| Interprocedural Global-IV LLVM prototype | Public repository, README, tests and implementation history | VERIFIED | Very high | MCST/project bullet |
| Global-IV legality and verification discipline | Separate legality phase; unsupported cases rejected; LLVM Verifier; 29 positive/negative regressions; structural/idempotence/observable-behavior checks | VERIFIED | Very high | Core compiler proof point |
| Roslyn CFG fixed-point null-state analysis | DerefAfterNullAnalyzer repository and tests | VERIFIED | High | Selected project / program-analysis proof |
| x86-64 backend and register allocation | x86-64-codegen-ra-playground: SSA/CFG checks, liveness/interference, allocators, spills, phi lowering, SysV x86-64, differential execution | VERIFIED | High | Selected project / backend proof |
| UniversalToolchain language infrastructure | Current repo, architecture, tests and current manifest | VERIFIED | High | Web CV / language-infrastructure proof |
| UniversalToolchain current test manifest: 1,324 passing | Current repository state/commit | VERIFIED | Medium | Use precise current test count |
| “UniversalToolchain.Wist alpha.7 is published” | Current source version exists, but publication evidence only supported older alpha package | DO_NOT_USE | Negative if wrong | Removed stale publication claim |
| VpnMediator state/reliability architecture | Private repository, case study and release-validation artifacts | VERIFIED | High supporting signal | Compact Production Systems / Independent Engineering block |
| VpnMediator 388 Python + 148 .NET tests in release validation | Current validation artifact | VERIFIED | High | One concrete production-quality metric |
| VpnMediator real user count | User-reported; exact external evidence not established in this pass | USER_REPORTED | Medium | Omit exact number from main CV |
| CompilationLabLMS architecture/payment/recovery/deployment contracts | Private repository and current release branch README | VERIFIED | Medium/high | Portfolio/backend evidence; not needed in one-page compiler CV |
| KeyAuth/LoginAsset prove mature security platform ownership | Accessible code is small/historical prototype-level | DO_NOT_USE as mature claim | Low | Historical interest only; add prototype disclaimer if surfaced |
| Old licensing/software-protection interest | KeyAuth/LoginAsset and user-reported history | PARTIAL | Medium for hardening niche | Supporting history only, not primary CV claim |
| Specific obfuscation / anti-tamper transformation personally implemented | No sufficiently strong accessible artifact found | NEEDS_CONFIRMATION | Potentially very high | Required before dedicated software-protection CV |

### Evidence interpretation

The key correction is that the profile is **not best represented as “a student with many pet projects.”** The evidence supports a stronger but bounded statement: there is professional compiler/static-analysis exposure, several technically inspectable compiler/program-analysis projects, and a separate body of production-system work proving reliability and architecture maturity.

The production work should therefore answer a hiring concern (“can this person reason about real state, failure, rollout and correctness?”), not become a second center of gravity.

---

## B. Market map

The market sample covered more than 20 materially useful current/recent postings across NVIDIA, Apple, AMD, Yandex, Guardsquare and program-analysis/security vendors. The repeated hiring signals are summarized below.

| Role cluster | Observed requirements | Candidate strength | Main gaps | Strongest evidence | Likely rejection reason |
|---|---|---|---|---|---|
| Compiler / LLVM | C/C++, LLVM IR/codegen, optimization, testing, correctness, often register allocation; MLIR/GPU increasingly common | **STRONG** for junior/new-grad/early-career roles | MLIR; GPU/SIMT; upstream LLVM contribution; duration for 2–3+ year roles | MCST, Global-IV, x86-64 backend | Experience-duration or MLIR/GPU gap, not lack of compiler fundamentals |
| Program Analysis / Static Analysis | CFG/data-flow, abstract interpretation/symbolic execution, interprocedural reasoning, production-quality tools, testing/debugging | **STRONG–GOOD** | Exact personal SharpChecker symbolic component is not externally attributable yet | SharpChecker, DerefAfterNullAnalyzer, Global-IV | Recruiter cannot see precise SharpChecker contribution if bullet stays vague |
| Language / Compiler Infrastructure | IR design, passes/lowering, deterministic infrastructure, LLVM/Clang/MLIR, maintainable tooling | **GOOD** | MLIR/Clang/upstream shared-infra experience | UniversalToolchain + LLVM projects | Architecture may look research/prototype-heavy without concise evidence |
| Software Protection / Compiler Hardening | C++/LLVM, code transformations, anti-reverse-engineering, tamper resistance, mature testing | **PARTIAL** | Direct evidence of personal hardening/obfuscation transformations; experience duration | LLVM depth + historical licensing interest | Profile looks adjacent rather than proven hardening engineer |
| C++ / Systems | C++, low-level/runtime/performance, debugging, robust systems, sometimes compiler/static-analysis tooling | **GOOD** | Deep production C++ duration/performance ownership relative to specialist systems candidates | LLVM C++, x86-64, production reliability | Less differentiated than compiler/program-analysis narrative |

### Representative market signals

The following recurring signals appeared across the sample:

1. **LLVM/C++ plus correctness discipline is valuable even at new-grad level.** Several compiler roles explicitly ask for significant compiler projects, LLVM IR/codegen knowledge and unit testing rather than only years of employment.
2. **MLIR is the most visible presentation/competency gap.** It appears repeatedly in modern compiler infrastructure, ML and GPU roles.
3. **Program analysis is a distinct market, not just a compiler subtopic.** Data flow, abstract interpretation and symbolic execution are explicit differentiators in static-analysis/security roles.
4. **Software protection is a real adjacent niche.** Current Guardsquare roles combine C++/LLVM with code hardening against reverse engineering/tampering. The opportunity is real, but the CV should enter it only after specific personal hardening evidence is recoverable.
5. **Experience-duration filters remain real.** Many senior/compiler-security roles require 2–5+ years. No wording should disguise that gap; the CV should maximize technical evidence for roles where duration is flexible.

### Gap classification

- **Competency gap:** MLIR; GPU/SIMT-specific compiler work; possibly upstream workflow depth.
- **CV presentation gap:** SharpChecker was too generic; production reliability was almost absent from compiler narrative.
- **Evidence gap:** exact SharpChecker symbolic-execution component; old obfuscation/hardening implementation details; exact production usage numbers.
- **Experience-duration gap:** roles requiring multiple years of industrial compiler/security work.

---

## C. Positioning decision

### Narrative A — Compiler & Program Analysis Engineer — **WINNER**

**Opens:** Compiler Engineer, LLVM Engineer, Static Analysis Engineer, Program Analysis Engineer, Compiler Infrastructure, some language/runtime roles.

**Unique signal:** industrial LLVM + industrial static analysis + public legality/data-flow/codegen work + production reliability maturity.

**What it loses:** some broad backend/platform discoverability.

**Recruiter confusion risk:** low if non-compiler production work is kept to one compact proof block.

### Narrative B — Compiler / Static Analysis / Software Protection Engineer

**Opens:** compiler hardening, obfuscation, anti-tamper, software-protection roles.

**Unique signal:** potentially rare combination of LLVM, program analysis, licensing/protection history.

**What it loses:** clarity if hardening evidence is weak.

**Recruiter confusion risk:** currently high; could look like keyword expansion rather than demonstrated ownership.

**Decision:** do not publish a dedicated hardening CV yet.

### Narrative C — Systems / Platform Engineer with deep compiler specialization

**Opens:** C++ systems, platform/reliability, backend/platform roles.

**Unique signal:** compiler reasoning plus stateful production systems.

**What it loses:** the compiler/program-analysis specialization becomes less immediate.

**Recruiter confusion risk:** medium; profile can read as “does everything.”

**Decision:** retain backend/systems variants separately; do not make them primary.

---

## D. Current-CV diagnosis

| Section | Decision | Diagnosis |
|---|---|---|
| Headline | KEEP / tighten surroundings | “Compiler & Program Analysis Engineer” is the best center of gravity |
| Summary | REWRITE | Needed professional signals first, then public proof, then production maturity |
| ISP RAS | REWRITE | One generic line materially under-sold the strongest current professional signal |
| MCST | KEEP / REWRITE | Strong evidence, but legality/conservative boundary should be explicit |
| Production experience | ADD compactly | Existing compiler CV under-sold architecture/reliability ownership |
| Projects | REORDER / reduce print set | Each retained project must have a distinct hiring job |
| UniversalToolchain | REWRITE metric | Remove stale “published alpha package” claim; use current test/evidence boundary |
| Skills | REWRITE | Organize by capabilities: Compiler/IR, Program Analysis, Backend/Codegen, Infrastructure/Reliability |
| Recognition | KEEP | Strong proof; education/age should not dominate narrative |
| Education | KEEP compact | Fact, not identity |

### Valuable facts previously missing or under-sold

- current SharpChecker work involves symbolic-computation / symbolic-execution tasks (`USER_REPORTED`, bounded);
- production reliability ownership: explicit state, idempotent reconciliation, migrations, backup/restore, health gates, rollback;
- concrete VpnMediator release-validation surface: 388 Python + 148 .NET tests;
- current UniversalToolchain test manifest: 1,324/1,324;
- the distinction between verified transformation correctness and unsupported cases rejected unchanged.

---

## E. Final rewritten CV text

### English compiler/program-analysis CV

**Mikhail Razakov**  
**Compiler & Program Analysis Engineer**

Compiler and program-analysis engineer: LLVM 22 optimization at MCST and C# static analysis at ISP RAS/SharpChecker. Public projects demonstrate conservative legality, Roslyn fixed-point data flow, and x86-64 register allocation; beyond compiler work I own a stateful backend with idempotency, recovery, and rollback.

#### Experience

**ISP RAS — Static Analysis Engineer** · 2026 — present  
*SharpChecker · C#/.NET · program analysis*

- Contribute to SharpChecker, ISP RAS’s industrial Roslyn-based static-analysis platform for C#/.NET.
- Current tasks include symbolic-computation / symbolic-execution work in C# program analysis.

**MCST — Compiler Engineering Intern** · July — August 2026  
*LLVM 22 · C++23 · compiler engineering*

- Implemented an LLVM 22 LICM pass with loop analysis, side-effect/speculative-safety checks, and hoisting only proven invariants to preheaders.
- Developed a conservative interprocedural global-IV prototype with APInt affine evolution, transitive call effects, a separate legality phase, and LLVM IR transformation; unsupported cases are rejected unchanged.

**Independent Engineering — stateful systems & reliability** · 2026 — present  
*VpnMediator · payments · recovery · Linux*

- Own a stateful subscription backend: explicit payment/access states, idempotent reconciliation, migrations, backup/restore, health gates, and rollback; release gate: 388 Python + 148 .NET tests.

#### Selected projects

**LLVM Interprocedural Global IV Optimization** — C++23, LLVM 22  
An LLVM 22 pass localizes supported induction-like globals after interprocedural effects/affine analysis and a separate legality decision; APInt models fixed-width wraparound. 29 positive/negative regression cases cover the pass, LLVM Verifier, structural expectations, idempotence and observable before/after execution.

**DerefAfterNullAnalyzer** — C#, Roslyn  
A Roslyn ControlFlowGraph analyzer propagates null state over conditional edges to a fixed point, handles loops/back edges and merges states from multiple predecessors. Dedicated analyzer tests cover supported dereference forms and invalidation after assignment/ref/out.

**x86-64 Codegen & Register Allocation Lab** — Rust, SysV x86-64  
Compiler backend with SSA/CFG validation, liveness/interference analysis, linear-scan and seeded simulated-annealing allocators, spills, phi lowering and a SysV x86-64 emitter. Includes independent assignment verification and native-vs-interpreter differential execution.

**UniversalToolchain** — .NET, compiler/language infrastructure  
Modular compiler/runtime infrastructure with typed artifact contracts, dependencies/conflicts, provider selection, pass ordering and artifact routes compiled into an immutable LanguagePlan. Current exact test manifest: 1,324/1,324 passing.

#### Skills

- **Compiler / IR:** C++23, LLVM 22/IR, APInt, interprocedural analysis, CFG/SSA, dominators, loops, LICM, legality, LLVM Verifier.
- **Program Analysis:** C#/.NET, Roslyn CFG, fixed-point data flow, symbolic execution, conditional edges, loops/back edges, state propagation/joins.
- **Backend / Codegen:** Rust, SysV x86-64, liveness/interference, linear scan, simulated annealing, spills, phi lowering, differential execution.
- **Infrastructure / Reliability:** typed contracts, deterministic planning, interpreter/CIL parity, state machines, idempotency, recovery, migrations, rollback.

#### Recognition

- LangDev’26 — accepted talk, “Build the Language, Then Make the Abstractions Disappear.”
- Baltic Science and Engineering Competition — First Degree Diploma and Grand Prize for UniversalToolchain.
- MEPhI Junior — overall winner; First Degree Diploma, 96/100 for UniversalToolchain.

#### Education

HSE University — Software Engineering, 2026–2030.

### Russian compiler/program-analysis CV

**Михаил Разаков**  
**Compiler & Program Analysis Engineer**

Инженер по компиляторам и анализу программ: МЦСТ — LLVM 22 optimization; ИСП РАН/SharpChecker — C# static analysis. Публичные проекты подтверждают conservative legality, Roslyn fixed-point data-flow и x86-64 register allocation; вне compiler work отвечаю за stateful backend с idempotency, recovery и rollback.

#### Опыт

**ИСП РАН — инженер по статическому анализу** · 2026 — сейчас  
*SharpChecker · C#/.NET · program analysis*

- Участвую в разработке SharpChecker — промышленной Roslyn-based платформы статического анализа C#/.NET в ИСП РАН.
- Текущие задачи включают symbolic computations / symbolic execution в анализе C#-программ.

**МЦСТ — стажёр по разработке компиляторов** · июль — август 2026  
*LLVM 22 · C++23 · разработка компиляторов*

- Реализовал LLVM 22 LICM-pass: loop analysis, side-effect/speculative-safety checks и вынос доказанно инвариантных инструкций в preheader.
- Разработал консервативный interprocedural global-IV prototype: APInt-аффинная эволюция, транзитивные call effects, отдельная legality-проверка и LLVM IR transformation; unsupported cases отклоняются без изменения программы.

**Independent Engineering — stateful systems & reliability** · 2026 — сейчас  
*VpnMediator · payments · recovery · Linux*

- Отвечаю за stateful subscription backend: explicit payment/access states, idempotent reconciliation, migrations, backup/restore, health gates и rollback; release gate — 388 Python + 148 .NET tests.

#### Избранные проекты

**LLVM Interprocedural Global IV Optimization** — C++23, LLVM 22  
LLVM 22 pass локализует поддерживаемые induction-like globals после межпроцедурного анализа эффектов и аффинной эволюции с отдельным legality-решением; APInt моделирует fixed-width wraparound. 29 позитивных и негативных regression cases проверяют pass, LLVM Verifier, структуру, идемпотентность и наблюдаемое поведение до/после transformation.

**DerefAfterNullAnalyzer** — C#, Roslyn  
Roslyn ControlFlowGraph analyzer распространяет null-state по conditional edges до fixed point, обрабатывает loops/back edges и объединяет состояния нескольких predecessors; отдельные analyzer tests покрывают поддерживаемые dereference forms и invalidation после assignment/ref/out.

**x86-64 Codegen & Register Allocation Lab** — Rust, SysV x86-64  
Compiler backend с SSA/CFG validation, liveness/interference analysis, linear-scan и seeded simulated-annealing allocators, spills, phi lowering и SysV x86-64 emitter. Есть независимый verifier раскладки и native-vs-interpreter differential execution.

**UniversalToolchain** — .NET, compiler/language infrastructure  
Модульная compiler/runtime infrastructure с typed artifact contracts, dependencies/conflicts, provider selection, pass ordering и artifact routes, компилируемыми в immutable LanguagePlan. Текущий exact test manifest: 1 324/1 324 passing.

#### Навыки

- **Compiler / IR:** C++23, LLVM 22/IR, APInt, interprocedural analysis, CFG/SSA, dominators, loops, LICM, legality, LLVM Verifier.
- **Анализ программ:** C#/.NET, Roslyn CFG, fixed-point data-flow, symbolic execution, conditional edges, loops/back edges, state propagation/joins.
- **Backend / codegen:** Rust, SysV x86-64, liveness/interference, linear scan, simulated annealing, spills, phi lowering, differential execution.
- **Infrastructure / reliability:** typed contracts, deterministic planning, interpreter/CIL parity, state machines, idempotency, recovery, migrations, rollback.

#### Достижения

- LangDev’26 — принят доклад “Build the Language, Then Make the Abstractions Disappear.”
- Балтийский научно-инженерный конкурс — диплом I степени и Главная премия за UniversalToolchain.
- НИЯУ МИФИ «Юниор» — абсолютный победитель; диплом I степени, 96/100 за UniversalToolchain.

#### Образование

НИУ ВШЭ — Программная инженерия, 2026–2030.

---

## F. Before / after

| Area | OLD | NEW | WHY |
|---|---|---|---|
| SharpChecker | “Contribute to SharpChecker…” | Industrial Roslyn-based platform + bounded current symbolic-computation/symbolic-execution scope | Turns the strongest current employer signal into technical evidence without claiming the whole engine |
| Summary | Professional employers + list of projects | Employer specialization → inspectable compiler evidence → compact production maturity | Faster 15–20 second recruiter read |
| MCST Global-IV | Strong but less explicit boundary | “separate legality phase; unsupported cases rejected unchanged” | Signals correctness/conservatism to compiler leads |
| Production | Essentially absent from compiler identity | One compact VpnMediator experience item with explicit state/reconciliation/recovery/rollback and validated test surface | Proves architecture/reliability maturity without diluting compiler focus |
| UniversalToolchain result | Claimed published current alpha package | Current 1,324/1,324 test manifest + runtime correctness boundaries | Removes stale publication claim; replaces it with verified evidence |
| Print projects | Four compiler projects crowded the page | Three distinct print proof points; UniversalToolchain remains on web profile | Preserves one-page CV and avoids redundant signals |
| Skills | Technology-heavy | Capability families | Improves recruiter scanning and reduces keyword noise |

---

## G. Evidence gaps that could materially improve the CV

1. Exact current SharpChecker issue/task/component and, ideally, a sanitized description of the implemented symbolic-execution change.
2. Whether personal SharpChecker work includes symbolic values/expressions, path conditions, state propagation/merging, summaries, detectors, taint or library models — only claim what can be bounded to an actual task.
3. Concrete old software-protection techniques personally implemented: IL/native transformations, control-flow obfuscation, anti-decompilation, integrity/anti-tamper, virtualization, string/data protection, etc.
4. Exact VpnMediator production usage metric if it can be supported by billing/provider/database evidence; otherwise keep it qualitative.
5. Recoverable evidence for real small-business/client software: client type, delivered system, end-to-end ownership, deployment/maintenance and security/integration boundaries.
6. Upstream LLVM/Clang/MLIR contributions or substantial external review history.
7. A small but real MLIR project or contribution; this is the clearest recurring current-market technical gap.
8. Public benchmark/performance evidence where it genuinely maps to target compiler roles; do not invent speedup numbers.

---

## GitHub / portfolio plan

Recommended top-level proof set:

- UniversalToolchain — language/compiler infrastructure;
- LLVM-interprocedural-global-IV-optimization — legality/interprocedural LLVM;
- DerefAfterNullAnalyzer — program analysis;
- x86-64-codegen-ra-playground — backend/register allocation;
- ps_form_analyzer — if its current public state remains strong enough after a separate audit;
- VpnMediator-public — production state/reliability proof.

Projects such as graph-course tasks, generic compiler coursework and older NASM coursework should not displace the six distinct proof signals above. KeyAuth/LoginAsset should remain historical artifacts rather than be deleted, but should be labelled as historical prototypes if a recruiter is likely to land on them.

README follow-ups with highest return:

- Global-IV: keep the legality boundary and exact regression contract prominent.
- x86-64 codegen: make “educational scope / unsupported calls” explicit while keeping verifier/differential-execution evidence first.
- UniversalToolchain: distinguish current source package version from actually published NuGet versions.
- VpnMediator-public: front-load the state machine, idempotency, reconciliation, recovery and rollout boundaries rather than “VPN bot” framing.

---

## Adversarial review

### Reviewer 1 — compiler team lead

**Strongest rejection reason:** “SharpChecker is vague; I can see projects but not enough current industrial analysis depth.”

**Packaging fix applied:** added bounded symbolic-computation/symbolic-execution scope and made LLVM legality/correctness explicit.

**Remaining real issue:** exact SharpChecker component is still an evidence gap.

### Reviewer 2 — skeptical recruiter

**Strongest rejection reason:** “This is a student with many unrelated projects.”

**Packaging fix applied:** professional ISP RAS + MCST appear first; projects are selected by distinct hiring signal; one production block proves maturity.

### Reviewer 3 — senior engineer

**Strongest rejection reason:** “Claims may be toy-project inflation or system-wide ownership by implication.”

**Packaging fix applied:** conservative/unsupported-case boundaries, verifiers/tests/differential execution, no mature-security claim for KeyAuth/LoginAsset, and no exact production-user metric without evidence.

**Remaining real issue:** experience-duration filters cannot be fixed by wording.

---

## Implementation and validation

Implementation branch: `refactor/cv-evidence-first-rebuild-2026-09`.

The rebuild changed the canonical compiler profile and regenerated site/PDF artifacts through the existing build pipeline. The validation sequence covered:

- HTML regeneration;
- EN/RU PDF generation;
- one-page PDF enforcement;
- content and external-link validation;
- desktop/mobile/no-JS visual regression and overflow checks;
- final manifest/tree validation.

The first iteration correctly failed because the RU PDF expanded to two pages. The copy/project budget was tightened, after which both compiler PDFs returned to one page. The next run surfaced only an intentional compiler-page visual-baseline change; reviewed desktop/mobile screenshots showed no clipping/overlap, the baseline was updated, and the final workflow completed successfully.

`main` was not merged or deployed.
