# Architecture profile review — 2026-09-15

## Decision

Add a separate `Software Engineer — Architecture & Platforms` profile without replacing the compiler-focused profiles. Do not use `Software Architect`, Staff, Principal, enterprise-scale, or multi-team-governance titles/claims.

## Evidence order

1. **UniversalToolchain** — current source exposes one public semantic planner (`LanguageCompiler`), resolves a typed immutable `LanguagePlan`, and keeps runtime on the selected plan. This is the strongest architecture-ownership signal.
2. **VpnMediator** — independent backend evidence: explicit payment/access state, idempotency, reconciliation/recovery, migrations, backup/restore, health gates, and rollback.
3. **x86-64 backend** — decision/verification separation: register-allocation output is checked by an independent assignment verifier and generated native behavior is compared against a reference interpreter.

## Information hierarchy

Hero proofs are `Architecture ownership`, `State & recovery`, and `Correctness boundaries`. Professional employment remains ISP RAS + MCST with the same bounded wording as the current compiler-infrastructure profile; architecture evidence is not misrepresented as employment.

## Anti-overclaim boundary

The profile is meant for hands-on Software / Platform Engineer roles with meaningful architecture ownership. The repository still does not claim long-running multi-team architecture authority, enterprise governance, cloud/Kubernetes platform ownership, large-scale distributed-system traffic, or years of formal architect tenure.

## Validation expectation

The architecture profile must pass the same canonical build, one-page PDF, source-of-truth, link, visual smoke/regression, and manifest gates as every other profile.
