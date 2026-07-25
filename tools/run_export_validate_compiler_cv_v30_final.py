from __future__ import annotations

from pathlib import Path

source_path = Path(__file__).with_name("export_validate_compiler_cv_v30.py")
source = source_path.read_text(encoding="utf-8")

case_old = '''            missing = [token for token in required if token not in normalized]
            bad = [token for token in stale if token in normalized]
'''
case_new = '''            normalized_folded = normalized.casefold()
            missing = [token for token in required if token.casefold() not in normalized_folded]
            bad = [token for token in stale if token.casefold() in normalized_folded]
'''
if case_old not in source:
    raise RuntimeError("PDF wording comparison block not found")
source = source.replace(case_old, case_new, 1)

ru_old = 'ordered = ("Михаил Разаков", "UniversalToolchain", "МЦСТ", "PS-form")'
ru_new = 'ordered = ("Михаил Разаков", "UniversalToolchain", "МЦСТ", "PS-form Memory Dependence Analyzer")'
en_old = 'ordered = ("Mikhail Razakov", "UniversalToolchain", "MCST", "PS-form")'
en_new = 'ordered = ("Mikhail Razakov", "UniversalToolchain", "MCST", "PS-form Memory Dependence Analyzer")'
for old, new in ((ru_old, ru_new), (en_old, en_new)):
    if old not in source:
        raise RuntimeError(f"ATS order marker not found: {old}")
    source = source.replace(old, new, 1)

namespace = {"__name__": "__main__", "__file__": str(source_path)}
exec(compile(source, str(source_path), "exec"), namespace)
