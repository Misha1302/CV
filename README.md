# CV site — generated, role-specific, verifiable

This repository publishes Mikhail Razakov's CV site and role-specific PDFs.

## Canonical source

All public profile content lives in one file:

- `data/site.json`

The generator produces:

- canonical RU/EN profile pages;
- the landing page;
- project case studies;
- redirect pages for deprecated profile URLs;
- metadata, Open Graph, JSON-LD, sitemap, and robots.txt;
- one-page role-specific PDFs.

Generated HTML and PDF files must not be edited manually.

## Canonical profiles

1. General Software Engineer
2. Compiler / Language Platforms
3. .NET Backend
4. C++ / LLVM Systems

The landing page exposes only the three specializations plus the general profile. Older narrow URLs redirect to the nearest canonical profile.

## Local build

```bash
python -m pip install beautifulsoup4 pymupdf pillow playwright weasyprint
python tools/build_site.py
python tools/build_cv.py --output-dir pdf --evidence-dir /tmp/cv-pdf-evidence
python tools/build_site.py --manifest
python tools/validate_cv.py --pdf-dir pdf
```

For browser layout and screenshot regression:

```bash
python -m playwright install chromium
python tools/visual_regression.py --output-dir /tmp/cv-visual
```

## Validation contracts

The checks enforce:

- `data/site.json` as the single source of truth;
- no content rewriting from JavaScript;
- matching title, description, Open Graph, JSON-LD, visible role, print role, and PDF role;
- no stale availability wording;
- no untranslated English sentences in Russian profiles or Cyrillic in English profiles;
- valid internal links and optional live external-link checks;
- local portrait asset, no remote avatar dependency;
- one-page A4 PDFs with text layers and links;
- desktop, mobile, and JavaScript-disabled screenshot regressions;
- recursive SHA-256 manifest integrity.
