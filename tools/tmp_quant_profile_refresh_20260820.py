#!/usr/bin/env python3
import json
from pathlib import Path

path = Path("data/site.json")
data = json.loads(path.read_text(encoding="utf-8"))
data["version"] = max(int(data.get("version", 0)), 36)
data["updated_at"] = "2026-08-20"

ru = data["profiles"]["quant"]["ru"]
ru.update({
    "title": "Михаил Разаков — Quantitative Research | C++ · Python · Algorithms",
    "role": "Quantitative Research | C++ · Python · алгоритмы",
    "brand": "C++ · Python · алгоритмы · эксперименты",
    "eyebrow": "Алгоритмы · проверка гипотез · количественные исследования",
    "summary": "Сильная база в computer science и алгоритмическом решении задач; практический опыт C++ и Python, компиляторов и самостоятельных исследовательских проектов. Работаю в цикле «гипотеза → эксперимент → проверка»: строю точные оракулы, randomized/metamorphic tests, Python-harnesses, измеримые benchmarks и воспроизводимые контрпримеры. Реализовывал LLVM-оптимизации, графовые алгоритмы и program analysis; этот подход напрямую переносится на data-driven quantitative research.",
    "description": "Quantitative Research профиль Михаила Разакова: C++, Python, алгоритмы, LLVM, program analysis, проверка гипотез, точные оракулы и воспроизводимые эксперименты.",
    "proofs": [
        ["Алгоритмы и соревнования", "Призёр «Высшей пробы»; абсолютный победитель конкурса «Юниор» НИЯУ МИФИ в 2025 и 2026 годах; Главная премия Балтийского научно-инженерного конкурса"],
        ["Гипотеза → эксперимент", "Точные оракулы, randomized/metamorphic testing, adversarial counterexamples, воспроизводимые harnesses и benchmarks"],
        ["C++ и Python", "LLVM/C++23 оптимизации, анализ программ и Python-инструменты для автоматизированной проверки гипотез"],
    ],
    "experience": [
        {
            "date": "1 июля — 31 августа 2026",
            "title": "МЦСТ — стажёр по разработке компиляторов",
            "org": "LLVM · C++23 · Python · 0,25 ставки",
            "bullets": [
                "Реализовал LLVM-проход loop-invariant code motion на C++; анализировал инвариантность, side effects, обращения к памяти, speculative safety и структуру циклов.",
                "Построил Python-harness, который сравнивает поведение до и после оптимизации и отдельно проверяет ожидаемые случаи transformation / no-transformation.",
                "Реализовал и протестировал на C++23 RPO с детектированием циклов, Dijkstra, Dinic max-flow и Tarjan SCC.",
            ],
        },
        {
            "date": "2026",
            "title": "PS-form Memory Dependence Analyzer",
            "org": "C17 · program analysis · экспериментальная проверка",
            "bullets": [
                "Занял 1-е место среди 49 решений: единственная оценка 5,0/5,0 и 104/104 официальных тестов.",
                "Построил точный оракул для малых областей, metamorphic/randomized проверки и воспроизводимые WA/TL-контрпримеры.",
            ],
        },
        {
            "date": "2024 — сейчас",
            "title": "UniversalToolchain / Wist2 — создатель и основной разработчик",
            "org": ".NET · компиляторы · языковые системы",
            "bullets": [
                "Самостоятельно спроектировал и развиваю сложную языковую систему с промежуточными представлениями, SSA/оптимизациями и interpreter/CIL backend-ами.",
                "Использую benchmarking, differential/metamorphic verification и воспроизводимые проверки для сравнения реализаций и конфигураций.",
                "Контрольная проверка от 25.07.2026: 1 465/1 465 тестов без падений по девяти пакетам и clean-consumer проектам.",
            ],
        },
    ],
    "skills": [
        ["Programming", "C++23, Python, C17, C#, Rust"],
        ["Алгоритмы и CS", "структуры данных, алгоритмы графов, program analysis, CFG/SSA, compiler optimizations"],
        ["Эксперименты и верификация", "формулировка и проверка гипотез, exact oracles, differential/metamorphic testing, randomized testing, benchmarks, анализ контрпримеров"],
        ["Research tooling", "LLVM, Linux, Git, CMake, Python-harnesses, AI/LLM-assisted research с независимой проверкой результатов"],
    ],
    "recognition": [
        ["2025–2026", "Олимпиады и инженерные конкурсы", "Призёр «Высшей пробы»; абсолютный победитель конкурса «Юниор» НИЯУ МИФИ в 2025 и 2026 годах; диплом I степени и Главная премия Балтийского научно-инженерного конкурса."],
        ["2026", "PS-form Memory Dependence Analyzer", "1-е место среди 49 решений; единственная оценка 5,0/5,0; 104/104 официальных тестов."],
        ["2025–2026", "Олимпиадное программирование", "Призёр регионального этапа ВсОШ по информатике и «Высшей пробы» по олимпиадному и промышленному программированию."],
    ],
    "contact_heading": "Открыт к quantitative research и research-software задачам, где важны алгоритмы, проверка гипотез и воспроизводимые эксперименты.",
    "footer": "Quantitative Research · C++ · Python · алгоритмы",
})

en = data["profiles"]["quant"]["en"]
en.update({
    "title": "Mikhail Razakov — Quantitative Research | C++ · Python · Algorithms",
    "role": "Quantitative Research | C++ · Python · Algorithms",
    "brand": "C++ · Python · algorithms · experiments",
    "eyebrow": "Algorithms · hypothesis testing · quantitative research",
    "summary": "Strong computer-science and algorithmic problem-solving background with hands-on C++ and Python, compiler engineering, and independent research-oriented projects. I work in a hypothesis → experiment → validation loop: exact oracles, randomized/metamorphic tests, Python harnesses, measurable benchmarks, and reproducible counterexamples. I have implemented LLVM optimizations, graph algorithms, and program-analysis tools; the same workflow transfers directly to data-driven quantitative research.",
    "description": "Mikhail Razakov quantitative-research profile: C++, Python, algorithms, LLVM, program analysis, hypothesis testing, exact oracles, and reproducible experiments.",
    "proofs": [
        ["Algorithms & competitions", "HSE Vysshaya Proba prize-winner; overall winner of the MEPhI Junior competition in 2025 and 2026; Grand Prize at the Baltic science and engineering competition"],
        ["Hypothesis → experiment", "Exact oracles, randomized/metamorphic testing, adversarial counterexamples, reproducible harnesses, and benchmarks"],
        ["C++ & Python", "LLVM/C++23 optimization work, program analysis, and Python tooling for automated hypothesis validation"],
    ],
    "experience": [
        {
            "date": "July 1 — August 31, 2026",
            "title": "MCST — compiler engineering intern",
            "org": "LLVM · C++23 · Python · 0.25 FTE",
            "bullets": [
                "Implemented an LLVM loop-invariant code-motion pass in C++; reasoned about loop invariance, side effects, memory access, speculative safety, and loop structure.",
                "Built a Python verification harness comparing execution behavior before and after optimization and checking expected transformation / no-transformation cases.",
                "Implemented and tested C++23 graph algorithms including RPO with cycle detection, Dijkstra, Dinic max-flow, and Tarjan SCC.",
            ],
        },
        {
            "date": "2026",
            "title": "PS-form Memory Dependence Analyzer",
            "org": "C17 · program analysis · experimental validation",
            "bullets": [
                "Ranked 1st of 49: the only 5.0/5.0 result and 104/104 official tests.",
                "Built an exact oracle for small domains, metamorphic/randomized checks, and reproducible wrong-answer/time-limit counterexamples.",
            ],
        },
        {
            "date": "2024 — present",
            "title": "UniversalToolchain / Wist2 — creator and primary developer",
            "org": ".NET · compilers · language systems",
            "bullets": [
                "Independently designed and developed a complex compiler/language system with intermediate representations, SSA/optimizations, and interpreter/CIL backends.",
                "Use benchmarking, differential/metamorphic verification, and reproducible checks to compare implementations and configurations.",
                "Verification as of July 25, 2026: 1,465/1,465 tests with zero failures across nine packages and clean-consumer projects.",
            ],
        },
    ],
    "skills": [
        ["Programming", "C++23, Python, C17, C#, Rust"],
        ["Algorithms & CS", "data structures, graph algorithms, program analysis, CFG/SSA, compiler optimizations"],
        ["Experiments & verification", "hypothesis formulation and validation, exact oracles, differential/metamorphic testing, randomized testing, benchmarks, counterexample analysis"],
        ["Research tooling", "LLVM, Linux, Git, CMake, Python harnesses, AI/LLM-assisted research with independent verification"],
    ],
    "recognition": [
        ["2025–2026", "Olympiads & engineering competitions", "HSE Vysshaya Proba prize-winner; overall winner of the MEPhI Junior competition in 2025 and 2026; first-degree diploma and Grand Prize at the Baltic science and engineering competition."],
        ["2026", "PS-form Memory Dependence Analyzer", "Ranked 1st of 49; the only 5.0/5.0 result; 104/104 official tests."],
        ["2025–2026", "Programming competitions", "Regional Russian informatics olympiad and HSE Vysshaya Proba prize-winner in competitive and industrial programming."],
    ],
    "contact_heading": "Open to quantitative research and research-software roles where algorithms, hypothesis testing, and reproducible experiments matter.",
    "footer": "Quantitative Research · C++ · Python · Algorithms",
})

# Intentionally leave global location metadata unchanged: Moscow / remote.
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
