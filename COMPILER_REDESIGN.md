# Compiler CV redesign

The compiler profile uses the shared `data/site.json` model for person, experience, project, link, and result data.

`tools/build_compiler_redesign.py` owns only compiler-profile presentation and concise localized labels. It generates:

- `ru-compiler.html`
- `en-compiler.html`

The normal asset workflow runs the main site generator first, then this role-specific renderer, then creates and validates all one-page PDFs.

## Local checks

```bash
python tools/build_site.py
python tools/build_compiler_redesign.py
python tools/build_compiler_redesign.py --check
python tools/build_cv.py --output-dir pdf
python tools/validate_cv.py --pdf-dir pdf
```

## Design decisions

- The portrait stays on the first screen; the Wist2 pipeline lives inside the featured project.
- Hero text and mobile controls are compact; language switching is only in the header.
- Recognition is raised above projects as external evidence.
- Wist2, PlanFuzz, and PS-form are the only featured projects.
- Case-study links are preserved.
- The downloadable PDF is generated from the same HTML and validated as a one-page A4 document.
