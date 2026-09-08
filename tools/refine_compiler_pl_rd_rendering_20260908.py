from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "site.json"
BUILD_SITE = ROOT / "tools" / "build_site.py"


def strengthen_compiler_profile(data: dict) -> None:
    compiler_ru = data["profiles"]["compiler"]["ru"]
    compiler_en = data["profiles"]["compiler"]["en"]

    compiler_en.update(
        {
            "summary": (
                "Compiler engineer spanning LLVM middle-end transformations, program/static analysis, and compiler infrastructure. "
                "At MCST, I implemented an LLVM 22 LICM pass and a conservative interprocedural global-state promotion pass; "
                "at ISP RAS, I contribute to SharpChecker, an industrial C#/.NET static-analysis platform. Independent work covers "
                "Roslyn fixed-point data flow, SSA/x86-64 code generation and register allocation, and deterministic language composition."
            ),
            "experience": [
                {
                    "date": "2026 — present",
                    "title": "ISP RAS — Static Analysis Engineer",
                    "org": "SharpChecker · C#/.NET · industrial static analysis",
                    "bullets": [
                        "Contribute to SharpChecker, ISP RAS's industrial static-analysis platform for C#/.NET."
                    ],
                },
                {
                    "date": "July — August 2026",
                    "title": "MCST — Compiler Engineering Intern",
                    "org": "LLVM 22 · C++23 · middle-end / interprocedural analysis",
                    "bullets": [
                        "Implemented an LLVM LICM pass with loop analysis, side-effect/speculative-safety checks, and hoisting of loop-invariant instructions to preheaders.",
                        "Built a conservative interprocedural LLVM pass for localizing induction-like integer globals: APInt affine evolution, transitive call effects, dominance/must-execute legality, and explicit synchronization around known calls; unsupported cases fail closed.",
                    ],
                },
            ],
            "skills": [
                [
                    "Compilers / LLVM",
                    "C++23, LLVM 22, LLVM IR, optimization passes, interprocedural analysis, CFG/SSA, dominators, loop analysis, APInt, transformation legality, LLVM Verifier, CMake, Linux",
                ],
                [
                    "Program / Static Analysis",
                    "C#, .NET, Roslyn ControlFlowGraph, worklist/fixed-point data flow, edge-sensitive states, branch refinement, joins, loops/back edges, conservative analysis",
                ],
                [
                    "Backend / Code Generation",
                    "Rust, SSA-like IR, liveness, interference, deterministic register allocation, phi lowering, SysV x86-64, differential execution",
                ],
                [
                    "Compiler Infrastructure & Verification",
                    "typed artifact/component contracts, deterministic planning/pass ordering, provider/capability resolution, exact runtime binding, idempotence and differential checks",
                ],
            ],
            "recognition": [
                [
                    "2026",
                    "LangDev'26 — accepted speaker",
                    "Accepted technical talk on UniversalToolchain's architecture; LangDev'26 takes place October 8–9, 2026 in Málaga.",
                ],
                [
                    "2026",
                    "Compiler / engineering competitions",
                    "Grand Prize at the Baltic Science and Engineering Competition; MEPhI Junior overall winner, 96/100 for UniversalToolchain.",
                ],
            ],
        }
    )

    compiler_ru.update(
        {
            "summary": (
                "Инженер по компиляторам: LLVM middle-end, статический анализ и анализ программ, инфраструктура компилятора. "
                "В МЦСТ реализовал LICM и консервативный межпроцедурный проход LLVM 22 для локализации глобального состояния; "
                "в ИСП РАН участвую в разработке SharpChecker — промышленной платформы статического анализа C#/.NET. "
                "В собственных проектах — Roslyn data-flow до неподвижной точки, SSA/x86-64 codegen и register allocation, "
                "детерминированная композиция языковых компонентов."
            ),
            "experience": [
                {
                    "date": "2026 — сейчас",
                    "title": "ИСП РАН — инженер по статическому анализу",
                    "org": "SharpChecker · C#/.NET · промышленный статический анализ",
                    "bullets": [
                        "Участвую в разработке SharpChecker — промышленной платформы статического анализа C#/.NET в ИСП РАН."
                    ],
                },
                {
                    "date": "июль — август 2026",
                    "title": "МЦСТ — стажёр по разработке компиляторов",
                    "org": "LLVM 22 · C++23 · middle-end / межпроцедурный анализ",
                    "bullets": [
                        "Реализовал LLVM LICM-pass: анализ циклов, проверки side effects/speculative safety и вынос loop-invariant инструкций в preheader.",
                        "Разработал консервативный межпроцедурный LLVM-pass для локализации induction-like integer globals: APInt-аффинная эволюция, транзитивные эффекты вызовов, dominance/must-execute legality и синхронизация вокруг известных вызовов; неподдерживаемые случаи отклоняются без изменения IR.",
                    ],
                },
            ],
            "skills": [
                [
                    "Компиляторы / LLVM",
                    "C++23, LLVM 22, LLVM IR, optimization passes, interprocedural analysis, CFG/SSA, dominators, loop analysis, APInt, transformation legality, LLVM Verifier, CMake, Linux",
                ],
                [
                    "Анализ программ",
                    "C#, .NET, Roslyn ControlFlowGraph, worklist/fixed-point data flow, edge-sensitive states, branch refinement, joins, loops/back edges, conservative analysis",
                ],
                [
                    "Backend / Code Generation",
                    "Rust, SSA-like IR, liveness, interference, deterministic register allocation, phi lowering, SysV x86-64, differential execution",
                ],
                [
                    "Compiler Infrastructure & Verification",
                    "typed artifact/component contracts, deterministic planning/pass ordering, provider/capability resolution, exact runtime binding, idempotence и differential checks",
                ],
            ],
            "recognition": [
                [
                    "2026",
                    "LangDev'26 — принятый доклад",
                    "Принят технический доклад по архитектуре UniversalToolchain; LangDev'26 пройдёт 8–9 октября 2026 в Малаге.",
                ],
                [
                    "2026",
                    "Компиляторные / инженерные конкурсы",
                    "Главная премия Балтийского научно-инженерного конкурса; абсолютный победитель НИЯУ МИФИ «Юниор», 96/100 за UniversalToolchain.",
                ],
            ],
        }
    )

    compiler_en["project_summaries"].update(
        {
            "globaliv": {
                "type": "C++23 · LLVM 22 · interprocedural analysis · IR transformation",
                "solution": (
                    "LLVM 22 pass for safe localization of induction-like integer globals. Affine evolution is modeled with APInt; "
                    "direct/transitive call effects and explicit legality checks are resolved before IR mutation."
                ),
                "result": (
                    "29 transform/reject regressions; every case runs through global-iv,verify, a canonical second pass checks idempotence, "
                    "and executable cases compare observable behavior before/after transformation when clang is available."
                ),
                "application": (
                    "APInt affine evolution + transitive call-effect analysis + fail-closed legality; 29 transform/reject regressions use LLVM Verifier, idempotence, and executable before/after checks."
                ),
            },
            "deref": {
                "type": "C# · Roslyn CFG · fixed-point program analysis",
                "solution": (
                    "Worklist analysis over Roslyn ControlFlowGraph with separate conditional-edge null states, branch refinement, joins, "
                    "loops/back edges, assignment invalidation, and ref/out invalidation."
                ),
                "result": "State is propagated to a fixed point; diagnostics are tested with Microsoft.CodeAnalysis.CSharp.Testing.",
                "application": (
                    "Roslyn CFG worklist/fixed-point null analysis with edge-sensitive branch states, joins, loops/back edges, and assignment/ref/out invalidation."
                ),
            },
            "codegen": {
                "type": "Rust · SSA/CFG · register allocation · SysV x86-64",
                "solution": (
                    "Educational backend pipeline from SSA-like IR through CFG/SSA validation, liveness/interference, deterministic register allocation, "
                    "independent assignment verification, phi lowering, and SysV x86-64 code generation."
                ),
                "result": "A reference interpreter and differential execution check generated native-code semantics independently of code generation.",
                "application": (
                    "SSA-like IR → liveness/interference → deterministic register allocation → phi lowering → SysV x86-64; independent RA verifier + differential execution vs a reference interpreter."
                ),
            },
            "wist": {
                "type": ".NET · compiler/language infrastructure · deterministic composition",
                "solution": (
                    "Typed artifact/component contracts compile dependencies, conflicts, providers, ordering, and artifact routes into an immutable LanguagePlan before execution; "
                    "runtime materializes the exact selected graph without semantic replanning."
                ),
                "result": (
                    "The repository enforces an exact 1,324-test manifest plus architecture/documentation and package/runtime gates; interpreter/CIL parity and exact-binding checks protect the composition contract."
                ),
                "application": (
                    "Typed contracts compile dependencies/providers/order/routes into an immutable LanguagePlan; exact runtime binding avoids semantic replanning, backed by a 1,324-test exact manifest."
                ),
            },
        }
    )

    compiler_ru["project_summaries"].update(
        {
            "globaliv": {
                "type": "C++23 · LLVM 22 · межпроцедурный анализ · преобразование IR",
                "solution": (
                    "LLVM 22 pass для безопасной локализации induction-like integer globals. Аффинная эволюция моделируется через APInt; "
                    "прямые/транзитивные эффекты вызовов и legality проверяются до изменения IR."
                ),
                "result": (
                    "29 transform/reject regressions; каждый случай проходит global-iv,verify, второй канонический запуск проверяет idempotence, "
                    "а executable cases сравниваются до/после преобразования при наличии clang."
                ),
                "application": (
                    "APInt-аффинная эволюция + транзитивный анализ эффектов вызовов + fail-closed legality; 29 transform/reject regressions проверяют LLVM Verifier, idempotence и выполнение до/после."
                ),
            },
            "deref": {
                "type": "C# · Roslyn CFG · fixed-point анализ программ",
                "solution": (
                    "Worklist-анализ поверх Roslyn ControlFlowGraph с отдельными null-состояниями условных рёбер, branch refinement, joins, "
                    "loops/back edges и invalidation после assignment/ref/out."
                ),
                "result": "Состояния распространяются до неподвижной точки; диагностики проверяются через Microsoft.CodeAnalysis.CSharp.Testing.",
                "application": (
                    "Roslyn CFG worklist/fixed-point null analysis: edge-sensitive branch states, joins, loops/back edges и invalidation после assignment/ref/out."
                ),
            },
            "codegen": {
                "type": "Rust · SSA/CFG · register allocation · SysV x86-64",
                "solution": (
                    "Учебный backend pipeline: SSA-like IR, CFG/SSA validation, liveness/interference, deterministic register allocation, "
                    "независимая проверка assignment, phi lowering и генерация SysV x86-64."
                ),
                "result": "Reference interpreter и differential execution независимо проверяют семантику сгенерированного native code.",
                "application": (
                    "SSA-like IR → liveness/interference → deterministic register allocation → phi lowering → SysV x86-64; независимый RA verifier + differential execution против reference interpreter."
                ),
            },
            "wist": {
                "type": ".NET · compiler/language infrastructure · deterministic composition",
                "solution": (
                    "Typed artifact/component contracts сводят dependencies, conflicts, providers, ordering и artifact routes в immutable LanguagePlan до исполнения; "
                    "runtime материализует точный выбранный граф без повторного semantic planning."
                ),
                "result": (
                    "Репозиторий контролирует exact manifest из 1 324 тестов, architecture/documentation и package/runtime gates; interpreter/CIL parity и exact-binding checks защищают контракт композиции."
                ),
                "application": (
                    "Typed contracts сводят dependencies/providers/order/routes в immutable LanguagePlan; exact runtime binding исключает semantic replanning, контракт покрыт exact manifest из 1 324 тестов."
                ),
            },
        }
    )

    for lang, compiler in (("ru", compiler_ru), ("en", compiler_en)):
        compiler["show_portrait"] = True
        general = data["profiles"]["general"][lang]
        general["experience"] = copy.deepcopy(compiler["experience"])
        general["skills"] = copy.deepcopy(compiler["skills"])
        general["recognition"] = copy.deepcopy(compiler["recognition"])
        general["summary"] = compiler["summary"]


def refine_data() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))

    for lang in ("ru", "en"):
        general = data["profiles"]["general"][lang]
        general["role"] = "Compiler & Program Analysis Engineer"
        general["footer"] = "Compiler & Program Analysis Engineer · LLVM · Language Infrastructure"

    # Keep the application CV ordered by the fastest role-specific proof.
    data["profiles"]["compiler"]["ru"]["project_ids"] = ["globaliv", "deref", "codegen", "wist"]
    data["profiles"]["compiler"]["en"]["project_ids"] = ["globaliv", "deref", "codegen", "wist"]
    data["profiles"]["research"]["ru"]["project_ids"] = ["wist", "globaliv", "codegen", "deref"]
    data["profiles"]["research"]["en"]["project_ids"] = ["wist", "globaliv", "codegen", "deref"]

    strengthen_compiler_profile(data)

    # The web profiles intentionally keep the portrait; the one-page application PDFs do not render it.
    for lang in ("ru", "en"):
        data["profiles"]["research"][lang]["show_portrait"] = True

    # Avoid long untranslated prose in the Russian research page while preserving technical search terms.
    data["profiles"]["research"]["ru"]["proofs"] = [
        [
            "Исследовательский цикл",
            "UniversalToolchain: явная модель задачи → четыре verification policy → frozen corpus и valid controls → fault injection → ablations → явно заблокированные неподтверждённые claims.",
        ],
        [
            "Корректность компилятора при неполной модели",
            "Global-IV: аффинная модель, транзитивные эффекты вызовов и границы legality/must-execute; неподдерживаемые случаи fail-closed отклоняются и покрыты reject-regressions.",
        ],
        [
            "Практическая systems-глубина",
            "Профессиональный LLVM и static analysis плюс Roslyn fixed-point data flow и отдельно проверяемый x86-64 register-allocation/codegen pipeline.",
        ],
    ]

    # Shorten the research project copy enough for a one-page application PDF while
    # preserving research-process evidence and explicit claim boundaries.
    data["profiles"]["research"]["ru"]["project_summaries"]["wist"] = {
        "type": ".NET · extensible compiler/language systems · research engineering",
        "solution": (
            "Contract-guided reverification для расширяемых compiler pipelines: typed facts/effects/invalidations "
            "и verifier routes управляют fail-closed selective verification поверх детерминированного LanguagePlan."
        ),
        "result": (
            "Evidence-backed anonymous CGO’27 draft, не submission: 4 policies, frozen corpus, valid controls, "
            "fault injection и ablations; performance/external-corpus claims явно оставлены blocked."
        ),
    }
    data["profiles"]["research"]["en"]["project_summaries"]["wist"] = {
        "type": ".NET · extensible compiler/language systems · research engineering",
        "solution": (
            "Contract-guided reverification for extensible compiler pipelines: typed facts/effects/invalidations "
            "and verifier routes drive fail-closed selective verification over a deterministic LanguagePlan."
        ),
        "result": (
            "Evidence-backed anonymous CGO’27 draft, not a submission: four policies, a frozen corpus, valid controls, "
            "fault injection, and ablations; performance/external-corpus claims remain explicitly blocked."
        ),
    }

    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_build_site() -> None:
    raw = BUILD_SITE.read_text(encoding="utf-8")

    # Application PDFs should use profile-specific evidence copy when it exists. This lets
    # the compiler CV expose method + verification, while other profiles retain the shared fallback.
    old_application_projects = '''        projects = []
        project_limit = int(profile.get("print_project_limit", 3))
        for project_id in profile["project_ids"][:project_limit]:
            project = data["projects"][project_id]
            target = project.get("repo") or project[f"case_{lang}"]
            projects.append(
                f'<article class="pcv-app-project"><h3><a href="{esc(target)}">{esc(project["title"])}</a></h3>'
                f'<p>{esc(project[f"result_{lang}"])}</p></article>'
            )
'''
    new_application_projects = '''        projects = []
        project_limit = int(profile.get("print_project_limit", 3))
        project_summaries = profile.get("project_summaries", {})
        for project_id in profile["project_ids"][:project_limit]:
            project = data["projects"][project_id]
            target = project.get("repo") or project[f"case_{lang}"]
            summary = project_summaries.get(project_id, {})
            project_text = summary.get("application") or summary.get("result") or project[f"result_{lang}"]
            projects.append(
                f'<article class="pcv-app-project"><h3><a href="{esc(target)}">{esc(project["title"])}</a></h3>'
                f'<p>{esc(project_text)}</p></article>'
            )
'''
    if old_application_projects not in raw:
        raise RuntimeError("application project renderer shape changed; refusing blind patch")
    raw = raw.replace(old_application_projects, new_application_projects, 1)

    # The non-application print path should also use role-specific project copy whenever present,
    # not only for the historical compiler profile.
    raw = raw.replace(
        'summary = project_summaries.get(project_id, {}) if is_compiler_print else {}\n'
        '        if is_compiler_print and summary:',
        'summary = project_summaries.get(project_id, {})\n'
        '        if summary:',
    )

    # Give the research page its own information hierarchy while reusing the existing
    # project-summary renderer and avoiding a new template/export mechanism.
    old = '''    if profile_key == "compiler":\n        main_content = f"{compiler_hero(data, lang, profile)}{experience_section(lang, profile, compact=True)}{compiler_projects_section(data, lang, profile)}{skills_section(lang, profile, compact=True)}{recognition_section(data, lang, profile, compact=True)}{education_section(data, lang)}{contact_section(data, lang, profile)}"\n    else:\n        main_content = f"{hero(data, lang, profile)}{proof_strip(profile)}{experience_section(lang, profile)}{projects_section(data, lang, profile)}{skills_section(lang, profile)}{recognition_section(data, lang, profile)}{education_section(data, lang)}{contact_section(data, lang, profile)}"'''
    new = '''    if profile_key == "compiler":\n        main_content = f"{compiler_hero(data, lang, profile)}{experience_section(lang, profile, compact=True)}{compiler_projects_section(data, lang, profile)}{skills_section(lang, profile, compact=True)}{recognition_section(data, lang, profile, compact=True)}{education_section(data, lang)}{contact_section(data, lang, profile)}"\n    elif profile_key == "research":\n        main_content = f"{hero(data, lang, profile)}{proof_strip(profile)}{experience_section(lang, profile, compact=True)}{compiler_projects_section(data, lang, profile)}{skills_section(lang, profile, compact=True)}{recognition_section(data, lang, profile, compact=True)}{education_section(data, lang)}{contact_section(data, lang, profile)}"\n    else:\n        main_content = f"{hero(data, lang, profile)}{proof_strip(profile)}{experience_section(lang, profile)}{projects_section(data, lang, profile)}{skills_section(lang, profile)}{recognition_section(data, lang, profile)}{education_section(data, lang)}{contact_section(data, lang, profile)}"'''
    if old not in raw:
        raise RuntimeError("profile_page dispatch shape changed; refusing blind patch")
    raw = raw.replace(old, new)

    # Make the landing page agree with the selected default identity.
    raw = raw.replace('title = "Михаил Разаков — Compiler / Static Analysis Engineer"',
                      'title = "Михаил Разаков — Compiler & Program Analysis Engineer"')
    raw = raw.replace('<span>Compiler / Static Analysis Engineer</span>',
                      '<span>Compiler & Program Analysis Engineer</span>')
    raw = raw.replace('<h1>Compiler / Static Analysis Engineer</h1>',
                      '<h1>Compiler & Program Analysis Engineer</h1>')
    raw = raw.replace('Основной профиль — Compiler / Static Analysis Engineer.',
                      'Основной профиль — Compiler & Program Analysis Engineer.')

    BUILD_SITE.write_text(raw, encoding="utf-8")


def main() -> None:
    refine_data()
    patch_build_site()


if __name__ == "__main__":
    main()
