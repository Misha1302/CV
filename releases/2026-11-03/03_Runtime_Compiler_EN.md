# Mikhail Razakov

**C# / .NET · RUNTIME, COMPILERS & PERFORMANCE**

Moscow / remote · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Profile

I work on CLR/CIL, compiler infrastructure, LLVM and static analysis. Current focus: SharpChecker symbolic computation at ISP RAS; previously LLVM 22 at MCST. I also build backend systems, with approximately one year of aggregate commercial work across a mixed stack.

## Technical skills

- C#/.NET, CIL, Reflection.Emit, DynamicMethod, CLR internals, Roslyn, BenchmarkDotNet
- LLVM 22/C++23, CFG/SSA, x86-64/SysV, Rust, differential testing; ASP.NET Core, PostgreSQL, Git/Linux

## Experience

**ISP RAS · SharpChecker · Oct 2026 — present**

Symbolic computation and structured C# code/declaration metadata for static analysis and AI-assisted defect recognition.

**MCST · compiler engineering internship · Jul — Aug 2026**

C++23/LLVM 22: experimental LICM with conservative legality checks; Python differential checks of before/after behavior.

**Commercial development · C#/.NET & adjacent technologies · approx. 1 year total**

Application and backend work with C#/.NET, Unity, ASP.NET Core, SQL/PostgreSQL, file I/O and servers. Duration is candidate-reported.

## Projects

**[UniversalToolchain · modular compiler/runtime](https://github.com/Misha1302/UniversalToolchain)**

Typed contracts and dependencies → validated LanguagePlan → runtime; Bytecode/AIR, interpreter and CIL backends. Repository manifest lists 1,324 tests; parity has dedicated scenarios.

**[Quark2 · generated-code invocation](https://github.com/Misha1302/Quark2)**

DynamicMethod/Reflection.Emit, RuntimeMethodHandle and native pointers. BenchmarkDotNet compares reflection Invoke, delegates and pointer calls; CLR internals are experimental only.

**[x86-64 codegen · Rust](https://github.com/Misha1302/x86-64-codegen-ra-playground)**

SSA/CFG, liveness, register allocation, spills, phi-lowering and SysV ABI; supported subset has differential native execution versus an IR interpreter.

**[LLVM Global IV / LICM · C++](https://github.com/Misha1302/LLVM-interprocedural-global-IV-optimization)**

Interprocedural effects and legality checks for optimizations; negative regression cases prevent unsafe transformations.

## Education and recognition

HSE University — Software Engineering.

MEPhI Junior 2026, 1st-degree diploma; LangDev 2026 speaker.
