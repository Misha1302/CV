from pathlib import Path
import json
import re

RU_PROOF = '''<section aria-label="Ключевые подтверждения" class="proof-strip">
<div><strong>#1 · 104/104</strong><span>Отбор МЦСТ по LLVM-компилятору</span></div>
<div><strong>2 направления</strong><span>Призёр «Высшей пробы»</span></div>
<div><strong>≈50</strong><span>Учеников по программированию</span></div>
<div><strong>10</strong><span>Подтверждённых отзывов на Avito</span></div>
</section>'''

EN_PROOF = '''<section aria-label="Selected evidence" class="proof-strip"><div><strong>#1 · 104/104</strong><span>MCST LLVM compiler selection</span></div><div><strong>2 tracks</strong><span>Vysshaya Proba prize-winner</span></div><div><strong>~50</strong><span>Programming students</span></div><div><strong>10</strong><span>Verified Avito reviews</span></div></section>'''

RU_RECOGNITION = '''<div class="recognition-list recognition-evidence">
<article><span>2026 · МЦСТ</span><h3>Отбор по направлению LLVM-компилятора</h3><p>Первое место среди 49 присланных решений; единственное решение, получившее 5,0/5,0 и прошедшее все 104 теста.</p><div class="evidence-links"></div></article>
<article><span>2025–26 · НИЯУ МИФИ</span><h3>Конкурс «Юниор»</h3><p>Первое место по России в 2025 году и второе в 2026-м; дипломы I степени в оба года.</p><div class="evidence-links"><a href="https://olymp.mephi.ru/junior/winners/2026" rel="noopener noreferrer" target="_blank">Официальные результаты ↗</a></div></article>
<article><span>2026 · «Высшая проба»</span><h3>Промышленное программирование</h3><p>Призёр, диплом II степени по профилю второго уровня «Промышленное программирование».</p><div class="evidence-links"></div></article>
<article><span>2026 · «Высшая проба»</span><h3>Информатика</h3><p>Призёр, диплом III степени по профилю первого уровня «Информатика».</p><div class="evidence-links"></div></article>
<article><span>2026 · Балтийский конкурс</span><h3>Наука и инженерия</h3><p>Диплом I степени и премия «Совершенство как надежда» за UniversalToolchain.</p><div class="evidence-links"><a href="https://baltkonkurs.ru/features/po-godam/xxii-konkurs-2026/" rel="noopener noreferrer" target="_blank">Официальная страница ↗</a></div></article>
<article><span>2025/26 · НИУ ВШЭ</span><h3>«Высший пилотаж» · Computer Science</h3><p>Победитель направления Computer Science среди учеников 11 класса.</p><div class="evidence-links"><a href="https://olymp.hse.ru/projects/papers" rel="noopener noreferrer" target="_blank">Официальные результаты ↗</a></div></article>
</div>'''

EN_RECOGNITION = '''<div class="recognition-list recognition-evidence">
<article><span>2026 · MCST</span><h3>LLVM Compiler Selection</h3><p>Ranked 1st among 49 submitted solutions; the only submission to score 5.0/5.0 and pass all 104 tests.</p><div class="evidence-links"></div></article>
<article><span>2025–26 · MEPhI</span><h3>Junior Olympiad</h3><p>Ranked 1st nationally in 2025 and 2nd in 2026; received first-degree diplomas in both years.</p><div class="evidence-links"><a href="https://olymp.mephi.ru/junior/winners/2026" rel="noopener noreferrer" target="_blank">Official results ↗</a></div></article>
<article><span>2026 · Vysshaya Proba</span><h3>Industrial Programming</h3><p>Prize-winner, second-degree diploma in the Level 2 Industrial Programming track.</p><div class="evidence-links"></div></article>
<article><span>2026 · Vysshaya Proba</span><h3>Informatics</h3><p>Prize-winner, third-degree diploma in the Level 1 Informatics track.</p><div class="evidence-links"></div></article>
<article><span>2026 · Baltic Competition</span><h3>Science and Engineering</h3><p>First-degree diploma and the “Excellence as Hope” award for UniversalToolchain.</p><div class="evidence-links"><a href="https://baltkonkurs.ru/features/po-godam/xxii-konkurs-2026/" rel="noopener noreferrer" target="_blank">Official page ↗</a></div></article>
<article><span>2025/26 · HSE University</span><h3>Higher Pilotage Student Research Competition · Computer Science</h3><p>Winner of the Computer Science track among grade 11 students.</p><div class="evidence-links"><a href="https://olymp.hse.ru/projects/papers" rel="noopener noreferrer" target="_blank">Official results ↗</a></div></article>
</div>'''

CV_AWARDS = '''      <div class="section-body award-grid">
        <article><span>2026</span><h2>MCST LLVM Compiler Selection</h2><p>Ranked 1st among 49 submitted solutions; the only submission to score 5.0/5.0 and pass all 104 tests.</p></article>
        <article><span>2025–26</span><h2>MEPhI Junior</h2><p>Ranked 1st nationally in 2025 and 2nd in 2026; first-degree diplomas in both years.</p></article>
        <article><span>2026</span><h2>Vysshaya Proba · Industrial Programming</h2><p>Prize-winner, second-degree diploma.</p></article>
        <article><span>2026</span><h2>Vysshaya Proba · Informatics</h2><p>Prize-winner, third-degree diploma in the Level 1 track.</p></article>
        <article><span>2026</span><h2>Baltic Science &amp; Engineering Competition</h2><p>First-degree diploma and “Excellence as Hope” award.</p></article>
        <article><span>2025/26</span><h2>HSE Higher Pilotage Student Research Competition · Computer Science</h2><p>Winner of the Computer Science track among grade 11 students. <a href="https://olymp.hse.ru/projects/papers">Official results</a></p></article>
      </div>'''

def replace_once(text, pattern, replacement, label, flags=0):
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise SystemExit(f"{label}: expected one replacement, got {count}")
    return updated

ru = Path("ru.html").read_text(encoding="utf-8")
en = Path("en.html").read_text(encoding="utf-8")
cv = Path("cv.html").read_text(encoding="utf-8")

ru = replace_once(ru, r'<section aria-label="Ключевые подтверждения" class="proof-strip">.*?</section>', RU_PROOF, "ru proof", re.S)
ru = replace_once(ru, r'<article><time>2026</time><div><h3>Стажёр МЦСТ · LLVM-компилятор</h3>.*?</article>', '<article><time>2026</time><div><h3>Стажёр МЦСТ · LLVM-компилятор</h3><p class="meta">Направление «Системы программирования»</p><p>Стажировка по направлению «Системы программирования: компилятор LLVM» с фокусом на разработке компиляторов и анализе программ.</p><b>Компиляторы · Анализ программ</b></div></article>', "ru experience", re.S)
ru = replace_once(ru, r'<article><span>Текущая роль</span><strong>МЦСТ · направление LLVM-компилятора</strong><p>.*?</p></article>', '<article><span>Текущая роль</span><strong>МЦСТ · направление LLVM-компилятора</strong><p>Стажировка по направлению «Системы программирования: компилятор LLVM».</p></article>', "ru role", re.S)
ru = ru.replace('<strong>104/104</strong></footer>', '</footer>', 1)
ru = replace_once(ru, r'<div class="recognition-list recognition-evidence">.*?</div>\n</section>\n<section class="section" id="public">', RU_RECOGNITION + '\n</section>\n<section class="section" id="public">', "ru recognition", re.S)

en = replace_once(en, r'<section aria-label="Selected evidence" class="proof-strip">.*?</section>', EN_PROOF, "en proof", re.S)
en = replace_once(en, r'<article><time>2026</time><div><h3>MCST intern · LLVM compiler</h3>.*?</article>', '<article><time>2026</time><div><h3>MCST intern · LLVM compiler</h3><p class="meta">Programming Systems track</p><p>Compiler engineering internship in the “Programming Systems: LLVM Compiler” track, focused on compiler development and program analysis.</p><b>Compiler engineering · Program analysis</b></div></article>', "en experience", re.S)
en = replace_once(en, r'<article><span>Current role</span><strong>MCST · LLVM compiler track</strong><p>.*?</p></article>', '<article><span>Current role</span><strong>MCST · LLVM compiler track</strong><p>Internship in the “Programming Systems: LLVM Compiler” track.</p></article>', "en role", re.S)
en = en.replace('<strong>104/104</strong></footer>', '</footer>', 1)
en = replace_once(en, r'<div class="recognition-list recognition-evidence">.*?</div>\n</section>\n<section class="section" id="public">', EN_RECOGNITION + '\n</section>\n<section class="section" id="public">', "en recognition", re.S)

cv = replace_once(cv, r'    <div class="evidence-strip">.*?    </div>\n\n    <section class="cv-section">', '    <div class="evidence-strip">\n      <div><strong>#1 · 104/104</strong><span>MCST LLVM selection</span></div>\n      <div><strong>2 tracks</strong><span>Vysshaya Proba prize-winner</span></div>\n      <div><strong>~50</strong><span>Programming students</span></div>\n      <div><strong>10</strong><span>Verified Avito reviews</span></div>\n    </div>\n\n    <section class="cv-section">', "cv proof", re.S)
cv = replace_once(cv, r'<div><h2>MCST intern · LLVM compiler</h2><p class="meta">Programming Systems track</p><p>.*?</p></div>', '<div><h2>MCST intern · LLVM compiler</h2><p class="meta">Programming Systems track</p><p>Compiler engineering internship in the “Programming Systems: LLVM Compiler” track, focused on compiler development and program analysis.</p></div>', "cv experience", re.S)
cv = cv.replace('C17 · Python · 104/104', 'C17 · Python', 1)
cv = replace_once(cv, r'      <div class="section-body award-grid">.*?      </div>\n    </section>\n\n    <section class="cv-section compact">\n      <div class="section-label">Education</div>', CV_AWARDS + '\n    </section>\n\n    <section class="cv-section compact">\n      <div class="section-label">Education</div>', "cv awards", re.S)

Path("ru.html").write_text(ru, encoding="utf-8")
Path("en.html").write_text(en, encoding="utf-8")
Path("index.html").write_text(en, encoding="utf-8")
Path("cv.html").write_text(cv, encoding="utf-8")

assert en == Path("index.html").read_text(encoding="utf-8")
assert ru.count('2026 · МЦСТ') == 1
assert en.count('2026 · MCST') == 1
assert cv.count('MCST LLVM Compiler Selection') == 1
assert '<strong>104/104</strong></footer>' not in ru
assert '<strong>104/104</strong></footer>' not in en
assert 'C17 · Python · 104/104' not in cv

for filename in ("ru.html", "en.html", "index.html"):
    content = Path(filename).read_text(encoding="utf-8")
    block = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.S)
    if not block:
        raise SystemExit(f"{filename}: missing JSON-LD")
    json.loads(block.group(1))
    proof = re.search(r'class="proof-strip"(.*?)</section>', content, re.S)
    recognition = re.search(r'class="recognition-list recognition-evidence"(.*?)</div>\n</section>', content, re.S)
    if not proof or proof.group(1).count('<div>') != 4:
        raise SystemExit(f"{filename}: proof grid is not 4 cards")
    if not recognition or recognition.group(1).count('<article>') != 6:
        raise SystemExit(f"{filename}: recognition grid is not 6 cards")
