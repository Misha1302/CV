from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "data" / "site.json"


def clean_text(text: str) -> str:
    # Remove LangDev acceptance sentences from legacy secondary profiles.
    text = re.sub(r"\s*Доклад о проекте принят на LangDev 2026\.?", "", text)
    text = re.sub(r"\s*A talk about the project was accepted for LangDev 2026\.?", "", text)
    text = re.sub(r"\s*Доклад по UniversalToolchain/Wist2 принят к выступлению\.?", "", text)
    text = re.sub(r"\s*UniversalToolchain/Wist2 talk accepted\.?", "", text)
    return text.strip()


def clean_profile(profile: dict[str, Any], lang: str) -> None:
    # Remove proof/recognition cards whose only value is an unsupported external claim.
    for key in ("proofs", "recognition"):
        if key in profile:
            profile[key] = [
                item for item in profile[key]
                if not any("LangDev" in str(part) for part in item)
            ]

    # Normalize legacy PS-form ranking/test-count claims in secondary profiles.
    if lang == "ru":
        replacements = {
            "1-е из 49 · 104/104": "Conservative analysis",
            "1-е место из 49": "PS-form analysis",
            "PS-form Memory Dependence Analyzer — 1-е место из 49": "PS-form Memory Dependence Analyzer",
            "Реализовал анализ пересечения параметрических обращений к памяти на C17; 104/104 официальных тестов и 1-е место из 49.": "Реализовал консервативный анализ пересечения параметрических обращений к памяти на C17; корректность проверял exact oracle на малых областях и randomized/metamorphic cases.",
            "Реализовал консервативный анализ параметрических обращений к памяти; занял 1-е место среди 49 решений, 104/104 тестов.": "Реализовал консервативный анализ параметрических обращений к памяти; недоказанные случаи не превращаются в ложный yes/no, а проверка опирается на независимый exact oracle.",
            "104/104 официальных тестов и 1-е место среди 49 решений.": "Консервативный анализ с независимым exact oracle на малых областях и randomized/metamorphic проверками.",
        }
    else:
        replacements = {
            "#1 of 49 · 104/104": "Conservative analysis",
            "#1 of 49": "PS-form analysis",
            "PS-form Memory Dependence Analyzer — #1 of 49": "PS-form Memory Dependence Analyzer",
            "Implemented analysis of whether parametric memory accesses can overlap; passed 104/104 official tests and ranked #1 of 49.": "Implemented conservative analysis of whether parametric memory accesses can overlap, checked against an exact oracle on small domains plus randomized/metamorphic cases.",
            "Implemented conservative analysis of parametric memory accesses; ranked #1 of 49 with 104/104 tests.": "Implemented conservative analysis of parametric memory accesses; unresolved cases do not become false yes/no answers, and correctness is checked against an independent exact oracle.",
            "Passed 104/104 official tests and ranked #1 of 49 submissions.": "Conservative analysis checked by an independent exact oracle on small domains plus randomized/metamorphic tests.",
        }

    def walk(value: Any) -> Any:
        if isinstance(value, str):
            value = clean_text(value)
            for old, new in replacements.items():
                value = value.replace(old, new)
            return value
        if isinstance(value, list):
            return [walk(item) for item in value]
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

    # Shared project data is used by the one-page PDF generator, so keep it evidence-safe.
    psform = data["projects"]["psform"]
    psform["result_ru"] = "Консервативный результат yes/no/maybe с независимым exact oracle на малых областях, randomized/metamorphic проверками и воспроизводимыми контрпримерами."
    psform["result_en"] = "Conservative yes/no/maybe results checked by an independent exact oracle on small domains, randomized/metamorphic tests, and reproducible counterexamples."

    for profile_key, variants in data["profiles"].items():
        clean_profile(variants["ru"], "ru")
        clean_profile(variants["en"], "en")

    SITE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    (ROOT / "CONTENT-REVIEW-v47.md").write_text(
        """# Content review — CV v47 final consistency pass\n\n## Decision\n\nPASS. The three primary CV narratives remain Architecture / Platforms, Compiler Infrastructure, and .NET Backend / Reliability.\n\n## Post-render finding repaired\n\nThe compiler PDF correctly used the new profile content but its project list still read shared `projects.psform.result_*`, which retained the old ranking/test-count wording. v47 moves the shared project result to evidence-safe analysis/verification language so the claim cannot reappear through another renderer.\n\n## Repository-wide consistency\n\nLegacy LangDev acceptance cards/sentences and PS-form ranking/test-count wording are removed from public profile data. This is a credibility cleanup, not a claim that the underlying historical result was false; the issue is that the stronger independent evidence currently available supports the technical design and verification more cleanly than the external ranking claim.\n\n## Final routing\n\n- Architecture / Platforms: broad hands-on architecture and platform engineering.\n- Compiler Infrastructure: LLVM, language platforms, IR/runtime, program analysis, compiler verification.\n- .NET Backend / Reliability: payment state, idempotency, recovery, provider verification, migrations, release safety.\n\n## Remaining boundaries\n\nNo Staff/Principal/Senior Architect, high-load, Kubernetes/cloud, formal verification, or multi-team architecture-governance claim is made.\n""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
