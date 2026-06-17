#!/usr/bin/env bash
set -euo pipefail
awk '
  /^H4s/ { capture = 1 }
  capture && /^PAYLOAD$/ { exit }
  capture { print }
' .github/workflows/apply-final-cv-fixes.yml | tr -d '\n' | base64 --decode | gzip --decompress > /tmp/cv-final.patch
git apply --check /tmp/cv-final.patch
git apply /tmp/cv-final.patch
node --check script.js
git diff --check
grep -q 'scroll-padding-top: 88px' style.css
grep -q 'Incoming MCST intern · LLVM compiler' en.html
grep -q 'физико-технический лицей (ФТЛ)' ru.html
grep -q '<link rel="canonical" href="https://misha1302.github.io/CV/">' index.html
git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git rm .github/workflows/apply-final-cv-fixes.yml
git rm .github/workflows/finalize-cv.yml
git rm .github/finalize-cv.sh
git rm .cv-final-trigger
git add en.html index.html ru.html style.css
git diff --cached --check
git commit -m 'fix: finalize CV content and responsive layout'
git push origin HEAD:main
