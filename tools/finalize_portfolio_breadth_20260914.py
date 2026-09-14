from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "site.json"
VALIDATOR_PATH = ROOT / "tools" / "validate_cv.py"
AUDIT_PATH = ROOT / "CV-SEMANTIC-PORTFOLIO-AUDIT-2026-09-14.md"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    independent_ru = {
        "date": "2023–2026",
        "title": "Независимая / freelance-разработка — product systems",
        "org": ".NET · Unity · jQuery · Linux",
        "bullets": [
            "VpnMediator: подписки, платежи и состояние доступа, ограничения по устройствам, Linux-развёртывание, recovery и rollback.",
            "Diploma.school: jQuery dropdown и адаптивная навигация; Unity licensing: server-side activation limits и интеграция с Unity-клиентом.",
        ],
    }
    independent_en = {
        "date": "2023–2026",
        "title": "Independent / freelance engineering — product systems",
        "org": ".NET · Unity · jQuery · Linux",
        "bullets": [
            "VpnMediator: subscription, payment, and access state, device limits, Linux deployment, recovery, and rollback.",
            "Diploma.school: jQuery dropdown interactions and responsive navigation; Unity licensing: server-side activation limits and Unity client integration.",
        ],
    }

    # Keep compiler-specialist project slots focused. Breadth appears after the two
    # professional roles in the infrastructure and broad fallback CVs.
    for key in ("general", "compiler"):
        data["profiles"][key]["ru"]["experience"] = data["profiles"][key]["ru"]["experience"][:2] + [independent_ru]
        data["profiles"][key]["en"]["experience"] = data["profiles"][key]["en"]["experience"][:2] + [independent_en]

    # Backend already uses VpnMediator as a primary production proof. Replace the
    # redundant UT experience row with product-delivery breadth; UT stays a project.
    backend_ru = data["profiles"]["backend"]["ru"]
    backend_en = data["profiles"]["backend"]["en"]
    backend_ru["experience"] = backend_ru["experience"][:2] + [{
        "date": "2023–2026",
        "title": "Freelance / client product work — Diploma.school & Unity",
        "org": "jQuery · responsive UI · ASP.NET · Unity",
        "bullets": [
            "Diploma.school: реализовал jQuery dropdown-компоненты, адаптивную mobile/desktop navigation и исправления UI-регрессий.",
            "Unity licensing: сделал server-side key activation с ограничением числа активаций и интеграцию проверки лицензии в Unity-клиент.",
        ],
    }]
    backend_en["experience"] = backend_en["experience"][:2] + [{
        "date": "2023–2026",
        "title": "Freelance / client product work — Diploma.school & Unity",
        "org": "jQuery · responsive UI · ASP.NET · Unity",
        "bullets": [
            "Diploma.school: implemented jQuery dropdown components, responsive mobile/desktop navigation, and UI regression fixes.",
            "Unity licensing: built server-side key activation with activation-count limits and integrated license validation into a Unity client.",
        ],
    }]

    # Protection remains selective, but VpnMediator is useful adjacent evidence for
    # server-side access/subscription state. The first three print rows remain
    # ISP RAS, MCST, and the dedicated Unity licensing/protection project.
    protection_ru = data["profiles"]["software_protection"]["ru"]
    protection_en = data["profiles"]["software_protection"]["en"]
    vpn_ru = {
        "date": "2026 — сейчас",
        "title": "VpnMediator — backend состояния доступа",
        "org": "ASP.NET Core · subscriptions · payments · Linux",
        "bullets": [
            "Реализовал server-side состояние подписок/доступа, ограничения по устройствам, payment flows и пути recovery/rollback при сбоях и перезапусках."
        ],
    }
    vpn_en = {
        "date": "2026 — present",
        "title": "VpnMediator — access-state backend",
        "org": "ASP.NET Core · subscriptions · payments · Linux",
        "bullets": [
            "Built server-side subscription/access state, device limits, payment flows, and recovery/rollback paths across failures and restarts."
        ],
    }
    if not any("VpnMediator" in item.get("title", "") for item in protection_ru["experience"]):
        protection_ru["experience"].append(vpn_ru)
    if not any("VpnMediator" in item.get("title", "") for item in protection_en["experience"]):
        protection_en["experience"].append(vpn_en)

    # Make the user-attested/private evidence boundary explicit without pretending
    # that the private Diploma repository was independently inspected this turn.
    if AUDIT_PATH.exists():
        audit = AUDIT_PATH.read_text(encoding="utf-8")
        audit = audit.replace(
            "| Diploma | No independently located artifact during this execution. | **NEEDS_VERIFICATION — omitted from CV.** |",
            "| Diploma.school | User-attested private/freelance project: jQuery dropdown interactions, responsive mobile/desktop navigation, and UI regression fixes. | **USER_ATTESTED / PRIVATE — included with bounded wording; no public-repository claim.** |",
        )
        audit = audit.replace(
            "The prompt named three prior-review artifacts",
            "Additional breadth retained: VpnMediator production/reliability work and the bounded Unity licensing/protection project are used as supporting engineering evidence without replacing the strongest compiler-specific project slots.\n\nThe prompt named three prior-review artifacts",
        )
        AUDIT_PATH.write_text(audit, encoding="utf-8")

    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # External-link validation remains fail-closed, but transient upstream 5xx or
    # network timeouts get bounded retries before a real failure is reported.
    validator = VALIDATOR_PATH.read_text(encoding="utf-8")
    if "import time\n" not in validator:
        validator = validator.replace("import sys\n", "import sys\nimport time\n", 1)
    start = validator.index("def check_external_url(url: str) -> tuple[str, int]:")
    end = validator.index("\n\ndef validate_pdfs", start)
    new_function = '''def check_external_url(url: str) -> tuple[str, int]:
    headers = {"User-Agent": "Mozilla/5.0 CV-link-validator/1.0"}
    transient_http = {500, 502, 503, 504}
    accepted_http = {401, 403, 405, 429, 999}
    for method in ("HEAD", "GET"):
        last_error: Exception | None = None
        for attempt in range(3):
            request = urllib.request.Request(url, headers=headers, method=method)
            try:
                with urllib.request.urlopen(request, timeout=15) as response:
                    return url, int(response.status)
            except urllib.error.HTTPError as exc:
                if exc.code in accepted_http:
                    return url, exc.code
                last_error = exc
                if exc.code in transient_http and attempt < 2:
                    time.sleep(1 + attempt)
                    continue
                break
            except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
                last_error = exc
                if attempt < 2:
                    time.sleep(1 + attempt)
                    continue
                break
        if method == "HEAD":
            continue
        if isinstance(last_error, urllib.error.HTTPError):
            raise RuntimeError(f"External link failed after retries: {url} -> HTTP {last_error.code}") from last_error
        if last_error is not None:
            raise RuntimeError(f"External link failed after retries: {url} -> {last_error}") from last_error
    raise RuntimeError(f"External link failed: {url}")
'''
    validator = validator[:start] + new_function + validator[end:]
    VALIDATOR_PATH.write_text(validator, encoding="utf-8")

    print("Added Diploma/Unity/VPN breadth and hardened transient link validation")


if __name__ == "__main__":
    main()
