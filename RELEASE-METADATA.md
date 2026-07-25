# Release metadata — targeted CV v31

- Release date: 2026-07-25
- Baseline: v30 / `dd725723029479767fadc788b925ad2dfdcb4f4e`
- Scope: all RU/EN targeted HTML pages, all 14 targeted PDFs, selector, canonical facts, generators, validators and release evidence.

## Canonical facts

- Education: `Студент программы «Программная инженерия» НИУ ВШЭ` / `Software Engineering student at HSE University`.
- Wist2 verification: 1,459/1,459 tests, 0 failed, 0 skipped, Release build with 0 warnings/errors, 9 verified packages, clean template and cross-package consumer smoke.
- Wist2 architecture: typed cross-package language plans, exact manifest binding, fail-closed runtime policies, callable-first SSA and PlanFuzz experimental research tooling.
- Baltic award: `Диплом I степени и Главная премия «Совершенство как надежда» Балтийского научно-инженерного конкурса.`

## Artifact contract

- 14 targeted PDFs are generated from `data/cv-print-profiles.json` through `tools/build_cv.py`.
- CI rebuilds them in a clean directory and checks A4/one page, scale 1.0, text layer, links, minimum 8.4 pt font, canonical facts and recursive manifest equality.
- Full portfolio pages remain HTML follow-up artifacts and are not first-contact CVs.
