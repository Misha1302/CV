from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "site.json"
BUILD_SITE = ROOT / "tools" / "build_site.py"


def refine_data() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))

    for lang in ("ru", "en"):
        general = data["profiles"]["general"][lang]
        general["role"] = "Compiler & Program Analysis Engineer"
        general["footer"] = "Compiler & Program Analysis Engineer · LLVM · Language Infrastructure"

    # Keep the application CV ordered by the fastest role-specific proof.
    data["profiles"]["compiler"]["ru"]["project_ids"] = ["globaliv", "deref", "codegen", "wist"]
    data["profiles"]["compiler"]["en"]["project_ids"] = ["globaliv", "deref", "codegen", "wist"]
    data["profiles"]["research"]["ru"]["project_ids"] = ["wist", "globaliv", "codegen", "deref"]
    data["profiles"]["research"]["en"]["project_ids"] = ["wist", "globaliv", "codegen", "deref"]

    # Shorten the research project copy enough for a one-page application PDF while
    # preserving research-process evidence and explicit claim boundaries.
    data["profiles"]["research"]["ru"]["project_summaries"]["wist"] = {
        "type": ".NET · extensible compiler/language systems · research engineering",
        "solution": (
            "Contract-guided reverification для расширяемых compiler pipelines: typed facts/effects/invalidations "
            "и verifier routes управляют fail-closed selective verification поверх детерминированного LanguagePlan."
        ),
        "result": (
            "Evidence-backed anonymous CGO’27 draft, не submission: 4 policies, frozen corpus, valid controls, "
            "fault injection и ablations; performance/external-corpus claims явно оставлены blocked."
        ),
    }
    data["profiles"]["research"]["en"]["project_summaries"]["wist"] = {
        "type": ".NET · extensible compiler/language systems · research engineering",
        "solution": (
            "Contract-guided reverification for extensible compiler pipelines: typed facts/effects/invalidations "
            "and verifier routes drive fail-closed selective verification over a deterministic LanguagePlan."
        ),
        "result": (
            "Evidence-backed anonymous CGO’27 draft, not a submission: four policies, a frozen corpus, valid controls, "
            "fault injection, and ablations; performance/external-corpus claims remain explicitly blocked."
        ),
    }

    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_build_site() -> None:
    raw = BUILD_SITE.read_text(encoding="utf-8")

    # The application layout should use role-specific project copy whenever present,
    # not only for the historical compiler profile.
    raw = raw.replace(
        'summary = project_summaries.get(project_id, {}) if is_compiler_print else {}\n'
        '        if is_compiler_print and summary:',
        'summary = project_summaries.get(project_id, {})\n'
        '        if summary:',
    )

    # Give the research page its own information hierarchy while reusing the existing
    # project-summary renderer and avoiding a new template/export mechanism.
    old = '''    if profile_key == "compiler":\n        main_content = f"{compiler_hero(data, lang, profile)}{experience_section(lang, profile, compact=True)}{compiler_projects_section(data, lang, profile)}{skills_section(lang, profile, compact=True)}{recognition_section(data, lang, profile, compact=True)}{education_section(data, lang)}{contact_section(data, lang, profile)}"\n    else:\n        main_content = f"{hero(data, lang, profile)}{proof_strip(profile)}{experience_section(lang, profile)}{projects_section(data, lang, profile)}{skills_section(lang, profile)}{recognition_section(data, lang, profile)}{education_section(data, lang)}{contact_section(data, lang, profile)}"'''
    new = '''    if profile_key == "compiler":\n        main_content = f"{compiler_hero(data, lang, profile)}{experience_section(lang, profile, compact=True)}{compiler_projects_section(data, lang, profile)}{skills_section(lang, profile, compact=True)}{recognition_section(data, lang, profile, compact=True)}{education_section(data, lang)}{contact_section(data, lang, profile)}"\n    elif profile_key == "research":\n        main_content = f"{hero(data, lang, profile)}{proof_strip(profile)}{experience_section(lang, profile, compact=True)}{compiler_projects_section(data, lang, profile)}{skills_section(lang, profile, compact=True)}{recognition_section(data, lang, profile, compact=True)}{education_section(data, lang)}{contact_section(data, lang, profile)}"\n    else:\n        main_content = f"{hero(data, lang, profile)}{proof_strip(profile)}{experience_section(lang, profile)}{projects_section(data, lang, profile)}{skills_section(lang, profile)}{recognition_section(data, lang, profile)}{education_section(data, lang)}{contact_section(data, lang, profile)}"'''
    if old not in raw:
        raise RuntimeError("profile_page dispatch shape changed; refusing blind patch")
    raw = raw.replace(old, new)

    # Make the landing page agree with the selected default identity.
    raw = raw.replace('title = "Михаил Разаков — Compiler / Static Analysis Engineer"',
                      'title = "Михаил Разаков — Compiler & Program Analysis Engineer"')
    raw = raw.replace('<span>Compiler / Static Analysis Engineer</span>',
                      '<span>Compiler & Program Analysis Engineer</span>')
    raw = raw.replace('<h1>Compiler / Static Analysis Engineer</h1>',
                      '<h1>Compiler & Program Analysis Engineer</h1>')
    raw = raw.replace('Основной профиль — Compiler / Static Analysis Engineer.',
                      'Основной профиль — Compiler & Program Analysis Engineer.')

    BUILD_SITE.write_text(raw, encoding="utf-8")


def main() -> None:
    refine_data()
    patch_build_site()


if __name__ == "__main__":
    main()
