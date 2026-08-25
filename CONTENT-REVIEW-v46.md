# Content review — targeted CV v46

## Decision

PASS for three primary narratives: Architecture / Platforms, Compiler Infrastructure, and .NET Backend / Reliability.

## Routing

- `ru.html` / `en.html`: broad architecture-heavy Software / Platform Engineer roles.
- `ru-compiler.html` / `en-compiler.html`: LLVM, compiler infrastructure, language-platform, IR/runtime, program-analysis roles.
- `ru-backend.html` / `en-backend.html`: .NET backend/platform roles where state correctness, payments, recovery, and release safety dominate.

## Strongest alternative considered

Keeping the older Compiler Engineer and generic .NET Backend pages would preserve more keywords, but it fragments the evidence and retains stale or weak claims. The v46 versions instead reuse the master architecture narrative and reorder only verified evidence by role.

## Anti-overclaim review

- No Staff/Principal/Senior Architect title.
- No production-scale/high-load/Kubernetes/cloud claims.
- Compiler page does not claim a production optimization; unsupported analysis cases explicitly fall back to unknown.
- Targeted compiler/backend pages contain no LangDev acceptance claim, no `#1 of 49` claim, and no `104/104 official tests` claim.
- Current UniversalToolchain test count remains 1,306/1,306 only where useful.
- Backend claims are about concrete state/recovery mechanisms, not generic “distributed systems” seniority.

## Recruiter read

Each page answers three questions within the first screen: target role, strongest proof, and why the engineering decisions matter. Technology names are supporting evidence rather than the primary narrative.

## Principal/Staff read

The bullets expose decision ownership and failure semantics: single planning owner, representation boundaries, conservative unknown, independent verifier, provider re-verification, durable recovery, and rollback. These are inspectable design decisions rather than architecture buzzwords.

## Remaining gaps

Multi-team architecture, long-lived high-scale production ownership, and formal organizational leadership are still not established and are not claimed.
