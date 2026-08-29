#!/usr/bin/env python3
import json
from pathlib import Path

path = Path("data/site.json")
data = json.loads(path.read_text(encoding="utf-8"))
data["version"] = int(data.get("version", 0)) + 1
data["updated_at"] = "2026-08-29"

# Keep the landing/profile chooser aligned with the new primary positioning.
data["profile_ui"]["general"].update({
    "label_ru": "Compiler / Static Analysis",
    "label_en": "Compiler / Static Analysis",
    "landing_title": "Compiler / Static Analysis Engineer",
    "landing_description_ru": "LLVM, static/program analysis, Roslyn data-flow analysis, compiler backends и developer tooling."
})
data["profile_ui"]["compiler"].update({
    "label_ru": "Compiler / LLVM",
    "label_en": "Compiler / LLVM",
    "landing_title": "Compiler / LLVM Engineer",
    "landing_description_ru": "LLVM optimization passes, interprocedural analysis, legality, IR transforms и compiler infrastructure."
})

isp_ru = {
    "date": "2026 — сейчас",
    "title": "ИСП РАН — SharpChecker",
    "org": "Static analysis · C#/.NET",
    "bullets": [
        "Работаю над SharpChecker — платформой статического анализа C#/.NET в ИСП РАН."
    ]
}
isp_en = {
    "date": "2026 — present",
    "title": "ISP RAS — SharpChecker",
    "org": "Static analysis · C#/.NET",
    "bullets": [
        "Working on SharpChecker, ISP RAS's static-analysis platform for C#/.NET."
    ]
}
mcst_ru = {
    "date": "июль — август 2026",
    "title": "МЦСТ — стажёр по разработке компиляторов",
    "org": "LLVM 22 · C++23 · compiler engineering",
    "bullets": [
        "Реализовал собственный LLVM LICM-pass: loop analysis, проверки side effects/speculative safety и hoisting loop-invariant инструкций в preheader.",
        "Развивал консервативный межпроцедурный анализ глобальных IV: affine evolution на APInt, transitive effects, отдельная legality-фаза и LLVM IR transformation; неподдерживаемые CFG/call cases отклоняются."
    ]
}
mcst_en = {
    "date": "July — August 2026",
    "title": "MCST — Compiler Engineering Intern",
    "org": "LLVM 22 · C++23 · compiler engineering",
    "bullets": [
        "Implemented an LLVM LICM pass with loop analysis, side-effect/speculative-safety checks, and hoisting of loop-invariant instructions to preheaders.",
        "Developed conservative interprocedural global-IV analysis with APInt affine evolution, transitive effects, a separate legality phase, and LLVM IR transformation; unsupported CFG/call cases are rejected."
    ]
}

award_ru = [[
    "2026",
    "UniversalToolchain — Балтийский научно-инженерный конкурс",
    "Диплом I степени и Главная премия «Совершенство как надежда» за UniversalToolchain."
]]
award_en = [[
    "2026",
    "UniversalToolchain — Baltic Science and Engineering Competition",
    "First Degree Diploma and Grand Prize “Perfection as Hope” for UniversalToolchain."
]]

common_projects = ["globaliv", "deref", "wist", "codegen"]

general_ru = {
    "filename": "ru.html",
    "pdf": "Mikhail_Razakov_Software_Engineer_RU.pdf",
    "title": "Михаил Разаков — Compiler / Static Analysis Engineer",
    "role": "Compiler / Static Analysis Engineer",
    "brand": "LLVM · static analysis · program analysis · compiler infrastructure",
    "eyebrow": "LLVM · Roslyn · CFG/SSA · data-flow · x86-64",
    "summary": "Инженер по компиляторам и статическому анализу: LLVM-оптимизации и program analysis, data-flow-анализ на Roslyn, compiler infrastructure и backend/codegen.",
    "description": "Михаил Разаков — Compiler / Static Analysis Engineer: LLVM, static/program analysis, Roslyn data-flow analysis, CFG/SSA, register allocation и x86-64 code generation.",
    "proofs": [
        ["Compiler engineering", "Опыт МЦСТ: LLVM optimization passes, loop analysis, interprocedural analysis и legality для IR transforms."],
        ["Static analysis", "SharpChecker в ИСП РАН и самостоятельный Roslyn CFG fixed-point data-flow analyzer."],
        ["Backends & verification", "SSA-like IR, liveness/interference, register allocation, x86-64 codegen и differential execution."]
    ],
    "experience": [isp_ru, mcst_ru],
    "project_ids": common_projects,
    "skills": [
        ["Compilers", "C++, LLVM, LLVM IR, optimization passes, interprocedural analysis, CFG, SSA, dominators, loop analysis, LICM, legality analysis"],
        ["Static / Program Analysis", "C#, .NET, Roslyn, ControlFlowGraph, fixed-point data-flow analysis, state propagation and joins"],
        ["Codegen / Tooling", "register allocation, liveness analysis, x86-64, CMake, Linux, GitHub Actions, differential testing"]
    ],
    "contact_heading": "Целевые роли: Compiler Engineer · LLVM Engineer · Static / Program Analysis Engineer · Compiler Infrastructure",
    "footer": "Compiler / Static Analysis Engineer",
    "recognition": award_ru
}
general_en = {
    "filename": "en.html",
    "pdf": "Mikhail_Razakov_Software_Engineer_EN.pdf",
    "title": "Mikhail Razakov — Compiler / Static Analysis Engineer",
    "role": "Compiler / Static Analysis Engineer",
    "brand": "LLVM · static analysis · program analysis · compiler infrastructure",
    "eyebrow": "LLVM · Roslyn · CFG/SSA · data-flow · x86-64",
    "summary": "Compiler and static-analysis engineer working across LLVM optimization and program analysis, Roslyn data-flow analysis, compiler infrastructure, and backend/codegen projects.",
    "description": "Mikhail Razakov — Compiler / Static Analysis Engineer: LLVM, static/program analysis, Roslyn data-flow analysis, CFG/SSA, register allocation, and x86-64 code generation.",
    "proofs": [
        ["Compiler engineering", "MCST experience with LLVM optimization passes, loop analysis, interprocedural analysis, and legality for IR transforms."],
        ["Static analysis", "SharpChecker at ISP RAS plus an independent Roslyn CFG fixed-point data-flow analyzer."],
        ["Backends & verification", "SSA-like IR, liveness/interference, register allocation, x86-64 codegen, and differential execution."]
    ],
    "experience": [isp_en, mcst_en],
    "project_ids": common_projects,
    "skills": [
        ["Compilers", "C++, LLVM, LLVM IR, optimization passes, interprocedural analysis, CFG, SSA, dominators, loop analysis, LICM, legality analysis"],
        ["Static / Program Analysis", "C#, .NET, Roslyn, ControlFlowGraph, fixed-point data-flow analysis, state propagation and joins"],
        ["Codegen / Tooling", "register allocation, liveness analysis, x86-64, CMake, Linux, GitHub Actions, differential testing"]
    ],
    "contact_heading": "Target roles: Compiler Engineer · LLVM Engineer · Static / Program Analysis Engineer · Compiler Infrastructure",
    "footer": "Compiler / Static Analysis Engineer",
    "recognition": award_en
}

compiler_ru = dict(general_ru)
compiler_ru.update({
    "filename": "ru-compiler.html",
    "pdf": "Mikhail_Razakov_Compiler_RU.pdf",
    "title": "Михаил Разаков — Compiler / LLVM Engineer",
    "role": "Compiler / LLVM Engineer",
    "brand": "LLVM · LLVM IR · optimization · program analysis",
    "summary": "Compiler / LLVM engineer: optimization passes, interprocedural analysis, loop/dominator reasoning, legality analysis и проверяемые LLVM IR transforms; также static analysis и backend/codegen.",
    "description": "Михаил Разаков — Compiler / LLVM Engineer: LLVM IR, optimization passes, interprocedural analysis, loop analysis, legality, static analysis и compiler backends.",
    "contact_heading": "Целевые роли: Compiler Engineer · LLVM Engineer · Compiler Infrastructure · Program Analysis",
    "footer": "Compiler / LLVM Engineer"
})
compiler_en = dict(general_en)
compiler_en.update({
    "filename": "en-compiler.html",
    "pdf": "Mikhail_Razakov_Compiler_EN.pdf",
    "title": "Mikhail Razakov — Compiler / LLVM Engineer",
    "role": "Compiler / LLVM Engineer",
    "brand": "LLVM · LLVM IR · optimization · program analysis",
    "summary": "Compiler / LLVM engineer focused on optimization passes, interprocedural analysis, loop/dominator reasoning, legality analysis, and verifiable LLVM IR transforms, with additional static-analysis and backend/codegen work.",
    "description": "Mikhail Razakov — Compiler / LLVM Engineer: LLVM IR, optimization passes, interprocedural analysis, loop analysis, legality, static analysis, and compiler backends.",
    "contact_heading": "Target roles: Compiler Engineer · LLVM Engineer · Compiler Infrastructure · Program Analysis",
    "footer": "Compiler / LLVM Engineer"
})

data["profiles"]["general"]["ru"] = general_ru
data["profiles"]["general"]["en"] = general_en
data["profiles"]["compiler"]["ru"] = compiler_ru
data["profiles"]["compiler"]["en"] = compiler_en

projects = data["projects"]
projects["globaliv"] = {
    "title": "LLVM Interprocedural Global IV Optimization",
    "type_ru": "C++23 · LLVM 22 · interprocedural analysis · optimization",
    "type_en": "C++23 · LLVM 22 · interprocedural analysis · optimization",
    "problem_ru": "Нужно доказуемо распознавать affine evolution глобальных IV между функциями и выполнять IR transformation только при достаточных условиях корректности.",
    "problem_en": "The pass must recognize affine evolution of global IVs across calls and transform IR only when correctness conditions are established.",
    "solution_ru": "Affine b + k·x на APInt, transitive function/module effects, loop/dominator/must-execute reasoning и отдельная conservative legality-фаза с отказом на unsupported CFG/calls.",
    "solution_en": "APInt affine b + k·x evolution, transitive function/module effects, loop/dominator/must-execute reasoning, and a separate conservative legality phase that rejects unsupported CFG/calls.",
    "result_ru": "Консервативный LLVM 22 prototype/MVP с реальным IR transform; 29 positive/negative regression cases проверяют verifier validity, idempotence и before/after execution.",
    "result_en": "A conservative LLVM 22 prototype/MVP with an actual IR transform; 29 positive/negative regression cases cover verifier validity, idempotence, and before/after execution.",
    "repo": "https://github.com/Misha1302/LLVM-interprocedural-global-IV-optimization",
    "public": True
}
projects["deref"] = {
    "title": "DerefAfterNullAnalyzer",
    "type_ru": "C# · Roslyn · static analysis · data-flow",
    "type_en": "C# · Roslyn · static analysis · data-flow",
    "problem_ru": "Нужно находить потенциально небезопасное разыменование после возможного null с учётом ветвлений, циклов и слияния control-flow.",
    "problem_en": "The analyzer must detect potentially unsafe dereferences after a possible null while accounting for branches, loops, and control-flow joins.",
    "solution_ru": "Roslyn ControlFlowGraph и forward fixed-point data-flow analysis: состояния Unknown/MaybeNull/NotNull передаются между basic blocks и объединяются на join points.",
    "solution_en": "Roslyn ControlFlowGraph with forward fixed-point data-flow analysis: Unknown/MaybeNull/NotNull states propagate across basic blocks and merge at join points.",
    "result_ru": "Диагностика потенциально небезопасных dereference paths поверх реального CFG, включая повторную обработку successors до стабилизации состояния.",
    "result_en": "Diagnostics for potentially unsafe dereference paths over the real CFG, with successor reprocessing until the data-flow state reaches a fixed point.",
    "repo": "https://github.com/Misha1302/DerefAfterNullAnalyzer",
    "public": True
}
projects["wist"].update({
    "title": "UniversalToolchain",
    "type_ru": ".NET · modular compiler/runtime framework",
    "type_en": ".NET · modular compiler/runtime framework",
    "problem_ru": "Независимые компоненты языка должны детерминированно собираться в compiler/runtime pipeline без скрытой зависимости от порядка регистрации.",
    "problem_en": "Independent language components must compose into a compiler/runtime pipeline deterministically, without hidden registration-order dependencies.",
    "solution_ru": "Typed intermediate artifacts, детерминированный LanguagePlan, зависимости/конфликты contributions, pass ordering и точная backend routing.",
    "solution_en": "Typed intermediate artifacts, deterministic LanguagePlan construction, contribution dependencies/conflicts, pass ordering, and exact backend routing.",
    "result_ru": "Модульный framework отделяет language composition от runtime execution и закрепляет контракты executable verification/tests.",
    "result_en": "The modular framework separates language composition from runtime execution and backs its contracts with executable verification/tests."
})
projects["codegen"].update({
    "type_ru": "Rust · SSA/CFG · register allocation · SysV x86-64",
    "type_en": "Rust · SSA/CFG · register allocation · SysV x86-64",
    "solution_ru": "SSA-подобное IR с CFG/SSA validation, liveness/interference, register allocation с независимым assignment verifier, phi lowering и SysV x86-64 codegen.",
    "solution_en": "SSA-like IR with CFG/SSA validation, liveness/interference, register allocation with an independent assignment verifier, phi lowering, and SysV x86-64 code generation.",
    "result_ru": "Reference interpreter и differential execution проверяют семантическую эквивалентность сгенерированного кода; allocator contract валидируется отдельно.",
    "result_en": "A reference interpreter and differential execution check generated-code semantics; the allocator assignment contract is verified independently."
})

# Remove the not-yet-publicly-confirmed LangDev acceptance claim.
for lang in ("ru", "en"):
    data["recognition"][lang] = [item for item in data["recognition"][lang] if "LangDev" not in item[1]]

# Wist2 is an old repository/product name; keep public copy on the current name.
def replace_old_name(value):
    if isinstance(value, str):
        return value.replace("UniversalToolchain / Wist2", "UniversalToolchain").replace("UniversalToolchain/Wist2", "UniversalToolchain")
    if isinstance(value, list):
        return [replace_old_name(x) for x in value]
    if isinstance(value, dict):
        return {k: replace_old_name(v) for k, v in value.items()}
    return value

data = replace_old_name(data)
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
