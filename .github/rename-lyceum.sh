#!/usr/bin/env bash
set -euo pipefail
python3 - <<'PY'
from pathlib import Path
path = Path('ru.html')
text = path.read_text(encoding='utf-8')
replacements = {
    'физико-технический лицей (ФТЛ)': 'физтех лицей',
    'физико технический лицей': 'физтех лицей',
    'физико-технический лицей': 'физтех лицей',
}
changed = text
for old, new in replacements.items():
    changed = changed.replace(old, new)
if changed == text:
    raise SystemExit('target lyceum wording was not found')
path.write_text(changed, encoding='utf-8')
PY
grep -q 'физтех лицей' ru.html
! grep -q 'физико-технический лицей' ru.html
! grep -q 'физико технический лицей' ru.html
git diff --check
git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git rm .github/workflows/rename-lyceum.yml
git rm .github/rename-lyceum.sh
git rm .cv-rename-lyceum-trigger
git add ru.html
git diff --cached --check
git commit -m 'fix: rename lyceum wording'
git push origin HEAD:main
