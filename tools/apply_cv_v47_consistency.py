from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "data" / "site.json"


def safe_recognition(lang: str) -> list[list[str]]:
    if lang == "ru":
        return [
            ["2026", "UniversalToolchain — Балтийский научно-инженерный конкурс", "Диплом I степени и Главная премия «Совершенство как надежда» за UniversalToolchain."],
            ["2026", "НИЯУ МИФИ «Юниор»", "Диплом I степени, 96/100 за проект UniversalToolchain."],
        ]
    return [
        ["2026", "UniversalToolchain — Baltic Science and Engineering Competition", "First-degree diploma and the Grand Prize “Perfection as Hope” for UniversalToolchain."],
        ["2026", "MEPhI Junior", "First-degree diploma, 96/100 for the UniversalToolchain project."],
    ]


def clean_text(text: str, lang: str) -> str:
    # Remove old LangDev acceptance wording from any legacy profile field.
    if "LangDev" in text:
        return ""

    if lang == "ru":
        exact = {
            "1-е из 49 · 104/104": "Conservative analysis",
            "1-е место среди 49 решений: единственная оценка 5,0/5,0 и 104/104 официальных тестов.": "Консервативный анализ проверен независимым exact oracle на малых областях, randomized/metamorphic cases и воспроизводимыми контрпримерами.",
            "Занял 1-е место среди 49 решений: единственная оценка 5,0/5,0 и 104/104 официальных тестов.": "Построил консервативный анализ и проверил его независимым exact oracle на малых областях, randomized/metamorphic cases и воспроизводимыми контрпримерами.",
            "1-е место среди 49 решений; единственная оценка 5,0/5,0; 104/104 официальных тестов.": "Консервативный PS-form анализ с независимым exact oracle, randomized/metamorphic проверками и воспроизводимыми контрпримерами.",
            "Реализовал анализ пересечения параметрических обращений к памяти на C17; 104/104 официальных тестов и 1-е место из 49.": "Реализовал консервативный анализ пересечения параметрических обращений к памяти на C17; корректность проверял независимым exact oracle на малых областях и randomized/metamorphic cases.",
            "Реализовал консервативный анализ параметрических обращений к памяти; занял 1-е место среди 49 решений, 104/104 тестов.": "Реализовал консервативный анализ параметрических обращений к памяти; недоказанные случаи не превращаются в ложный yes/no, а корректность проверяется независимым exact oracle.",
            "104/104 официальных тестов и 1-е место среди 49 решений.": "Консервативный анализ с независимым exact oracle на малых областях и randomized/metamorphic проверками.",
            "Контрольная проверка от 25.07.2026: 1 465/1 465 тестов без падений по девяти пакетам и clean-consumer проектам.": "Текущий exact manifest: 1 306/1 306 passed; отдельно проверяются interpreter/CIL parity и clean-consumer сценарии.",
        }
    else:
        exact = {
            "#1 of 49 · 104/104": "Conservative analysis",
            "1st of 49 · 104/104": "Conservative analysis",
            "Ranked 1st of 49: the only 5.0/5.0 result and 104/104 official tests.": "Built conservative analysis checked by an independent exact oracle on small domains, randomized/metamorphic cases, and reproducible counterexamples.",
            "Ranked 1st of 49; the only 5.0/5.0 result; 104/104 official tests.": "Conservative PS-form analysis with an independent exact oracle, randomized/metamorphic checks, and reproducible counterexamples.",
            "Implemented analysis of whether parametric memory accesses can overlap; passed 104/104 official tests and ranked #1 of 49.": "Implemented conservative analysis of whether parametric memory accesses can overlap, checked against an independent exact oracle on small domains plus randomized/metamorphic cases.",
            "Implemented conservative analysis of parametric memory accesses; ranked 1st of 49 with 104/104 tests.": "Implemented conservative analysis of parametric memory accesses; unresolved cases do not become false yes/no answers, and correctness is checked against an independent exact oracle.",
            "Passed 104/104 official tests and ranked #1 of 49 submissions.": "Conservative analysis checked by an independent exact oracle on small domains plus randomized/metamorphic tests.",
            "Verification as of July 25, 2026: 1,465/1,465 tests with zero failures across nine packages and clean-consumer projects.": "Current exact manifest: 1,306/1,306 passing, with interpreter/CIL parity and clean-consumer scenarios checked separately.",
        }

    for old, new in exact.items():
        text = text.replace(old, new)

    # Catch formatting variants without deleting surrounding useful technical content.
    if lang == "ru":
        text = re.sub(r"1-е место среди 49 решений[^.;]*[.;]?", "", text, flags=re.I)
        text = re.sub(r"104/104\s+(?:официальных\s+)?тест(?:ов|а)[^.;]*[.;]?", "", text, flags=re.I)
    else:
        text = re.sub(r"(?:ranked\s+)?1st of 49[^.;]*[.;]?", "", text, flags=re.I)
        text = re.sub(r"104/104\s+(?:official\s+)?tests?[^.;]*[.;]?", "", text, flags=re.I)
    return re.sub(r"\s{2,}", " ", text).strip(" ;,.-")


def clean_profile(profile: dict[str, Any], lang: str) -> None:
    def walk(value: Any) -> Any:
        if isinstance(value, str):
            return clean_text(value, lang)
        if isinstance(value, list):
            cleaned = [walk(item) for item in value]
            # Drop proof/recognition-style rows that became empty after cleanup.
            return [item for item in cleaned if not (isinstance(item, list) and any(str(part).strip() == "" for part in item))]
        if isinstance(value, dict):
            return {k: walk(v) for k, v in value.items()}
        return value

    cleaned = walk(profile)
    profile.clear()
    profile.update(cleaned)


def main() -> None:
    data = json.loads(SITE.read_text(encoding="utf-8"))
    if data.get("version") != 46:
        raise SystemExit(f"Expected CV source v46, got {data.get('version')!r}")
    data["version"] = 47
    data["updated_at"] = "2026-08-25"

    # Shared project data is consumed by every one-page PDF renderer.
    psform = data["projects"]["psform"]
    psform["result_ru"] = "Консервативный результат yes/no/maybe с независимым exact oracle на малых областях, randomized/metamorphic проверками и воспроизводимыми контрпримерами."
    psform["result_en"] = "Conservative yes/no/maybe results checked by an independent exact oracle on small domains, randomized/metamorphic tests, and reproducible counterexamples."

    for variants in data["profiles"].values():
        clean_profile(variants["ru"], "ru")
        clean_profile(variants["en"], "en")

    # Secondary profiles used inherited/legacy recognition; make those surfaces explicit and safe.
    for key in ("systems", "quant"):
        data["profiles"][key]["ru"]["recognition"] = safe_recognition("ru")
        data["profiles"][key]["en"]["recognition"] = safe_recognition("en")

    SITE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    (ROOT / "CONTENT-REVIEW-v47.md").write_text(
        """# Content review — CV v47 final consistency pass\n\n## Decision\n\nPASS. The three primary CV narratives remain Architecture / Platforms, Compiler Infrastructure, and .NET Backend / Reliability.\n\n## Post-render findings repaired\n\nThe compiler PDF used shared `projects.psform.result_*`, so v47 moves that shared result to evidence-safe analysis/verification language. A repository-wide pass also removed legacy LangDev acceptance wording, PS-form ranking/test-count wording, and the stale 1,465-test UniversalToolchain snapshot from secondary public profiles.\n\n## Final routing\n\n- Architecture / Platforms: broad hands-on architecture and platform engineering.\n- Compiler Infrastructure: LLVM, language platforms, IR/runtime, program analysis, compiler verification.\n- .NET Backend / Reliability: payment state, idempotency, recovery, provider verification, migrations, release safety.\n\n## Adversarial review\n\nThe targeted pages now differ by evidence ordering rather than by incompatible facts. Shared project data cannot silently reintroduce the removed claims into PDFs. Secondary C++/quant pages use the same evidence floor.\n\n## Remaining boundaries\n\nNo Staff/Principal/Senior Architect, high-load, Kubernetes/cloud, formal verification, or multi-team architecture-governance claim is made.\n""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
