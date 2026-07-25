from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cv-print-profiles.json"

profiles = json.loads(DATA.read_text(encoding="utf-8"))

roles = {
    "ru-devtools.html": "Инженер по тестированию компиляторов и инструментам разработчика",
    "ru-cpp-systems.html": "Инженер по C++-системам и анализу программ",
    "ru-algorithms.html": "Инженер по алгоритмам и оптимизации",
    "ru-backend.html": ".NET-бэкенд-разработчик · надёжные системы",
    "ru-platform.html": ".NET-бэкенд-разработчик · корректность состояния и восстановление",
    "ru-edtech.html": ".NET-бэкенд-разработчик · EdTech",
}

proof_titles = {
    "7 oracle families": "7 семейств оракулов",
    "Fresh-process evidence": "Подтверждение в свежих процессах",
    "1 459 tests": "1 459 тестов",
    "12 C++23 modules": "12 модулей C++23",
    "Strict toolchain": "Строгая сборка",
    "500k vertices": "500 тыс. вершин",
    "Payments & recovery": "Платежи и восстановление",
    "State invariants": "Инварианты состояния",
    "Fail-safe recovery": "Восстановление после сбоев",
    "Verifiable releases": "Проверяемые релизы",
}

skill_titles = {
    "Language architecture": "Архитектура языков",
    "Verification": "Верификация",
    "Languages": "Языки",
    "C++ systems": "C++-системы",
    "Program analysis": "Анализ программ",
    "Low-level": "Низкоуровневая разработка",
    "Algorithms": "Алгоритмы",
    "Correctness": "Корректность",
    "Complexity": "Сложность",
    "Backend": "Бэкенд",
    "Data": "Данные",
    "Reliability": "Надёжность",
    "Operations": "Эксплуатация",
    "State correctness": "Корректность состояния",
    "Recovery": "Восстановление",
    "Release safety": "Безопасность релизов",
    "EdTech domain": "Предметная область EdTech",
    "Product support": "Поддержка продукта",
    "Teaching": "Преподавание",
}

summaries = {
    "ru-devtools.html": "Разработал PlanFuzz — нейтральную к языку систему дифференциального тестирования с учётом конфигурации: семь семейств оракулов, повторное выполнение в свежих процессах, точные отпечатки и детерминированное сокращение программ и планов.",
    "ru-cpp-systems.html": "C++23, анализ программ и низкоуровневая разработка: PS-form Analyzer, AdvancedAlgorithms, стажировка на LLVM-направлении, NASM IA-32 и генерация x86-64-кода.",
    "ru-algorithms.html": "Разрабатываю переиспользуемые алгоритмические компоненты: AdvancedAlgorithms, анализ зависимостей памяти PS-form и графовую инфраструктуру для стажировки на LLVM-направлении.",
    "ru-backend.html": "Проектирую .NET-сервисы с явными моделями состояния: подписки, платежи, роли, устройства, миграции, восстановление, проверки работоспособности и безопасные релизы.",
    "ru-platform.html": "Бэкенд с фокусом на инварианты состояния, идемпотентное восстановление и проверяемые релизы — не отдельная SRE-роль, а ответственность разработчика за поведение сервиса после сбоев.",
}

phrase_replacements = {
    "VPN, LMS and licensing API": "VPN, LMS и API лицензирования",
    "idempotency, outbox, audit trail, reconciliation": "идемпотентность, outbox, журнал аудита, reconciliation",
    "API, data, deployment and rollback": "API, данные, развёртывание и откат",
    "contracts, differential tests, sanitizers and stress": "контракты, дифференциальные тесты, санитайзеры и stress-тесты",
    "stress tests for recursion and accidental O(n²)": "stress-тесты против рекурсии и случайной O(n²)",
    "graphs, trees, strings and data structures": "графы, деревья, строки и структуры данных",
    "subscriptions, payments, balances, devices": "подписки, платежи, балансы и устройства",
    "outbox, audit trail, reconciliation": "outbox, журнал аудита и reconciliation",
    "backup/restore, health gates, rollback": "backup/restore, проверки работоспособности и откат",
}

for filename, profile in profiles["profiles"].items():
    if profile.get("lang") != "ru":
        continue
    if filename in roles:
        profile["role"] = roles[filename]
    if filename in summaries:
        profile["summary"] = summaries[filename]
    for proof in profile.get("proofs", []):
        proof[0] = proof_titles.get(proof[0], proof[0])
        proof[1] = phrase_replacements.get(proof[1], proof[1])
    for skill in profile.get("skills", []):
        skill[0] = skill_titles.get(skill[0], skill[0])
    def walk(value):
        if isinstance(value, str):
            return phrase_replacements.get(value, value)
        if isinstance(value, list):
            return [walk(item) for item in value]
        if isinstance(value, dict):
            return {key: walk(item) for key, item in value.items()}
        return value
    polished = walk(profile)
    profiles["profiles"][filename] = polished

DATA.write_text(json.dumps(profiles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

subprocess.run([
    "python", "tools/build_cv.py", "--write-html", "--render-dir", "pdf",
    "--evidence-dir", "/tmp/cv-v31-polish", "--report", "/tmp/cv-v31-polish-report.json"
], cwd=ROOT, check=True)
subprocess.run(["python", "tools/validate_cv.py", "--skip-manifest"], cwd=ROOT, check=True)

# Remove this one-shot script before the release commit.
Path(__file__).unlink()

manifest = ROOT / "MANIFEST.sha256"
ignored = ".github/workflows/cv-v31-ru-polish.yml"
lines = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or path == manifest or ".git" in path.parts:
        continue
    if path.relative_to(ROOT).as_posix() == ignored:
        continue
    lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  ./{path.relative_to(ROOT).as_posix()}")
manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
