# QA report — targeted CV v31

- Source baseline: CV v30 / `dd725723029479767fadc788b925ad2dfdcb4f4e`.
- Wist2 evidence baseline: canonical verification record dated 2026-07-25.
- Updated HTML: all RU/EN targeted variants, full portfolio and selector.
- Rebuilt PDF: all 14 targeted variants from canonical generated print sources.
- Export contract: A4, one page, `scale=1.0`, minimum font >= 8.4 pt, selectable text and clickable links.
- Canonical Wist2 gate: 1,459/1,459 passed, 0 failed/skipped, 0 build warnings/errors, 9 packages and clean consumers.
- Claim boundaries retained: PlanFuzz is experimental/non-packable; SSA is opt-in/partial; no sandbox or performance-superiority claim.

PDF metrics are stored in the workflow evidence artifact as `pdf-report.json`; rendered PNGs are included for manual review.
