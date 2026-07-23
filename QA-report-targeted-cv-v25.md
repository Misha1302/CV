# QA report — targeted CV v25

## Content checks

- Full RU/EN and compiler RU/EN were reviewed after the rewrite.
- Russian compiler HTML and PDF contain none of the rejected mixed-language headings or the old `AdvancedAlgorithms — 12 modules` skills insertion.
- Wist2 remains experimental and verifier-gated; no unsupported performance or production claim was added.
- Canonical email and update date remain synchronized.

## HTML checks

- 17 HTML files parse successfully.
- All 16 resume pages now use `stack-lines` / `stack-line`; no `skills-grid` or `skill-group` remains.
- All 16 resume pages were checked at 1440, 1100, 1001, 1000, 900, 761, 760, 560, 430 and 390 CSS px.
- Across 160 viewport checks: horizontal overflow 0 px; every skills row remains inside the viewport; no legacy skills markup remains.
- Compiler RU/EN and full RU/EN were additionally rendered at desktop, tablet and mobile widths for visual inspection.
- All local files and fragment links resolve; no duplicate IDs were found.
- Every `target="_blank"` link has `noopener noreferrer`.
- `script.js` passes `node --check`.
- Every HTML page references `style.css?v=25` and `script.js?v=25` where applicable.

## PDF checks

- Compiler RU/EN PDFs were regenerated from dedicated HTML sources using the revised expertise wording.
- Both changed PDFs are exactly one A4 page and were rendered at 180 DPI for visual inspection.
- No clipping, overlap, broken glyphs or unreadable columns were observed.
- Extracted PDF text contains none of the rejected compiler skills headings.
- The remaining 12 role PDFs are unchanged from the validated v24 baseline; all 14 PDFs were checked for a one-page count.

## Artifact checks

- Stale v24 review filenames were replaced with v25 equivalents.
- No `.git`, build/cache directories, `CHANGELOG.md`, environment files, keys or editor-temporary files are included.
- Recursive `MANIFEST.sha256` is regenerated after all edits.
- The final archive is extracted into a clean directory and every manifest entry is verified before handoff.

Verdict: GO. Clean-unpack verification completed before handoff.
