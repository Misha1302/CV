#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "data" / "site.json"
FACTS = ROOT / "FACT-RETENTION.md"


def pick_experience(profile: dict, needle: str) -> dict:
    for entry in profile["experience"]:
        if needle.casefold() in entry["title"].casefold():
            return entry
    raise RuntimeError(f"Missing experience entry containing {needle!r}")


def rebuild() -> None:
    data = json.loads(SITE.read_text(encoding="utf-8"))
    profiles = data["profiles"]
    ru = profiles["compiler"]["ru"]
    en = profiles["compiler"]["en"]

    assert ru["role"] == "Compiler & Program Analysis Engineer"
    assert en["role"] == "Compiler & Program Analysis Engineer"

    # Preserve canonical dates/titles already present in the source; rebuild only claims.
    ru_isp = pick_experience(ru, "ИСП РАН")
    ru_mcst = pick_experience(ru, "МЦСТ")
    en_isp = pick_experience(en, "ISP RAS")
    en_mcst = pick_experience(en, "MCST")

    ru_isp["org"] = "SharpChecker · C#/.NET · program analysis"
    ru_isp["bullets"] = [
        "Участвую в разработке SharpChecker — промышленной Roslyn-based платформы статического анализа C#/.NET в ИСП РАН.",
        "Текущие задачи включают symbolic computations / symbolic execution в анализе C#-программ.",
    ]
    en_isp["org"] = "SharpChecker · C#/.NET · program analysis"
    en_isp["bullets"] = [
        "Contribute to SharpChecker, ISP RAS’s industrial Roslyn-based static-analysis platform for C#/.NET.",
        "Current tasks include symbolic-computation / symbolic-execution work in C# program analysis.",
    ]

    ru_mcst["bullets"] = [
        "Реализовал LLVM 22 LICM-pass: loop analysis, side-effect/speculative-safety checks и вынос доказанно инвариантных инструкций в preheader.",
        "Разработал консервативный interprocedural global-IV prototype: APInt-аффинная эволюция, транзитивные call effects, отдельная legality-проверка и LLVM IR transformation; unsupported cases отклоняются без изменения программы.",
    ]
    en_mcst["bullets"] = [
        "Implemented an LLVM 22 LICM pass with loop analysis, side-effect/speculative-safety checks, and hoisting only proven invariants to preheaders.",
        "Developed a conservative interprocedural global-IV prototype with APInt affine evolution, transitive call effects, a separate legality phase, and LLVM IR transformation; unsupported cases are rejected unchanged.",
    ]

    ru_vpn = pick_experience(profiles["backend"]["ru"], "VpnMediator")
    en_vpn = pick_experience(profiles["backend"]["en"], "VpnMediator")
    ru_production = {
        "date": ru_vpn["date"],
        "title": "Independent Engineering — stateful systems & reliability",
        "org": "VpnMediator · payments · recovery · Linux",
        "bullets": [
            "Отвечаю за stateful subscription backend: explicit payment/access states, idempotent reconciliation, migrations, backup/restore, health gates и rollback; release gate — 388 Python + 148 .NET tests."
        ],
    }
    en_production = {
        "date": en_vpn["date"],
        "title": "Independent Engineering — stateful systems & reliability",
        "org": "VpnMediator · payments · recovery · Linux",
        "bullets": [
            "Own a stateful subscription backend: explicit payment/access states, idempotent reconciliation, migrations, backup/restore, health gates, and rollback; release gate: 388 Python + 148 .NET tests."
        ],
    }

    ru["brand"] = "LLVM · static analysis · x86-64 codegen · language infrastructure"
    en["brand"] = "LLVM · static analysis · x86-64 codegen · language infrastructure"
    ru["eyebrow"] = "LLVM 22 · interprocedural analysis · Roslyn · x86-64 backend"
    en["eyebrow"] = "LLVM 22 · interprocedural analysis · Roslyn · x86-64 backend"

    ru["summary"] = (
        "Инженер по компиляторам и анализу программ: МЦСТ — LLVM 22 optimization; ИСП РАН/SharpChecker — C# static analysis. "
        "Публичные проекты подтверждают conservative legality, Roslyn fixed-point data-flow и x86-64 register allocation; вне compiler work отвечаю за stateful backend с idempotency, recovery и rollback."
    )
    en["summary"] = (
        "Compiler and program-analysis engineer: LLVM 22 optimization at MCST and C# static analysis at ISP RAS/SharpChecker. "
        "Public projects demonstrate conservative legality, Roslyn fixed-point data flow, and x86-64 register allocation; beyond compiler work I own a stateful backend with idempotency, recovery, and rollback."
    )

    ru["description"] = (
        "Михаил Разаков — Compiler & Program Analysis Engineer: LLVM 22, interprocedural analysis, legality, Roslyn data-flow, symbolic execution, x86-64 codegen и reliability ownership."
    )
    en["description"] = (
        "Mikhail Razakov — Compiler & Program Analysis Engineer: LLVM 22, interprocedural analysis, legality, Roslyn data flow, symbolic execution, x86-64 code generation, and reliability ownership."
    )

    ru["proofs"] = [
        ["Professional compiler / analysis", "МЦСТ: LLVM 22 LICM/global-IV; ИСП РАН: SharpChecker C#/.NET static analysis."],
        ["Validated LLVM transformation", "Global-IV: 29 positive/negative regressions, LLVM Verifier, structural checks, idempotence и before/after execution."],
        ["Production ownership", "VpnMediator: explicit state, reconciliation, migrations, backup/restore, health gates и rollback; release gate — 388 Python + 148 .NET tests."],
    ]
    en["proofs"] = [
        ["Professional compiler / analysis", "MCST: LLVM 22 LICM/global-IV; ISP RAS: SharpChecker C#/.NET static analysis."],
        ["Validated LLVM transformation", "Global-IV: 29 positive/negative regressions, LLVM Verifier, structural checks, idempotence, and before/after execution."],
        ["Production ownership", "VpnMediator: explicit state, reconciliation, migrations, backup/restore, health gates, and rollback; release gate: 388 Python + 148 .NET tests."],
    ]

    ru["experience"] = [ru_isp, ru_mcst, ru_production]
    en["experience"] = [en_isp, en_mcst, en_production]

    # One-page CV budget: each printed project has a distinct hiring job.
    # UniversalToolchain remains on the web CV as language-infrastructure evidence.
    ru["project_ids"] = ["globaliv", "deref", "codegen", "wist"]
    en["project_ids"] = ["globaliv", "deref", "codegen", "wist"]
    ru["print_project_limit"] = 3
    en["print_project_limit"] = 3

    ru["skills"] = [
        ["Compiler / IR", "C++23, LLVM 22/IR, APInt, interprocedural analysis, CFG/SSA, dominators, loops, LICM, legality, LLVM Verifier"],
        ["Анализ программ", "C#/.NET, Roslyn CFG, fixed-point data-flow, symbolic execution, conditional edges, loops/back edges, state propagation/joins"],
        ["Backend / codegen", "Rust, SysV x86-64, liveness/interference, linear scan, simulated annealing, spills, phi lowering, differential execution"],
        ["Infrastructure / reliability", "typed contracts, deterministic planning, interpreter/CIL parity, state machines, idempotency, recovery, migrations, rollback"],
    ]
    en["skills"] = [
        ["Compiler / IR", "C++23, LLVM 22/IR, APInt, interprocedural analysis, CFG/SSA, dominators, loops, LICM, legality, LLVM Verifier"],
        ["Program Analysis", "C#/.NET, Roslyn CFG, fixed-point data flow, symbolic execution, conditional edges, loops/back edges, state propagation/joins"],
        ["Backend / Codegen", "Rust, SysV x86-64, liveness/interference, linear scan, simulated annealing, spills, phi lowering, differential execution"],
        ["Infrastructure / Reliability", "typed contracts, deterministic planning, interpreter/CIL parity, state machines, idempotency, recovery, migrations, rollback"],
    ]

    ru["contact_heading"] = "Целевые роли: Compiler Engineer · Program Analysis · Static Analysis · Compiler / Language Infrastructure"
    en["contact_heading"] = "Target roles: Compiler Engineer · Program Analysis · Static Analysis · Compiler / Language Infrastructure"

    ru["project_summaries"]["wist"]["result"] = (
        "Текущий exact test manifest: 1 324/1 324 passing; interpreter/CIL parity, exact package binding и fail-closed runtime checks защищают выбранный execution plan."
    )
    en["project_summaries"]["wist"]["result"] = (
        "Current exact test manifest: 1,324/1,324 passing; interpreter/CIL parity, exact package binding, and fail-closed runtime checks protect the selected execution plan."
    )

    SITE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    facts = FACTS.read_text(encoding="utf-8")
    facts = facts.replace(
        "UniversalToolchain current exact test manifest on master (verified at commit `36206b66548fec365be6e03381ba44d50c2cafe5`): 1,306 passed, 0 failed, 0 skipped.",
        "UniversalToolchain current exact test manifest on master (verified at commit `40117eb68c630f7129c120aaaadc69be8f4ecbfb`): 1,324 passed, 0 failed, 0 skipped.",
    )
    if "SharpChecker contribution boundary:" not in facts:
        facts += (
            "- SharpChecker contribution boundary: current employment and symbolic-computation/symbolic-execution task scope are user-reported; public evidence verifies SharpChecker's Roslyn-based industrial analyzer architecture but not ownership of the overall engine.\n"
            "- VpnMediator reliability evidence: current release-validation record reports 388 Python + 148 .NET tests together with idempotence, reconciliation, migration, backup/restore, health-gate, and rollback checks.\n"
        )
    FACTS.write_text(facts, encoding="utf-8")


if __name__ == "__main__":
    rebuild()
