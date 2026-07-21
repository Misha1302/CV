# Self-review — Quantitative & Trading Infrastructure CV Site

Review date: 22 July 2026

## Scope

Reviewed the English and Russian static CV pages for:

- factual restraint and role positioning;
- recruiter and technical-reader scan order;
- duplication and information density;
- HTML structure, navigation and local assets;
- desktop, tablet and mobile rendering;
- mobile-menu behavior and horizontal overflow.

## Content decisions

### Changed

- Moved `Selected work` before `Experience` so the strongest technical evidence appears first.
- Changed the role line to `C++ / Python Systems Engineer — Quantitative & Trading Infrastructure` while keeping the structured-data job title at `C++ / Python Systems Engineer`.
- Reduced the hero summary to current capabilities, MCST selection outcome and target internship type.
- Replaced compiler-specific hero cards with three faster screening signals: `1st / 49`, `C++23 / Python`, and the dated `1,325 tests` Wist2 baseline.
- Replaced the repeated graph-project card with a full Wist2 project card.
- Kept the x86-64 project explicitly described as educational.
- Removed Wist2 from the employment timeline to avoid presenting open-source work as paid employment and to prevent duplication.
- Reduced teaching to one evidence-bearing bullet.
- Split skills into `Core`, `Engineering` and `Additional` instead of implying equal depth in every technology.
- Added a short explanation of interest in quantitative infrastructure without claiming financial-market experience.
- Reduced English/Russian hybrid phrasing in the Russian page.

### Claims deliberately not made

The site does not claim:

- professional quant or trading experience;
- production HFT or low-latency networking;
- alpha research, pricing models, Sharpe, PnL or profitability;
- a numerical Wist2 performance advantage;
- production maturity for the experimental SSA route;
- that the 1,325-test figure is a continuously current repository total.

## Adversarial content review

### Strongest evidence retained

- MCST result: first among 49, only full score and only submission to pass all 104 official tests.
- PS-form solver: portfolio approach, exact/sound methods and oracle-based validation.
- Wist2: multi-stage compiler/runtime pipeline, verifier-gated AIR → SSA → AIR route and interpreter/CIL differential testing on the supported shared subset.
- x86-64 lab: liveness, linear-scan allocation, code generation and reference-interpreter comparison.

### Remaining positioning limitation

The site presents a strong systems/compiler candidate targeting quantitative infrastructure. It still does not provide direct evidence of market-data handling, order-book reconstruction, execution simulation or quantitative research. The wording is intentionally limited to target roles rather than current domain experience.

## Observed checks

Static checks on both `en-quant.html` and `ru-quant.html`:

- exactly one HTML doctype;
- exactly one `h1`;
- no duplicate element IDs;
- all internal anchors resolve;
- all local file references resolve;
- JSON-LD parses and uses a non-inflated systems-engineer job title;
- all external links opened in a new tab include `noopener noreferrer`;
- English and Russian pages use the same section order.

Chromium rendering was checked at:

- 1440 × 1000;
- 768 × 900;
- 390 × 844;
- 320 × 760.

Observed results:

- no horizontal overflow in either language at any checked viewport;
- no JavaScript or console errors;
- mobile menu opens and closes after selecting a section;
- section order is `top → work → experience → skills → recognition → education → contact`;
- desktop and mobile layouts preserve readable hierarchy and project ordering.

The repository integration reuses the existing `style.css`, `script.js`, favicon and Open Graph asset. A small page-scoped style block changes only the quantitative profile’s project grid and motivation paragraph, so existing CV variants are not affected.

## Remaining non-blocking gaps

- External website availability was not rechecked during this revision.
- Personal award/admission claims retain the evidence links already present in the source CV but were not independently revalidated in this edit pass.
- The quantitative profile has no generated PDF yet; only the browser versions are published.
