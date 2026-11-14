# Mikhail Razakov

**SOFTWARE ENGINEER · .NET SYSTEMS & RELIABILITY**

Moscow / remote · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Profile

I build .NET services with explicit state boundaries and recovery paths. VpnMediator handles duplicate payment events, access reconciliation and deployment rollback; UniversalToolchain validates module contracts before execution. I built the client licensing API KeyAuth and design access-control boundaries for TuringSquare-LMS.

## Technical skills

- Stack: C#, .NET, ASP.NET Core, EF Core, REST/OpenAPI, SQL, PostgreSQL, SQLite; Python, C++/LLVM; Git, Linux, Docker Compose, systemd
- Engineering: idempotency, state machines, background workers, state reconciliation and recovery, coordinated backup/rollback, contract validation and regression testing

## Experience

**Client software development · C#/.NET and Unity · individual projects, 2023–2024**

Built KeyAuth, an ASP.NET Core license registration and activation API using EF Core/PostgreSQL, with Unity client integration. Delivered the components and supported authentication and compatibility with older clients.

**ISP RAS · SharpChecker · Oct 2026 — present**

Working on symbolic computation for C#/.NET static program analysis.

**MCST · Compiler Engineering Internship · Jul — Aug 2026**

C++23/LLVM 22: experimental LICM, conservative legality checks and Python-based before/after behavior comparison.

## Projects

**[VpnMediator · payment and access consistency](https://misha1302.github.io/CV/cases/en-vpn.html)**

Two-service .NET/Python system with separate payment/access state, idempotent duplicate handling and reconciliation. The updater coordinates backups of two SQLite databases, switches releases and rolls back services after failed health checks.

**[UniversalToolchain · validated module contracts](https://github.com/Misha1302/UniversalToolchain)**

Building modular language infrastructure: LanguagePlan validates module composition, execution routes and ordering constraints before runtime. Interpreter and CIL backends are checked with execution-parity tests.

**[TuringSquare-LMS · learning platform](https://misha1302.github.io/CV/cases/en-lms.html)**

I design role/course/material-access rules and review agent-produced implementation. The platform has approximately 40 users by my account (November 2026). Full task publication and judging are not yet production-verified.

## Education and recognition

HSE University, Faculty of Computer Science — Software Engineering, since 2026.

First-degree diploma, MEPhI Junior competition (2026); presented UniversalToolchain at LangDev 2026 — [Official recording](https://youtu.be/2jqmw-1c7kE)
