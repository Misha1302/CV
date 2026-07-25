from __future__ import annotations

from pathlib import Path

source_path = Path(__file__).with_name("export_validate_compiler_cv_v30.py")
source = source_path.read_text(encoding="utf-8")
old = '''            missing = [token for token in required if token not in normalized]
            bad = [token for token in stale if token in normalized]
'''
new = '''            normalized_folded = normalized.casefold()
            missing = [token for token in required if token.casefold() not in normalized_folded]
            bad = [token for token in stale if token.casefold() in normalized_folded]
'''
if old not in source:
    raise RuntimeError("PDF wording comparison block not found")
patched = source.replace(old, new, 1)
namespace = {"__name__": "__main__", "__file__": str(source_path)}
exec(compile(patched, str(source_path), "exec"), namespace)
