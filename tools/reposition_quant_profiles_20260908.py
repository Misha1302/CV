from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "site.json"


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    data["version"] = max(int(data.get("version", 0)), 57)
    data["updated_at"] = "2026-09-08"

    order = [key for key in data["profile_order"] if key != "quantdev"]
    insert_at = order.index("quant") if "quant" in order else len(order)
    order.insert(insert_at, "quantdev")
    data["profile_order"] = order

    data["profile_ui"]["quantdev"] = {
        "label_ru": "Quant Developer / Research Engineer",
        "label_en": "Quant Developer / Research Engineer",
        "landing_title": "Quant Developer / Research Engineer",
        "landing_description_ru": (
            "C++/Python, алгоритмы, профессиональный LLVM/static-analysis опыт, "
            "консервативные преобразования и воспроизводимая экспериментальная проверка."
        ),
    }
    data["profile_ui"]["quant"] = {
        "label_ru": "Quant Research — selective",
        "label_en": "Quant Research — selective",
        "landing_title": "Quant Research Candidate",
        "landing_description_ru": (
            "Research-oriented CS профиль: controlled experiments, exact/reference oracles, "
            "randomized/metamorphic validation и алгоритмическое исследование без неподтверждённых finance claims."
        ),
    }
    data["profile_ui"]["systems"] = {
        "label_ru": "C++ / Systems",
        "label_en": "C++ / Systems",
        "landing_title": "C++ / Systems Engineer · LLVM · x86-64",
        "landing_description_ru": (
            "LLVM, x86-64 codegen/register allocation, алгоритмы, program analysis и "
            "дифференциальная проверка машинного кода."
        ),
    }

    recognition_ru = [
        [
            "2025–2026",
            "«Высшая проба»",
            "Призёр «Высшей пробы» по олимпиадному и промышленному программированию.",
        ],
        [
            "2025–2026",
            "Всероссийские конкурсы",
            "Абсолютный победитель конкурса «Юниор» НИЯУ МИФИ в 2025 и 2026 годах; "
            "диплом I степени и Главная премия Балтийского научно-инженерного конкурса.",
        ],
    ]
    recognition_en = [
        [
            "2025–2026",
            "HSE Vysshaya Proba",
            "Prize-winner in HSE Vysshaya Proba in competitive and industrial programming.",
        ],
        [
            "2025–2026",
            "National competitions",
            "Overall winner of the MEPhI Junior competition in 2025 and 2026; "
            "first-degree diploma and Grand Prize at the Baltic science and engineering competition.",
        ],
    ]

    isp_ru = {
        "date": "2026 — сейчас",
        "title": "ИСП РАН — инженер по статическому анализу",
        "org": "SharpChecker · C#/.NET · program analysis",
        "bullets": [
            "Участвую в разработке SharpChecker — промышленной платформы статического анализа C#/.NET в ИСП РАН."
        ],
    }
    isp_en = {
        "date": "2026 — present",
        "title": "ISP RAS — Static Analysis Engineer",
        "org": "SharpChecker · C#/.NET · program analysis",
        "bullets": [
            "Contribute to SharpChecker, ISP RAS's industrial static-analysis platform for C#/.NET."
        ],
    }
    mcst_ru = {
        "date": "1 июля — 31 августа 2026",
        "title": "МЦСТ — стажёр по разработке компиляторов",
        "org": "LLVM 22 · C++23 · Python · 0,25 ставки",
        "bullets": [
            "Реализовал LLVM LICM-pass на C++: допустимость преобразования определяется по структуре цикла, обращениям к памяти, side effects и speculative safety.",
            "Построил Python-harness для сравнения исполнения до/после оптимизации и явной проверки transformation / no-transformation cases; также реализовал RPO, Dijkstra, Dinic и Tarjan SCC на C++23.",
        ],
    }
    mcst_en = {
        "date": "July 1 — August 31, 2026",
        "title": "MCST — Compiler Engineering Intern",
        "org": "LLVM 22 · C++23 · Python · 0.25 FTE",
        "bullets": [
            "Implemented an LLVM LICM pass in C++; transformation legality is derived from loop structure, memory accesses, side effects, and speculative-safety constraints.",
            "Built a Python harness comparing execution before/after optimization and checking explicit transformation / no-transformation cases; also implemented RPO, Dijkstra, Dinic, and Tarjan SCC in C++23.",
        ],
    }

    data["profiles"]["quantdev"] = {
        "ru": {
            "filename": "ru-quant-dev.html",
            "pdf": "Mikhail_Razakov_Quant_Developer_RU.pdf",
            "title": "Михаил Разаков — Quant Developer / Research Engineer | C++ · Python",
            "role": "Quant Developer / Research Engineer | C++ · Python",
            "brand": "C++ · Python · алгоритмы · research engineering",
            "eyebrow": "Алгоритмы · экспериментальная проверка · correctness-critical systems",
            "summary": (
                "Research engineer с профессиональным опытом compiler/static analysis и сильной базой C++/Python и алгоритмов. "
                "Разрабатываю correctness-critical анализы и экспериментальную инфраструктуру: exact/reference oracles, "
                "differential/randomized/metamorphic testing, воспроизводимые harnesses и консервативные LLVM-преобразования."
            ),
            "description": (
                "Quant Developer / Research Engineer Михаил Разаков: C++, Python, LLVM, алгоритмы, program analysis, "
                "exact/reference oracles и воспроизводимая экспериментальная проверка."
            ),
            "proofs": [
                [
                    "Профессиональный engineering",
                    "ИСП РАН: промышленный static analysis C#/.NET; МЦСТ: LLVM 22, C++23, optimization legality и verification harnesses.",
                ],
                [
                    "Алгоритмы и исследование",
                    "PS-form: conservative solver, exact oracle, randomized/metamorphic validation; UniversalToolchain: controlled verifier experiment.",
                ],
                [
                    "C++ / Python research tooling",
                    "LLVM, Python harnesses, graph algorithms, differential execution, reproducible counterexamples и test oracles.",
                ],
            ],
            "experience": [copy.deepcopy(isp_ru), copy.deepcopy(mcst_ru)],
            "project_ids": ["psform", "globaliv", "wist"],
            "skills": [
                ["Programming", "C++23, Python, C17, C#, Rust"],
                ["Algorithms & analysis", "data structures, graph algorithms, CFG/SSA, program analysis, memory dependence"],
                ["Research engineering", "exact/reference oracles, differential/randomized/metamorphic testing, reproducible harnesses, counterexamples"],
                ["Systems", "LLVM 22, x86-64, Linux, CMake, generated-code analysis"],
            ],
            "recognition": recognition_ru,
            "contact_heading": "Целевые роли: Quant Developer · Research Engineer · Algorithm / Research Software Engineering",
            "footer": "Quant Developer / Research Engineer · C++ · Python",
            "print_project_limit": 3,
        },
        "en": {
            "filename": "en-quant-dev.html",
            "pdf": "Mikhail_Razakov_Quant_Developer_EN.pdf",
            "title": "Mikhail Razakov — Quant Developer / Research Engineer | C++ · Python",
            "role": "Quant Developer / Research Engineer | C++ · Python",
            "brand": "C++ · Python · algorithms · research engineering",
            "eyebrow": "Algorithms · experimental validation · correctness-critical systems",
            "summary": (
                "Research engineer with professional compiler/static-analysis experience and a strong C++/Python algorithms background. "
                "I build correctness-critical analyses and experimental infrastructure using exact/reference oracles, "
                "differential/randomized/metamorphic testing, reproducible harnesses, and conservative LLVM transformations."
            ),
            "description": (
                "Mikhail Razakov — Quant Developer / Research Engineer: C++, Python, LLVM, algorithms, program analysis, "
                "exact/reference oracles, and reproducible experimental validation."
            ),
            "proofs": [
                [
                    "Professional engineering",
                    "ISP RAS: industrial C#/.NET static analysis; MCST: LLVM 22, C++23, optimization legality, and verification harnesses.",
                ],
                [
                    "Algorithms & research",
                    "PS-form: conservative solver, exact oracle, randomized/metamorphic validation; UniversalToolchain: controlled verifier experiment.",
                ],
                [
                    "C++ / Python research tooling",
                    "LLVM, Python harnesses, graph algorithms, differential execution, reproducible counterexamples, and test oracles.",
                ],
            ],
            "experience": [copy.deepcopy(isp_en), copy.deepcopy(mcst_en)],
            "project_ids": ["psform", "globaliv", "wist"],
            "skills": [
                ["Programming", "C++23, Python, C17, C#, Rust"],
                ["Algorithms & analysis", "data structures, graph algorithms, CFG/SSA, program analysis, memory dependence"],
                ["Research engineering", "exact/reference oracles, differential/randomized/metamorphic testing, reproducible harnesses, counterexamples"],
                ["Systems", "LLVM 22, x86-64, Linux, CMake, generated-code analysis"],
            ],
            "recognition": recognition_en,
            "contact_heading": "Target roles: Quant Developer · Research Engineer · Algorithm / Research Software Engineering",
            "footer": "Quant Developer / Research Engineer · C++ · Python",
            "print_project_limit": 3,
        },
    }

    quant_ru = data["profiles"]["quant"]["ru"]
    quant_ru.update(
        {
            "title": "Михаил Разаков — Quantitative Research Candidate | C++ · Python · Experimental Research",
            "role": "Quantitative Research Candidate | C++ · Python · Experimental Research",
            "brand": "C++ · Python · controlled experiments · algorithms",
            "eyebrow": "Controlled experiments · exact oracles · алгоритмическое исследование",
            "summary": (
                "Research-oriented CS student с профессиональным compiler/static-analysis опытом и практикой C++/Python. "
                "Проектирую controlled experiments, exact/reference oracles, randomized/metamorphic проверки и воспроизводимые "
                "исследования контрпримеров; текущая сильнейшая evidence-база — алгоритмы, program analysis и systems research."
            ),
            "description": (
                "Quantitative Research Candidate Михаил Разаков: C++, Python, controlled experiments, exact/reference oracles, "
                "randomized/metamorphic validation и алгоритмическое исследование."
            ),
            "proofs": [
                [
                    "Controlled experiments",
                    "UniversalToolchain: frozen corpus, valid controls, post-freeze holdouts, paired comparison и repeated timing runs.",
                ],
                [
                    "Математическое и алгоритмическое reasoning",
                    "PS-form: normalization, modular/GCD reasoning, exact affine analysis и independent exact oracle.",
                ],
                [
                    "C++ / Python research tooling",
                    "LLVM, Python harnesses, randomized/metamorphic testing, reproducible counterexamples и differential execution.",
                ],
            ],
            "experience": [copy.deepcopy(isp_ru), copy.deepcopy(mcst_ru)],
            "project_ids": ["wist", "psform", "globaliv"],
            "skills": [
                ["Programming", "C++23, Python, C17, C#"],
                ["Experimental methods", "controlled experiments, exact/reference oracles, randomized/metamorphic testing, reproducibility"],
                ["Algorithms & CS", "data structures, graph algorithms, program analysis, CFG/SSA, compiler optimizations"],
                ["Research tooling", "Python harnesses, Linux, Git, CMake, counterexample analysis"],
            ],
            "recognition": recognition_ru,
            "contact_heading": "Целевые роли: Quantitative Research internships / research roles, где ценятся алгоритмы и строгая экспериментальная проверка",
            "footer": "Quantitative Research Candidate · C++ · Python · Experimental Research",
            "print_project_limit": 3,
        }
    )

    quant_en = data["profiles"]["quant"]["en"]
    quant_en.update(
        {
            "title": "Mikhail Razakov — Quantitative Research Candidate | C++ · Python · Experimental Research",
            "role": "Quantitative Research Candidate | C++ · Python · Experimental Research",
            "brand": "C++ · Python · controlled experiments · algorithms",
            "eyebrow": "Controlled experiments · exact oracles · algorithmic research",
            "summary": (
                "Research-oriented CS student with professional compiler/static-analysis experience and hands-on C++/Python. "
                "I design controlled experiments, exact/reference oracles, randomized/metamorphic checks, and reproducible "
                "counterexample studies; my strongest current evidence is in algorithms, program analysis, and systems research."
            ),
            "description": (
                "Mikhail Razakov — Quantitative Research Candidate: C++, Python, controlled experiments, exact/reference oracles, "
                "randomized/metamorphic validation, and algorithmic research."
            ),
            "proofs": [
                [
                    "Controlled experiments",
                    "UniversalToolchain: frozen corpus, valid controls, post-freeze holdouts, paired comparison, and repeated timing runs.",
                ],
                [
                    "Mathematical & algorithmic reasoning",
                    "PS-form: normalization, modular/GCD reasoning, exact affine analysis, and an independent exact oracle.",
                ],
                [
                    "C++ / Python research tooling",
                    "LLVM, Python harnesses, randomized/metamorphic testing, reproducible counterexamples, and differential execution.",
                ],
            ],
            "experience": [copy.deepcopy(isp_en), copy.deepcopy(mcst_en)],
            "project_ids": ["wist", "psform", "globaliv"],
            "skills": [
                ["Programming", "C++23, Python, C17, C#"],
                ["Experimental methods", "controlled experiments, exact/reference oracles, randomized/metamorphic testing, reproducibility"],
                ["Algorithms & CS", "data structures, graph algorithms, program analysis, CFG/SSA, compiler optimizations"],
                ["Research tooling", "Python harnesses, Linux, Git, CMake, counterexample analysis"],
            ],
            "recognition": recognition_en,
            "contact_heading": "Target roles: Quantitative Research internships / research roles valuing algorithms and rigorous experimental validation",
            "footer": "Quantitative Research Candidate · C++ · Python · Experimental Research",
            "print_project_limit": 3,
        }
    )

    systems_ru = data["profiles"]["systems"]["ru"]
    systems_ru.update(
        {
            "title": "Михаил Разаков — C++ / Systems Engineer | LLVM · x86-64 · Algorithms",
            "role": "C++ / Systems Engineer | LLVM · x86-64 · Algorithms",
            "brand": "C++23 · LLVM · x86-64 · algorithms",
            "eyebrow": "Compiler optimization · machine code · program analysis",
            "summary": (
                "C++/systems engineer с профессиональным LLVM и static-analysis опытом. Работаю с optimization legality, "
                "графовыми алгоритмами, x86-64 codegen/register allocation и differential execution; фокус — correctness, "
                "machine-level behavior и воспроизводимая проверка."
            ),
            "description": (
                "C++ / Systems Engineer Михаил Разаков: C++23, LLVM 22, x86-64 code generation, register allocation, "
                "algorithms, program analysis и differential execution."
            ),
            "proofs": [
                ["Professional systems / analysis", "МЦСТ: LLVM 22/C++23 optimization; ИСП РАН: промышленный C#/.NET static analysis."],
                ["x86-64 pipeline", "SSA/CFG validation, liveness/interference, linear scan, seeded simulated annealing, SysV codegen и differential execution."],
                ["Conservative optimization", "LLVM Global-IV: APInt affine evolution, transitive effects, explicit legality и 29 verifier/idempotence/execution regressions."],
            ],
            "experience": [copy.deepcopy(isp_ru), copy.deepcopy(mcst_ru)],
            "project_ids": ["codegen", "globaliv", "psform"],
            "skills": [
                ["C++ / toolchain", "C++23, C17, LLVM 22, CMake, Linux, clang-tidy, ASan/UBSan"],
                ["Algorithms / analysis", "graph algorithms, CFG, dominance, SSA, SCC, dataflow, memory dependence"],
                ["Machine-level systems", "x86-64 SysV, code generation, liveness/interference, register allocation, generated-code analysis"],
                ["Verification", "exact/reference oracles, differential/metamorphic testing, isolated execution, reproducible counterexamples"],
            ],
            "recognition": recognition_ru,
            "contact_heading": "Целевые роли: C++ systems · compiler/runtime · trading infrastructure · performance engineering",
            "footer": "C++ / Systems Engineer · LLVM · x86-64 · Algorithms",
            "print_project_limit": 3,
        }
    )

    systems_en = data["profiles"]["systems"]["en"]
    systems_en.update(
        {
            "title": "Mikhail Razakov — C++ / Systems Engineer | LLVM · x86-64 · Algorithms",
            "role": "C++ / Systems Engineer | LLVM · x86-64 · Algorithms",
            "brand": "C++23 · LLVM · x86-64 · algorithms",
            "eyebrow": "Compiler optimization · machine code · program analysis",
            "summary": (
                "C++/systems engineer with professional LLVM and static-analysis experience. I work on optimization legality, "
                "graph algorithms, x86-64 code generation/register allocation, and differential execution, with a focus on "
                "correctness, machine-level behavior, and reproducible validation."
            ),
            "description": (
                "Mikhail Razakov — C++ / Systems Engineer: C++23, LLVM 22, x86-64 code generation, register allocation, "
                "algorithms, program analysis, and differential execution."
            ),
            "proofs": [
                ["Professional systems / analysis", "MCST: LLVM 22/C++23 optimization; ISP RAS: industrial C#/.NET static analysis."],
                ["x86-64 pipeline", "SSA/CFG validation, liveness/interference, linear scan, seeded simulated annealing, SysV codegen, and differential execution."],
                ["Conservative optimization", "LLVM Global-IV: APInt affine evolution, transitive effects, explicit legality, and 29 verifier/idempotence/execution regressions."],
            ],
            "experience": [copy.deepcopy(isp_en), copy.deepcopy(mcst_en)],
            "project_ids": ["codegen", "globaliv", "psform"],
            "skills": [
                ["C++ / toolchain", "C++23, C17, LLVM 22, CMake, Linux, clang-tidy, ASan/UBSan"],
                ["Algorithms / analysis", "graph algorithms, CFG, dominance, SSA, SCC, dataflow, memory dependence"],
                ["Machine-level systems", "x86-64 SysV, code generation, liveness/interference, register allocation, generated-code analysis"],
                ["Verification", "exact/reference oracles, differential/metamorphic testing, isolated execution, reproducible counterexamples"],
            ],
            "recognition": recognition_en,
            "contact_heading": "Target roles: C++ systems · compiler/runtime · trading infrastructure · performance engineering",
            "footer": "C++ / Systems Engineer · LLVM · x86-64 · Algorithms",
            "print_project_limit": 3,
        }
    )

    data["projects"]["wist"]["result_ru"] = (
        "Текущий exact test manifest: 1 324/1 324. В frozen-corpus verifier experiment режим B2 обнаружил "
        "32/32 primary и 10/10 challenge operators при 0/100 false positives на valid controls; отдельно проверены 4 post-freeze holdouts."
    )
    data["projects"]["wist"]["result_en"] = (
        "Current exact test manifest: 1,324/1,324. In a frozen-corpus verifier experiment, B2 detected "
        "32/32 primary and 10/10 challenge operators with 0/100 false positives on valid controls; four post-freeze holdouts were checked separately."
    )

    def refresh_counts(value):
        if isinstance(value, dict):
            return {key: refresh_counts(item) for key, item in value.items()}
        if isinstance(value, list):
            return [refresh_counts(item) for item in value]
        if isinstance(value, str):
            return (
                value.replace("1,306/1,306", "1,324/1,324")
                .replace("1 306/1 306", "1 324/1 324")
            )
        return value

    data = refresh_counts(data)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
