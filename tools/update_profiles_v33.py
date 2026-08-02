"""Deterministically migrate targeted CV profiles before rebuilding published PDFs."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "cv-print-profiles.json"


def set_role(profile: dict, role: str) -> None:
    profile["role"] = role
    order = profile.get("ats_order", [])
    if len(order) >= 2:
        order[1] = role


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    data["verified_at"] = "2026-08-02"

    for profile in data["profiles"].values():
        profile["availability"] = "Москва / удалённо" if profile.get("lang") == "ru" else "Moscow / remote"

    ru_compiler = data["profiles"]["ru-compiler.html"]
    set_role(ru_compiler, "Инженер по компиляторам и .NET-платформам")
    ru_compiler["summary"] = (
        "Проектирую платформенные системы с явными контрактами и инвариантами: "
        "UniversalToolchain/Wist2, callable-first SSA, interpreter/CIL и PlanFuzz; "
        "дополнительно — .NET backend с платежами, состоянием, миграциями, recovery и проверяемыми релизами."
    )
    ru_compiler["proofs"] = [
        [
            "Архитектура платформы",
            "контракты, маршруты, manifests/locks и lifecycle ownership",
        ],
        [
            ".NET backend и recovery",
            "платежи, состояния, миграции, backup/restore и rollback",
        ],
        [
            "Компиляторная глубина",
            "SSA, interpreter/CIL, LLVM, анализ программ и x86-64",
        ],
    ]
    ru_compiler["skills"] = [
        [
            "Архитектура платформ",
            "типизированные контракты, независимые пакеты, маршруты, manifests/locks, lifecycle ownership",
        ],
        [
            ".NET / backend",
            "C#/.NET, ASP.NET Core, REST/OpenAPI, PostgreSQL/SQLite, payments/webhooks, recovery",
        ],
        [
            "IR / SSA",
            "байткод/AIR, callable-first SSA, CFG, доминирование, свёртка, SCCP-lite, DCE",
        ],
        [
            "Проверка и системы",
            "differential/metamorphic testing, exact oracles, C++23, C17, Python, Rust, Linux",
        ],
    ]

    en_compiler = data["profiles"]["en-compiler.html"]
    set_role(en_compiler, "Compiler and .NET Platform Engineer")
    en_compiler["summary"] = (
        "I design platform systems with explicit contracts and invariants: UniversalToolchain/Wist2, "
        "callable-first SSA, interpreter/CIL, and PlanFuzz, complemented by .NET backend work with "
        "payments, state transitions, migrations, recovery, and verifiable releases."
    )
    en_compiler["proofs"] = [
        ["Platform architecture", "typed contracts, deterministic routes, manifests/locks, lifecycle ownership"],
        [".NET backend and recovery", "payments, state transitions, migrations, backup/restore, rollback"],
        ["Compiler depth", "SSA, interpreter/CIL, LLVM, program analysis, and x86-64 codegen"],
    ]
    en_compiler["skills"] = [
        ["Platform architecture", "typed contracts, independent packages, routes, manifests/locks, lifecycle ownership"],
        [".NET / backend", "C#/.NET, ASP.NET Core, REST/OpenAPI, PostgreSQL/SQLite, payments/webhooks, recovery"],
        ["IR / SSA", "Bytecode/AIR, callable-first SSA, CFG, dominance, folding, SCCP-lite, DCE"],
        ["Verification and systems", "differential/metamorphic testing, exact oracles, C++23, C17, Python, Rust, Linux"],
    ]

    for filename in ["ru-backend.html", "ru-platform.html"]:
        profile = data["profiles"][filename]
        set_role(profile, ".NET Backend Engineer · надёжные системы")
        profile["summary"] = (
            "Проектирую .NET-сервисы, где критичны корректность состояния и восстановление после сбоев: "
            "REST/OpenAPI, платежи и webhooks, PostgreSQL/SQLite, идемпотентность, миграции, recovery, "
            "health gates, backup/restore и rollback."
        )

    for filename in ["en-backend.html", "en-platform.html"]:
        profile = data["profiles"][filename]
        set_role(profile, ".NET Backend Engineer · Reliable Systems")
        profile["summary"] = (
            "I design .NET services where state correctness and recovery matter: REST/OpenAPI, payments and "
            "webhooks, PostgreSQL/SQLite, idempotency, migrations, recovery, health gates, backup/restore, and rollback."
        )

    DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
