# QA report — targeted CV v16

## Release scope

- 13 HTML pages.
- 10 two-page A4 PDFs.
- Shared CSS, JavaScript, favicon and social preview image.
- HSE University enrollment/status update and preservation of v15 layout/link fixes.

## Requested changes

Status: **PASS**.

- official HSE University admission is reflected in all 12 Russian/English CV pages;
- the education section names the Faculty of Computer Science, programme 09.03.04 Software Engineering, 2026–2030 period and September 2026 start;
- all pages include a compact HSE status in the hero context; each education record links to the official programme page;
- stale planned-admission / secondary-education wording is absent;

- `https://lms-185-102-139-43.sslip.io/` is present in every relevant Russian and English CompilationLabLMS project card;
- the LMS URL is carried into the relevant generated PDFs;
- project links and technology tags are separated by a stable 14 px desktop / 13 px mobile gap;
- cards without links retain their original bottom-aligned technology tags;
- the project grid keeps equal-height cards without link/tag collisions.

## Browser and layout checks

- no duplicate IDs;
- no missing local files or broken fragment links;
- reciprocal RU/EN navigation;
- no horizontal overflow at 1440, 1255, 1024, 900, 768, 560, 390 and 320 px;
- project-card footer geometry checked on desktop and mobile;
- shared JavaScript passes syntax validation and produces no page errors in the inlined multi-viewport browser check.

## PDF checks

- 10/10 PDFs contain exactly two A4 pages;
- all PDF pages render without clipping, overlap, missing glyphs or black squares;
- PDF text remains selectable and links remain clickable;
- LMS link annotations are present in Backend, Reliability and EdTech PDFs in both languages.

## External URL availability

The supplied LMS URL was added exactly as requested. The build environment could not resolve the `sslip.io` hostname, so live HTTP availability is not claimed here.

`EVIDENCE_STATUS: VERIFIED` for delivered HTML/PDF contents, HSE programme naming, spacing, rendering and package integrity; the personal admission status is `USER-REPORTED` by the candidate.
