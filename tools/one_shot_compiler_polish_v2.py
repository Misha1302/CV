from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch_data() -> None:
    path = ROOT / "data" / "site.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["version"] = int(data.get("version", 0)) + 1
    data["updated_at"] = "2026-08-30"
    ru = data["profiles"]["compiler"]["ru"]

    ru["experience"][1]["bullets"] = [
        "Реализовал LLVM LICM-pass: анализ циклов, проверки побочных эффектов и безопасности спекулятивного выполнения, вынос инвариантных инструкций в preheader.",
        "Разрабатывал межпроцедурный анализ глобальных переменных и проверки допустимости (legality) для безопасных преобразований LLVM IR.",
    ]

    ru["project_summaries"]["globaliv"].update(
        {
            "type": "C++23 · LLVM 22 · межпроцедурный анализ · оптимизация",
            "solution": "Проход LLVM 22 для межпроцедурного анализа линейной эволюции глобальных переменных и безопасного преобразования IR. Использует APInt, анализ циклов и доминаторов, транзитивные эффекты вызовов и условия обязательного исполнения (must-execute).",
        }
    )
    ru["project_summaries"]["deref"] = {
        "type": "C# · Roslyn · статический анализ · анализ потоков данных",
        "solution": "Анализ на Roslyn ControlFlowGraph с прямым fixed-point data-flow: состояния Unknown/MaybeNull/NotNull распространяются между базовыми блоками и объединяются в точках слияния.",
        "result": "Повторно обрабатывает последующие блоки до стабилизации состояния и диагностирует потенциально небезопасное разыменование.",
    }
    ru["project_summaries"]["wist"].update(
        {
            "type": ".NET · модульная инфраструктура компилятора",
            "solution": "Модульный .NET framework для построения языковых и компиляторных цепочек: разбор → промежуточные представления → оптимизационные проходы → backend. Компоненты подключаются через явные контракты, а порядок и совместимость определяются до исполнения.",
        }
    )
    ru["project_summaries"]["codegen"] = {
        "type": "Rust · SSA/CFG · распределение регистров · SysV x86-64",
        "solution": "SSA-подобное IR, проверки CFG/SSA, анализ живости и интерференции, распределение регистров с независимой проверкой назначения, phi lowering и генерация SysV x86-64.",
        "result": "Эталонный интерпретатор и дифференциальное выполнение проверяют семантическую эквивалентность сгенерированного кода; распределитель регистров валидируется отдельно.",
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_generator() -> None:
    path = ROOT / "tools" / "build_site.py"
    source = path.read_text(encoding="utf-8")

    old_type = '    return f\'<article class="project-row"><div><span class="project-type">{esc(project[f"type_{lang}"])}</span><h3>{esc(project["title"])}</h3></div><div><p>{esc(copy[\'solution\'])}</p><p class="project-result">{esc(copy[\'result\'])}</p><div class="project-links">{"".join(links)}</div></div></article>\'\n'
    new_type = '    type_label = copy.get("type", project[f"type_{lang}"])\n    return f\'<article class="project-row"><div><span class="project-type">{esc(type_label)}</span><h3>{esc(project["title"])}</h3></div><div><p>{esc(copy[\'solution\'])}</p><p class="project-result">{esc(copy[\'result\'])}</p><div class="project-links">{"".join(links)}</div></div></article>\'\n'
    if source.count(old_type) != 1:
        raise RuntimeError(f"compiler project type anchor count={source.count(old_type)}")
    source = source.replace(old_type, new_type, 1)

    old_print = '''        project_text = summary.get("result") or project[f"result_{lang}"]
        projects.append(f'<article class="pcv-project"><h3><a href="{esc(target)}">{esc(project["title"])}</a></h3><p>{esc(project_text)}</p></article>')'''
    new_print = '''        if is_compiler_print and summary:
            project_body = f'<p>{esc(summary.get("solution", ""))}</p><p class="pcv-project-result">{esc(summary.get("result", ""))}</p>'
        else:
            project_body = f'<p>{esc(project[f"result_{lang}"])}</p>'
        projects.append(f'<article class="pcv-project"><h3><a href="{esc(target)}">{esc(project["title"])}</a></h3>{project_body}</article>')'''
    if source.count(old_print) != 1:
        raise RuntimeError(f"compiler print project anchor count={source.count(old_print)}")
    source = source.replace(old_print, new_print, 1)
    path.write_text(source, encoding="utf-8")


def patch_css() -> None:
    path = ROOT / "style.css"
    css = path.read_text(encoding="utf-8")
    marker = "/* compiler print completion v54 */"
    if marker in css:
        raise RuntimeError("v54 print marker already exists")
    css += r'''

/* compiler print completion v54 */
@media print {
  .profile-compiler .pcv-project p {
    margin-top: .8mm;
    font-size: 8pt;
    line-height: 1.25;
  }
  .profile-compiler .pcv-project .pcv-project-result {
    margin-top: .55mm;
    color: #211a1c;
  }
  .profile-compiler .pcv-project {
    margin-bottom: 2.7mm;
  }
  .profile-compiler .pcv-entry li {
    font-size: 8pt;
    line-height: 1.27;
  }
  .profile-compiler .pcv-skill span,
  .profile-compiler .pcv-compact p {
    font-size: 7.8pt;
    line-height: 1.25;
  }
  .profile-compiler .pcv-recognition span {
    font-size: 7.55pt;
    line-height: 1.22;
  }
}
'''
    path.write_text(css.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    patch_data()
    patch_generator()
    patch_css()
    print("Applied final compiler CV copy and print polish")


if __name__ == "__main__":
    main()
