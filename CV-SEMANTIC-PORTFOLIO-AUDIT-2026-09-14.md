# CV semantic portfolio audit — 2026-09-14

## Canonical fact model

| Fact | Canonical wording / boundary | Evidence status |
| --- | --- | --- |
| ISP RAS | Static Analysis Engineer, 2026–present; C#/.NET static-analysis context. No new concrete SharpChecker implementation claim was added. | Existing canonical employment fact; specific private contribution remains non-public. |
| MCST | Compiler Engineering Intern, July–August 2026; LLVM/compiler-engineering experience. | Existing canonical employment fact; public LICM repository supports the technical direction without expanding employer ownership. |
| UniversalToolchain | Dependency/conflict resolution, provider selection, deterministic contribution/pass ordering, typed artifact routing, pre-execution plan checks. | Verified in current public source and 1,324-test manifest. |
| LLVM Global-IV | Interprocedural direct/transitive effects, affine evolution with APInt, separate applicability/legality stage, transformation, 29 regressions with verifier/structure/idempotence/execution checks. | Verified in public source/tests; current CI green. |
| x86-64 backend | SSA/CFG checks, liveness/interference, register allocation/spills, assignment verifier, phi lowering, SysV emission, native runner, interpreter differential oracle. | Verified in public source; current CI green. Educational scope is retained. |
| DerefAfterNullAnalyzer | Roslyn CFG, worklist/fixed point, branch-edge refinement, predecessor joins, loops/back edges, assignment/ref/out invalidation, method/property/field/index/event dereferences. | Verified in public source/tests. |
| LangDev’26 | “Build the Language, Then Make the Abstractions Disappear: Extensible Programming on .NET” accepted for presentation. | Verified by organizer acceptance email dated 2026-08-13. Public program/speaker page was not yet populated during this audit. |
| Diploma.school | User-attested private/freelance project: jQuery dropdown interactions, responsive mobile/desktop navigation, and UI regression fixes. | **USER_ATTESTED / PRIVATE — included with bounded wording; no public-repository claim.** |

## Profile allocation

- **Compiler Infrastructure:** UniversalToolchain → Global-IV → x86-64 backend; LangDev as recognition.
- **Compiler Backend / Code Generation:** x86-64 backend → Global-IV → UniversalToolchain (compact).
- **Static / Program Analysis:** DerefAfterNullAnalyzer → Global-IV. No UniversalToolchain slot.
- **Broad Compiler:** Global-IV → x86-64 backend → DerefAfterNullAnalyzer.
- **Software Protection:** generated/direct-link profile only; excluded from the equal primary selector and kept `SELECTIVE / EVIDENCE-LIMITED`.

## Market-positioning check

Current compiler postings reviewed during the rewrite repeatedly separate backend/codegen depth, production toolchain/infrastructure work, and program-analysis responsibilities. The rewrite therefore emphasizes the candidate’s existing evidence instead of adding unsupported MLIR/MIR/TableGen/taint/points-to keywords.

## Inputs unavailable in this execution

Additional breadth retained: VpnMediator production/reliability work and the bounded Unity licensing/protection project are used as supporting engineering evidence without replacing the strongest compiler-specific project slots.

The prompt named three prior-review artifacts (`CV_SEMANTIC_PORTFOLIO_REVIEW_REPORT_2026-09-14.md`, `CV_EVIDENCE_SCORECARD_2026-09-14.csv`, `CV_MARKET_GAP_ROLES_2026-09-14.csv`). They were searched in the current Project/Library context but were not available, so no claim in this audit depends on having read them.
