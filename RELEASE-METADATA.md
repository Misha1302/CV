# Release metadata

- Version: v25
- Date: 2026-07-23
- Previous baseline: `mikhail-razakov-targeted-cv-v24-2026-07-23.tar.xz`
- Previous baseline SHA-256: `ca01f7676fa8bdec3186383fa9e632abcd2e3c93463a92e688436fbd0d3b08bb`
- Scope: skills-section content and presentation correction, with priority on full RU/EN and compiler RU/EN; compiler PDF regeneration.
- HTML surface: 17 files.
- Downloadable CV surface: 14 one-page A4 PDFs.
- Included technical paper: 1 PDF.
- Canonical email: `misha13022008@gmail.com`.

## v25 correction

- Replaced the unstyled `skills-grid` / `skill-group` markup with the existing `stack-lines` / `stack-line` component on all 16 resume pages.
- Rewrote compiler RU/EN expertise sections as coherent prose under four role-relevant headings.
- Rewrote full RU/EN expertise sections to separate the primary compiler/program-analysis profile from complementary backend and systems work.
- Removed stale mixed-language headings and the `AdvancedAlgorithms` promotional insertion from the compiler skills block.
- Polished Russian compiler hero and project wording without changing factual scope.
- Regenerated compiler RU/EN PDFs; retained the other 12 validated v24 PDFs byte-for-byte.
- Updated local asset cache keys to `?v=25`.

## Evidence boundaries

- `AdvancedAlgorithms`: 12 modules listed by the checked repository snapshot; educational/interview-oriented library, not a blanket production-suitability claim.
- Wist2: experimental opt-in verifier-gated AIR → SSA → AIR route; no SSA-native-backend or unsupported performance claim.
- Wist2 numeric baseline: dated 2026-07-14 where retained — 75 .NET projects, 1,325 tests, 0 warnings/errors.
- PS-form Analyzer: conservative result semantics, exact/randomized/metamorphic verification and the cited 1/49, 104/104 result.
- x86-64 playground: explicitly educational; native code executes in a separate constrained runner, not a hardened sandbox.
- MCST: presented as internship experience and engineering discipline, not as an independent algorithm portfolio project.

## Publication boundary

- The archive is sendable as local HTML/PDF material.
- The public `Misha1302/CV` GitHub Pages deployment was not modified in this task and may still expose an older release; do not send the site URL until that repository is updated.
- Role PDFs list email, Telegram and GitHub only.

The final archive SHA-256 is reported externally at handoff to avoid self-referential release metadata.
