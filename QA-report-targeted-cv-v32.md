# QA report — targeted CV v32

## Automated gates

- all 14 PDFs rebuild from canonical JSON in a clean directory;
- committed and rebuilt PDF text/link surfaces match;
- A4, one page, scale 1.0 and minimum font 8.4 pt;
- flagship direct project links and minimum six links;
- flagship DOM fill at least 0.78;
- profile-specific ATS marker order;
- canonical education, Wist2 facts and stale-marker rejection;
- recursive `MANIFEST.sha256` equality.

## Manual review

Flagship RU/EN renders inspected for clipping, overlap, language noise, weak hierarchy and excessive whitespace. The v32 roomy layout uses free page height for larger type and spacing rather than additional claims.

## Status

PASS after clean rebuild and final permanent-CI validation.
