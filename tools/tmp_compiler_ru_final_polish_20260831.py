from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data_path = ROOT / "data" / "site.json"
style_path = ROOT / "style.css"

data = json.loads(data_path.read_text(encoding="utf-8"))
if data.get("version") != 55:
    raise RuntimeError(f"Expected site version 55, got {data.get('version')!r}")

data["version"] = 56
data["updated_at"] = "2026-08-31"
ru = data["profiles"]["compiler"]["ru"]

ru["brand"] = "LLVM · преобразования IR · межпроцедурный анализ · статический анализ"
ru["eyebrow"] = "LLVM 22 · CFG/SSA · допустимость преобразований · Roslyn"
ru["summary"] = (
    "Инженер по компиляторам с профессиональным опытом разработки на LLVM и статического анализа. "
    "В МЦСТ реализовал LICM-pass для LLVM 22 и прототип межпроцедурного анализа глобальных переменных "
    "с отдельными проверками допустимости преобразований IR; сейчас участвую в разработке SharpChecker в ИСП РАН. "
    "В собственных проектах занимаюсь анализом CFG и потоков данных, генерацией x86-64 кода, "
    "распределением регистров и инфраструктурой компилятора."
)
ru["description"] = (
    "Михаил Разаков — Compiler / LLVM Engineer: LLVM 22, оптимизационные проходы, межпроцедурный анализ, "
    "проверки допустимости преобразований IR, анализ потоков данных Roslyn и генерация x86-64 кода."
)

ru["experience"][1]["org"] = "LLVM 22 · C++23 · разработка компиляторов"
ru["experience"][1]["bullets"] = [
    "Реализовал LICM-pass для LLVM 22: анализ циклов, проверки побочных эффектов и безопасности спекулятивного выполнения, вынос инвариантных инструкций в preheader.",
    "Разработал консервативный прототип межпроцедурного анализа глобальных переменных: аффинная эволюция на APInt, транзитивные эффекты вызовов, отдельная проверка допустимости и преобразование LLVM IR; неподдерживаемые CFG и вызовы отклоняются без изменения программы.",
]

summaries = ru["project_summaries"]
summaries["globaliv"]["solution"] = (
    "Проход LLVM 22 для межпроцедурного анализа линейной эволюции глобальных переменных и безопасного преобразования IR. "
    "Использует APInt, анализ циклов и доминаторов, транзитивные эффекты вызовов и условия must-execute."
)
summaries["deref"] = {
    "type": "C# · Roslyn · статический анализ · анализ потоков данных",
    "solution": "Анализ на Roslyn ControlFlowGraph с прямым анализом потоков данных до неподвижной точки: состояния Unknown/MaybeNull/NotNull распространяются между базовыми блоками и объединяются в точках слияния.",
    "result": "Повторно обрабатывает последующие блоки до стабилизации состояния и диагностирует потенциально небезопасное разыменование.",
}
summaries["wist"] = {
    "type": ".NET · инфраструктура компилятора · детерминированная композиция",
    "solution": "Модульная .NET-инфраструктура для построения языковых и компиляторных цепочек. Типизированные контракты артефактов, зависимости и конфликты, выбор провайдеров, порядок проходов и маршруты артефактов заранее сводятся в неизменяемый LanguagePlan.",
    "result": "Исполняющая часть проверяет точный запланированный граф пакетов и компонентов и создаёт выбранные компоненты без повторного планирования; контракт покрыт проверками детерминизма, точного связывания, владения ресурсами и согласованности интерпретатора с CIL-backend.",
}
summaries["codegen"] = {
    "type": "Rust · SSA/CFG · распределение регистров · SysV x86-64",
    "solution": "SSA-подобное IR, проверки CFG/SSA, анализ живости и интерференции, распределение регистров с независимой проверкой назначения, понижение phi-узлов и генерация SysV x86-64.",
    "result": "Эталонный интерпретатор и дифференциальное выполнение проверяют семантическую эквивалентность сгенерированного кода; распределитель регистров валидируется отдельно.",
}

ru["skills"] = [
    ["Компиляторы", "C++23, LLVM 22, LLVM IR, оптимизационные проходы, межпроцедурный анализ, CFG/SSA, доминаторы, анализ циклов, LICM, проверки допустимости"],
    ["Статический анализ", "C#, .NET, Roslyn ControlFlowGraph, анализ потоков данных до неподвижной точки, распространение и объединение состояний"],
    ["Генерация кода", "Rust, SysV x86-64, анализ живости и интерференции, распределение регистров, понижение phi-узлов, дифференциальное выполнение"],
    ["Инфраструктура компилятора", "типизированные контракты артефактов, детерминированное планирование и порядок проходов, маршрутизация артефактов, композиция backend/runtime"],
]

data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

css = style_path.read_text(encoding="utf-8")
marker = "/* compiler editorial print v53 */"
if marker not in css:
    raise RuntimeError("Compiler print style anchor not found")
css = css[: css.index(marker)].rstrip() + "\n\n" + r'''/* compiler print readability v56 */
@media print {
  .profile-compiler .print-cv {
    padding: 11mm 12mm 10.5mm;
  }
  .profile-compiler .pcv-summary {
    margin: 3.8mm 0 4.5mm;
    font-size: 10pt;
    line-height: 1.38;
  }
  .profile-compiler .pcv-columns {
    grid-template-columns: 1.45fr .9fr;
    gap: 5mm;
  }
  .profile-compiler .pcv-main section + section,
  .profile-compiler .pcv-side section + section {
    margin-top: 3.8mm;
  }
  .profile-compiler .pcv-section-title {
    margin-bottom: 2mm;
    font-size: 9.8pt;
  }
  .profile-compiler .pcv-entry {
    grid-template-columns: 25mm 1fr;
    gap: 2.4mm;
    margin-bottom: 2.8mm;
  }
  .profile-compiler .pcv-date {
    font-size: 8.2pt;
  }
  .profile-compiler .pcv-entry h3,
  .profile-compiler .pcv-project h3 {
    font-size: 9.6pt;
  }
  .profile-compiler .pcv-entry li {
    font-size: 8.5pt;
    line-height: 1.32;
  }
  .profile-compiler .pcv-project {
    margin-bottom: 3mm;
  }
  .profile-compiler .pcv-project p {
    margin-top: .9mm;
    font-size: 8.45pt;
    line-height: 1.31;
  }
  .profile-compiler .pcv-project .pcv-project-result {
    margin-top: .6mm;
    color: #211a1c;
  }
  .profile-compiler .pcv-skill {
    margin-bottom: 2.2mm;
  }
  .profile-compiler .pcv-skill strong {
    font-size: 8.7pt;
  }
  .profile-compiler .pcv-skill span,
  .profile-compiler .pcv-compact p {
    font-size: 8.2pt;
    line-height: 1.28;
  }
  .profile-compiler .pcv-recognition {
    margin-bottom: 2.1mm;
    break-inside: avoid;
  }
  .profile-compiler .pcv-recognition strong {
    display: block;
    font-size: 8.25pt;
    line-height: 1.18;
  }
  .profile-compiler .pcv-recognition span {
    display: block;
    margin-top: .5mm;
    color: #4e4547;
    font-size: 7.9pt;
    line-height: 1.25;
  }
}
'''
style_path.write_text(css.rstrip() + "\n", encoding="utf-8")
