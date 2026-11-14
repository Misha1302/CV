# Mikhail Razakov

**Quantitative Research Candidate — Python · C++ · Time-Series Research**

Moscow / remote · [razakov.mikhail@outlook.com](mailto:razakov.mikhail@outlook.com) · [Telegram](https://t.me/Micodiy) · [GitHub](https://github.com/Misha1302)

## Profile

I work on algorithmic research and reproducible experiments in Python and C++. I prepared an XAGUSD OHLC benchmark and a blind price-channel calibration interface. My other projects compare verification policies using frozen fault cases, valid controls and reference oracles. I work on symbolic computation at ISP RAS and previously completed a C++/LLVM compiler internship at MCST. Predictive financial effectiveness is not established.

## Technical skills

- **Languages and data:** Python, NumPy, pandas, SciPy, C++23, GNU C17, SQL, Git, Linux
- **Mathematics and algorithms:** Integer arithmetic, affine models, modular/GCD checks, graph algorithms, OHLC and time-series processing
- **Research validation:** Deterministic experiments, valid controls, reference oracles, blind calibration, randomized/metamorphic testing and counterexample analysis

## Experience

**ISP RAS · SharpChecker · October 2026 — present**

- Working on symbolic computation for C#/.NET static program analysis.

**MCST · Compiler Engineering Internship · July — August 2026**

- Worked on experimental LLVM LICM with Python before/after checks. Implemented RPO, Dijkstra, Dinic and Tarjan SCC; a local fixture run passed 14/14 tests.

## Engineering projects

**Simple Parallel Channel Tracker**

Built a private Python multi-timeframe OHLC research prototype and a deterministic benchmark of 31 heuristically labeled cases across 10 timeframes. Both structural validators passed; blind calibration has 20 cases and eight relations. Labels were constructed retrospectively; there is no expert gold set, validated prediction or established profitability. Source remains private.

**[UniversalToolchain / Wist2](https://github.com/Misha1302/UniversalToolchain/blob/master/UniversalToolchain/Experiments/UniversalToolchain.ContractExperiments/README.md)**

Built an experimental comparison of four policies with frozen author-designed faults, valid controls, additional post-freeze cases and independent oracles. The outcomes are reproducible within the UniversalToolchain study, but internally designed corpora limit external validity. This is compiler-systems research, not a financial-market experiment.

**[PS-form Memory Dependence Analyzer](https://github.com/Misha1302/ps_form_analizer/tree/758001fdadba56b4f2bd7601464bd6fe0cd2b388)**

Built a GNU C17 analyzer using exact counting for supported affine cases, modular/GCD reasoning and comparisons to an independent oracle. An extended test run found five conservative maybe results where the oracle expected no. This reflects analysis incompleteness, not a financial forecast.

## Education

HSE University — Software Engineering

## Recognition

- **2025–2026 — MEPhI Junior:** First-degree diplomas in the Information Technologies section in 2025 and 2026.
- **2026 — MCST LLVM/C++ selection:** According to organizer correspondence: 5.0/5.0 and 104/104 official tests among 49 submitted solutions.
- **2026 — LangDev — UniversalToolchain:** Presented on 9 October 2026; organizer published the talk recording. [Talk recording](https://youtu.be/2jqmw-1c7kE)
