# Hiring / claim audit — 2026-09-01

## CONFIRMED

- UniversalToolchain canonical `eng/test-counts.json`: `totalPassed = 1306`.
- LLVM Interprocedural Global IV Optimization: CI regression contract records `passed=29 failed=0 warnings=0`; its README explicitly calls it a conservative prototype/MVP rather than production LLVM infrastructure.
- DerefAfterNullAnalyzer documents Roslyn `ControlFlowGraph`, conditional edge states, loops/back edges, joins, and fixed-point iteration.
- x86-64 Codegen & Register Allocation Playground is an educational backend with SSA/CFG validation, liveness/interference, allocation verification, SysV x86-64 emission, and differential execution; it explicitly says it is not production-ready.
- PS-form Memory Dependence Analyzer documents conservative yes/no/maybe semantics and an exact small-domain oracle; the repository records 104/104 official tests and 5.0/5.0.
- VpnMediator public mirror documents payment state machines, idempotency, outbox/audit trail, recovery workers, backup/restore, versioned deployment, health checks, and rollback.
- CompilationLabLMS documents a working MVP, YooKassa re-verification/reconciliation, ledger/idempotency, and deployment contracts while explicitly distinguishing those contracts from real production readiness.

## SUPPORTED BUT STRONG

- LangDev'26 acceptance is stated in the candidate's public announcement; the official conference site confirms the Oct 8–9 dates, while its public program/speaker list was not yet populated during this audit. The CV keeps the acceptance claim but does not infer broader conference status.
- ISP RAS / SharpChecker and MCST role labels are retained from the canonical CV history; no additional confidential responsibility is invented.

## NEEDS VERIFICATION

- Any future claim about production users, traffic, revenue, measured performance gains, or finance/statistics research needs new evidence before publication.

## OVERCLAIM removed or softened

- `Quantitative Research` -> `Quantitative Developer / Research Software`.
- `.NET Backend / Platform Engineer` -> `.NET Backend Engineer`.
- `C++ / LLVM Systems Engineer` -> `C++ / Compiler Systems & Program Analysis`.
- VpnMediator `Production service` wording -> evidence-backed state/recovery and deployment-tooling wording.

## MISLEADING structure removed

- CompilationLabLMS, VpnMediator, UniversalToolchain, PS-form, and codegen are no longer listed as Professional Experience. All profiles use ISP RAS and MCST as Professional Experience and keep independent work under Projects.
- The duplicate `general` / `compiler` personas are merged into one public Compiler Engineer profile; old compiler URLs redirect to it.
