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
    require(isp.get("category") == "professional_experience", "ISP RAS must reflect user-confirmed employment")
    require(isp.get("status") == "ACTIVE_WORK__USER_CONFIRMED_2026_10_11", "ISP RAS active-work status lost")
    require("USER_ATTESTED" in isp.get("evidence_level", []), "ISP RAS work needs an explicit user provenance")
    require(isp.get("resume_priority") == "VERY_HIGH", "Current ISP RAS work must be prioritized")
    claims = isp.get("claims", {})
    for lang, token in (("ru", "символьн"), ("en", "symbolic")):
        text = str(claims.get(f"safe_{lang}", "")).casefold()
        require("sharpchecker" in text and token in text, f"ISP RAS {lang} claim must name scoped symbolic-computation work")

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

    # A self-reported LMS user count is evidence of the candidate's statement, not
    # independent analytics and not proof that the full Judge workflow is live.
    lms = by_id.get("project_compilationlab_lms")
    require(lms is not None, "missing LMS evidence asset")
    usage = lms.get("user_attested_current_users", {})
    require("USER_ATTESTED" in lms.get("evidence_level", []), "LMS user estimate must retain USER_ATTESTED provenance")
    require(usage.get("as_of") == "2026-11-13" and usage.get("reported_count") == "approximately 40",
            "LMS count must remain a dated approximate self-report")
    boundary = str(usage.get("boundary", "")).lower()
    require("independently" in boundary and "active" in boundary and "paying" in boundary,
            "LMS 40-user claim must not be upgraded to independent active/paying users")

    # Regression receipts must remain tied to immutable revisions, toolchain
    # and test scope; neither count proves production use or speedup.
    for asset_id, commit, total in (
        ("project_global_iv", "0d759dcf3af7a5652432eb0fea5b9ca27ec88f74", "29"),
        ("project_deref_after_null", "a18102e988dbf854e67b356a44e1d81caba5b080", "18"),
    ):
        asset = by_id.get(asset_id)
        require(asset is not None and "LOCAL_REPRODUCED" in asset.get("evidence_level", []),
                f"Missing local verification provenance for {asset_id}")
        receipt = asset.get("regression_replay_2026_11_13", {})
        require(receipt.get("source_commit") == commit
                and receipt.get("date") == "2026-11-13"
                and total in str(receipt.get("observed", "")),
                f"Missing pinned scoped regression receipt for {asset_id}")
        limit = str(receipt.get("limitation", "")).lower()
        require("not" in limit and ("production" in limit or "sharpchecker" in limit),
                f"Overbroad or missing boundary for {asset_id}")

    # C++ profile: a failed expanded smoke suite is not an industrial defect
    # claim, and the official MCST selection test result was not replayed.
    ps = by_id.get("project_ps_form")
    mcst = by_id.get("experience_mcst_2026")
    require(ps is not None and mcst is not None, "Missing C++/MCST evidence assets")
    require("LOCAL_REPRODUCED" in ps.get("evidence_level", []), "PS-form local smoke provenance required")
    require("LOCAL_REPRODUCED" in mcst.get("evidence_level", []), "Graph fixture provenance required")
    smoke = ps.get("local_smoke_replay_2026_11_13", {})
    require(smoke.get("source_commit") == "758001fdadba56b4f2bd7601464bd6fe0cd2b388"
            and "907 passed" in smoke.get("observed", "")
            and "5 failed" in smoke.get("observed", "")
            and "not" in smoke.get("boundary", "").lower(),
            "PS-form 907/912 limits must remain recorded")
    graph = mcst.get("graph_fixture_replay_2026_11_13", {})
    require(graph.get("source_commit") == "1b840dae228dc10008e5b49f3bec1940be5e8c30"
            and "14/14" in graph.get("observed", "")
            and "no complete lint" in graph.get("boundary", "").lower(),
            "C++23 graph fixture verification must not imply full lint or selection result")

    # Pinned Rust compiler-backend results: a clean Fedora debug run,
    # not a completed local release run or a production-ready backend.
    rust = by_id.get("project_x86_codegen")
    require(rust is not None and "LOCAL_REPRODUCED" in rust.get("evidence_level", []),
            "Rust backend must retain local verification provenance")
    receipt = rust.get("local_replay_2026_11_14", {})
    require(receipt.get("source_commit") == "dd0693c3af06dc9a3612b68ecb94f9637d6b0514"
            and receipt.get("date") == "2026-11-14"
            and "42 passed" in receipt.get("debug_observed", "")
            and "0 failed" in receipt.get("debug_observed", ""),
            "Rust backend 42/42 claim must be pinned to the verified source and date")
    require("NOT_VERIFIED" in receipt.get("release_status", "")
            and "disk quota" in receipt.get("release_status", "").lower()
            and "NOT_VERIFIED" not in receipt.get("debug_observed", ""),
            "Local release build limitations cannot be interpreted as test success/failure")
    ci = receipt.get("public_ci", {})
    require(ci.get("head_sha") == receipt.get("source_commit")
            and ci.get("run_id") == 34896109843
            and ci.get("conclusion") == "success",
            "Public CI source identity must match the pinned Rust backend commit")

    # Financial research evidence is private, structural and not predictive.
    # Never replace machine bootstrap labels with expert gold ground truth.
    benchmark = by_id.get("research_channel_tracker_benchmark")
    calib = by_id.get("research_channel_tracker_calibration")
    for asset in (benchmark, calib):
        require(asset is not None, "Missing private Quant Developer research evidence")
        require("PRIVATE_LOCAL_REPRODUCED" in asset.get("evidence_level", [])
                and not asset.get("public_sources"),
                "Private research cannot be upgraded to public-source evidence")
        require(str(asset.get("source_visibility", "")).startswith("private_local_only"),
                "Private tracker provenance/privacy boundary missing")
        checks = asset.get("checks", {})
        require(checks.get("date") == "2026-11-14",
                "Quant private structural verification date must remain exact")
    b = benchmark.get("checks", {})
    require(b.get("source_snapshots_sha256", {}).get("README.md")
            == "ca3ab565546e6f2c2a23776b7b2b9cfbfd0b5e453620fb165c5fddd6fc26c0d6"
            and "VALIDATION_OK" in b.get("observed", "")
            and all(part in b.get("observed", "") for part in ("cases=31", "positive=25", "negative=6",
                                                               "nested_pairs=6", "successor_pairs=3")),
            "Private OHLC data contract must remain reproducible and bounded")
    c = calib.get("checks", {})
    require("CALIBRATION_VALIDATION_OK" in c.get("observed", "")
            and all(part in c.get("observed", "") for part in ("cases=20", "relations=8", "images=20"))
            and "NOT_COLLECTED" in c.get("expert_gold", ""),
            "Blind-calibration structural completion is not expert gold or accuracy")
    for asset in (benchmark, calib):
        boundary = " ".join(str(x) for x in asset.get("boundaries", [])).lower()
        require("no" in boundary
                and any(word in boundary for word in ("profit", "accuracy", "expert")),
                "Quant outcomes must retain explicit non-performance boundaries")

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
