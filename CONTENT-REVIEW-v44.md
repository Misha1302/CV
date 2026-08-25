# Content review — architecture-first CV v44

## Decision

PASS for hands-on Software / Platform Engineer roles with substantial architecture ownership. The default title is deliberately `Software Engineer — Architecture & Platforms`, not `Software Architect`: the evidence strongly supports architectural decision-making, while multi-team/enterprise architecture ownership is not claimed.

## Strongest evidence retained

- UniversalToolchain has one semantic planning owner (`LanguageCompiler` -> immutable `LanguagePlan`), with runtime restricted to materializing the selected graph.
- Syntax, semantic binding, Bytecode, AIR, optimization, and backend are represented as explicit ownership/representation boundaries.
- Exact package-manifest binding, ownership validation, architecture regression tests, and interpreter/CIL parity make architectural assumptions mechanically testable.
- VpnMediator / CompilationLabLMS provide independent backend evidence through explicit payment states, idempotency, durable inbox/outbox, reconciliation, recovery, backup/restore, health gates, and rollback.
- The x86-64 backend project separates allocation strategy from an independent assignment verifier and checks generated native behavior against an interpreter oracle.

## Corrections and anti-overclaim decisions

- The current UniversalToolchain exact manifest is 1,306/1,306 passing; the older 1,465 snapshot is not presented as the current count.
- No claim that the current Wist 0.1.0-alpha.7 source candidate is published on NuGet.org.
- No Staff/Principal/Senior Architect title and no high-load, large distributed-systems, Kubernetes/cloud, or multi-team governance claim.
- MCST wording is limited to the implemented interprocedural linear-evolution analysis/pass work; the unfinished Global IV project is not presented as a production optimization.
- Architecture bullets describe decisions, invariants, and validation rather than SOLID/Clean Architecture/DDD buzzwords.

## Adversarial review

### Skeptical recruiter

The headline remains credible because it says Software Engineer, while `Architecture & Platforms` is demonstrated by concrete system boundaries and not by inflated seniority. Formal internship and employment dates remain explicit.

### Principal/Staff engineer

The strongest bullets are inspectable in code: single planning ownership, representation boundaries, exact manifest/ownership enforcement, durable state/recovery, and allocator verification. The CV avoids treating technology names as architecture evidence.

## Remaining evidence gaps

Multi-team architecture, long-running ownership at large production scale, enterprise integrations, and cloud/Kubernetes platform governance remain weaker than the repository-level architecture/correctness evidence. The CV does not claim them.
