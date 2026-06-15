from pathlib import Path

CHECK_URL = "https://diploma.rsr-olymp.ru/check"

ru = Path("ru.html").read_text(encoding="utf-8")
en = Path("en.html").read_text(encoding="utf-8")
cv = Path("cv.html").read_text(encoding="utf-8")

ru = ru.replace("Официальные результаты и проверяемые источники.", "Официальные результаты и подтверждающие документы.", 1)
ru = ru.replace('<article><span>2026 · МЦСТ</span><h3>Отбор по направлению LLVM-компилятора</h3><p>Первое место среди 49 присланных решений; единственное решение, получившее 5,0/5,0 и прошедшее все 104 теста.</p><div class="evidence-links"></div></article>', '<article><span>2026 · МЦСТ</span><h3>Отбор по направлению LLVM-компилятора</h3><p>Первое место среди 49 присланных решений; единственное решение, получившее 5,0/5,0 и прошедшее все 104 теста.</p></article>', 1)
ru = ru.replace('<article><span>2025–26 · НИЯУ МИФИ</span><h3>Конкурс «Юниор»</h3><p>Первое место по России в 2025 году и второе в 2026-м; дипломы I степени в оба года.</p><div class="evidence-links"><a href="https://olymp.mephi.ru/junior/winners/2026" rel="noopener noreferrer" target="_blank">Официальные результаты ↗</a></div></article>', f'<article><span>2025–26 · НИЯУ МИФИ</span><h3>Конкурс «Юниор»</h3><p>Первое место по России в 2025 году и второе в 2026-м; дипломы I степени в оба года.</p><div class="evidence-links"><a href="https://olymp.mephi.ru/junior/winners/2026" rel="noopener noreferrer" target="_blank">Официальные результаты ↗</a><a href="{CHECK_URL}" rel="noopener noreferrer" target="_blank">Проверить диплом РСОШ · 415 7412-33532 ↗</a></div></article>', 1)
ru = ru.replace('<article><span>2026 · «Высшая проба»</span><h3>Промышленное программирование</h3><p>Призёр, диплом II степени по профилю второго уровня «Промышленное программирование».</p><div class="evidence-links"></div></article>', f'<article><span>2026 · «Высшая проба»</span><h3>Промышленное программирование</h3><p>Призёр, диплом II степени по профилю второго уровня «Промышленное программирование».</p><div class="evidence-links"><a href="{CHECK_URL}" rel="noopener noreferrer" target="_blank">Проверить диплом РСОШ · 414 8554-64780 ↗</a></div></article>', 1)
ru = ru.replace('<article><span>2026 · «Высшая проба»</span><h3>Информатика</h3><p>Призёр, диплом III степени по профилю первого уровня «Информатика».</p><div class="evidence-links"></div></article>', f'<article><span>2026 · «Высшая проба»</span><h3>Информатика</h3><p>Призёр, диплом III степени по профилю первого уровня «Информатика».</p><div class="evidence-links"><a href="{CHECK_URL}" rel="noopener noreferrer" target="_blank">Проверить диплом РСОШ · 414 8680-58542 ↗</a></div></article>', 1)

en = en.replace("Official results and verifiable records.", "Official results and supporting documents.", 1)
en = en.replace('<article><span>2026 · MCST</span><h3>LLVM Compiler Selection</h3><p>Ranked 1st among 49 submitted solutions; the only submission to score 5.0/5.0 and pass all 104 tests.</p><div class="evidence-links"></div></article>', '<article><span>2026 · MCST</span><h3>LLVM Compiler Selection</h3><p>Ranked 1st among 49 submitted solutions; the only submission to score 5.0/5.0 and pass all 104 tests.</p></article>', 1)
en = en.replace('<article><span>2025–26 · MEPhI</span><h3>Junior Olympiad</h3><p>Ranked 1st nationally in 2025 and 2nd in 2026; received first-degree diplomas in both years.</p><div class="evidence-links"><a href="https://olymp.mephi.ru/junior/winners/2026" rel="noopener noreferrer" target="_blank">Official results ↗</a></div></article>', f'<article><span>2025–26 · MEPhI</span><h3>Junior Olympiad</h3><p>Ranked 1st nationally in 2025 and 2nd in 2026; received first-degree diplomas in both years.</p><div class="evidence-links"><a href="https://olymp.mephi.ru/junior/winners/2026" rel="noopener noreferrer" target="_blank">Official results ↗</a><a href="{CHECK_URL}" rel="noopener noreferrer" target="_blank">Verify RSOSH diploma · 415 7412-33532 ↗</a></div></article>', 1)
en = en.replace('<article><span>2026 · Vysshaya Proba</span><h3>Industrial Programming</h3><p>Prize-winner, second-degree diploma in the Level 2 Industrial Programming track.</p><div class="evidence-links"></div></article>', f'<article><span>2026 · Vysshaya Proba</span><h3>Industrial Programming</h3><p>Prize-winner, second-degree diploma in the Level 2 Industrial Programming track.</p><div class="evidence-links"><a href="{CHECK_URL}" rel="noopener noreferrer" target="_blank">Verify RSOSH diploma · 414 8554-64780 ↗</a></div></article>', 1)
en = en.replace('<article><span>2026 · Vysshaya Proba</span><h3>Informatics</h3><p>Prize-winner, third-degree diploma in the Level 1 Informatics track.</p><div class="evidence-links"></div></article>', f'<article><span>2026 · Vysshaya Proba</span><h3>Informatics</h3><p>Prize-winner, third-degree diploma in the Level 1 Informatics track.</p><div class="evidence-links"><a href="{CHECK_URL}" rel="noopener noreferrer" target="_blank">Verify RSOSH diploma · 414 8680-58542 ↗</a></div></article>', 1)

cv = cv.replace('<article><span>2025–26</span><h2>MEPhI Junior</h2><p>Ranked 1st nationally in 2025 and 2nd in 2026; first-degree diplomas in both years.</p></article>', f'<article><span>2025–26</span><h2>MEPhI Junior</h2><p>Ranked 1st nationally in 2025 and 2nd in 2026; first-degree diplomas in both years. <a href="{CHECK_URL}">RSOSH verification: 415 7412-33532</a></p></article>', 1)
cv = cv.replace('<article><span>2026</span><h2>Vysshaya Proba · Industrial Programming</h2><p>Prize-winner, second-degree diploma.</p></article>', f'<article><span>2026</span><h2>Vysshaya Proba · Industrial Programming</h2><p>Prize-winner, second-degree diploma. <a href="{CHECK_URL}">RSOSH verification: 414 8554-64780</a></p></article>', 1)
cv = cv.replace('<article><span>2026</span><h2>Vysshaya Proba · Informatics</h2><p>Prize-winner, third-degree diploma in the Level 1 track.</p></article>', f'<article><span>2026</span><h2>Vysshaya Proba · Informatics</h2><p>Prize-winner, third-degree diploma in the Level 1 track. <a href="{CHECK_URL}">RSOSH verification: 414 8680-58542</a></p></article>', 1)

assert 'class="evidence-links"></div>' not in ru
assert 'class="evidence-links"></div>' not in en
assert ru.count(CHECK_URL) == 3
assert en.count(CHECK_URL) == 3
assert cv.count(CHECK_URL) == 3

Path("ru.html").write_text(ru, encoding="utf-8")
Path("en.html").write_text(en, encoding="utf-8")
Path("index.html").write_text(en, encoding="utf-8")
Path("cv.html").write_text(cv, encoding="utf-8")
