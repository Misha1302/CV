from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "site.json"


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    data["version"] = max(int(data.get("version", 0)), 59)
    data["updated_at"] = "2026-09-08"

    # The public default should use the broadest market-legible compiler identity.
    data["profile_ui"]["general"].update(
        {
            "label_ru": "Compiler / Program Analysis",
            "label_en": "Compiler / Program Analysis",
            "landing_title": "Compiler & Program Analysis Engineer · LLVM · Language Infrastructure",
            "landing_description_ru": (
                "Профессиональный LLVM и industrial static analysis; correctness-oriented compiler transformations, "
                "language infrastructure и backend/codegen как единая compiler-systems траектория."
            ),
        }
    )
    data["profile_ui"]["compiler"].update(
        {
            "label_ru": "Compiler / LLVM / Program Analysis",
            "label_en": "Compiler / LLVM / Program Analysis",
            "landing_title": "Compiler Engineer · LLVM · Program Analysis",
            "landing_description_ru": (
                "LLVM transformations и legality, interprocedural/program analysis, static analysis, "
                "CFG/SSA и дополнительная backend/codegen глубина."
            ),
        }
    )

    order = [key for key in data["profile_order"] if key != "research"]
    insert_at = order.index("compiler") + 1 if "compiler" in order else len(order)
    order.insert(insert_at, "research")
    data["profile_order"] = order
    data["profile_ui"]["research"] = {
        "label_ru": "Research Engineering — Compilers / PL",
        "label_en": "Research Engineering — Compilers / PL",
        "landing_title": "Research Engineer · Compilers & Programming Languages",
        "landing_description_ru": (
            "Исследовательская инженерия в компиляторах и языковых системах: явные модели, "
            "консервативные границы, controlled experiments, fault injection, ablations и executable verification."
        ),
    }

    general_ru = data["profiles"]["general"]["ru"]
    general_ru.update(
        {
            "title": "Михаил Разаков — Compiler & Program Analysis Engineer · LLVM · Language Infrastructure",
            "role": "Compiler & Program Analysis Engineer · LLVM · Language Infrastructure",
            "brand": "LLVM · program analysis · static analysis · language infrastructure",
            "eyebrow": "LLVM 22 · Roslyn CFG · transformation legality · language systems · x86-64",
            "summary": (
                "Инженер по компиляторам и анализу программ с профессиональным опытом LLVM и промышленного "
                "статического анализа. В МЦСТ работал с LLVM 22: loop/interprocedural analysis, legality и IR "
                "transformations; в ИСП РАН участвую в разработке SharpChecker для C#/.NET. Независимые проекты "
                "охватывают fixed-point program analysis, x86-64 codegen/register allocation и UniversalToolchain — "
                "language infrastructure с typed artifact contracts, детерминированным planning и exact runtime binding."
            ),
            "description": (
                "Михаил Разаков — Compiler & Program Analysis Engineer: LLVM 22, static/program analysis, "
                "interprocedural analysis, transformation legality, language infrastructure, register allocation и x86-64 codegen."
            ),
            "contact_heading": (
                "Целевые роли: Compiler Engineer · LLVM Engineer · Program / Static Analysis · Language Infrastructure"
            ),
            "footer": "Compiler & Program Analysis Engineer · LLVM · Language Infrastructure",
        }
    )
    general_en = data["profiles"]["general"]["en"]
    general_en.update(
        {
            "title": "Mikhail Razakov — Compiler & Program Analysis Engineer · LLVM · Language Infrastructure",
            "role": "Compiler & Program Analysis Engineer · LLVM · Language Infrastructure",
            "brand": "LLVM · program analysis · static analysis · language infrastructure",
            "eyebrow": "LLVM 22 · Roslyn CFG · transformation legality · language systems · x86-64",
            "summary": (
                "Compiler and program-analysis engineer with professional LLVM and industrial static-analysis experience. "
                "At MCST, I worked on LLVM 22 loop/interprocedural analysis, transformation legality, and IR transforms; "
                "at ISP RAS, I contribute to SharpChecker for C#/.NET. Independent work spans fixed-point program analysis, "
                "x86-64 code generation/register allocation, and UniversalToolchain language infrastructure built around "
                "typed artifact contracts, deterministic planning, and exact runtime binding."
            ),
            "description": (
                "Mikhail Razakov — Compiler & Program Analysis Engineer: LLVM 22, static/program analysis, "
                "interprocedural analysis, transformation legality, language infrastructure, register allocation, and x86-64 codegen."
            ),
            "contact_heading": (
                "Target roles: Compiler Engineer · LLVM Engineer · Program / Static Analysis · Language Infrastructure"
            ),
            "footer": "Compiler & Program Analysis Engineer · LLVM · Language Infrastructure",
        }
    )

    compiler_ru = data["profiles"]["compiler"]["ru"]
    compiler_ru.update(
        {
            "title": "Михаил Разаков — Compiler Engineer · LLVM · Program Analysis",
            "role": "Compiler Engineer · LLVM · Program Analysis",
            "brand": "LLVM · оптимизации · program analysis · static analysis",
            "eyebrow": "LLVM 22 · CFG/SSA · interprocedural analysis · legality · Roslyn",
            "summary": (
                "Инженер по компиляторам с профессиональным опытом LLVM и промышленного статического анализа. "
                "В МЦСТ реализовал LICM-pass и консервативный interprocedural global-IV prototype для LLVM 22 с "
                "отдельной legality-фазой; в ИСП РАН участвую в разработке SharpChecker. Независимые проекты добавляют "
                "Roslyn fixed-point data-flow, x86-64 codegen/register allocation и детерминированную language infrastructure."
            ),
            "description": (
                "Михаил Разаков — Compiler Engineer: LLVM 22, compiler optimization, interprocedural/program analysis, "
                "static analysis, CFG/SSA, transformation legality, register allocation и x86-64 codegen."
            ),
            "proofs": [
                [
                    "LLVM optimization & legality",
                    "LICM и global-IV: loop/dominator reasoning, APInt affine evolution, transitive call effects, must-execute и conservative rejection.",
                ],
                [
                    "Program / static analysis",
                    "SharpChecker в ИСП РАН; Roslyn ControlFlowGraph fixed-point analyzer с edge-sensitive состояниями и joins до сходимости.",
                ],
                [
                    "Backend & language infrastructure",
                    "SSA/CFG validation, liveness/register allocation и differential x86-64 execution; UniversalToolchain typed contracts и deterministic LanguagePlan.",
                ],
            ],
            "skills": [
                [
                    "Компиляторы / LLVM",
                    "C++23, LLVM 22, LLVM IR, optimization passes, interprocedural analysis, CFG/SSA, dominators, loop analysis, LICM, transformation legality",
                ],
                [
                    "Program / Static Analysis",
                    "C#, .NET, Roslyn ControlFlowGraph, fixed-point data-flow analysis, state propagation, joins, conservative analysis",
                ],
                [
                    "Code Generation",
                    "Rust, SysV x86-64, liveness, interference, register allocation, phi lowering, differential execution",
                ],
                [
                    "Language / Compiler Infrastructure",
                    "typed artifact contracts, deterministic planning/pass ordering, capability/provider resolution, artifact routing, backend/runtime composition",
                ],
            ],
            "contact_heading": (
                "Целевые роли: Compiler Engineer · LLVM Engineer · Compiler Optimization · Program / Static Analysis · Backend Codegen"
            ),
            "footer": "Compiler Engineer · LLVM · Program Analysis",
            "print_layout": "application",
            "show_portrait": False,
            "print_project_limit": 4,
        }
    )
    compiler_en = data["profiles"]["compiler"]["en"]
    compiler_en.update(
        {
            "title": "Mikhail Razakov — Compiler Engineer · LLVM · Program Analysis",
            "role": "Compiler Engineer · LLVM · Program Analysis",
            "brand": "LLVM · compiler optimization · program analysis · static analysis",
            "eyebrow": "LLVM 22 · CFG/SSA · interprocedural analysis · legality · Roslyn",
            "summary": (
                "Compiler engineer with professional LLVM and industrial static-analysis experience. At MCST, I implemented "
                "an LLVM 22 LICM pass and a conservative interprocedural global-IV prototype with a separate legality phase; "
                "at ISP RAS, I contribute to SharpChecker. Independent work adds Roslyn fixed-point data flow, x86-64 "
                "codegen/register allocation, and deterministic language infrastructure."
            ),
            "description": (
                "Mikhail Razakov — Compiler Engineer: LLVM 22, compiler optimization, interprocedural/program analysis, "
                "static analysis, CFG/SSA, transformation legality, register allocation, and x86-64 code generation."
            ),
            "proofs": [
                [
                    "LLVM optimization & legality",
                    "LICM and global-IV: loop/dominator reasoning, APInt affine evolution, transitive call effects, must-execute reasoning, and conservative rejection.",
                ],
                [
                    "Program / static analysis",
                    "SharpChecker at ISP RAS; a Roslyn ControlFlowGraph fixed-point analyzer with edge-sensitive states and joins to convergence.",
                ],
                [
                    "Backend & language infrastructure",
                    "SSA/CFG validation, liveness/register allocation, and differential x86-64 execution; UniversalToolchain typed contracts and deterministic LanguagePlan.",
                ],
            ],
            "skills": [
                [
                    "Compilers / LLVM",
                    "C++23, LLVM 22, LLVM IR, optimization passes, interprocedural analysis, CFG/SSA, dominators, loop analysis, LICM, transformation legality",
                ],
                [
                    "Program / Static Analysis",
                    "C#, .NET, Roslyn ControlFlowGraph, fixed-point data-flow analysis, state propagation, joins, conservative analysis",
                ],
                [
                    "Code Generation",
                    "Rust, SysV x86-64, liveness, interference, register allocation, phi lowering, differential execution",
                ],
                [
                    "Language / Compiler Infrastructure",
                    "typed artifact contracts, deterministic planning/pass ordering, capability/provider resolution, artifact routing, backend/runtime composition",
                ],
            ],
            "contact_heading": (
                "Target roles: Compiler Engineer · LLVM Engineer · Compiler Optimization · Program / Static Analysis · Backend Codegen"
            ),
            "footer": "Compiler Engineer · LLVM · Program Analysis",
            "print_layout": "application",
            "show_portrait": False,
            "print_project_limit": 4,
        }
    )

    # Build the research profile from the same verified facts, but with a different
    # information hierarchy: ambiguous problem -> model -> boundary -> experiment -> evidence.
    research = copy.deepcopy(data["profiles"]["compiler"])
    research["ru"].update(
        {
            "filename": "ru-research.html",
            "pdf": "Mikhail_Razakov_Research_Engineer_RU.pdf",
            "title": "Михаил Разаков — Research Engineer · Компиляторы и языки программирования",
            "role": "Research Engineer · Компиляторы и языки программирования",
            "brand": "compiler R&D · program analysis · language systems · experimental validation",
            "eyebrow": "models · conservative boundaries · fault injection · ablations · executable verification",
            "summary": (
                "Research-oriented compiler engineer: формализую неопределённую compiler/language-system задачу в явную модель, "
                "реализую прототип, фиксирую границы применимости и проверяю его контрпримерами и воспроизводимыми экспериментами. "
                "Профессиональная база — LLVM в МЦСТ и промышленный static analysis в ИСП РАН; strongest independent evidence — "
                "UniversalToolchain/contract-guided reverification и консервативный interprocedural Global-IV pass."
            ),
            "description": (
                "Research Engineer в compilers/programming languages: LLVM, program analysis, extensible language systems, "
                "controlled experiments, fault injection, ablations, differential testing и correctness-oriented engineering."
            ),
            "proofs": [
                [
                    "Research engineering cycle",
                    "UniversalToolchain: problem model → four verification policies → frozen corpora/controls → injected faults → ablations → explicit blocked claims.",
                ],
                [
                    "Compiler correctness under uncertainty",
                    "Global-IV: affine model + transitive call effects + legality/must-execute boundaries; unsupported cases fail closed and are covered by reject regressions.",
                ],
                [
                    "Hands-on systems depth",
                    "Professional LLVM/static analysis plus Roslyn fixed-point data flow and a separately verified x86-64 register-allocation/codegen pipeline.",
                ],
            ],
            "project_ids": ["wist", "globaliv", "deref", "codegen"],
            "skills": [
                [
                    "Research Engineering",
                    "hypothesis-driven prototyping, controlled experiments, frozen corpora, fault injection, matched controls, ablations, explicit validity boundaries",
                ],
                [
                    "Compilers / Program Analysis",
                    "LLVM 22, LLVM IR, CFG/SSA, dominators, loop/interprocedural analysis, Roslyn CFG, fixed-point data flow, transformation legality",
                ],
                [
                    "Language Systems",
                    "typed artifact contracts, feature/component composition, deterministic planning, provider/order/conflict resolution, exact runtime binding",
                ],
                [
                    "Verification & Backends",
                    "LLVM Verifier, idempotence checks, differential execution, interpreter/CIL parity, x86-64 codegen, register-allocation verification",
                ],
            ],
            "contact_heading": (
                "Целевые роли: Research Engineer · Compiler R&D · Programming Languages / Language Systems · Program Analysis"
            ),
            "footer": "Research Engineer · Compilers & Programming Languages",
            "recognition": copy.deepcopy(data["profiles"]["compiler"]["ru"]["recognition"]),
            "project_summaries": copy.deepcopy(data["profiles"]["compiler"]["ru"]["project_summaries"]),
            "print_layout": "application",
            "show_portrait": False,
            "print_project_limit": 4,
        }
    )
    research["ru"]["project_summaries"]["wist"] = {
        "type": ".NET · extensible compiler/language systems · research engineering",
        "solution": (
            "Исследую contract-guided reverification для расширяемых compiler pipelines: компоненты декларируют owned facts, effects, "
            "invalidations и verifier routes; fail-closed scheduler применяет structural-only, invalidation-only, selective и always-verify policies. "
            "Базовая UniversalToolchain architecture сводит typed contributions/providers/order/routes в immutable LanguagePlan до исполнения."
        ),
        "result": (
            "Evidence-backed anonymous CGO’27 draft, ещё не submission: frozen boundary corpus, 100 valid controls на policy, "
            "source-to-result fault injection, second language package и mechanism/policy ablations. Selective/always обнаруживают все "
            "целевые semantic faults; whole-compilation speedup и independent external corpus явно оставлены неподтверждёнными."
        ),
    }
    research["ru"]["project_summaries"]["globaliv"] = {
        "type": "C++23 · LLVM 22 · interprocedural analysis · conservative optimization",
        "solution": (
            "Смоделировал безопасную локализацию induction-like global state через APInt affine evolution, transitive call effects, "
            "loop/dominator reasoning и must-execute conditions; legality отделена от transformation, неопределённые CFG/call cases отклоняются."
        ),
        "result": (
            "29 transform/reject regressions; LLVM Verifier, second-pass idempotence и executable before/after comparison используются как независимые oracles корректности."
        ),
    }

    research["en"].update(
        {
            "filename": "en-research.html",
            "pdf": "Mikhail_Razakov_Research_Engineer_EN.pdf",
            "title": "Mikhail Razakov — Research Engineer · Compilers & Programming Languages",
            "role": "Research Engineer · Compilers & Programming Languages",
            "brand": "compiler R&D · program analysis · language systems · experimental validation",
            "eyebrow": "models · conservative boundaries · fault injection · ablations · executable verification",
            "summary": (
                "Research-oriented compiler engineer who turns ambiguous compiler/language-system problems into explicit models, "
                "prototypes them, records applicability boundaries, and tests them with counterexamples and reproducible experiments. "
                "Professional grounding comes from LLVM work at MCST and industrial static analysis at ISP RAS; the strongest independent "
                "evidence is UniversalToolchain/contract-guided reverification and a conservative interprocedural Global-IV pass."
            ),
            "description": (
                "Research Engineer in compilers and programming languages: LLVM, program analysis, extensible language systems, "
                "controlled experiments, fault injection, ablations, differential testing, and correctness-oriented engineering."
            ),
            "proofs": [
                [
                    "Research engineering cycle",
                    "UniversalToolchain: problem model → four verification policies → frozen corpora/controls → injected faults → ablations → explicit blocked claims.",
                ],
                [
                    "Compiler correctness under uncertainty",
                    "Global-IV: affine model + transitive call effects + legality/must-execute boundaries; unsupported cases fail closed and are covered by reject regressions.",
                ],
                [
                    "Hands-on systems depth",
                    "Professional LLVM/static analysis plus Roslyn fixed-point data flow and a separately verified x86-64 register-allocation/codegen pipeline.",
                ],
            ],
            "project_ids": ["wist", "globaliv", "deref", "codegen"],
            "skills": [
                [
                    "Research Engineering",
                    "hypothesis-driven prototyping, controlled experiments, frozen corpora, fault injection, matched controls, ablations, explicit validity boundaries",
                ],
                [
                    "Compilers / Program Analysis",
                    "LLVM 22, LLVM IR, CFG/SSA, dominators, loop/interprocedural analysis, Roslyn CFG, fixed-point data flow, transformation legality",
                ],
                [
                    "Language Systems",
                    "typed artifact contracts, feature/component composition, deterministic planning, provider/order/conflict resolution, exact runtime binding",
                ],
                [
                    "Verification & Backends",
                    "LLVM Verifier, idempotence checks, differential execution, interpreter/CIL parity, x86-64 codegen, register-allocation verification",
                ],
            ],
            "contact_heading": (
                "Target roles: Research Engineer · Compiler R&D · Programming Languages / Language Systems · Program Analysis"
            ),
            "footer": "Research Engineer · Compilers & Programming Languages",
            "recognition": copy.deepcopy(data["profiles"]["compiler"]["en"]["recognition"]),
            "project_summaries": copy.deepcopy(data["profiles"]["compiler"]["en"]["project_summaries"]),
            "print_layout": "application",
            "show_portrait": False,
            "print_project_limit": 4,
        }
    )
    research["en"]["project_summaries"]["wist"] = {
        "type": ".NET · extensible compiler/language systems · research engineering",
        "solution": (
            "Investigate contract-guided reverification for extensible compiler pipelines: components declare owned facts, effects, "
            "invalidations, and verifier routes; a fail-closed scheduler applies structural-only, invalidation-only, selective, and always-verify policies. "
            "The underlying UniversalToolchain architecture freezes typed contributions/providers/order/routes into an immutable LanguagePlan before execution."
        ),
        "result": (
            "Evidence-backed anonymous CGO’27 draft, not yet a submission: frozen boundary corpus, 100 valid controls per policy, "
            "source-to-result fault injection, a second language package, and mechanism/policy ablations. Selective/always detect all "
            "targeted semantic faults; whole-compilation speedup and an independent external corpus remain explicitly unsupported."
        ),
    }
    research["en"]["project_summaries"]["globaliv"] = {
        "type": "C++23 · LLVM 22 · interprocedural analysis · conservative optimization",
        "solution": (
            "Modeled safe localization of induction-like global state using APInt affine evolution, transitive call effects, "
            "loop/dominator reasoning, and must-execute conditions; legality is separate from transformation and uncertain CFG/call cases are rejected."
        ),
        "result": (
            "29 transform/reject regressions; LLVM Verifier, second-pass idempotence, and executable before/after comparison act as independent correctness oracles."
        ),
    }
    data["profiles"]["research"] = research

    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
