# Compiler CV redesign

This branch contains an isolated redesign of the Russian and English compiler-focused CV pages.

## Source of truth

- `tools/build_compiler_redesign.py` — deterministic bilingual HTML generator; it reads shared contact metadata from `data/site.json`.
- `compiler-redesign.css` — styles scoped under `.compiler-redesign`.
- `ru-compiler.html`, `en-compiler.html` — generated outputs.

The regular site generator still owns the rest of the portfolio. Run the compiler generator last:

```bash
python3 tools/build_site.py
python3 tools/build_compiler_redesign.py
python3 tools/build_compiler_redesign.py --check
```

## Implemented changes

- simpler, role-oriented hero copy;
- explicit availability and conservative education wording;
- Wist pipeline instead of the decorative portrait card;
- exactly three primary projects with purpose, ownership, maturity, challenge, result, technologies, and links;
- a four-step engineering approach section;
- capability-oriented skills instead of a keyword cloud;
- expanded external achievements;
- one primary contact action and no stale PDF call-to-action.

## Validation performed

- Python bytecode compilation;
- deterministic build followed by `--check`;
- HTML parsing and required-section checks;
- Chromium rendering at desktop and mobile widths with horizontal-overflow assertions.

The PDF files were intentionally not changed in this branch because the available GitHub text-file connector cannot safely publish binary replacements. The redesigned pages do not advertise the old PDF as if it matched the new layout.
