# Mikhail Razakov

**SYSTEMS / PLATFORM ENGINEER · .NET**

Moscow / remote · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Profile

I design and build .NET services and infrastructure with explicit module boundaries and recoverable, testable state. VpnMediator handles duplicate payment events and access recovery; UniversalToolchain checks dependencies before execution; in the LMS I own architectural invariants and review. Approx. one year of aggregate commercial development across a mixed stack.

## Technical skills

- C#/.NET, ASP.NET Core, EF Core, SQL/PostgreSQL, SQLite, REST/OpenAPI, async/await, Git/Linux
- Idempotency, payment/access state, reconciliation, recovery/rollback; typed module contracts, dependency graphs, invariant checks

## Experience

**ISP RAS · SharpChecker · Oct 2026 — present**

Symbolic computation and structured C# code/declaration metadata for static analysis and AI-assisted defect recognition.

**MCST · compiler engineering internship · Jul — Aug 2026**

C++23/LLVM 22: experimental LICM with conservative legality checks; Python differential checks of before/after behavior.

**Commercial development · C#/.NET & adjacent technologies · approx. 1 year total**

Application and backend work with C#/.NET, Unity, ASP.NET Core, SQL/PostgreSQL, file I/O and servers. Duration is candidate-reported.

## Projects

**[UniversalToolchain · module contracts before runtime](https://github.com/Misha1302/UniversalToolchain)**

Module contracts and dependencies form a validated LanguagePlan before runtime. Separate interpreter/CIL routes allow execution results to be compared instead of relying on module registration order.

**[VpnMediator · payment/access consistency](https://misha1302.github.io/CV/cases/en-vpn.html)**

Payment events and access entitlements are separate. Duplicate events are processed idempotently, provider state is reconciled, and operational scripts provide backup, health gates and rollback.

**[TuringSquare-LMS · access control and implementation review](https://misha1302.github.io/CV/cases/en-lms.html)**

Role/course-access invariants and acceptance criteria for T-Bank sandbox payments. The project is in development; my focus is architecture decisions and review of agent-produced implementation.

## Education and recognition

HSE University — Software Engineering.

MEPhI Junior 2026, 1st-degree diploma; LangDev 2026 UniversalToolchain talk.
