#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
site_path = root / "data" / "site.json"
data = json.loads(site_path.read_text(encoding="utf-8"))

ru_summaries = {
    "globaliv": {
        "solution": "Affine b + k·x на APInt, transitive effects, loop/dominator/must-execute reasoning и отдельная conservative legality-фаза перед IR transform.",
        "result": "LLVM 22 prototype/MVP: 29 positive/negative regression cases, verifier validity, idempotence и before/after execution checks."
    },
    "deref": {
        "solution": "Roslyn ControlFlowGraph + forward fixed-point data-flow: Unknown/MaybeNull/NotNull состояния передаются между basic blocks и объединяются на join points.",
        "result": "Анализ повторно обходит successors до стабилизации и выдаёт diagnostics для потенциально небезопасных dereference paths."
    },
    "wist": {
        "solution": "Модульный .NET compiler/runtime framework с typed intermediate artifacts, детерминированным LanguagePlan, pass ordering и exact backend routing.",
        "result": "Language composition отделена от runtime execution; архитектурные контракты закреплены executable verification/tests."
    },
    "codegen": {
        "solution": "SSA-like IR, CFG/SSA validation, liveness/interference, register allocation с independent assignment verifier, phi lowering и SysV x86-64 codegen.",
        "result": "Reference interpreter и differential execution проверяют семантику generated code; allocator contract валидируется отдельно."
    }
}
en_summaries = {
    "globaliv": {
        "solution": "APInt affine b + k·x evolution, transitive effects, loop/dominator/must-execute reasoning, and a separate conservative legality phase before IR transformation.",
        "result": "LLVM 22 prototype/MVP with 29 positive/negative regression cases covering verifier validity, idempotence, and before/after execution."
    },
    "deref": {
        "solution": "Roslyn ControlFlowGraph with forward fixed-point data-flow: Unknown/MaybeNull/NotNull states propagate across basic blocks and merge at join points.",
        "result": "Successors are reprocessed until the state stabilizes, producing diagnostics for potentially unsafe dereference paths."
    },
    "wist": {
        "solution": "A modular .NET compiler/runtime framework with typed intermediate artifacts, deterministic LanguagePlan construction, pass ordering, and exact backend routing.",
        "result": "Language composition is separated from runtime execution and backed by executable verification/tests."
    },
    "codegen": {
        "solution": "SSA-like IR, CFG/SSA validation, liveness/interference, register allocation with an independent assignment verifier, phi lowering, and SysV x86-64 codegen.",
        "result": "A reference interpreter and differential execution check generated-code semantics; the allocator contract is verified independently."
    }
}

for lang, summaries in (("ru", ru_summaries), ("en", en_summaries)):
    profile = data["profiles"]["compiler"][lang]
    profile["project_summaries"] = summaries
    profile["show_portrait"] = True
    profile["portrait_asset"] = "assets/portrait.jpg"

site_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

build_path = root / "tools" / "build_site.py"
text = build_path.read_text(encoding="utf-8")

def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected one occurrence, got {count}: {old[:80]!r}")
    text = text.replace(old, new, 1)

replace_once('title = "Михаил Разаков — Software Engineer"', 'title = "Михаил Разаков — Compiler / Static Analysis Engineer"')
replace_once('project_cases = "".join(project_card(data, "ru", project_id) for project_id in ["wist", "vpn", "psform"])', 'project_cases = "".join(project_card(data, "ru", project_id) for project_id in ["globaliv", "deref", "wist"])')
replace_once('<span>Software Engineer</span>', '<span>Compiler / Static Analysis Engineer</span>')
replace_once('<p class="eyebrow">Архитектура платформ · .NET backend · compiler/runtime</p><h1>Проектирую и реализую сложные программные системы.</h1>', '<p class="eyebrow">LLVM · static analysis · program analysis · compiler infrastructure</p><h1>Compiler / Static Analysis Engineer</h1>')
replace_once('<div class="landing-evidence"><span>Typed contracts · exact runtime binding</span><span>State machines · idempotency · recovery</span><span>LLVM · SSA · x86-64</span></div>', '<div class="landing-evidence"><span>MCST · LLVM 22 · C++</span><span>ISP RAS · SharpChecker · static analysis</span><span>CFG/SSA · data-flow · x86-64</span></div>')
replace_once('Основной профиль — Software Engineer — Architecture & Platforms. Специализированные версии меняют приоритет доказательств, но не противоречат друг другу.', 'Основной профиль — Compiler / Static Analysis Engineer. Специализированные версии меняют приоритет доказательств, но сохраняют единый набор проверенных фактов.')
replace_once('<span>{esc(p[\'name_ru\'])} · Software Engineer</span>', '<span>{esc(p[\'name_ru\'])} · Compiler / Static Analysis Engineer</span>')

replace_once(
'        "codegen": "Нужно сравнивать высокоуровневую семантику и машинный код в изолированном процессе с ограничениями ресурсов." if lang == "ru" else "High-level semantics and machine code must be compared in an isolated, resource-limited process.",\n',
'        "codegen": "Нужно сравнивать высокоуровневую семантику и машинный код в изолированном процессе с ограничениями ресурсов." if lang == "ru" else "High-level semantics and machine code must be compared in an isolated, resource-limited process.",\n        "globaliv": "Transform допустим только при доказанной affine evolution и legality; unsupported CFG/calls должны приводить к отказу, а не к небезопасной оптимизации." if lang == "ru" else "The transform is allowed only when affine evolution and legality are established; unsupported CFG/calls must be rejected rather than optimized unsafely.",\n        "deref": "Анализ должен корректно сходиться на ветвлениях, циклах и join points без path explosion." if lang == "ru" else "The analysis must converge correctly across branches, loops, and join points without path explosion.",\n')
replace_once(
'        "codegen": "Differential comparison with an IR interpreter, isolated execution, disassembly, and spill/reload metrics." if lang == "en" else "Дифференциальное сравнение с IR-интерпретатором, изолированный запуск, дизассемблирование и метрики spill/reload.",\n',
'        "codegen": "Differential comparison with an IR interpreter, isolated execution, disassembly, and spill/reload metrics." if lang == "en" else "Дифференциальное сравнение с IR-интерпретатором, изолированный запуск, дизассемблирование и метрики spill/reload.",\n        "globaliv": "29 positive/negative IR regressions, LLVM verifier checks, idempotence, and before/after execution comparison." if lang == "en" else "29 positive/negative IR regression cases, LLVM verifier, idempotence и сравнение исполнения до/после преобразования.",\n        "deref": "Analyzer tests plus fixed-point worklist convergence over the Roslyn CFG, including branches and loops." if lang == "en" else "Analyzer tests и сходимость fixed-point worklist по Roslyn CFG, включая ветвления и циклы.",\n')
replace_once(
'        "codegen": "IR, liveness, register allocation, code emission и differential harness." if lang == "ru" else "IR, liveness, register allocation, code emission, and the differential harness.",\n',
'        "codegen": "IR, liveness, register allocation, code emission и differential harness." if lang == "ru" else "IR, liveness, register allocation, code emission, and the differential harness.",\n        "globaliv": "Модель affine evolution, interprocedural effects, legality analysis, LLVM IR transform и regression harness." if lang == "ru" else "Affine-evolution model, interprocedural effects, legality analysis, LLVM IR transform, and regression harness.",\n        "deref": "CFG/data-flow реализация, merge logic, diagnostics и analyzer tests." if lang == "ru" else "CFG/data-flow implementation, merge logic, diagnostics, and analyzer tests.",\n')

build_path.write_text(text, encoding="utf-8")
