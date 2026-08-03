# CV site — canonical, role-specific, reproducible

This repository publishes Mikhail Razakov's role-specific CV site, ATS text exports, and tagged PDF files.

## Single source of truth

All public facts and profile content are owned by `data/site.json`. Exact evidence values such as the Wist2 verification date, count, scope, source commit, and source blob SHA live once under `evidence` and are formatted by the generators.

Generated HTML, ATS text, PDF, metadata, redirects, sitemap, and manifests must not be edited manually.

## Build

```bash
python -m pip install beautifulsoup4 pymupdf pillow playwright weasyprint
python tools/build_site.py
python tools/build_cv.py --output-dir pdf --evidence-dir /tmp/cv-evidence
python tools/validate_cv.py --pdf-dir pdf --check-external
python tools/visual_regression.py --output-dir /tmp/cv-visual
python tools/build_site.py --manifest
```

## Contracts

- compiler positioning is explicitly junior/intern;
- compiler PDF uses a single-column semantic order;
- all PDF annotations are external `https:` or `mailto:` URI actions;
- Wist2 exact facts are generated from one evidence owner;
- ATS plain text is generated rather than inferred from layout;
- HTML works without JavaScript at 320 px and 200% reflow;
- tagged PDF/UA output is validated for structure markers, text order, fonts, bounds, links, and page occupancy;
- CI performs two clean builds and compares normalized output plus SHA-256 manifests.
