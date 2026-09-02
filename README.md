# CV site — generated, role-specific, verifiable

All public profile content lives in `data/site.json`. Generated HTML and PDF files must not be edited manually.

## Public identity

The root page and default RU/EN CV present one professional identity: **Compiler Engineer** — LLVM · Program Analysis · Compiler / Language Infrastructure.

Direct-link variants exist for targeted applications:

1. `.NET Backend Engineer`
2. `C++ / Compiler Systems & Program Analysis`
3. `Quantitative Developer / Research Software`

They reorder evidence but keep the same professional history. ISP RAS and MCST are Professional Experience; independent systems stay under Projects. Older compiler URLs redirect to the public Compiler Engineer CV.

## Build and validation

```bash
python -m pip install beautifulsoup4 pymupdf pillow playwright weasyprint
python tools/build_site.py
python tools/build_cv.py --output-dir pdf --evidence-dir /tmp/cv-pdf-evidence
python tools/build_site.py --manifest
python tools/validate_cv.py --pdf-dir pdf
python -m playwright install chromium
python tools/visual_regression.py --output-dir /tmp/cv-visual
```

The browser matrix covers 1440, 1024, 768, and 390 px layouts plus JavaScript-disabled smoke checks. PDF validation enforces one-page A4 output, text extraction, links, role parity, and an ATS prefix containing identity, contact details, employers, and role-specific technologies.
