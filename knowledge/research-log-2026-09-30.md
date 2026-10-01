# Resume research log — 2026-09-30

## Executive finding

The existing CV suite is weaker than the underlying evidence.

The main problem is not lack of projects or achievements. It is **evidence selection and information architecture**:

- strong facts are scattered across role-specific CV copy, repositories, old research notes, and external result pages;
- some profiles omit foundational evidence (for example, the compiler profile omits UniversalToolchain from its main project list);
- several of the strongest differentiators are longitudinal rather than single-project facts and therefore disappear from one-page project lists;
- current CV copy sometimes compresses external recognition too aggressively;
- evidence strength is not encoded, so user-attested, repository-attributed, and primary-verified claims can look equally authoritative;
- metrics exist, but their measurement boundaries are not always carried with them.

The correct upstream object is therefore an evidence graph / knowledge base. CVs should be downstream projections.

## Strongest engineering model

The broadest accurate current model is:

> **Software Engineer — Systems & Architecture**, with unusually deep compiler/runtime evidence.

The distinguishing technical pattern is repeated work on **representations, transformation/execution boundaries, correctness conditions, and verifiable invariants**.

The compiler/runtime lineage is valuable because it is longitudinal, not because every historical project belongs in a modern CV.

A prior repository-forensics pass established the following chronology and remains useful as historical evidence:

- 2022 — custom language frontend and custom bytecode/VM/runtime work;
- 2023 — runtime-generated CIL, then native x86-64 machine-code emission;
- 2024 — explicit AST → IR → backend/execution layering;
- 2025 — shift from individual compilers to reusable/extensible toolchain composition;
- 2026 — SSA/CFG-aware backend engineering, register allocation, professional LLVM work, project-based LLVM/Roslyn analysis, and much stronger verification discipline.

Exact early dates are retained as `PRIOR_REPO_FORENSICS` and should be replayed from commit history before being used as headline date claims.

## High-value current evidence

### UniversalToolchain / Wist

Direct repository evidence supports a materially stronger story than most current CV variants expose:

- modular .NET compiler/runtime infrastructure;
- reusable language/toolchain composition;
- typed planning and contracts;
- Bytecode/AIR/optimization pipeline;
- interpreter and CIL execution paths;
- optional AIR → SSA → AIR experiment;
- deterministic pass/runtime composition;
- exact package/plan binding and fail-closed validation;
- external-language authoring path;
- exact current test manifest of **1,324 tests**.

External LangDev program material adds independent validation: the UniversalToolchain architecture talk is accepted for LangDev 2026.

The LangDev session description also records a bounded performance result: on six selected arithmetic hot-execution benchmarks, cached Wist CIL artifacts are reported within 10% of a no-inlining C# baseline with 0 B measured-execution allocation. Parsing and compilation are excluded. This is useful evidence only with those boundaries.

Sources:
- https://github.com/Misha1302/UniversalToolchain
- https://github.com/Misha1302/UniversalToolchain/blob/master/eng/test-counts.json
- https://langdevcon.org/2026/program

### LLVM Interprocedural Global IV Optimization

Direct repository evidence:

- LLVM 22;
- affine evolution using APInt;
- direct/transitive effect analysis;
- separate legality decision before transformation;
- conservative rejection of unsupported CFG/call/synchronization cases;
- actual IR transformation;
- **29** positive/negative regressions;
- LLVM verifier checks;
- structural expectations;
- idempotence;
- observable before/after execution comparison.

This is stronger than a generic “LLVM project” bullet because it demonstrates the analysis → legality → transform boundary.

Source:
- https://github.com/Misha1302/LLVM-interprocedural-global-IV-optimization

### x86-64 Codegen & Register Allocation Lab

Direct repository evidence:

- compact IR and reference interpreter;
- SSA/CFG/dominance/phi validation;
- edge-specific liveness;
- interference;
- deterministic linear-scan allocation;
- seeded simulated-annealing experiment;
- allocator-independent assignment verification;
- spills and stack-slot reuse;
- SysV x86-64 emission with iced-x86;
- parallel-copy cycle breaking for phi lowering;
- native-vs-interpreter differential execution;
- fault containment for generated-code execution.

This is the strongest narrow backend/codegen proof.

Source:
- https://github.com/Misha1302/x86-64-codegen-ra-playground

### PS-form Memory Dependence Analyzer

Direct repository evidence shows a much richer algorithmic/analysis project than a contest-result bullet alone:

- conservative yes/no/maybe semantics;
- symbolic normalization;
- byte-overlap reduction;
- modular/GCD global proofs;
- exact affine/lattice-point strategy;
- monotonic two-pointer strategy;
- cost-guarded exhaustive fallback;
- bounded witness search that cannot turn failure-to-find into a false “no”;
- exact small-domain oracle;
- randomized/metamorphic wrong-answer hunting;
- timeout/performance hunting.

The README attributes the selection result to organizer final results: first place, only 5.0/5.0, only 104/104 official tests. Until the primary organizer artifact is linked, that result remains `PUBLIC_REPO_ATTRIBUTED`, not `PUBLIC_PRIMARY`.

Source:
- https://github.com/Misha1302/ps_form_analizer

### Roslyn data-flow analysis and ISP RAS boundary

Direct organizer correspondence shows that ISP RAS supplied the `DEREF_AFTER_NULL` Roslyn detector as the standard test task for its student-track process. The public repository therefore has a stronger provenance signal than a random pet analyzer, but this **does not establish current employment**. Later user context reports an offer; an accepted offer, actual start date, canonical title, and completed job work remain unconfirmed.

DerefAfterNullAnalyzer provides direct inspectable evidence of:

- Roslyn ControlFlowGraph;
- conditional-edge states;
- fixed-point iteration;
- loops/back edges;
- predecessor joins;
- invalidation on assignment/ref/out;
- explicit current limits for alias/points-to, access paths, and interprocedural analysis.

Source:
- https://github.com/Misha1302/DerefAfterNullAnalyzer

### Backend / reliability breadth

VpnMediator and CompilationLabLMS make the architecture story materially broader without replacing the compiler differentiator.

VpnMediator evidence includes explicit payment/state machinery, idempotency, outbox/audit, recovery workers, migrations, coordinated backups, versioned releases and rollback-aware deployment.

CompilationLabLMS evidence includes BFF/domain boundaries, PostgreSQL source-of-truth semantics, exactly-once payment crediting, provider re-verification/reconciliation, private object-storage flows, and production deployment/backup contracts.

Sources:
- https://github.com/Misha1302/VpnMediator-public
- https://github.com/Misha1302/CompilationLabLMS

## External recognition — verified boundaries

### LangDev 2026

**Public-primary verified:** accepted speaker / scheduled talk.

Safe now:
- “Accepted LangDev 2026 speaker.”
- “Talk accepted to LangDev 2026.”

Not safe before the event occurs:
- “Spoke at LangDev 2026.”
- “Presented at LangDev 2026.”

Primary source:
- https://langdevcon.org/2026/program

### HSE FCS open-source projects competition

The official HSE competition page verifies the competition and its criteria. The personal winner status is currently grounded in organizer correspondence supplied by the user.

Safe wording:
- “UniversalToolchain / Wist2 — one of the winners…”
- “Selected as one of the winners…”

Do not infer:
- first place;
- absolute winner;
- sole winner;
- exact competition size;
- prize value.

Primary competition source:
- https://cs.hse.ru/opensource/open_source

### MEPhI Junior 2025 and 2026

Official MEPhI result pages independently confirm:

- 2025 — Mikhail Razakov, IT section, 45 project + 46 written = **91 total**, first-degree diploma;
- 2026 — Mikhail Razakov, Universal Toolchain, IT section, 49 project + 47 written = **96 total**, first-degree diploma.

The 2025 table shows 91 as the highest displayed engineering-sciences total. The 2026 table contains another engineering-sciences participant with 100, so the public evidence does **not** support “two-time absolute/overall winner” across the full engineering-sciences category. The safe public claim is therefore two first-degree diplomas; a stronger title requires an official artifact that explicitly defines it and its scope.

Primary sources:
- https://olymp.mephi.ru/junior/winners/2025
- https://olymp.mephi.ru/junior/winners/2026

### Baltic Science and Engineering Competition 2026

The competition's own sources conflict on the prize label:

- the official final-news article calls Razakov a holder of the **Main Prize** “Совершенство как надежда”;
- the official protocol/PDF places Razakov under the **Section Prize** heading.

Both agree on the invariant fact: **first-degree diploma + “Совершенство как надежда” prize**. Until a diploma or organizer clarification resolves the label, that invariant wording is the canonical CV wording.

Primary sources:
- https://baltkonkurs.ru/news/v-sankt-peterburge-podveli-itogi-baltijskogo-nauchno-inzhenernogo-konkursa/
- https://baltkonkurs.ru/features/po-godam/xxii-konkurs-2026/
- https://baltkonkurs.ru/wp-content/uploads/2026/03/bk26protocol.pdf

### HSE Vysshaya Proba

Current status in this pass is track-specific:

- **Industrial Programming:** private HSE Olympiad organizer correspondence invites confirmed attendees to a meeting with diploma holders of this track. That establishes diploma-holder status, but not diploma degree, rank, or score.
- **Informatics:** prize-winner status is user-attested. A private file index points to a result PDF, but the actual result document was not ingested, so the filename is not upgraded into primary evidence.

Do not invent exact degree/rank/score until the primary result artifacts are read.

## Hidden strengths current CVs underuse

### 1. Longitudinal continuity

The powerful claim is not “many projects”.

It is that the same engineering concerns recur over years at increasing depth:

> execution model → code generation → IR boundaries → composition → legality → verification.

That is evidence of durable specialization rather than a recently assembled keyword portfolio.

### 2. Cross-abstraction range

The portfolio spans:

- custom VM/bytecode;
- CIL;
- native x86-64;
- LLVM IR;
- SSA/CFG/data flow;
- register allocation;
- Roslyn;
- backend/service state and recovery.

This should not be presented as a technology list. It should be presented as repeated ownership of **execution and correctness boundaries**.

### 3. Verification is a cross-project competency

A recurring modern pattern is stronger than “writes tests”:

- exact test contracts;
- conservative legality;
- independent verifiers;
- differential execution;
- fixed-point convergence;
- exact/reference oracles;
- randomized/metamorphic testing;
- failure/recovery contracts.

This is a major recruiter signal for systems, compiler, infrastructure, and architecture roles.

### 4. Architecture is not just a preference

The actual projects contain architecture work:

- typed/immutable planning;
- deterministic composition;
- explicit service/data boundaries;
- state machines;
- recovery/reconciliation;
- verifier boundaries;
- isolation of transformation from legality.

So the broad “Systems & Architecture” positioning can be evidence-backed rather than aspirational.

### 5. Technical communication has real proof

The combination of an accepted specialist conference talk and a structured low-level course is a better communication signal than a generic “good communication skills” line.

## Main weaknesses of the current CV suite

1. **No canonical evidence model.** Facts are embedded directly in profile copy.
2. **Arbitrary project omission.** The compiler profile excluding UniversalToolchain is a direct symptom.
3. **Achievement compression.** Distinct external validations are collapsed into one line and lose signal.
4. **Historical signal has no compact representation.** Old projects should not be individual cards, but the lineage should not vanish either.
5. **Evidence classes are mixed.** Public-primary, user-attested and repository-attributed facts need different wording.
6. **Metrics lack transportable boundaries.** Benchmark and contest numbers should always carry exactly what was measured.
7. **Professional vs project experience needs strict separation.** Personal/OSS depth is a strength, but must never be converted into fake professional tenure.
8. **Broad CV still risks hiding compiler depth; narrow CVs risk hiding architecture ownership.**

## Recommended resume architecture after the knowledge base

A strong one-page CV should usually contain:

- one broad role title;
- a 2–3 line thesis;
- professional experience;
- 2–3 role-specific projects selected from the knowledge base;
- 3–4 evidence-backed skill clusters;
- 2–3 highest-value external recognition items;
- one compact historical-lineage sentence when relevant.

The website can remain multi-profile, but every profile should be generated from the same evidence inventory.

## Missing evidence queue

Highest-value unresolved items:

1. exact Vysshaya Proba Informatics result and Industrial Programming diploma/result artifacts;
2. Junior diploma/final protocol only if the literal “absolute/overall winner” title is worth retaining;
3. primary organizer artifact for PS-form rank/5.0/104-of-104;
4. ISP RAS offer acceptance/start/title evidence before it is represented as employment;
5. diploma or organizer clarification resolving Baltic Main-vs-Section prize wording;
6. fresh historical commit replay for early CIL/native-codegen dates before exact dates become headline copy;
7. VpnMediator ownership/commercial/user-count evidence if business impact is ever claimed.

These gaps should be closed **before** inventing stronger marketing wording.


## 2026-10-01 — Career adjacency and market-entry research

Purpose: test whether the current compiler/program-analysis profile can expand into a broader systems market without discarding existing depth.

### Finding 1 — YDB / Yandex Infrastructure is a real adjacent systems market

Current YDB materials expose distributed-storage, distributed-system-infrastructure, query/core and tablet/transaction work. The YDB service page explicitly describes C++ as the core implementation language and lists storage, actor-system, recovery, transaction and query-processing challenges.

Yandex Infrastructure currently describes core infrastructure, storage, networking, container/platform and build/repository systems.

A current YDB distributed-storage opening is senior-level, so it is used as a skill/role specification, not as evidence of an available junior slot.

An archived base-infrastructure internship is retained only as evidence that low-level systems internships without prior experience have existed; it is **not open now**.

Sources:
- https://yandex.ru/jobs/services/ydb
- https://yandex.ru/jobs/services/infrastructure
- https://yandex.ru/jobs/vacancies/razrabotchik-na-s-v-komandu-raspredelyonnogo-hranilischa-ydb-21947
- https://yandex.ru/jobs/vacancies/sistemniy-razrabotchik-stazhyor-v-sluzhbu-bazovoy-infrastrukturi-44923

CV/career implication:
- add Linux/concurrency/storage/distributed-systems evidence rather than abandoning compiler/runtime work;
- use current senior vacancies as capability maps, not direct junior targets.

### Finding 2 — YADRO exposes several adjacent systems families

Current YADRO careers pages show work around Linux/OpenBMC/firmware, RISC-V/CPU, QEMU/system simulation, embedded C/C++ and storage products.

Sources:
- https://careers.yadro.com/
- https://careers.yadro.com/vacancy/18719
- https://careers.yadro.com/vacancy/14718

CV/career implication:
- CPU/OS/Linux/C/C++/simulation/storage skills are transferable targets;
- do not frame the market as “compiler jobs only”.

### Finding 3 — ISP RAS spans static analysis, compilers/JIT and adjacent systems analysis

Current ISP RAS student/research pages list source-code static analysis, interprocedural/path-sensitive analysis, Clang Static Analyzer work, .NET analysis, LLM-assisted analysis, LLVM/GCC optimization, JIT/runtime work and binary-analysis directions.

Sources:
- https://education.at.ispras.ru/static-analysis
- https://education.at.ispras.ru/optimization
- https://education.at.ispras.ru/compile-projects

CV/career implication:
- static/program analysis is a strong near-term base;
- professional/team work should be mined for one heavyweight case with measurable correctness/performance/quality impact.

### Finding 4 — External review is the clearest missing proof

The current evidence base already contains substantial personal/compiler work. The marginal value of another standalone toolchain is lower than the value of passing review in a mature external codebase.

Current low-cost entry points verified on 2026-10-01:

- YDB C++ SDK #553 — open, labels `student-projects` and `30min`:
  https://github.com/ydb-platform/ydb-cpp-sdk/issues/553
- LLVM InstCombine #216127 — open, `good first issue`:
  https://github.com/llvm/llvm-project/issues/216127
- LLVM RISC-V #222933 — open, `good first issue`:
  https://github.com/llvm/llvm-project/issues/222933

These issue states are time-sensitive and must be rechecked immediately before starting work.

### Finding 5 — LangDev 2026 is an immediate networking event, not only recognition

The published draft program currently places Mikhail Razakov's talk on Friday, 2026-10-09 at 10:00.

Sources:
- https://langdevcon.org/2026/program
- https://langdevcon.org/2026/speakers.html

Career implication:
- measure the conference by technical conversations, follow-up contacts and introductions in addition to the talk itself;
- re-check the draft schedule before the event.

### Strategy synthesis

The evidence-supported expansion path is:

> compiler/runtime depth + program-analysis base → broader systems/storage/runtime competence → external review + production ownership.

Architecture should be accumulated as subsystem ownership and trade-off responsibility, not pursued as an entry-level title.

The detailed action plan is maintained in `knowledge/career-execution-plan-2026-10.md`.
