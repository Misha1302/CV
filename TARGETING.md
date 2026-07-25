# Targeting guide - v30

## Compiler / Runtime / Program Analysis

Send `ru-compiler.html` / `en-compiler.html` or the corresponding PDF to compiler, runtime, VM, static-analysis and language-engineering teams.

Evidence hierarchy:
1. UniversalToolchain/Wist2 - multi-IR runtime pipeline, verifier-gated AIR -> SSA -> AIR, optimization passes and interpreter/CIL parity.
2. PS-form Analyzer - conservative program analysis, exact oracle and 1/49, 104/104 result.
3. NASM IA-32 plus x86-64 codegen lab - machine-level understanding, liveness, register allocation and native validation.
4. AdvancedAlgorithms - additional C++23 foundation.

Assembly must remain supporting evidence in this version, not the primary headline.

## C++ Systems / Program Analysis

Send `ru-cpp-systems.html` / `en-cpp-systems.html` to C++ systems internships, algorithm libraries, compiler infrastructure, program analysis and verification tooling.
Primary evidence: PS-form Analyzer, AdvancedAlgorithms, MCST internship, x86 codegen lab and Wist2 IR/SSA.

## Algorithms / Compiler Tools / Backend

- algorithms: `ru/en-algorithms.html`;
- compiler testing/tooling: `ru/en-devtools.html`;
- backend/reliability/EdTech: corresponding focused variants.

## Full portfolio

Use `ru.html` / `en.html` after first contact or as a technical-lead follow-up. Do not attach it instead of a focused PDF.

## Do not claim without new evidence

- FASM proficiency;
- complete System V AMD64 ABI support;
- HFT/quant experience;
- production-ready sandbox or formal verification;
- performance multipliers without a fresh reproducible benchmark.
