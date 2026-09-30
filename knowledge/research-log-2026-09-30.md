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
- 2026 — SSA/CFG-aware backend engineering, register allocation, LLVM optimization/interprocedural analysis, Roslyn fixed-point data flow, and much stronger verification discipline.

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

### Roslyn data-flow analysis

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

- 2025 — Mikhail Razakov, IT section, first-degree diploma;
- 2026 — Mikhail Razakov, Universal Toolchain, IT section, 49 project + 47 written = 96 total, first-degree diploma.

The user also states “absolute/overall winner” for both years. The public result pages retrieved in this pass do **not** use that literal label, so the stronger wording is held pending the exact diploma/final protocol.

Primary sources:
- https://olymp.mephi.ru/junior/winners/2025
- https://olymp.mephi.ru/junior/winners/2026

### Baltic Science and Engineering Competition 2026

Official final-news material names Mikhail Razakov / UniversalToolchain with:

- first-degree diploma;
- Main Prize “Совершенство как надежда”.

That wording is strong enough for a CV.

Primary source:
- https://baltkonkurs.ru/news/v-sankt-peterburge-podveli-itogi-baltijskogo-nauchno-inzhenernogo-konkursa/

### HSE Vysshaya Proba

Current status in this pass:
- user-attested: prize-winner in informatics/competitive programming and industrial programming;
- project/library indexes indicate relevant result files exist;
- the exact result artifacts were not successfully ingested here.

Therefore keep the achievement, but do not invent exact rank/category wording until the source PDFs are read.

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

1. exact Vysshaya Proba result artifacts;
2. exact “absolute/overall winner” evidence for Junior;
3. primary organizer artifact for PS-form rank/5.0/104-of-104;
4. exact public-safe ISP RAS title/start/contribution boundary;
5. fresh historical commit replay for early CIL/native-codegen dates;
6. VpnMediator ownership/commercial/user-count evidence if business impact is ever claimed.

These gaps should be closed **before** inventing stronger marketing wording.
