from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "site.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    ui = data["profile_ui"]
    ui["general"]["landing_description_ru"] = (
        "Главный проект — UniversalToolchain: разрешение зависимостей и конфликтов, выбор реализаций, "
        "детерминированный порядок проходов и проверка конфигурации до запуска; профессиональный опыт LLVM и статического анализа."
    )
    ui["compiler_backend"]["landing_description_ru"] = (
        "x86-64 backend от SSA/CFG до native execution: анализ живости и интерференции, register allocation, spills, "
        "phi lowering и сравнение с эталонным интерпретатором; LLVM 22 — профессиональный опыт."
    )
    ui["program_analysis"]["landing_description_ru"] = (
        "Анализ потоков данных по Roslyn CFG до неподвижной точки и межпроцедурный LLVM-анализ эффектов и аффинной эволюции; "
        "профессиональный опыт статического анализа C#/.NET в ИСП РАН."
    )
    ui["compiler"]["landing_description_ru"] = (
        "Широкий профиль для compiler/program-analysis ролей: LLVM-преобразования, Roslyn data-flow и x86-64 backend — "
        "только три сильнейших публично проверяемых проекта."
    )

    ru = data["profiles"]["general"]["ru"]
    ru["summary"] = (
        "Инженер инфраструктуры компиляторов и языковых инструментов с профессиональным опытом LLVM и статического анализа. "
        "В UniversalToolchain реализовал разрешение зависимостей и конфликтов, выбор реализаций компонентов, детерминированный "
        "порядок проходов, маршрутизацию типизированных артефактов и проверку конфигурации до запуска; доклад об архитектуре проекта принят на LangDev’26."
    )
    ru["proofs"] = [
        [
            "Сборка компиляторного конвейера",
            "UniversalToolchain разрешает зависимости и конфликты, однозначно выбирает реализации и фиксирует порядок проходов и маршруты артефактов до запуска.",
        ],
        ["LLVM и статический анализ", "МЦСТ: разработка LLVM 22; ИСП РАН: статический анализ C#/.NET."],
        [
            "Проверка корректности",
            "1 324/1 324 теста; отдельно проверяются совпадение результатов интерпретатора и CIL-бэкенда и отказ от неподдерживаемых конфигураций до исполнения.",
        ],
    ]
    ru["skills"] = [
        [
            "Инфраструктура компилятора",
            "разрешение зависимостей и конфликтов, выбор реализаций, детерминированный порядок проходов, типизированные маршруты артефактов, проверка перед запуском",
        ],
        ["LLVM / IR", "C++23, LLVM 22/IR, CFG/SSA, анализ циклов, межпроцедурный анализ, условия применимости преобразований"],
        ["Backends / Runtime", ".NET, interpreter/CIL, SysV x86-64, register allocation, композиция runtime"],
        ["Проверка", "регрессионные тесты, LLVM Verifier, сравнение interpreter/backend, differential execution"],
    ]
    ru["project_summaries"]["wist"] = {
        "type": ".NET · инфраструктура компилятора и языков · детерминированная композиция",
        "solution": (
            "Модули языка разрешают зависимости и конфликты, однозначно выбирают реализации требуемых возможностей и runtime-компонентов, "
            "получают детерминированный порядок проходов и типизированные маршруты артефактов до создания runtime."
        ),
        "result": (
            "Текущий manifest: 1 324/1 324 теста; отдельно проверяются совпадение результатов interpreter/CIL и целостность конфигурации до исполнения."
        ),
    }
    ru["project_summaries"]["globaliv"] = {
        "type": "C++23 · LLVM 22 · межпроцедурный анализ · преобразования",
        "solution": (
            "LLVM 22 pass локализует поддерживаемые глобальные переменные, изменяющиеся как индукционные, после межпроцедурного анализа эффектов, "
            "аффинной эволюции и отдельной проверки условий применимости; APInt моделирует арифметику фиксированной разрядности."
        ),
        "result": (
            "29 позитивных и негативных регрессионных сценариев: LLVM Verifier, структурные ожидания, идемпотентность и сравнение наблюдаемого поведения до/после преобразования."
        ),
    }
    ru["project_summaries"]["codegen"] = {
        "type": "Rust · x86-64 backend · register allocation",
        "solution": (
            "Проверка SSA/CFG → анализ живости и интерференции → register allocation и spills → phi lowering → генерация кода SysV x86-64."
        ),
        "result": (
            "Независимый verifier раскладки и differential execution: native-код сравнивается с эталонным интерпретатором; тесты покрывают ветвления, циклы, spills и parallel phi moves."
        ),
    }

    backend = data["profiles"]["compiler_backend"]["ru"]
    backend["summary"] = (
        "Инженер по компиляторам с профессиональным опытом LLVM 22 в МЦСТ и отдельным x86-64 backend-проектом. "
        "Реализовал путь SSA/CFG → анализ живости и интерференции → register allocation/spills → phi lowering → SysV x86-64; "
        "сгенерированный код исполняется отдельно и сравнивается с эталонным интерпретатором."
    )
    backend["proofs"] = [
        ["Полный backend pipeline", "SSA/CFG → анализ живости и интерференции → register allocation/spills → phi lowering → native SysV x86-64."],
        [
            "Независимая проверка",
            "Verifier раскладки запрещает конфликтующие назначения; native execution сравнивается с эталонным интерпретатором на ветвлениях, циклах и spills.",
        ],
        [
            "LLVM-преобразования",
            "МЦСТ: LLVM 22 compiler engineering; Global-IV: межпроцедурные эффекты, аффинная эволюция, отдельная проверка применимости и 29 regression cases.",
        ],
    ]
    backend["skills"] = [
        ["Backend / Codegen", "SysV x86-64, анализ живости и интерференции, register allocation, spills, phi lowering, native execution"],
        ["LLVM / IR", "C++23, LLVM 22/IR, CFG/SSA, анализ циклов, межпроцедурный анализ, преобразования IR"],
        ["Тестирование", "verifier раскладки, LLVM Verifier, структурные проверки, идемпотентность, differential execution"],
        ["Языки", "C++23, Rust, C#, .NET, Linux, CMake"],
    ]
    backend["project_summaries"]["codegen"] = {
        "type": "Rust · x86-64 backend · register allocation",
        "solution": "Проверка SSA/CFG → анализ живости и интерференции → register allocation/spills → phi lowering → генерация SysV x86-64.",
        "result": "Verifier раскладки + сравнение native execution с эталонным интерпретатором; актуальный CI проекта зелёный.",
    }
    backend["project_summaries"]["globaliv"] = ru["project_summaries"]["globaliv"]
    backend["project_summaries"]["wist"] = {
        "type": ".NET · инфраструктура компилятора · композиция pipeline",
        "solution": "Разрешение зависимостей и конфликтов, выбор реализаций, порядок проходов и типизированные маршруты артефактов до исполнения.",
        "result": "1 324/1 324 теста; interpreter/CIL parity и проверка конфигурации до runtime.",
    }

    analysis = data["profiles"]["program_analysis"]["ru"]
    analysis["summary"] = (
        "Инженер по статическому анализу с профессиональным опытом C#/.NET в ИСП РАН и LLVM 22 в МЦСТ. "
        "DerefAfterNullAnalyzer выполняет внутрипроцедурный анализ потоков данных по Roslyn CFG до неподвижной точки, уточняет состояния по ветвям, "
        "объединяет состояния предшественников и обрабатывает циклы; Global-IV дополняет это межпроцедурным анализом эффектов и аффинной эволюции."
    )
    analysis["proofs"] = [
        [
            "Roslyn data-flow",
            "Worklist до неподвижной точки, состояния на ветвях CFG, объединение состояний предшественников, циклы/back edges и сброс состояния после assignment/ref/out.",
        ],
        [
            "Межпроцедурный LLVM-анализ",
            "Global-IV вычисляет прямые и транзитивные эффекты и аффинную эволюцию; преобразование запускается только после отдельной проверки условий применимости.",
        ],
        [
            "Профессиональный опыт",
            "ИСП РАН: статический анализ C#/.NET; МЦСТ: LLVM 22. Конкретные неподтверждённые изменения SharpChecker не заявляются.",
        ],
    ]
    analysis["skills"] = [
        ["Анализ потоков данных", "Roslyn CFG, worklist/fixed point, уточнение по ветвям, объединение состояний, циклы/back edges"],
        ["Межпроцедурный анализ / LLVM", "анализ эффектов, аффинная эволюция, APInt, условия применимости преобразований, LLVM IR"],
        ["Корректность анализа", "assignment/ref/out invalidation, консервативный отказ от неподдерживаемых случаев, regression tests, LLVM Verifier"],
        ["Языки / инструменты", "C#, C++23, Roslyn, LLVM 22, .NET"],
    ]
    analysis["project_summaries"]["deref"] = {
        "type": "C# · Roslyn · CFG · fixed-point data-flow",
        "solution": (
            "Roslyn ControlFlowGraph analyzer распространяет null-state по ветвям CFG до неподвижной точки, объединяет состояния предшественников "
            "и повторно обрабатывает successors для циклов/back edges."
        ),
        "result": (
            "Проверяются method/property/field/index/event dereferences; состояния сбрасываются после assignment/ref/out; отдельные analyzer tests используют Microsoft.CodeAnalysis.CSharp.Testing."
        ),
    }
    analysis["project_summaries"]["globaliv"] = ru["project_summaries"]["globaliv"]

    broad = data["profiles"]["compiler"]["ru"]
    broad["summary"] = (
        "Инженер по компиляторам и анализу программ с профессиональным опытом LLVM 22 и статического анализа C#/.NET. "
        "Сильнейшие публичные подтверждения: межпроцедурный LLVM pass с явными условиями применимости, полный учебный x86-64 backend "
        "и анализ потоков данных по Roslyn CFG до неподвижной точки."
    )

    # One canonical employment story across compiler-focused profiles. Global-IV is
    # intentionally kept as an independent project rather than presented as MCST work.
    ru_isp = {
        "fact_ref": "isp_ras",
        "date": "2026 — сейчас",
        "title": "ИСП РАН — инженер по статическому анализу",
        "org": "SharpChecker · C#/.NET · статический анализ",
        "bullets": ["Участвую в разработке SharpChecker — платформы статического анализа C#/.NET в ИСП РАН."],
    }
    en_isp = {
        "fact_ref": "isp_ras",
        "date": "2026 — present",
        "title": "ISP RAS — Static Analysis Engineer",
        "org": "SharpChecker · C#/.NET · static analysis",
        "bullets": ["Contribute to SharpChecker, ISP RAS's C#/.NET static-analysis platform."],
    }
    ru_mcst = {
        "fact_ref": "mcst",
        "date": "июль — август 2026",
        "title": "МЦСТ — стажёр по разработке компиляторов",
        "org": "LLVM 22 · C++23 · compiler engineering",
        "bullets": [
            "Реализовал LICM-проход для LLVM 22 на C++; условия переноса проверяются по структуре цикла, обращениям к памяти, побочным эффектам и безопасности speculative execution.",
            "Собрал Python-harness для сравнения поведения программы до/после оптимизации и проверки случаев с преобразованием и без него.",
        ],
    }
    en_mcst = {
        "fact_ref": "mcst",
        "date": "July — August 2026",
        "title": "MCST — Compiler Engineering Intern",
        "org": "LLVM 22 · C++23 · compiler engineering",
        "bullets": [
            "Implemented a LICM pass for LLVM 22 in C++; hoisting conditions check loop structure, memory access, side effects, and speculative safety.",
            "Built a Python harness comparing program behavior before/after optimization and checking transform/no-transform cases.",
        ],
    }
    for key in ("general", "compiler_backend", "program_analysis", "compiler"):
        data["profiles"][key]["ru"]["experience"] = [ru_isp, ru_mcst]
        data["profiles"][key]["en"]["experience"] = [en_isp, en_mcst]

    # Keep the historical protection entry, but normalize the shared employment facts.
    for lang, isp, mcst in (("ru", ru_isp, ru_mcst), ("en", en_isp, en_mcst)):
        protection = data["profiles"]["software_protection"][lang]
        historical = [entry for entry in protection["experience"] if entry.get("fact_ref") not in {"isp_ras", "mcst"}]
        protection["experience"] = [isp, mcst, *historical]

    # Global project copy is also used on landing/case pages.
    codegen = data["projects"]["codegen"]
    codegen["solution_ru"] = (
        "Проверка SSA/CFG, анализ живости и интерференции, linear-scan и seeded simulated-annealing allocators, spills, phi lowering и генерация SysV x86-64."
    )
    codegen["result_ru"] = (
        "Verifier назначения регистров/stack slots и differential execution: native-код сравнивается с эталонным интерпретатором; тесты покрывают ветвления, циклы и spills."
    )
    wist = data["projects"]["wist"]
    wist["solution_ru"] = (
        "Модули языка разрешают зависимости и конфликты, выбирают реализации требуемых возможностей и runtime-компонентов, "
        "получают детерминированный порядок contributions и типизированные маршруты артефактов до создания runtime."
    )

    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Refined RU language and normalized compiler experience facts")


if __name__ == "__main__":
    main()
