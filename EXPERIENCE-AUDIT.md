# Experience audit — v25

## Source-of-truth order

1. public repository code, README files and verification records;
2. current Wist2 architecture status;
3. included UniversalToolchain technical paper;
4. prior CV wording only when not contradicted by stronger evidence.

## Confirmed differentiators

- creator and primary developer of UniversalToolchain/Wist2, a multi-stage compiler/runtime framework;
- Bytecode/AIR/SSA boundaries, reference interpreter, CIL/DynamicMethod backend and module/capability composition;
- experimental opt-in AIR → SSA → AIR lowering/emission with constant folding, SCCP-lite, branch folding, unreachable cleanup and dead pure-instruction elimination;
- structural verification around transforms and interpreter/CIL parity for supported semantics;
- dated Wist2 baseline: 75 projects, 1,325 tests, 0 warnings/errors;
- creator of `AdvancedAlgorithms`, a header-only C++23 library with 12 graph, tree, string, data-structure and optimization modules;
- differential tests, structural invariants, invalid-input cases, ASan/UBSan and large-input checks;
- PS-form Analyzer: 1st out of 49, the only 5.0/5.0 and 104/104 result, with conservative analysis and exact/randomized/metamorphic verification;
- x86-64 educational lab with liveness, live intervals, linear scan, simulated-annealing allocation, code generation and interpreter-vs-native validation;
- MCST internship with C++23, CMake, warnings-as-errors, ASan/UBSan, clang-tidy, explicit include dependencies and reproducible I/O tests.

## Positioning boundary for MCST

The internship is legitimate experience, but its graph algorithms overlap with `AdvancedAlgorithms`. Therefore:

- keep MCST in Experience;
- emphasize engineering constraints, review and build/test discipline;
- do not retain an MCST graph-components project card;
- do not call it an independent algorithmic proof layer.

## Claims intentionally excluded

- HFT, market-data or quant experience;
- production sandbox guarantees;
- formal verification;
- unverified test counts;
- performance multipliers without a fresh benchmark report;
- blanket production suitability of `AdvancedAlgorithms`.

Verdict: GO for compiler/runtime, algorithms/program analysis, compiler tooling and C++ systems targeting after the hierarchy correction, layout hardening and v25 skills rewrite.
