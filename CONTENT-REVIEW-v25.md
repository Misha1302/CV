# Content review — v25

## Scope

Highest attention was given to:

- `ru.html` / `en.html`;
- `ru-compiler.html` / `en-compiler.html`;
- `Mikhail_Razakov_Compiler_RU.pdf` / `Mikhail_Razakov_Compiler_EN.pdf`.

## Confirmed defect

The previous compiler skills section was not acceptable despite correct factual coverage:

- Russian and English headings were mixed on the Russian page;
- each row was a raw keyword list rather than a readable competence statement;
- `AdvancedAlgorithms` was inserted into the toolchain row as promotional evidence instead of remaining a project;
- `skills-grid` and `skill-group` had no dedicated visual styling, so the section rendered as a flat text block.

## Implemented correction

Compiler RU/EN now use four coherent groups:

1. architecture and IR;
2. analysis and optimization;
3. correctness validation;
4. languages and toolchain.

Each group is written as a concise technical statement rather than a keyword dump. The Russian page uses Russian headings while retaining only domain terms whose translation would reduce precision.

Full RU/EN now explicitly separate:

- primary compiler and program-analysis expertise;
- optimization and analysis;
- algorithms and low-level work;
- complementary backend/operations experience;
- validation methods.

All resume variants use the row-based `stack-lines` component, producing a visible label/content hierarchy instead of unstyled paragraphs.

## Positioning retained

The portfolio still uses three complementary technical areas:

1. **Wist2** — compiler/runtime architecture and optimization algorithms inside an integrated IR pipeline;
2. **PS-form Analyzer** — conservative program analysis, symbolic/affine reasoning and exact-reference validation;
3. **AdvancedAlgorithms** — reusable classical algorithms and data structures on C++23 with explicit contracts and differential testing.

MCST remains internship experience only.

## Verdict

The corrected compiler PDF is suitable for direct applications. Full RU/EN remain portfolio pages for technical follow-up rather than first-contact attachments.
