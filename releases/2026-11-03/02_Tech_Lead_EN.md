# Mikhail Razakov

**SYSTEMS / PLATFORM ENGINEER · .NET**

Moscow / remote · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Profile

I design and build .NET services and infrastructure with explicit module boundaries and recoverable, testable state. VpnMediator handles duplicate payment events and access recovery; UniversalToolchain checks dependencies before execution; in the LMS I own production invariants, judging and review. Before that — commercial C#/.NET projects.

## Technical skills

- C#/.NET, ASP.NET Core, EF Core, SQL/PostgreSQL, SQLite, REST/OpenAPI, async/await, Git/Linux
- Idempotency, payment/access state, reconciliation, recovery/rollback; typed module contracts, dependency graphs, invariant checks

## Experience

**ISP RAS · SharpChecker · Oct 2026 — present**

Symbolic computation and structured C# code/declaration metadata for static analysis and AI-assisted defect recognition.

**MCST · compiler engineering internship · Jul — Aug 2026**

C++23/LLVM 22: experimental LICM with conservative legality checks; Python differential checks of before/after behavior.

**Commercial development · C#/.NET & adjacent technologies · commercial projects**

Application and backend work in C#/.NET and Unity for private clients and product teams: ASP.NET Core, SQL/PostgreSQL, file I/O and server environments, integrations and maintenance of shipped builds.

## Projects

**[UniversalToolchain · module contracts before runtime](https://github.com/Misha1302/UniversalToolchain)**

Module contracts and dependencies form a validated LanguagePlan before runtime. Separate interpreter/CIL routes allow execution results to be compared instead of relying on module registration order.

**[VpnMediator · payment/access consistency](https://misha1302.github.io/CV/cases/en-vpn.html)**

Payment events and access entitlements are separate. Duplicate events are processed idempotently, provider state is reconciled, and operational scripts provide backup, health gates and rollback.

**[TuringSquare-LMS · production, judging and entitlements](https://misha1302.github.io/CV/cases/en-lms.html)**

Live in production: roles and course entitlements, a balance ledger, idempotent payments with provider re-verification, an isolated four-worker judge, and release/recovery procedures. 120+ active students.

## Education and recognition

HSE University — Software Engineering.

MEPhI Junior, 1st-degree diploma; LangDev UniversalToolchain talk.
