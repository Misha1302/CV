# QA report - targeted CV v30

## Scope

- Compiler RU/EN were reviewed against v29 and rebuilt at scale=1.0.
- Education, Wist2 qualifiers, LLVM-track positioning, Russian terminology, typography and technical communication were checked.
- All 17 HTML files parse; local links/fragments resolve and IDs are unique.
- All 14 PDFs remain one-page A4 documents with text layers and clickable links.
- ATS validation checks the main reading flow separately from the side-column education marker.
- `MANIFEST.sha256` is regenerated after temporary files are removed.

## Layout result

```json
{
  "ru-compiler.html": {
    "clientHeight": 1123,
    "scrollHeight": 1123,
    "clientWidth": 794,
    "scrollWidth": 794,
    "minCssFontPx": 11.3333,
    "usedRatio": 0.9047758243899723
  },
  "en-compiler.html": {
    "clientHeight": 1123,
    "scrollHeight": 1123,
    "clientWidth": 794,
    "scrollWidth": 794,
    "minCssFontPx": 11.3333,
    "usedRatio": 0.8310296348881558
  }
}
```

## Focused PDF result

```json
{
  "Mikhail_Razakov_Compiler_EN.pdf": {
    "pages": 1,
    "min_font_pt": 8.5,
    "text_chars": 2678,
    "links": 6
  },
  "Mikhail_Razakov_Compiler_RU.pdf": {
    "pages": 1,
    "min_font_pt": 8.5,
    "text_chars": 2917,
    "links": 6
  }
}
```

## ATS text-layer result

- Extracted main flow is ordered as identity → Wist2 experience → MCST/LLVM experience → selected projects.
- The PS-form project heading is used as the unique project marker; the shorter `PS-form` token also appears earlier in the proof strip and is therefore not a valid ordering marker.
- Education and technical-communication sections are present in the side column and remain extractable.

## Human render review

The RU and EN before/after renders were reviewed at full-page and readable zoom. No clipping, overlap, broken glyphs, accidental second page, or unreadably small text was found. The revised proof hierarchy, LLVM-track wording, Software Engineering education, technical-communication block, and compact recognition text are visually legible.

## Verdict

**PASS / GO.** Compiler RU/EN are suitable for first-contact applications; detailed HTML pages remain supporting technical portfolios.
