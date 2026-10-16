# CV improvement decisions — 16 October 2026

Baseline: `9494ff6b146dc8bf1acc058ef6fa9fbae6899487` (13 October generated refresh). Canonical CV render source: `data/site.json`. This note records editorial decisions; it is not new primary technical evidence.

| Prior-audit issue | Decision | Evidence / rationale |
|---|---|---|
| 1. Main summary too abstract | ALREADY DONE | October 13 wording describes actual compiler/backend/offline projects. |
| 2. Immutable LanguagePlan | IMPLEMENT | Resolve semantics once, verify and materialize without replanning. |
| 3. PS-form algorithmic methods | IMPLEMENT | Exact affine count; modular/GCD necessary exclusions. |
| 4. Unknown/Maybe semantics | REVISE | Keep precise per-project statements, not generic formal proofs. |
| 5. Independent PS-form oracle | IMPLEMENT | Small-domain exact oracle and randomized/metamorphic cases. |
| 6. Global-IV legality, provenance | ALREADY DONE | Current wording and internship boundaries are distinct. |
| 7. x86 allocator verification | REVISE | Elevate independent checking in Compiler Backend summary. |
| 8. botay validated witness | IMPLEMENT | Architecture section now notes verified schedule witness. |
| 9. PlanFuzz negative/control cases | IMPLEMENT | Explicit experimental replay and fingerprint-preserving reduction. |
| 10. Backend recovery | ALREADY DONE | Retain provider verification, reconciliation and audit state. |
| 11. Teaching / LangDev | DEFER | Already visible through recognition; do not displace stronger code proof. |
| 12. Employment, prizes, dates | ALREADY DONE | Preserve bounded claims and privacy. |
| 13. Quant profile honesty | REVISE | Focus Quant Developer on mathematical algorithms; research profile remains selective. |
| 14. Software protection limits | IMPLEMENT | Rewrite overly broad bilingual summary with actual Unity prototype scope. |
| 15. Generic skills overload | REVISE | Prefer concrete summary/project edits; leave verified skills. |
| 16. Reorder projects | REJECT | Role-specific order already deliberate and coherent. |
| 17. PS-form case detail | IMPLEMENT | Upgrade shared case copy with algorithm/oracle boundaries. |
| 18. Selector overload | ALREADY DONE | Default landing selector already narrowed on October 13. |
| 19. Documentation mismatch | IMPLEMENT | README lists all ten profiles; targeting clarifies algorithm use. |
| 20. Visual review | REQUIRED QA | Regenerate all 20 PDFs, verify one-page A4 and compare actual renders. |
| 21. Additional claim risk | IMPLEMENT | Rephrase backend 'exactly-once replay' as idempotent operation replay. |

## Provenance and scope

- Earlier direct source evidence: PS-form `main.c` (`calc_floor_sum`, `try_solve_affine`, `try_solve_for_const`, one-sided witness strategy), `psf_total_harness_v3.py`; UniversalToolchain `LanguageCompiler.cs` and `LanguagePlanVerifier.cs`; botay `feasibility.py` and `sync/commands.py`.
- No edits to work experience, awards, academic institution, dates of projects, or professional positions.
- No new formal-verification claim, seniority, external-user metric, salary, performance benchmark or confidential company detail.
- Generated HTML/PDF must be produced by canonical tools and validated; build correctness is not proof of visual quality.
