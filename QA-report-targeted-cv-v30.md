# QA report - targeted CV v30

## Scope

- Compiler RU/EN were reviewed against v29 and rebuilt at scale=1.0.
- Education, Wist2 qualifiers, LLVM-track positioning, Russian terminology, typography and technical communication were checked.
- All 17 HTML files parse; local links/fragments resolve and IDs are unique.
- All 14 PDFs remain one-page A4 documents with text layers and clickable links.
- ATS validation checks the main reading flow separately from the side-column education marker.
- MANIFEST.sha256 is regenerated after temporary files are removed.

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

## Automated verdict

**PASS.** Human before/after render review required before merge.
