# QA report - targeted CV v29

## Scope

- 17 HTML files parse; local links/fragments resolve and IDs are unique.
- Detailed HTML and focused PDFs use the current Wist2 result: 1,358/1,358 tests, 0 failures, build succeeded.
- Stale `75 projects / 1,325 tests` and duplicated `differential testing` wording are absent from the public HTML surface.
- Russian C++ systems labels are localized without changing conventional identifiers.
- All 14 role PDFs remain single-page A4 documents with a text layer and clickable links.
- Compiler RU/EN and C++ systems RU/EN are rebuilt at `scale=1.0`; the strict 8.45 pt readability gate applies to these four focused PDFs.
- `MANIFEST.sha256` verifies after a clean generated commit.

## Evidence boundaries

- MEPhI result tables support the top total score in Engineering Sciences (2025) and Information Technology (2026).
- The Baltic result is stated as a first-degree diploma plus the Grand Prize, without claiming a unique nationwide rank.
- Assembly claims remain split between NASM IA-32/CDECL/x87 evidence and the separate x86-64 SysV code-generation laboratory.

## Print-layout result

```json
{
  "ru-compiler.html": {
    "minCssFontPx": 11.3333,
    "usedRatio": 0.8889492072771815,
    "overflow": false
  },
  "en-compiler.html": {
    "minCssFontPx": 11.3333,
    "usedRatio": 0.8286354588605392,
    "overflow": false
  },
  "ru-cpp-systems.html": {
    "minCssFontPx": 11.3333,
    "usedRatio": 0.9066967330632926,
    "overflow": false
  },
  "en-cpp-systems.html": {
    "minCssFontPx": 11.3333,
    "usedRatio": 0.8310296348881558,
    "overflow": false
  }
}
```

## Focused-PDF result

```json
{
  "Mikhail_Razakov_CPP_Systems_EN.pdf": {
    "pages": 1,
    "min_font_pt": 8.5,
    "text_chars": 2527,
    "links": 7
  },
  "Mikhail_Razakov_CPP_Systems_RU.pdf": {
    "pages": 1,
    "min_font_pt": 8.5,
    "text_chars": 2832,
    "links": 7
  },
  "Mikhail_Razakov_Compiler_EN.pdf": {
    "pages": 1,
    "min_font_pt": 8.5,
    "text_chars": 2572,
    "links": 6
  },
  "Mikhail_Razakov_Compiler_RU.pdf": {
    "pages": 1,
    "min_font_pt": 8.5,
    "text_chars": 2796,
    "links": 6
  }
}
```

## Human render review

Before/after renders for all four rebuilt PDFs were reviewed at full-page and readable zoom. No clipping, overlap, broken glyphs, accidental second page, or unreadably small column was found. The increased font floor improves reading without compromising the one-page hierarchy.

## Verdict

**PASS / GO.** The four focused PDFs are suitable for first-contact applications; detailed HTML pages remain supporting technical portfolios.
