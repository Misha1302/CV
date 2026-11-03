# Six application portfolio websites — implementation & QA

Date: 2026-11-03. Source: the current unified CV project.

## Direct public routes

| Application audience | Russian website | English website |
| --- | --- | --- |
| C#/.NET Backend / ATS | [RU](../../../ru-backend-ats.html) | [EN](../../../en-backend-ats.html) |
| Engineering / Tech Lead | [RU](../../../ru-tech-lead.html) | [EN](../../../en-tech-lead.html) |
| CLR / Compiler / Performance | [RU](../../../ru-runtime-compiler.html) | [EN](../../../en-runtime-compiler.html) |

Older RU/EN engineering URLs remain available and render the new Tech Lead edition with canonical URLs pointing at the explicit Tech Lead pages. Ten narrower specialty profiles and their PDF links remain unchanged.

## What each website displays

Each website uses the exact selected application_cvs variant in data/site.json, augmented by the same canonical project's problem / solution / result fields already used by case pages. It includes:

- Applicant name, role and summary; direct email, Telegram and GitHub links.
- Three professional experience records with dates and scope, without merging parallel work into a fictitious continuous employer tenure.
- All skills and all relevant project bullets, full problem / approach / outcome context, relevant source and detailed case links.
- Education and recognition; visible attribution/evidence boundaries and a link to the sanitized public evidence notes.
- Direct, role- and language-matched PDF, DOCX and Markdown downloads.
- Three-route specialization switcher, RU/EN toggle, keyboard focus and no-JavaScript operation.
- Canonical URLs, hreflang, metadata, social preview, JSON-LD and sitemap entries.

The user-facing presentation has a dedicated editorial layout with three subtle role accents (backend / engineering / runtime), typographic hierarchy, readable project cases and a mobile layout. No invented metrics, skill level or maturity claims were added.

## Actual local checks

| Check | Result |
| --- | --- |
| Canonical evidence validation | PASS — 35 evidence assets |
| All six website data matches, 3 profile switch links and PDF/DOCX/MD | PASS — tools/validate_application_sites.py |
| Existing HTML/PDF link and privacy validator | PASS — tools/validate_cv.py --skip-manifest |
| CV release and document integrity | PASS — tools/validate_release.py |
| 10 previously retained visual regression baseline cases | PASS |
| 77 smoke views across responsive breakpoints / JavaScript-disabled mode | PASS |
| Detailed Playwright page captures (including 390px mobile) | PASS — 10 views, no horizontal scroll and no JavaScript errors |
| JS-disabled six website navigation/content | PASS |
| Role switch and language switch | PASS |
| Local HTTP downloads for PDF, DOCX and Markdown | PASS |
| Full WCAG independent certification | NOT RUN |
| Public GitHub Pages delivery | To be checked by live-pages-smoke workflow after deploy |

## Technical honesty and privacy

Commercial tenure is candidate-attested. VpnMediator live usage should not be presented as independently measured in this change. UniversalToolchain counts belong to a repository manifest, not to a new full upstream test execution. TuringSquare-LMS is not yet a production launch; T-Bank tests are sandbox; partial agent-generated code is not claimed as fully personal implementation. Technical descriptions use the same bounded canonical site data as previously reviewed CV releases.

## Visual evidence

- [Backend RU desktop](backend-ru-desktop-full.webp) and [mobile](backend-ru-mobile-full.webp)
- [Engineering RU desktop](engineering-ru-desktop-full.webp) and [mobile](engineering-ru-mobile-full.webp)
- [Runtime RU desktop](runtime-ru-desktop-full.webp) and [mobile](runtime-ru-mobile-full.webp)
- [Backend EN desktop](backend-en-desktop-full.webp)
- [Runtime EN desktop](runtime-en-desktop-full.webp)

See [browser-qa.json](browser-qa.json) for tested pages, viewports, status codes, section counts and overflow measurements.
