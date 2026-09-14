from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "site.json"
BUILD_SITE_PATH = ROOT / "tools" / "build_site.py"
AUDIT_PATH = ROOT / "CV-SEMANTIC-PORTFOLIO-AUDIT-2026-09-14.md"


def set_fields(target: dict, **values: object) -> None:
    for key, value in values.items():
        target[key] = value


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    data["version"] = max(int(data.get("version", 0)) + 1, 58)
    data["updated_at"] = "2026-09-14"

    # Preserve every public profile/URL in generation and validation, but keep the
    # evidence-limited Software Protection profile out of the equal primary selector.
    data["selector_order"] = [
        key for key in data["profile_order"] if key != "software_protection"
    ]

    ui = data["profile_ui"]
    ui["general"]["landing_description_ru"] = (
        "UniversalToolchain как flagship: разрешение зависимостей и конфликтов, "
        "выбор реализаций, детерминированный порядок проходов и проверка плана до исполнения; "
        "профессиональный LLVM/static-analysis контекст."
    )
    ui["compiler_backend"]["landing_title"] = "Compiler Backend / Code Generation Engineer"
    ui["compiler_backend"]["landing_description_ru"] = (
        "Полный x86-64 backend pipeline: SSA/CFG, liveness/interference, register allocation, "
        "spills, phi lowering и native-vs-interpreter проверка; LLVM 22 — профессиональный контекст."
    )
    ui["program_analysis"]["landing_description_ru"] = (
        "Roslyn CFG data-flow до неподвижной точки + межпроцедурный LLVM-анализ эффектов и "
        "аффинной эволюции; профессиональный C#/.NET static-analysis контекст в ИСП РАН."
    )
    ui["compiler"]["landing_description_ru"] = (
        "Широкий fallback для compiler/program-analysis ролей: LLVM transformations, Roslyn data-flow "
        "и x86-64 backend без попытки уместить в профиль все проекты."
    )

    # ---- Infrastructure -------------------------------------------------
    general_ru = data["profiles"]["general"]["ru"]
    general_en = data["profiles"]["general"]["en"]
    set_fields(
        general_ru,
        updated_at="2026-09-14",
        brand="compiler infrastructure · language tooling · LLVM · deterministic composition",
        eyebrow="UniversalToolchain · LLVM · разрешение зависимостей · детерминированные pipelines",
        summary=(
            "Инженер compiler/language infrastructure с профессиональным опытом LLVM и статического анализа. "
            "В UniversalToolchain реализовал разрешение зависимостей и конфликтов, выбор реализаций компонентов, "
            "детерминированный порядок проходов, маршрутизацию типизированных артефактов и проверку плана до исполнения; "
            "доклад об архитектуре проекта принят на LangDev’26."
        ),
        description=(
            "Михаил Разаков — Compiler Infrastructure / Language Tooling Engineer: разрешение зависимостей и конфликтов, "
            "выбор компонентов, детерминированные compiler pipelines, LLVM 22 и проверка до исполнения."
        ),
        proofs=[
            [
                "Композиция compiler pipeline",
                "UniversalToolchain разрешает зависимости/конфликты, однозначно выбирает реализации и фиксирует порядок проходов и маршруты артефактов до runtime.",
            ],
            [
                "LLVM и статический анализ",
                "МЦСТ: LLVM 22 compiler engineering; ИСП РАН: C#/.NET static-analysis engineering.",
            ],
            [
                "Проверка корректности",
                "1 324/1 324 теста; проверки согласованности interpreter/CIL и явный отказ от неподдерживаемых конфигураций до исполнения.",
            ],
        ],
        project_ids=["wist", "globaliv", "codegen"],
        skills=[
            [
                "Compiler Infrastructure",
                "dependency/conflict resolution, component/provider selection, deterministic pass ordering, typed artifact routing, pre-execution checks",
            ],
            [
                "Compiler / IR",
                "C++23, LLVM 22/IR, CFG/SSA, loop and interprocedural analysis, transformation applicability",
            ],
            [
                "Backends / Runtime",
                ".NET, interpreter/CIL parity, SysV x86-64, register allocation, runtime composition",
            ],
            [
                "Проверка",
                "regression suites, LLVM Verifier, interpreter/backend parity, differential execution",
            ],
        ],
        contact_heading="Целевые роли: Compiler Infrastructure · Language Tooling · Compiler Engineer · LLVM Infrastructure",
        footer="Compiler Infrastructure / Language Tooling Engineer",
        print_project_limit=3,
    )
    general_ru["project_summaries"] = {
        "wist": {
            "type": ".NET · compiler/language infrastructure · deterministic composition",
            "solution": (
                "Language features разрешают зависимости и конфликты, выбирают capability/runtime providers, "
                "получают детерминированный порядок contributions и типизированные маршруты артефактов до создания runtime."
            ),
            "result": (
                "Текущий manifest: 1 324/1 324 теста; отдельно проверяются согласованность interpreter/CIL "
                "и целостность выбранной конфигурации до исполнения."
            ),
        },
        "globaliv": {
            "type": "C++23 · LLVM 22 · interprocedural analysis · transformations",
            "solution": (
                "LLVM 22 pass локализует поддерживаемые induction-like globals после межпроцедурного анализа эффектов, "
                "аффинной эволюции и отдельной проверки условий применимости; APInt моделирует fixed-width wraparound."
            ),
            "result": (
                "29 позитивных и негативных regression cases: LLVM Verifier, структурные ожидания, идемпотентность "
                "и сравнение наблюдаемого поведения до/после преобразования."
            ),
        },
        "codegen": {
            "type": "Rust · x86-64 compiler backend · register allocation",
            "solution": (
                "SSA/CFG validation → liveness/interference → register allocation/spills → phi lowering → SysV x86-64 emission."
            ),
            "result": (
                "Независимый verifier раскладки и native-vs-interpreter differential execution; тесты покрывают ветвления, циклы, spills и parallel phi moves."
            ),
        },
    }

    set_fields(
        general_en,
        updated_at="2026-09-14",
        brand="compiler infrastructure · language tooling · LLVM · deterministic composition",
        eyebrow="UniversalToolchain · LLVM · dependency resolution · deterministic pipelines",
        summary=(
            "Compiler/language-infrastructure engineer with professional LLVM and static-analysis experience. "
            "In UniversalToolchain I built dependency/conflict resolution, component/provider selection, deterministic pass ordering, "
            "typed artifact routing, and pre-execution plan checks; an architecture talk based on the project was accepted for LangDev’26."
        ),
        description=(
            "Mikhail Razakov — Compiler Infrastructure / Language Tooling Engineer: dependency/conflict resolution, "
            "component selection, deterministic compiler pipelines, LLVM 22, and pre-execution validation."
        ),
        proofs=[
            [
                "Compiler-pipeline composition",
                "UniversalToolchain resolves dependencies/conflicts, selects implementations unambiguously, and fixes pass/contribution order and artifact routes before runtime.",
            ],
            [
                "LLVM and static analysis",
                "MCST: LLVM 22 compiler engineering; ISP RAS: C#/.NET static-analysis engineering.",
            ],
            [
                "Correctness checks",
                "1,324/1,324 tests; interpreter/CIL parity checks and explicit rejection of unsupported configurations before execution.",
            ],
        ],
        project_ids=["wist", "globaliv", "codegen"],
        skills=[
            [
                "Compiler Infrastructure",
                "dependency/conflict resolution, component/provider selection, deterministic pass ordering, typed artifact routing, pre-execution checks",
            ],
            [
                "Compiler / IR",
                "C++23, LLVM 22/IR, CFG/SSA, loop and interprocedural analysis, transformation applicability",
            ],
            [
                "Backends / Runtime",
                ".NET, interpreter/CIL parity, SysV x86-64, register allocation, runtime composition",
            ],
            [
                "Verification",
                "regression suites, LLVM Verifier, interpreter/backend parity, differential execution",
            ],
        ],
        contact_heading="Target roles: Compiler Infrastructure · Language Tooling · Compiler Engineer · LLVM Infrastructure",
        footer="Compiler Infrastructure / Language Tooling Engineer",
        print_project_limit=3,
    )
    general_en["project_summaries"] = {
        "wist": {
            "type": ".NET · compiler/language infrastructure · deterministic composition",
            "solution": (
                "Language features resolve dependencies and conflicts, select capability/runtime providers, "
                "obtain deterministic contribution ordering, and build typed artifact routes before runtime materialization."
            ),
            "result": (
                "Current manifest: 1,324/1,324 tests; dedicated checks cover interpreter/CIL parity and configuration integrity before execution."
            ),
        },
        "globaliv": {
            "type": "C++23 · LLVM 22 · interprocedural analysis · transformations",
            "solution": (
                "An LLVM 22 pass localizes supported induction-like globals after interprocedural effect analysis, affine evolution, "
                "and a separate applicability check; APInt models fixed-width wraparound."
            ),
            "result": (
                "29 positive/negative regression cases cover LLVM Verifier checks, structural expectations, idempotence, "
                "and observable before/after behavior."
            ),
        },
        "codegen": {
            "type": "Rust · x86-64 compiler backend · register allocation",
            "solution": "SSA/CFG validation → liveness/interference → register allocation/spills → phi lowering → SysV x86-64 emission.",
            "result": (
                "An independent assignment verifier plus native-vs-interpreter differential execution; tests cover branches, loops, spills, and parallel phi moves."
            ),
        },
    }

    # ---- Backend / code generation -------------------------------------
    backend_ru = data["profiles"]["compiler_backend"]["ru"]
    backend_en = data["profiles"]["compiler_backend"]["en"]
    set_fields(
        backend_ru,
        updated_at="2026-09-14",
        title="Михаил Разаков — Compiler Backend / Code Generation Engineer",
        role="Compiler Backend / Code Generation Engineer",
        brand="x86-64 backend · register allocation · LLVM · code generation",
        eyebrow="SSA/CFG · liveness/interference · register allocation · SysV x86-64",
        summary=(
            "Инженер по компиляторам с профессиональным опытом LLVM 22 в МЦСТ и отдельным x86-64 backend-проектом. "
            "Реализовал путь SSA/CFG → liveness/interference → register allocation/spills → phi lowering → SysV x86-64; "
            "сгенерированный код исполняется отдельно и сравнивается с эталонным интерпретатором."
        ),
        description=(
            "Михаил Разаков — Compiler Backend / Code Generation Engineer: SSA/CFG, liveness, register allocation, spills, phi lowering, SysV x86-64 и LLVM 22."
        ),
        proofs=[
            [
                "Полный backend pipeline",
                "SSA/CFG → liveness/interference → register allocation/spills → phi lowering → native SysV x86-64.",
            ],
            [
                "Независимая проверка",
                "Verifier раскладки запрещает конфликтующие назначения; native execution сравнивается с reference interpreter на ветвлениях, циклах и spills.",
            ],
            [
                "LLVM transformations",
                "МЦСТ: LLVM 22 compiler engineering; Global-IV: interprocedural effects, affine evolution, отдельная проверка применимости и 29 regressions.",
            ],
        ],
        project_ids=["codegen", "globaliv", "wist"],
        skills=[
            ["Backend / Codegen", "SysV x86-64, liveness/interference, register allocation, spills, phi lowering, native execution"],
            ["LLVM / IR", "C++23, LLVM 22/IR, CFG/SSA, loop/interprocedural analysis, IR transformations"],
            ["Testing", "assignment verifier, LLVM Verifier, structural checks, idempotence, differential execution"],
            ["Languages", "C++23, Rust, C#, .NET, Linux, CMake"],
        ],
        contact_heading="Целевые роли: Compiler Backend · Code Generation · Register Allocation · LLVM",
        footer="Compiler Backend / Code Generation Engineer",
        print_project_limit=3,
    )
    backend_ru["project_summaries"] = {
        "codegen": {
            "type": "Rust · x86-64 compiler backend · register allocation",
            "solution": "SSA/CFG validation → liveness/interference → register allocation/spills → phi lowering → SysV x86-64 emission.",
            "result": "Assignment verifier + native-vs-interpreter differential execution; актуальный CI проекта зелёный.",
        },
        "globaliv": general_ru["project_summaries"]["globaliv"],
        "wist": {
            "type": ".NET · compiler infrastructure · pipeline composition",
            "solution": "Разрешение зависимостей/конфликтов, выбор реализации, порядок проходов и typed artifact routes до исполнения.",
            "result": "1 324/1 324 теста; interpreter/CIL parity и проверки конфигурации до runtime.",
        },
    }
    set_fields(
        backend_en,
        updated_at="2026-09-14",
        title="Mikhail Razakov — Compiler Backend / Code Generation Engineer",
        role="Compiler Backend / Code Generation Engineer",
        brand="x86-64 backend · register allocation · LLVM · code generation",
        eyebrow="SSA/CFG · liveness/interference · register allocation · SysV x86-64",
        summary=(
            "Compiler engineer with professional LLVM 22 experience at MCST and a separate x86-64 backend project. "
            "I implemented the path from SSA/CFG through liveness/interference, register allocation/spills, and phi lowering to SysV x86-64; "
            "generated code runs in a separate process and is compared against a reference interpreter."
        ),
        description=(
            "Mikhail Razakov — Compiler Backend / Code Generation Engineer: SSA/CFG, liveness, register allocation, spills, phi lowering, SysV x86-64, and LLVM 22."
        ),
        proofs=[
            ["End-to-end backend pipeline", "SSA/CFG → liveness/interference → register allocation/spills → phi lowering → native SysV x86-64."],
            [
                "Independent correctness checks",
                "The assignment verifier rejects conflicting locations; native execution is compared with a reference interpreter across branches, loops, and spills.",
            ],
            [
                "LLVM transformations",
                "MCST: LLVM 22 compiler engineering; Global-IV: interprocedural effects, affine evolution, a separate applicability check, and 29 regressions.",
            ],
        ],
        project_ids=["codegen", "globaliv", "wist"],
        skills=[
            ["Backend / Codegen", "SysV x86-64, liveness/interference, register allocation, spills, phi lowering, native execution"],
            ["LLVM / IR", "C++23, LLVM 22/IR, CFG/SSA, loop/interprocedural analysis, IR transformations"],
            ["Testing", "assignment verifier, LLVM Verifier, structural checks, idempotence, differential execution"],
            ["Languages", "C++23, Rust, C#, .NET, Linux, CMake"],
        ],
        contact_heading="Target roles: Compiler Backend · Code Generation · Register Allocation · LLVM",
        footer="Compiler Backend / Code Generation Engineer",
        print_project_limit=3,
    )
    backend_en["project_summaries"] = {
        "codegen": {
            "type": "Rust · x86-64 compiler backend · register allocation",
            "solution": "SSA/CFG validation → liveness/interference → register allocation/spills → phi lowering → SysV x86-64 emission.",
            "result": "Assignment verifier plus native-vs-interpreter differential execution; the current project CI is green.",
        },
        "globaliv": general_en["project_summaries"]["globaliv"],
        "wist": {
            "type": ".NET · compiler infrastructure · pipeline composition",
            "solution": "Dependency/conflict resolution, implementation selection, pass ordering, and typed artifact routes before execution.",
            "result": "1,324/1,324 tests; interpreter/CIL parity and configuration checks before runtime.",
        },
    }

    # ---- Static / program analysis -------------------------------------
    analysis_ru = data["profiles"]["program_analysis"]["ru"]
    analysis_en = data["profiles"]["program_analysis"]["en"]
    set_fields(
        analysis_ru,
        updated_at="2026-09-14",
        brand="static analysis · data-flow · LLVM · Roslyn",
        eyebrow="Roslyn CFG · fixed point · interprocedural LLVM analysis",
        summary=(
            "Инженер по статическому анализу с профессиональным C#/.NET-контекстом в ИСП РАН и LLVM 22 опытом МЦСТ. "
            "DerefAfterNullAnalyzer реализует intraprocedural data-flow до неподвижной точки поверх Roslyn CFG с уточнением по ветвям, "
            "объединением predecessor states и обработкой циклов; Global-IV дополняет это межпроцедурным анализом эффектов и аффинной эволюции."
        ),
        description=(
            "Михаил Разаков — Static / Program Analysis Engineer: Roslyn CFG fixed-point data-flow, branch refinement, joins, loops и interprocedural LLVM analysis."
        ),
        proofs=[
            [
                "Roslyn data-flow",
                "Worklist до неподвижной точки, состояния на conditional CFG edges, объединение predecessors, loops/back edges и invalidation после assignment/ref/out.",
            ],
            [
                "Interprocedural LLVM analysis",
                "Global-IV вычисляет прямые/транзитивные эффекты и affine evolution, а преобразование запускается только после отдельной проверки условий применимости.",
            ],
            [
                "Профессиональный контекст",
                "ИСП РАН: C#/.NET static analysis; МЦСТ: LLVM 22 compiler engineering. Конкретные неподтверждённые SharpChecker contributions не заявляются.",
            ],
        ],
        project_ids=["deref", "globaliv"],
        skills=[
            ["Data-flow Analysis", "Roslyn CFG, worklist/fixed point, edge refinement, predecessor joins, loops/back edges"],
            ["Interprocedural / LLVM", "effects analysis, affine evolution, APInt, transformation applicability, LLVM IR"],
            ["Analysis Correctness", "assignment/ref/out invalidation, conservative unsupported-case handling, regression tests, LLVM Verifier"],
            ["Languages / Tools", "C#, C++23, Roslyn, LLVM 22, .NET"],
        ],
        contact_heading="Целевые роли: Static Analysis · Program Analysis · Compiler Analysis · LLVM Analysis",
        footer="Static Analysis / Program Analysis Engineer",
        print_project_limit=2,
    )
    analysis_ru["project_summaries"] = {
        "deref": {
            "type": "C# · Roslyn · CFG · fixed-point data-flow",
            "solution": (
                "Roslyn ControlFlowGraph analyzer распространяет null-state по conditional edges до неподвижной точки, "
                "объединяет состояния predecessors и повторно обрабатывает successors на циклах/back edges."
            ),
            "result": (
                "Method/property/field/index/event dereferences; invalidation после assignment/ref/out; dedicated analyzer tests на Microsoft.CodeAnalysis.CSharp.Testing."
            ),
        },
        "globaliv": general_ru["project_summaries"]["globaliv"],
    }
    set_fields(
        analysis_en,
        updated_at="2026-09-14",
        brand="static analysis · data flow · LLVM · Roslyn",
        eyebrow="Roslyn CFG · fixed point · interprocedural LLVM analysis",
        summary=(
            "Static-analysis engineer with professional C#/.NET context at ISP RAS and LLVM 22 experience from MCST. "
            "DerefAfterNullAnalyzer implements intraprocedural fixed-point data flow over Roslyn CFG with branch refinement, predecessor joins, "
            "and loop/back-edge iteration; Global-IV adds interprocedural effect analysis and affine evolution."
        ),
        description=(
            "Mikhail Razakov — Static / Program Analysis Engineer: Roslyn CFG fixed-point data flow, branch refinement, joins, loops, and interprocedural LLVM analysis."
        ),
        proofs=[
            [
                "Roslyn fixed-point data flow",
                "Worklist iteration, conditional-edge states, predecessor joins, loops/back edges, and invalidation after assignment/ref/out.",
            ],
            [
                "Interprocedural LLVM analysis",
                "Global-IV computes direct/transitive effects and affine evolution; transformation runs only after a separate applicability check.",
            ],
            [
                "Professional context",
                "ISP RAS: C#/.NET static analysis; MCST: LLVM 22 compiler engineering. No unverified concrete SharpChecker contribution is claimed.",
            ],
        ],
        project_ids=["deref", "globaliv"],
        skills=[
            ["Data-flow Analysis", "Roslyn CFG, worklist/fixed point, edge refinement, predecessor joins, loops/back edges"],
            ["Interprocedural / LLVM", "effects analysis, affine evolution, APInt, transformation applicability, LLVM IR"],
            ["Analysis Correctness", "assignment/ref/out invalidation, conservative unsupported-case handling, regression tests, LLVM Verifier"],
            ["Languages / Tools", "C#, C++23, Roslyn, LLVM 22, .NET"],
        ],
        contact_heading="Target roles: Static Analysis · Program Analysis · Compiler Analysis · LLVM Analysis",
        footer="Static Analysis / Program Analysis Engineer",
        print_project_limit=2,
    )
    analysis_en["project_summaries"] = {
        "deref": {
            "type": "C# · Roslyn · CFG · fixed-point data flow",
            "solution": (
                "A Roslyn ControlFlowGraph analyzer propagates null state on conditional edges to a fixed point, "
                "joins predecessor states, and reprocesses successors for loops/back edges."
            ),
            "result": (
                "Method/property/field/index/event dereferences; invalidation after assignment/ref/out; dedicated analyzer tests use Microsoft.CodeAnalysis.CSharp.Testing."
            ),
        },
        "globaliv": general_en["project_summaries"]["globaliv"],
    }

    # ---- Broad compiler fallback ---------------------------------------
    broad_ru = data["profiles"]["compiler"]["ru"]
    broad_en = data["profiles"]["compiler"]["en"]
    set_fields(
        broad_ru,
        updated_at="2026-09-14",
        summary=(
            "Инженер по компиляторам и анализу программ с профессиональным LLVM 22 и C#/.NET static-analysis опытом. "
            "Сильнейшие публичные proof points: межпроцедурный LLVM pass с явными условиями применимости, "
            "полный учебный x86-64 backend и Roslyn CFG data-flow до неподвижной точки."
        ),
        project_ids=["globaliv", "codegen", "deref"],
        print_project_limit=3,
    )
    set_fields(
        broad_en,
        updated_at="2026-09-14",
        summary=(
            "Compiler/program-analysis engineer with professional LLVM 22 and C#/.NET static-analysis experience. "
            "The strongest public proof points are an interprocedural LLVM pass with explicit applicability boundaries, "
            "an end-to-end educational x86-64 backend, and Roslyn CFG fixed-point data flow."
        ),
        project_ids=["globaliv", "codegen", "deref"],
        print_project_limit=3,
    )

    # Keep Software Protection generated and directly addressable, but explicitly selective.
    for lang in ("ru", "en"):
        protection = data["profiles"]["software_protection"][lang]
        protection["updated_at"] = "2026-09-14"
        protection["publication_status"] = "SELECTIVE / EVIDENCE-LIMITED"

    # Global project labels/case-study headings should describe what the public code actually implements.
    data["projects"]["codegen"]["title"] = "x86-64 Compiler Backend & Register Allocation"
    data["projects"]["codegen"]["type_ru"] = "Rust · compiler backend · register allocation · SysV x86-64"
    data["projects"]["codegen"]["type_en"] = "Rust · compiler backend · register allocation · SysV x86-64"
    data["projects"]["wist"]["type_ru"] = ".NET · compiler/language infrastructure · deterministic composition"
    data["projects"]["wist"]["type_en"] = ".NET · compiler/language infrastructure · deterministic composition"
    data["projects"]["wist"]["solution_ru"] = (
        "Разрешение зависимостей/конфликтов между language features, выбор capability/runtime providers, "
        "детерминированный порядок contributions и типизированные artifact routes до создания runtime."
    )
    data["projects"]["wist"]["solution_en"] = (
        "Dependency/conflict resolution across language features, capability/runtime provider selection, "
        "deterministic contribution ordering, and typed artifact routes before runtime materialization."
    )

    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Split the primary selector/navigation from the complete generation list.
    build_site = BUILD_SITE_PATH.read_text(encoding="utf-8")
    old_links = '        for key in data["profile_order"]\n    ]\n\n\ndef recognition_items'
    new_links = '        for key in data.get("selector_order", data["profile_order"])\n    ]\n\n\ndef recognition_items'
    if old_links not in build_site:
        raise RuntimeError("profile_links source shape changed; refusing an unsafe edit")
    build_site = build_site.replace(old_links, new_links, 1)

    old_cards = '    for key in (profile_key for profile_key in data["profile_order"] if profile_key != "general"):'
    new_cards = '    for key in (profile_key for profile_key in data.get("selector_order", data["profile_order"]) if profile_key != "general"):'
    if old_cards not in build_site:
        raise RuntimeError("landing selector source shape changed; refusing an unsafe edit")
    build_site = build_site.replace(old_cards, new_cards, 1)
    BUILD_SITE_PATH.write_text(build_site, encoding="utf-8")

    AUDIT_PATH.write_text(
        """# CV semantic portfolio audit — 2026-09-14

## Canonical fact model

| Fact | Canonical wording / boundary | Evidence status |
| --- | --- | --- |
| ISP RAS | Static Analysis Engineer, 2026–present; C#/.NET static-analysis context. No new concrete SharpChecker implementation claim was added. | Existing canonical employment fact; specific private contribution remains non-public. |
| MCST | Compiler Engineering Intern, July–August 2026; LLVM/compiler-engineering experience. | Existing canonical employment fact; public LICM repository supports the technical direction without expanding employer ownership. |
| UniversalToolchain | Dependency/conflict resolution, provider selection, deterministic contribution/pass ordering, typed artifact routing, pre-execution plan checks. | Verified in current public source and 1,324-test manifest. |
| LLVM Global-IV | Interprocedural direct/transitive effects, affine evolution with APInt, separate applicability/legality stage, transformation, 29 regressions with verifier/structure/idempotence/execution checks. | Verified in public source/tests; current CI green. |
| x86-64 backend | SSA/CFG checks, liveness/interference, register allocation/spills, assignment verifier, phi lowering, SysV emission, native runner, interpreter differential oracle. | Verified in public source; current CI green. Educational scope is retained. |
| DerefAfterNullAnalyzer | Roslyn CFG, worklist/fixed point, branch-edge refinement, predecessor joins, loops/back edges, assignment/ref/out invalidation, method/property/field/index/event dereferences. | Verified in public source/tests. |
| LangDev’26 | “Build the Language, Then Make the Abstractions Disappear: Extensible Programming on .NET” accepted for presentation. | Verified by organizer acceptance email dated 2026-08-13. Public program/speaker page was not yet populated during this audit. |
| Diploma | No independently located artifact during this execution. | **NEEDS_VERIFICATION — omitted from CV.** |

## Profile allocation

- **Compiler Infrastructure:** UniversalToolchain → Global-IV → x86-64 backend; LangDev as recognition.
- **Compiler Backend / Code Generation:** x86-64 backend → Global-IV → UniversalToolchain (compact).
- **Static / Program Analysis:** DerefAfterNullAnalyzer → Global-IV. No UniversalToolchain slot.
- **Broad Compiler:** Global-IV → x86-64 backend → DerefAfterNullAnalyzer.
- **Software Protection:** generated/direct-link profile only; excluded from the equal primary selector and kept `SELECTIVE / EVIDENCE-LIMITED`.

## Market-positioning check

Current compiler postings reviewed during the rewrite repeatedly separate backend/codegen depth, production toolchain/infrastructure work, and program-analysis responsibilities. The rewrite therefore emphasizes the candidate’s existing evidence instead of adding unsupported MLIR/MIR/TableGen/taint/points-to keywords.

## Inputs unavailable in this execution

The prompt named three prior-review artifacts (`CV_SEMANTIC_PORTFOLIO_REVIEW_REPORT_2026-09-14.md`, `CV_EVIDENCE_SCORECARD_2026-09-14.csv`, `CV_MARKET_GAP_ROLES_2026-09-14.csv`). They were searched in the current Project/Library context but were not available, so no claim in this audit depends on having read them.
""",
        encoding="utf-8",
    )

    print("Applied semantic portfolio rewrite")


if __name__ == "__main__":
    main()
