# Current CV gap analysis — 2026-09-30

This review compares the current `data/site.json` profile design against the evidence knowledge base.

## Executive assessment

The current CVs are not weak because the engineering work is weak. They are weak because **the selection layer loses information**.

The most important failure mode is visible in the current compiler profile:

```json
"project_ids": ["globaliv", "codegen", "deref"]
```

That selection is coherent for a narrow optimization/program-analysis role, but the page is titled **Compiler & Program Analysis Engineer** and therefore silently drops UniversalToolchain/Wist — the strongest evidence of compiler-infrastructure ownership, external project recognition, and the accepted LangDev talk.

This is a data-model problem, not a copywriting problem.

## Cross-profile problems

### 1. Profile copy is acting as source of truth

Each profile independently stores:
- summary;
- experience copy;
- project selection;
- skill groups;
- recognition presentation.

This makes it easy for one profile to forget an asset that another profile knows about.

**Fix:** profiles should reference evidence IDs plus a selection strategy. Claims should be rendered from the knowledge layer.

### 2. Recognition is over-compressed

The shared recognition block currently has three rows, and the last row groups several unrelated achievements into “Другие достижения”.

That loses useful signal:
- MEPhI Junior is sustained project competition evidence across two years;
- Baltic is a separate external technical-project validation with a Main Prize;
- Vysshaya Proba is algorithmic/industrial-programming evidence;
- HSE open-source and LangDev validate the current UniversalToolchain work.

For a one-page CV not all of these should appear, but they should be **selected**, not collapsed in the source model.

### 3. Historical depth disappears

Old projects should not become six resume cards. But removing them completely loses a rare signal:

> compiler/runtime work did not begin with the 2026 internship.

The right representation is a compact evidence-backed lineage:
- 2022 language/VM work;
- 2023 CIL and native x86-64 emission;
- 2024 AST→IR→backend architecture;
- 2025 extensible toolchain composition;
- 2026 professional LLVM/static analysis + verification-oriented systems.

### 4. Verification is under-marketed

Across the strongest current projects, a repeated skill is not merely “testing”:
- exact test manifests;
- legality gates;
- verifier separation;
- differential execution;
- fixed-point convergence;
- exact/reference oracles;
- randomized/metamorphic counterexample search;
- replay/reduction;
- recovery/reconciliation contracts.

This is a cross-project competency and should appear in architecture, systems, compiler and research profiles.

### 5. Metrics need claim boundaries

Useful numbers exist, but must travel with their scope.

Examples:
- UniversalToolchain: current exact manifest = 1,324 tests.
- LangDev benchmark description: six selected arithmetic hot-execution workloads; cached CIL invocation; parsing/compilation excluded.
- Global-IV: 29 regression cases.
- PS-form: organizer-result numbers are currently repository-attributed rather than primary-linked.

A CV generator should never detach a number from its measurement boundary.

### 6. Professional and project work need stronger semantic separation

The portfolio contains serious personal/open-source/product systems. That is a strength.

But a reader must still be able to tell at a glance:
- employer/internship;
- client work;
- owned/personal product;
- open-source project;
- teaching;
- research experiment.

This is especially important for backend variants where CompilationLabLMS/VpnMediator can visually resemble employment entries.

## Profile-specific findings

### Systems & Architecture

Current project selection:
- UniversalToolchain;
- VpnMediator;
- x86-64 backend.

This is directionally strong.

What is still missing:
- the cross-project verification thesis;
- clearer evidence that architecture means concrete ownership of planning/state/recovery boundaries, not a preference adjective;
- a compact professional/compiler lineage signal;
- richer selection of external validation depending on audience.

Recommended top proof order:
1. UniversalToolchain;
2. professional LLVM/static-analysis context;
3. VpnMediator or x86-64 backend depending on target role;
4. one compact lineage line;
5. HSE open-source + LangDev as current external validation.

### Compiler & Program Analysis

Current project selection:
- Global-IV;
- x86-64 backend;
- DerefAfterNull.

Main defect:
- **UniversalToolchain is absent.**

Recommended default compiler-infrastructure version:
1. UniversalToolchain;
2. Global-IV;
3. x86-64 backend.

For a specifically program-analysis vacancy:
1. Global-IV;
2. DerefAfterNull;
3. PS-form.

There should not be one fixed “compiler” project trio for both intents.

### Compiler Backend

The current direction is strong because x86-64 codegen is genuinely deep.

It should additionally exploit:
- historical CIL/native-codegen continuity;
- allocator-independent verification;
- differential execution;
- phi parallel-copy cycles;
- professional LLVM context.

UniversalToolchain can be third project or a compact infrastructure line.

### Program Analysis

This profile has a coherent evidence base:
- ISP RAS context;
- Global-IV;
- DerefAfterNull;
- PS-form.

It should avoid letting the small Roslyn analyzer dominate the much stronger interprocedural/legality and PS-form evidence.

### C++ / Systems

The current codegen + Global-IV + PS-form selection is strong.

Potential improvement:
- frame all three around **correctness under low-level constraints**, not around a list of C++/LLVM/IR keywords.
- use graph-algorithm work as supporting evidence, not a centerpiece.

### .NET Backend / Platform

Strong evidence exists:
- VpnMediator;
- CompilationLabLMS;
- UniversalToolchain as a non-trivial .NET system.

The key risk is classification: owned/personal systems should not look like third-party employment.

The best narrative is:
> explicit state ownership, idempotency, reconciliation, recovery, migrations, rollback and trust boundaries.

### Research / Quant Developer

The current public portfolio is stronger for **research engineering / quant-dev infrastructure** than for quantitative finance.

Best evidence:
- PS-form exact/reference reasoning;
- contract experiments;
- PlanFuzz;
- Global-IV;
- x86 codegen experiments.

Do not imply trading/finance production experience.

## Current claim review

### UniversalToolchain/Wist

**Strengthen.**

Current CV should be able to draw from:
- typed language/toolchain composition;
- deterministic planning;
- exact package/runtime provenance;
- interpreter/CIL execution paths;
- optional SSA;
- external language-authoring alpha;
- exact current 1,324-test contract;
- LangDev accepted talk;
- HSE open-source winner status;
- bounded benchmark evidence.

### Junior

**Verify wording.**

Public MEPhI result pages retrieved in this pass support first-degree diplomas in 2025 and 2026.

The stronger “two-time absolute winner” wording is user-attested and also appears in the current CV, but should be tied to the exact diploma/final protocol before being treated as independently verified marketing copy.

### Baltic

**Keep strong wording.**

Official final competition material supports:
- first-degree diploma;
- Main Prize “Совершенство как надежда”.

### LangDev

**Keep as accepted/scheduled until the event occurs.**

After the talk actually takes place, the knowledge asset can be updated from:
- accepted speaker;
to:
- speaker / presented at LangDev 2026.

### HSE open-source competition

**Current wording is appropriately bounded.**

Use:
- “one of the winners” / “один из победителей”.

Do not invent ranking.

### ISP RAS

**Keep contribution wording bounded to shareable facts.**

The exact title/start/contribution boundary should eventually be backed by an authorized artifact. Do not use private technical detail just because it sounds stronger.

## Information that should usually stay outside a one-page CV

Keep in portfolio/history/interview material unless directly relevant:
- BigSharpCompiler;
- OwnAssembler;
- Wist2Msil;
- Visk;
- Wist4;
- small early projects;
- full PlanFuzz research status;
- full contract-experiment statistics;
- detailed benchmark methodology;
- every olympiad result.

Their purpose is to support the claim graph, not occupy the visible page.

## Proposed source architecture

```text
knowledge/resume-evidence.json
          │
          ├── evidence strength
          ├── safe RU/EN claims
          ├── metrics + boundaries
          ├── role fit
          ├── recruiter signal
          ├── do-not-claim rules
          └── gaps
                  │
                  ▼
          role selection playbook
                  │
                  ▼
          data/site.json projection
                  │
                  ▼
              HTML / PDF
```

This reverses the current ownership model: the CV stops being the database.

## Highest-value next rewrite after the KB is accepted

1. make the evidence base canonical;
2. convert current profile project selection to role playbooks;
3. rebuild the compiler profile so UniversalToolchain cannot disappear from compiler-infrastructure positioning;
4. separate compiler-infrastructure vs program-analysis project trios;
5. split achievements into independently selectable evidence assets;
6. add one compact historical-lineage component;
7. rewrite skills around demonstrated competencies rather than keyword buckets;
8. regenerate and visually validate every RU/EN PDF.
