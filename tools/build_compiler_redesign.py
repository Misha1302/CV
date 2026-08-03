from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SITE = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))

TEXT: dict[str, dict[str, Any]] = {
    "ru": {
        "file": "ru-compiler.html", "other": "en-compiler.html", "lang_name": "EN",
        "title": "Михаил Разаков — Compiler Engineer",
        "description": "Compiler Engineer: UniversalToolchain/Wist2, IR, SSA, runtime, LLVM и проверка компиляторов.",
        "role": "Compiler Engineer · языковые платформы и runtime",
        "eyebrow": "IR · SSA · runtime · LLVM · program analysis",
        "summary": "Строю компиляторы и языковые платформы для .NET — от IR, SSA и оптимизаций до runtime, SDK и инструментов проверки. Автор UniversalToolchain/Wist2; прохожу стажировку по разработке компиляторов в МЦСТ.",
        "education": "Поступление на программу «Программная инженерия» НИУ ВШЭ — 2026",
        "availability": "Ищу compiler / C++ / systems-позицию с сентября–октября 2026 года. Москва или удалённо; возможна частичная занятость.",
        "nav": [("Опыт", "experience"), ("Проекты", "work"), ("Подход", "process"), ("Компетенции", "skills"), ("Достижения", "recognition")],
        "cta": "Связаться", "github": "GitHub", "sections": ["Опыт", "Проекты", "Как я работаю", "Компетенции", "Достижения", "Образование"],
        "proofs": [("1 465 / 1 465", "тестов Wist2, 0 падений"), ("9 пакетов", "проверены clean-consumer проекты"), ("1-е из 49", "PS-form analyzer, 104/104 тестов")],
        "experience": [
            ("2024 — сейчас", "UniversalToolchain / Wist2 — автор и основной разработчик", ".NET · language SDK · runtime", ["Спроектировал модульную композицию языка: типизированные артефакты, возможности, конфликты и детерминированный порядок проходов.", "Реализовал связывание конфигурации с манифестом, lifecycle runtime-сессий, AIR/SSA pipeline и parity интерпретатора с CIL backend.", "Проверка: 1 465/1 465 тестов, 9 пакетов и отдельные clean-consumer проекты."]),
            ("1 июля — 31 августа 2026", "МЦСТ — стажёр по разработке компиляторов", "LLVM · C++23 · удалённо", ["Изучаю инфраструктуру LLVM и разрабатываю оптимизационный проход; реализовал и протестировал графовые алгоритмы на C++23."])
        ],
        "projects": [
            ("UniversalToolchain / Wist2", "Активный preview", "SDK для сборки языков и сред исполнения из независимых модулей.", "Архитектура платформы, IR/SSA, runtime, система пакетов и стратегия проверки.", "Сохранить детерминизм и совместимость при разных наборах пакетов, backend-ов и проходов.", "1 465/1 465 тестов; 9 пакетов; interpreter/CIL parity.", ["C#", ".NET", "AIR", "SSA", "CIL"], "https://github.com/Misha1302/Wist2", "https://misha1302.github.io/Wist2/"),
            ("PlanFuzz", "Эксперимент", "Конфигурационно-зависимое тестирование языковой платформы.", "Модель исходов, oracle core, replay, fingerprints и reducers.", "Отделять ошибки продукта от нестабильных и инфраструктурных результатов.", "Воспроизводимые артефакты и типизированная классификация исходов.", ["fuzzing", "oracles", "replay", "reducers"], "https://github.com/Misha1302/Wist2/blob/main/internal-docs/proposals/planfuzz/README.md", ""),
            ("PS-form Memory Dependence Analyzer", "Завершён", "Консервативный анализ пересечения параметрических обращений к памяти.", "Алгоритм, точный oracle, stress infrastructure и разбор контрпримеров.", "Избежать перебора больших диапазонов, не потеряв корректность.", "1-е место среди 49 решений; 104/104 тестов.", ["C17", "program analysis", "stress testing"], "https://github.com/Misha1302/ps_form_analizer", "")
        ],
        "process": [("01", "Фиксирую семантику", "Определяю наблюдаемое поведение, инварианты и ошибочные состояния."), ("02", "Проектирую границы", "Разделяю IR, runtime, пакеты и backend-ы явными контрактами."), ("03", "Делаю сквозной путь", "Провожу возможность через весь pipeline вместо изолированного прототипа."), ("04", "Доказываю результат", "Использую exact oracle, differential tests, replay, sanitizers и clean consumers.")],
        "skills": [("Архитектура языковых платформ", "Модульная композиция, контракты компонентов, capabilities/conflicts, manifests и lifecycle."), ("IR и оптимизации", "CFG, dominance, SSA, constant folding, SCCP-lite, unreachable elimination и DCE."), ("Runtime и code generation", "Интерпретатор, CIL backend, typed delegates и проверка эквивалентности backend-ов."), ("Проверка компиляторов", "Exact oracles, differential/metamorphic testing, replay, reducers, ASan/UBSan.")],
        "recognition": [("2026", "Высшая проба", "Призёр по промышленному и олимпиадному программированию."), ("2025–2026", "Юниор НИЯУ МИФИ", "Двукратный абсолютный победитель."), ("2026", "Балтийский конкурс", "Абсолютный победитель инженерно-научного конкурса."), ("2021 — сейчас", "Техническая коммуникация", "Около 50 учеников, курс NASM IA-32, документация и code review.")]
    },
    "en": {
        "file": "en-compiler.html", "other": "ru-compiler.html", "lang_name": "RU",
        "title": "Mikhail Razakov — Compiler Engineer",
        "description": "Compiler Engineer: UniversalToolchain/Wist2, IR, SSA, runtime, LLVM, and compiler verification.",
        "role": "Compiler Engineer · language platforms and runtimes",
        "eyebrow": "IR · SSA · runtime · LLVM · program analysis",
        "summary": "I build compilers and .NET language platforms, from IR, SSA, and optimizations to runtimes, SDKs, and verification tooling. I created UniversalToolchain/Wist2 and am completing a compiler-engineering internship at MCST.",
        "education": "Incoming HSE University Software Engineering student — 2026",
        "availability": "Seeking a compiler, C++, or systems role starting September–October 2026. Moscow or remote; part-time is possible.",
        "nav": [("Experience", "experience"), ("Projects", "work"), ("Process", "process"), ("Skills", "skills"), ("Recognition", "recognition")],
        "cta": "Contact", "github": "GitHub", "sections": ["Experience", "Projects", "How I work", "Skills", "Recognition", "Education"],
        "proofs": [("1,465 / 1,465", "Wist2 tests, zero failures"), ("9 packages", "verified with clean consumers"), ("1st of 49", "PS-form analyzer, 104/104 tests")],
        "experience": [
            ("2024 — present", "UniversalToolchain / Wist2 — creator and primary developer", ".NET · language SDK · runtime", ["Designed modular language composition with typed artifacts, capabilities, conflicts, and deterministic pass ordering.", "Implemented manifest-bound configuration, runtime-session lifecycle, the AIR/SSA pipeline, and interpreter/CIL parity.", "Verification: 1,465/1,465 tests, nine packages, and separate clean-consumer projects."]),
            ("July 1 — August 31, 2026", "MCST — compiler engineering intern", "LLVM · C++23 · remote", ["Studying LLVM infrastructure and developing an optimization pass; implemented and tested graph algorithms in C++23."])
        ],
        "projects": [
            ("UniversalToolchain / Wist2", "Active preview", "An SDK for composing languages and runtimes from independent modules.", "Platform architecture, IR/SSA, runtime, package system, and verification strategy.", "Preserve determinism and compatibility across package, backend, and pass configurations.", "1,465/1,465 tests; nine packages; interpreter/CIL parity.", ["C#", ".NET", "AIR", "SSA", "CIL"], "https://github.com/Misha1302/Wist2", "https://misha1302.github.io/Wist2/"),
            ("PlanFuzz", "Experimental", "Configuration-aware testing for language platforms.", "Outcome model, oracle core, replay, fingerprints, and reducers.", "Separate product defects from unstable and infrastructure outcomes.", "Reproducible artifacts with typed outcome classification.", ["fuzzing", "oracles", "replay", "reducers"], "https://github.com/Misha1302/Wist2/blob/main/internal-docs/proposals/planfuzz/README.md", ""),
            ("PS-form Memory Dependence Analyzer", "Completed", "Conservative overlap analysis for parametric memory accesses.", "Algorithm, exact oracle, stress infrastructure, and counterexample analysis.", "Avoid enumerating large domains without sacrificing correctness.", "Ranked 1st of 49 with 104/104 tests.", ["C17", "program analysis", "stress testing"], "https://github.com/Misha1302/ps_form_analizer", "")
        ],
        "process": [("01", "Lock the semantics", "Define observable behavior, invariants, and invalid states."), ("02", "Design boundaries", "Separate IR, runtimes, packages, and backends with explicit contracts."), ("03", "Build an end-to-end path", "Carry one capability through the full pipeline instead of an isolated prototype."), ("04", "Prove the result", "Use exact oracles, differential tests, replay, sanitizers, and clean consumers.")],
        "skills": [("Language-platform architecture", "Modular composition, component contracts, capabilities/conflicts, manifests, and lifecycle."), ("IR and optimizations", "CFG, dominance, SSA, constant folding, SCCP-lite, unreachable elimination, and DCE."), ("Runtime and code generation", "Interpreter, CIL backend, typed delegates, and backend-equivalence checks."), ("Compiler verification", "Exact oracles, differential/metamorphic testing, replay, reducers, ASan/UBSan.")],
        "recognition": [("2026", "HSE Vysshaya Proba", "Prize-winner in industrial and competitive programming."), ("2025–2026", "MEPhI Junior", "Two-time absolute winner."), ("2026", "Baltic competition", "Absolute winner of the engineering and science competition."), ("2021 — present", "Technical communication", "About 50 students, a NASM IA-32 course, documentation, and code review.")]
    }
}


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def page(lang: str) -> str:
    t = TEXT[lang]
    p = SITE["person"]
    name = p[f"name_{lang}"]
    links = "".join(f'<a href="#{anchor}">{e(label)}</a>' for label, anchor in t["nav"])
    proofs = "".join(f'<article><strong>{e(a)}</strong><span>{e(b)}</span></article>' for a, b in t["proofs"])
    exp = []
    for date, title, org, bullets in t["experience"]:
        exp.append(f'<article class="cr-timeline"><time>{e(date)}</time><div><h3>{e(title)}</h3><p>{e(org)}</p></div><ul>{"".join(f"<li>{e(x)}</li>" for x in bullets)}</ul></article>')
    cards = []
    for i, (title, status, purpose, role, challenge, result, tech, repo, docs) in enumerate(t["projects"]):
        facts = [("Назначение" if lang == "ru" else "Purpose", purpose), ("Мой вклад" if lang == "ru" else "Ownership", role), ("Сложность" if lang == "ru" else "Challenge", challenge), ("Результат" if lang == "ru" else "Outcome", result)]
        actions = f'<a href="{e(repo)}" target="_blank" rel="noopener noreferrer">GitHub ↗</a>' + (f'<a href="{e(docs)}" target="_blank" rel="noopener noreferrer">{"Документация" if lang == "ru" else "Documentation"} ↗</a>' if docs else "")
        cards.append(f'<article class="cr-project {"featured" if i == 0 else ""}"><header><span>{e(status)}</span><h3>{e(title)}</h3></header><div class="cr-facts">{"".join(f"<p><strong>{e(k)}</strong>{e(v)}</p>" for k,v in facts)}</div><div class="cr-tags">{"".join(f"<span>{e(x)}</span>" for x in tech)}</div><div class="cr-project-links">{actions}</div></article>')
    process = "".join(f'<article><span>{e(n)}</span><h3>{e(h)}</h3><p>{e(b)}</p></article>' for n,h,b in t["process"])
    skills = "".join(f'<article><h3>{e(h)}</h3><p>{e(b)}</p></article>' for h,b in t["skills"])
    recog = "".join(f'<article><time>{e(y)}</time><div><h3>{e(h)}</h3><p>{e(b)}</p></div></article>' for y,h,b in t["recognition"])
    schema = json.dumps({"@context":"https://schema.org","@type":"Person","name":name,"jobTitle":t["role"],"email":f"mailto:{p['email']}","url":SITE["site_url"]+t["file"],"sameAs":[p["github"],p["telegram"],p["linkedin"]]}, ensure_ascii=False, separators=(",",":"))
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(t['title'])}</title><meta name="description" content="{e(t['description'])}"><link rel="canonical" href="{e(SITE['site_url']+t['file'])}"><link rel="alternate" hreflang="{lang}" href="{e(SITE['site_url']+t['file'])}"><link rel="alternate" hreflang="{'en' if lang=='ru' else 'ru'}" href="{e(SITE['site_url']+t['other'])}"><link rel="stylesheet" href="style.css?v={e(SITE['version'])}"><link rel="stylesheet" href="compiler-redesign.css?v=1"><script type="application/ld+json">{schema}</script></head><body class="compiler-redesign"><a class="skip-link" href="#main">{'К содержанию' if lang=='ru' else 'Skip to content'}</a><header class="site-header"><div class="shell header-inner"><a class="brand" href="index.html"><span class="brand-mark">MR</span><span class="brand-copy"><strong>{e(name)}</strong><span>compiler · runtime · verification</span></span></a><nav class="primary-nav">{links}</nav><div class="header-actions"><a href="{e(t['other'])}">{e(t['lang_name'])}</a><a class="button compact" href="#contact">{e(t['cta'])}</a><details class="mobile-menu"><summary>Menu</summary><div class="mobile-panel"><nav>{links}</nav></div></details></div></div></header><main id="main"><section class="shell cr-hero"><div><p class="eyebrow">{e(t['eyebrow'])}</p><h1>{e(name)}</h1><p class="cr-role">{e(t['role'])}</p><p class="cr-summary">{e(t['summary'])}</p><div class="hero-actions"><a class="button primary" href="mailto:{e(p['email'])}">{e(t['cta'])}</a><a class="button" href="{e(p['github'])}" target="_blank" rel="noopener noreferrer">GitHub</a><a class="button" href="{e(t['other'])}">{e(t['lang_name'])}</a></div><p class="cr-availability">{e(t['availability'])}</p></div><aside class="cr-pipeline"><strong>Wist2 pipeline</strong><div><span>Source</span><b>→</b><span>Lexer</span><b>→</b><span>Parser</span><b>→</b><span>AST</span><b>→</b><span>Bytecode</span><b>→</b><span>AIR</span><b>→</b><span>SSA</span><b>→</b><span>Optimizations</span><b>→</b><span>Interpreter / CIL</span><b>→</b><span>Verification / PlanFuzz</span></div></aside></section><section class="shell cr-proofs">{proofs}</section><section class="shell section" id="experience"><div class="section-heading"><p class="section-label">01 · {e(t['sections'][0])}</p><div><h2>{e(t['sections'][0])}</h2><p class="section-intro">{'Личная ответственность и проверяемый результат.' if lang=='ru' else 'Personal ownership and verifiable outcomes.'}</p></div></div><div>{''.join(exp)}</div></section><section class="shell section" id="work"><div class="section-heading"><p class="section-label">02 · {e(t['sections'][1])}</p><div><h2>{'Три проекта вместо каталога технологий.' if lang=='ru' else 'Three projects instead of a technology catalogue.'}</h2></div></div><div class="cr-projects">{''.join(cards)}</div></section><section class="shell section" id="process"><div class="section-heading"><p class="section-label">03 · {e(t['sections'][2])}</p><div><h2>{e(t['sections'][2])}</h2></div></div><div class="cr-process">{process}</div></section><section class="shell section" id="skills"><div class="section-heading"><p class="section-label">04 · {e(t['sections'][3])}</p><div><h2>{'Задачи, которые умею решать.' if lang=='ru' else 'Problems I can solve.'}</h2></div></div><div class="cr-skills">{skills}</div></section><section class="shell section" id="recognition"><div class="section-heading"><p class="section-label">05 · {e(t['sections'][4])}</p><div><h2>{e(t['sections'][4])}</h2></div></div><div class="cr-recognition">{recog}</div></section><section class="shell section cr-education" id="education"><div class="section-heading"><p class="section-label">06 · {e(t['sections'][5])}</p><div><h2>{e(t['education'])}</h2><p class="section-intro">{e(p[f'location_{lang}'])}</p></div></div></section><section class="shell contact-section" id="contact"><div class="contact-panel"><div><h2>{e(t['availability'])}</h2><p><a href="mailto:{e(p['email'])}">{e(p['email'])}</a> · <a href="{e(p['telegram'])}" target="_blank" rel="noopener noreferrer">Telegram</a> · <a href="{e(p['linkedin'])}" target="_blank" rel="noopener noreferrer">LinkedIn</a></p></div><div class="contact-links"><a class="button primary" href="mailto:{e(p['email'])}">{e(t['cta'])}</a><a class="button" href="{e(p['github'])}" target="_blank" rel="noopener noreferrer">GitHub</a></div></div></section></main><footer class="shell site-footer"><span>{e(name)} · Compiler Engineer</span><span>2026-08-03</span></footer><script src="script.js?v={e(SITE['version'])}" defer></script></body></html>'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale: list[str] = []
    for lang in ("ru", "en"):
        target = ROOT / TEXT[lang]["file"]
        content = page(lang).rstrip() + "\n"
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != content:
                stale.append(target.name)
        else:
            target.write_text(content, encoding="utf-8")
    if stale:
        raise SystemExit("Generated files are stale: " + ", ".join(stale))


if __name__ == "__main__":
    main()
