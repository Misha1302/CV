# Compiler lineage audit — 2026-09-14

Baseline: `469a162dada1d7d44d86e6653e99bb37e8bcd5b6` (`origin/main` before this change).

Purpose: strengthen the compiler-focused CV without converting personal/open-source history into professional tenure.

## Decision

The previous four-step trajectory was too coarse. In particular, `2023 = Wist` and the jump from 2023 to 2025 hid stronger public evidence:

- native x86-64 generation/execution already existed in 2023;
- an AST → IR → x86-64 compiler pipeline existed in 2024;
- late-2024 Quark2 already separated frontend/ASG, bytecode and VM concerns;
- professional LLVM/static-analysis work begins in 2026 and remains a separate category.

Selected representation:

`2022 compiler/VM foundations → 2023 CIL + native x86-64 → 2024–2025 AST/IR/backends → toolchain architecture → 2026 professional LLVM/static analysis`.

## Evidence inventory

| Period | Public evidence | Defensible claim |
| --- | --- | --- |
| 2022 | BigSharpCompiler; OwnAssembler | Public compiler/VM/assembler-like work already existed. |
| 2023 | Wist; Wist2Msil; Visk | Language/runtime work, MSIL backend, and native x86-64 code generation/execution. |
| 2024 | Vl13.2; Wist4; Quark2 | Frontend/AST/IR/bytecode/VM work and a native x86-64 backend pipeline. |
| 2025 | UnifiedToolchain / UniversalToolchain line | Focus shifts from individual language implementations toward reusable compiler/language-tooling architecture. |
| 2026 | MCST; ISP RAS | Professional LLVM 22 compiler engineering and C#/.NET static-analysis context. |

## Claim boundaries

Allowed:

- `public compiler/runtime projects since 2022`;
- `CIL/MSIL and native x86-64 code generation by 2023`;
- `AST→IR→x86-64 pipeline by 2024`;
- `professional LLVM/static-analysis experience since 2026`.

Not allowed:

- `4+ years professional compiler experience`;
- `professional compiler engineer since 2022/2023`;
- treating Visk/Wist4/Quark2 as employment;
- treating Diploma.school as compiler employment;
- implying the current verified Rust backend is the same codebase as the historical projects.

## CV structure change

The compiler-focused variants now separate:

1. professional experience — ISP RAS and MCST only;
2. compiler project lineage — public technical history;
3. current proof projects — UniversalToolchain / Global-IV / x86-64 backend / Roslyn analyzer depending on target profile;
4. additional product experience — compact and explicitly separate where relevant.

The historical repositories are used as chronology evidence, not as extra large project cards. This preserves current technical depth while removing the false impression that compiler specialization began in 2026.

## Fresh GitHub history replay

Re-read from GitHub during implementation:

- BigSharpCompiler: first 2022 commit `088e2e92`, 2022-07-25 (`v0.1`).
- OwnAssembler: first 2022 commit `f5ebe2a6`, 2022-08-24 (`Initial commit`).
- Wist2Msil: first 2023 commit `17729f32`, 2023-07-29; 62 commits observed in the 2023 window.
- Visk: first 2023 commit `8b1faa03`, 2023-09-13; 85 commits observed in the 2023 window.
- Vl13.2: first 2024 commit `1fa5a529`, 2024-02-22; 51 commits observed in the 2024 window.
- Wist4: first 2024 commit `ff959e0d`, 2024-07-19; 78 commits observed in the 2024 window.
- Quark2: first 2024 commit `affbd96c`, 2024-11-21; 58 commits observed through 2024-12-31.

These counts are evidence of public repository activity, not professional tenure metrics.

## Validation performed

- canonical generator check: PASS;
- language/content validator: PASS for 18 profiles / 43 pages;
- 18/18 PDFs remain one page; compiler variants retain a 7.7 pt minimum observed font size;
- desktop/mobile/no-JS visual matrix: PASS after intentionally updating the golden structure for the new proof row and lineage strip;
- rendered PDF contact sheet plus focused compiler-infrastructure PDF inspection: no clipping or overlap observed;
- professional-experience boundary check: Diploma.school remains outside the four compiler-profile professional-experience arrays.
