from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
KB_PATH = ROOT / "knowledge" / "resume-evidence.json"
ID_RE = re.compile(r"^[a-z0-9_]+$")
EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@(gmail\.com|outlook\.com|yandex\.[a-z]+|mail\.ru|ispras\.ru)\b")
FORBIDDEN_KEY_PARTS = {
    "password",
    "passwd",
    "passport",
    "secret",
    "api_key",
    "access_token",
    "refresh_token",
    "attachment_id",
    "gmail_id",
    "message_id",
}


class KnowledgeValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise KnowledgeValidationError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def as_nonempty_string(value: object, label: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), f"{label}: expected non-empty string")
    return value.strip()


def as_string_list(value: object, label: str, *, allow_empty: bool = True) -> list[str]:
    require(isinstance(value, list), f"{label}: expected list")
    if not allow_empty:
        require(bool(value), f"{label}: must not be empty")
    result: list[str] = []
    for index, item in enumerate(value):
        result.append(as_nonempty_string(item, f"{label}[{index}]"))
    require(len(result) == len(set(result)), f"{label}: duplicate values")
    return result


def walk(value: object, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield f"{path}.{key}", key, child
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def validate_no_sensitive_material(data: dict) -> None:
    for path, key, value in walk(data):
        lowered = key.casefold()
        for part in FORBIDDEN_KEY_PARTS:
            if part in lowered:
                fail(f"{path}: sensitive-looking key is forbidden in the public knowledge base")
        if isinstance(value, str) and EMAIL_RE.search(value):
            fail(f"{path}: private email address is forbidden in the public knowledge base")


def validate_public_sources(asset: dict, asset_id: str) -> None:
    sources = as_string_list(asset.get("public_sources", []), f"asset {asset_id}.public_sources")
    for source in sources:
        parsed = urlparse(source)
        require(
            parsed.scheme == "https" and bool(parsed.netloc),
            f"asset {asset_id}: public source must be an absolute https URL: {source}",
        )


def validate_asset(asset: object, index: int, levels: set[str]) -> str:
    require(isinstance(asset, dict), f"assets[{index}]: expected object")
    asset_id = as_nonempty_string(asset.get("id"), f"assets[{index}].id")
    require(bool(ID_RE.fullmatch(asset_id)), f"asset id has invalid format: {asset_id}")

    for field in ("category", "name", "time", "resume_priority"):
        as_nonempty_string(asset.get(field), f"asset {asset_id}.{field}")

    evidence = as_string_list(asset.get("evidence_level"), f"asset {asset_id}.evidence_level", allow_empty=False)
    unknown = sorted(set(evidence) - levels)
    require(not unknown, f"asset {asset_id}: unknown evidence levels: {unknown}")

    validate_public_sources(asset, asset_id)
    as_string_list(asset.get("recruiter_signals", []), f"asset {asset_id}.recruiter_signals")
    as_string_list(asset.get("role_fit", []), f"asset {asset_id}.role_fit")
    return asset_id


def validate_role_playbooks(data: dict, asset_ids: set[str]) -> None:
    playbooks = data.get("role_playbooks")
    require(isinstance(playbooks, dict) and bool(playbooks), "role_playbooks: expected non-empty object")
    for role, playbook in playbooks.items():
        require(isinstance(playbook, dict), f"role_playbooks.{role}: expected object")
        as_nonempty_string(playbook.get("title"), f"role_playbooks.{role}.title")
        as_nonempty_string(playbook.get("thesis"), f"role_playbooks.{role}.thesis")
        for field in ("top_assets", "recognition", "project_slots"):
            refs = as_string_list(playbook.get(field, []), f"role_playbooks.{role}.{field}")
            missing = [ref for ref in refs if ref not in asset_ids]
            require(not missing, f"role_playbooks.{role}.{field}: unknown asset ids: {missing}")


def validate_semantic_boundaries(by_id: dict[str, dict]) -> None:
    isp = by_id.get("experience_isp_ras_2026")
    require(isp is not None, "missing ISP RAS boundary asset")
    require(isp.get("category") == "opportunity", "ISP RAS must not be modeled as confirmed employment")
    require(
        "NOT_STARTED" in str(isp.get("status", "")),
        "ISP RAS asset must explicitly preserve the not-started boundary",
    )
    require(isp.get("resume_priority") == "CONDITIONAL", "ISP RAS resume use must remain conditional")

    baltic = by_id.get("achievement_baltic_2026")
    require(baltic is not None, "missing Baltic achievement asset")
    conflict = baltic.get("source_conflict")
    require(
        isinstance(conflict, dict) and "CONFLICT" in str(conflict.get("status", "")),
        "Baltic primary-source conflict must remain explicit until resolved",
    )
    baltic_claims = baltic.get("claims", {})
    safe_baltic = " ".join(str(baltic_claims.get(k, "")) for k in ("safe_ru", "safe_en"))
    forbidden_baltic = ("Главная премия", "Секционная премия", "Main Prize", "Section Prize")
    require(
        not any(token in safe_baltic for token in forbidden_baltic),
        "Baltic safe claim must use wording invariant across the conflicting primary sources",
    )

    junior = by_id.get("achievement_mephi_junior_2025_2026")
    require(junior is not None, "missing Junior achievement asset")
    junior_claims = junior.get("claims", {})
    safe_junior = " ".join(str(junior_claims.get(k, "")) for k in ("safe_ru", "safe_en")).casefold()
    require("абсолют" not in safe_junior and "overall winner" not in safe_junior, "Junior safe claim overstates public evidence")

    langdev = by_id.get("achievement_langdev_2026")
    require(langdev is not None, "missing LangDev achievement asset")
    require(
        str(langdev.get("status", "")).startswith("DELIVERED__"),
        "LangDev must reflect the user-confirmed delivered talk after 2026-10-09",
    )

    hse = by_id.get("achievement_hse_open_source_2026")
    require(hse is not None, "missing HSE open-source achievement asset")
    hse_claims = hse.get("claims", {})
    safe_hse = " ".join(str(hse_claims.get(k, "")) for k in ("safe_ru", "safe_en")).casefold()
    require(
        ("один из победителей" in safe_hse or "one of the winners" in safe_hse)
        and "first place" not in safe_hse
        and "1st place" not in safe_hse,
        "HSE open-source safe claim must stay at 'one of the winners'",
    )


def validate_global_boundaries(data: dict) -> None:
    boundaries = data.get("global_claim_boundaries")
    require(isinstance(boundaries, dict), "global_claim_boundaries: expected object")
    for field in ("can_say", "can_say_with_qualifier", "do_not_say"):
        as_string_list(boundaries.get(field), f"global_claim_boundaries.{field}", allow_empty=False)


def main() -> None:
    require(KB_PATH.exists(), f"knowledge base missing: {KB_PATH.relative_to(ROOT)}")
    data = json.loads(KB_PATH.read_text(encoding="utf-8"))

    require(isinstance(data, dict), "knowledge root must be an object")
    require(isinstance(data.get("schema_version"), int) and data["schema_version"] >= 1, "invalid schema_version")
    as_nonempty_string(data.get("generated_at"), "generated_at")
    as_nonempty_string(data.get("purpose"), "purpose")

    evidence_levels = data.get("evidence_levels")
    require(isinstance(evidence_levels, dict) and bool(evidence_levels), "evidence_levels: expected non-empty object")
    levels = set(evidence_levels)
    for level, description in evidence_levels.items():
        as_nonempty_string(level, "evidence level id")
        as_nonempty_string(description, f"evidence_levels.{level}")

    assets = data.get("assets")
    require(isinstance(assets, list) and bool(assets), "assets: expected non-empty list")
    ids = [validate_asset(asset, index, levels) for index, asset in enumerate(assets)]
    require(len(ids) == len(set(ids)), "assets: duplicate ids")
    by_id = {asset["id"]: asset for asset in assets}

    skills = data.get("skills")
    require(isinstance(skills, list) and bool(skills), "skills: expected non-empty list")
    for index, skill in enumerate(skills):
        require(isinstance(skill, dict), f"skills[{index}]: expected object")
        as_nonempty_string(skill.get("skill"), f"skills[{index}].skill")
        as_string_list(skill.get("strongest_evidence", []), f"skills[{index}].strongest_evidence", allow_empty=False)
        as_nonempty_string(skill.get("level_for_resume"), f"skills[{index}].level_for_resume")

    as_string_list(data.get("research_gaps"), "research_gaps", allow_empty=False)
    validate_role_playbooks(data, set(ids))
    validate_global_boundaries(data)
    validate_semantic_boundaries(by_id)
    validate_no_sensitive_material(data)

    triage = data.get("repository_triage", {})
    require(isinstance(triage, dict), "repository_triage: expected object")
    snapshot = triage.get("inventory_snapshot", {})
    require(
        isinstance(snapshot, dict)
        and isinstance(snapshot.get("public_repositories_observed"), int)
        and snapshot["public_repositories_observed"] > 0,
        "repository_triage.inventory_snapshot.public_repositories_observed must be positive integer",
    )

    print(
        json.dumps(
            {
                "status": "ok",
                "assets": len(assets),
                "skills": len(skills),
                "role_playbooks": len(data["role_playbooks"]),
                "evidence_levels": len(levels),
                "research_gaps": len(data["research_gaps"]),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"KNOWLEDGE_VALIDATION_ERROR: {exc}", file=sys.stderr)
        raise
