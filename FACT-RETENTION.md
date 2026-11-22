# Canonical CV facts — v44

- Education RU: Студент программы «Программная инженерия» НИУ ВШЭ.
- Education EN: Software Engineering student at HSE University.
- UniversalToolchain current exact test manifest on master (verified at commit `40117eb68c630f7129c120aaaadc69be8f4ecbfb`): 1,324 passed, 0 failed, 0 skipped.
- `UniversalToolchain.Wist` source candidate `0.1.0-alpha.7` is not published on NuGet.org; package publication must not be inferred from project version.
- UniversalToolchain public boundary: typed .NET language/runtime platform with explicit package/contribution planning, exact runtime binding, and experimental non-packable PlanFuzz research tooling.
- SSA boundary: optional verifier-gated AIR → SSA → AIR routes; no universal SSA coverage or performance-superiority claim.
- Baltic award RU: Диплом I степени и Главная премия «Совершенство как надежда» Балтийского научно-инженерного конкурса 2026.
- Baltic award EN: First-degree diploma and the Grand Prize “Perfection as Hope” at the 2026 Baltic Science and Engineering Competition.
- MEPhI Junior 2026: First-degree diploma, 96/100 for UniversalToolchain (49 project + 47 written part).
- SharpChecker contribution boundary: current employment and symbolic-computation/symbolic-execution task scope are user-reported; public evidence verifies SharpChecker's Roslyn-based industrial analyzer architecture but not ownership of the overall engine.
- VpnMediator reliability evidence: current release-validation record reports 388 Python + 148 .NET tests together with idempotence, reconciliation, migration, backup/restore, health-gate, and rollback checks.

## v47 additions (2026-11-22)

- LMS production acceptance — CONFIRMED (repo evidence, `reports/judge90-emergency-20261118/parallel4-20261118/tour1-20261119/PRODUCTION_ACCEPTANCE.md`): five-problem Tour 1, 514 real tests, real C++17/Python3 verdicts read back after re-login, four parallel judge workers, lease protocol.
- Student counts — SUPPORTED_WITH_LIMITS: 128 `studentBindings` and 120 `eligibleCurrentGroupStudents` / 125 `activeConfirmedMembers` at 2026-11-19 (`reports/judge90-emergency-20261118/continuation-01/CHIEF_PRODUCTION_ACCEPTANCE_RU.md:55`, `reports/autonomy-audit-2026-11-19/evidence/production195-focused.json`). "150+ students" is product-owner data, not reproduced from the repo; keep the attribution.
- Load numbers — SUPPORTED_WITH_LIMITS: 959 sequential / 0 errors, p95 52–78 ms, peak 357–369 MiB; 2 880 synchronized with 223 HTTP 409 and 0 HTTP 5xx (`docs/implementation/STATE_HISTORY_PRE_CONSOLIDATION_2026-11-09.md:19`). Isolated rig with small fixtures. `reports/launch-20261115/LOAD_200_REAL_E2E_RU.md` is NO_GO for 200 concurrent users — never claim certified 200/1000-user capacity.
- Agentic LLM orchestration — USER_REPORTED scope, no external metrics: orchestrator, context isolation per role, independent fact/logic critics, verifier with pre-written checks and negative controls.
