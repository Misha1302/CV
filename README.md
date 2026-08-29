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

1. Compiler / Static Analysis Engineer
2. Compiler / LLVM Engineer
3. .NET Backend / Platform Reliability
4. C++ / LLVM Systems
5. Quantitative Research / Research Software Engineering

The landing page uses the compiler/static-analysis profile as the default and exposes four role-specific alternatives. Profile navigation and landing-card labels are defined by the canonical `profile_ui` metadata in `data/site.json`. Older narrow URLs redirect to the nearest canonical profile.

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

The visual workflow keeps the established regression baseline for existing representative pages and additionally smoke-checks every generated RU/EN profile on desktop, mobile, and with JavaScript disabled. The capture directory also contains `current.json` with replayable layout metrics and image hashes.

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
- desktop, mobile, and JavaScript-disabled screenshot regression/smoke checks;
- recursive SHA-256 manifest integrity.
