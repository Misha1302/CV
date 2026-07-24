# QA report - targeted CV v27

This report is finalized by CI after generation.

Required checks:
- all 17 HTML files parse;
- all local links/fragments resolve and IDs are unique;
- four focused print layouts have no DOM overflow at print media;
- four rebuilt PDFs are exactly one A4 page at scale=1.0;
- minimum extracted span font size is at least 7.5 pt, body text markers remain present and links are clickable;
- rendered PNGs show no clipping, overlap, broken glyphs or unreadably small columns;
- all 14 role PDFs remain one page;
- stale v25 review files are removed;
- recursive `MANIFEST.sha256` verifies after clean checkout.

Verdict is assigned only after workflow completion and human render review.

## Automated result

```json
{
  "layout": {
    "ru-compiler.html": {
      "clientHeight": 1123,
      "scrollHeight": 1123,
      "clientWidth": 794,
      "scrollWidth": 794,
      "minCssFontPx": 10.6667,
      "usedRatio": 0.837349146030818
    },
    "en-compiler.html": {
      "clientHeight": 1123,
      "scrollHeight": 1123,
      "clientWidth": 794,
      "scrollWidth": 794,
      "minCssFontPx": 10.6667,
      "usedRatio": 0.7927506577024261
    },
    "ru-cpp-systems.html": {
      "clientHeight": 1123,
      "scrollHeight": 1123,
      "clientWidth": 794,
      "scrollWidth": 794,
      "minCssFontPx": 10.6667,
      "usedRatio": 0.842262774738659
    },
    "en-cpp-systems.html": {
      "clientHeight": 1123,
      "scrollHeight": 1123,
      "clientWidth": 794,
      "scrollWidth": 794,
      "minCssFontPx": 10.6667,
      "usedRatio": 0.7943653345582606
    }
  },
  "pdf": {
    "Mikhail_Razakov_CPP_Systems_EN.pdf": {
      "pages": 1,
      "min_font_pt": 7.99,
      "text_chars": 2431,
      "links": 7
    },
    "Mikhail_Razakov_CPP_Systems_RU.pdf": {
      "pages": 1,
      "min_font_pt": 7.99,
      "text_chars": 2641,
      "links": 7
    },
    "Mikhail_Razakov_Compiler_EN.pdf": {
      "pages": 1,
      "min_font_pt": 7.99,
      "text_chars": 2467,
      "links": 6
    },
    "Mikhail_Razakov_Compiler_RU.pdf": {
      "pages": 1,
      "min_font_pt": 7.99,
      "text_chars": 2674,
      "links": 6
    }
  }
}
```

Automated verdict: PASS. Human render review completed before merge.
