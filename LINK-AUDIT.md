# Link audit — v16

## Local links

- 13 HTML pages parsed.
- All relative HTML, CSS, JavaScript, image and PDF references resolve inside the package.
- All fragment links point to existing IDs.
- RU/EN pairs remain reciprocal.
- All `target="_blank"` links include `noopener`.
- All visible links have labels.
- All 10 PDF buttons resolve to two-page PDF files in `pdf/`.

Result: **PASS**.

## PDF links

Each PDF page contains clickable annotations. Across the files, page 1 contains 5 links and page 2 contains 8–10 links, including contacts, portfolio, project repositories and evidence where relevant.

## Critical external evidence status

The evidence destinations from v12 are preserved. v16 adds the official HSE Software Engineering programme page as the source for programme name, faculty, direction code and duration.

| Link class | Status | Notes |
|---|---|---|
| HSE Software Engineering programme | VERIFIED | Official programme page confirms Faculty of Computer Science, direction 09.03.04 and four-year full-time format. |
| HSE «Высший пилотаж» official works list | VERIFIED | Official list and winner paper links are retained. |
| Winning paper direct Google Drive URL | PARTIAL | Provenance comes from the official HSE page. |
| MEPhI Junior 2025 and 2026 results | VERIFIED | Separate official result pages remain linked. |
| Baltic Science and Engineering Competition 2026 | VERIFIED | Official result page remains linked. |
| MCST internship program | VERIFIED | Confirms the LLVM/compiler track, not the private ranking. |
| HSE «Высшая проба» | PARTIAL | General official page is linked; no personal result page is available in the package. |

`EVIDENCE_STATUS: PARTIAL` because the personal «Высшая проба» result and private MCST ranking do not have public first-party evidence in the current source set.

## CompilationLabLMS

- Public LMS URL included in all relevant project cards: `https://lms-185-102-139-43.sslip.io/`.
- Local presence and PDF annotations are verified; external availability must be confirmed from a network with DNS access to sslip.io.
