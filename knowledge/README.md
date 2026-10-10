# Resume Knowledge Base

This directory is the **canonical evidence layer** for Mikhail Razakov's CV/portfolio suite.

The generated CVs are not the source of truth. They are role-specific projections of the evidence recorded here.

## Why this exists

The previous CV architecture mixed three different concerns:

1. what Mikhail has actually done;
2. how strong and verifiable each claim is;
3. which subset should appear in a particular one-page CV.

That made omissions and inconsistencies easy. A concrete example is the compiler profile: UniversalToolchain/Wist was one of the strongest compiler-infrastructure signals, yet it disappeared from the profile's main Projects section because project selection lived downstream in profile copy.

The knowledge base separates those concerns.

## Files

- `resume-evidence.json` — machine-readable facts, evidence levels, claim boundaries, role fit, metrics, gaps, and safe RU/EN wording.
- `research-log-2026-09-30.md` — human-readable research findings, source ledger, unresolved claims, and CV implications.
- `achievement-audit-2026-10-10.md` — 60-unit achievement inventory, rankings, timeline, claim gaps, and CV implications from the 2026-10-10 audit.
- `current-cv-gap-analysis.md` — review of the current rendered CV source against the evidence layer.

## Evidence hierarchy

Use the strongest available source, in this order:

1. **PUBLIC_PRIMARY** — official organizer, conference, university, employer, or result page.
2. **PUBLIC_REPO_DIRECT** — inspectable source code, tests, CI/build contracts, or checked-in evidence.
3. **PUBLIC_REPO_ATTRIBUTED** — repository text attributes a result to an external source that has not yet been independently retrieved.
4. **PUBLIC_SELF_AUTHORED** — public material authored by Mikhail; strong evidence of authorship/communication, but not independent validation of stronger claims.
5. **PRIVATE_DOCUMENT** — user-owned correspondence, invitation, diploma, contract, or other private artifact.
6. **USER_ATTESTED** — explicit statement by the user.
7. **PRIOR_REPO_FORENSICS** — a prior code/commit archaeology pass; useful, but exact dates should be replayed before becoming a headline.
8. **INFERENCE** — interpretation only; never serialize into a CV as a raw fact.
9. **NEEDS_VERIFICATION** — candidate claim that should not be strengthened yet.

A stronger-looking sentence never outranks weaker evidence.

## Canonical positioning

Default identity:

> **Software Engineer — Systems & Architecture**

This is intentionally broader than “compiler engineer”. The differentiator is not breadth for its own sake; it is the repeated ability to build correctness-sensitive systems across several abstraction levels.

The strongest technical proof is the compiler/runtime lineage:

> source / representations → IR / analysis → backend / execution → verification.

The strongest breadth proof is service/system architecture:

> explicit state → idempotency → recovery → migrations / rollback → operational verification.

Compiler/runtime work therefore remains prominent in the canonical CV, but it is evidence of technical depth rather than the only allowed identity.

## Role projections

The same evidence base should generate different one-page views:

| Role | Highest-priority evidence |
| --- | --- |
| Systems & Architecture | UniversalToolchain, MCST/LLVM, VpnMediator, x86-64 backend, service reliability |
| Compiler Infrastructure | UniversalToolchain, MCST/LLVM, Global-IV, x86-64 backend, historical compiler/runtime lineage |
| Compiler Backend / Codegen | x86-64 backend, MCST/LLVM, Global-IV, CIL/native-codegen lineage |
| Static / Program Analysis | Global-IV, DerefAfterNull, PS-form, MCST; ISP RAS selection task only as a bounded supporting signal |
| C++ / Systems | MCST, x86-64 backend, PS-form, graph algorithms |
| .NET Backend / Platform | CompilationLabLMS, VpnMediator, UniversalToolchain |
| Research / Quant Dev | PS-form, controlled experiments/oracles, Global-IV, UniversalToolchain experiment infrastructure |

Project selection must be **derived from role relevance + evidence strength**, never maintained as an unrelated hand-picked list.

## Resume generation contract

Every nontrivial CV bullet should map to at least one `asset.id` in `resume-evidence.json`.

Before emitting a claim:

1. select the role;
2. rank relevant assets by role fit, evidence strength, uniqueness, and recruiter signal;
3. choose the strongest exact claim that the evidence supports;
4. if first-party sources conflict, use only the wording invariant across them and record the conflict;
5. preserve any metric boundary;
6. keep professional employment separate from selection tasks, offers, client work, personal/open-source history, and owned products;
7. never upgrade `USER_ATTESTED`, `PUBLIC_REPO_ATTRIBUTED`, or `NEEDS_VERIFICATION` into primary verification;
8. keep one-page space for current high-signal work; historical projects should usually become a compact lineage statement or portfolio-history page.

## Important claim boundaries

Examples that are currently safe:

- “Several years of hands-on compiler/runtime/language-tooling project experience.”
- “Professional compiler experience in 2026 through the MCST internship.”
- “Accepted and publicly scheduled LangDev 2026 speaker.”
- “UniversalToolchain/Wist2 — one of the winners of the HSE FCS open-source projects competition.”
- “Current UniversalToolchain exact test manifest: 1,324 tests.”
- “Global-IV: 29 positive/negative LLVM IR regressions with verifier/idempotence/differential checks.”

Examples that must **not** be silently upgraded:

- “4 years of professional compiler experience.”
- “HSE open-source first place.”
- “Wist is as fast as C#” without the selected-workload and benchmark-boundary qualifiers.
- “Production-ready x86-64 backend.”
- “Spoke at LangDev 2026” before the scheduled talk actually occurs.
- “Current ISP RAS / SharpChecker employee” until an actual start date/title is confirmed.
- “Two-time absolute/overall winner of Junior” from the currently inspected evidence. The 2025 issued diploma supports **winner in the IT section**; the 2026 official result supports a first-degree diploma with 96 points.
- “Baltic Main Prize” or “Baltic Section Prize” as the canonical label while the competition's own final news and protocol conflict; use “first-degree diploma and the ‘Perfection as Hope’ prize”.

## Maintenance

When a new award, project result, job, benchmark, release, or external validation appears:

1. add/update the asset in `resume-evidence.json`;
2. attach the strongest source;
3. record what the source proves **and what it does not prove**;
4. update claim boundaries and role fit;
5. only then regenerate affected CV variants.

The purpose of this layer is not to maximize the number of claims. It is to maximize the amount of **credible engineering signal per line**.
