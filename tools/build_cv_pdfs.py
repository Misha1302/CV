from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "pdf"
OUT.mkdir(exist_ok=True)

pdfmetrics.registerFont(TTFont("CV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("CV-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

ACCENT = HexColor("#9d3043")
TEXT = HexColor("#171214")
MUTED = HexColor("#555055")
BORDER = HexColor("#d7cdd0")

COMMON = {
    "ru": {
        "contact": "Москва / удалённо  ·  razakov.misha@mail.ru  ·  t.me/Micodiy  ·  github.com/Misha1302",
        "status": "НИУ ВШЭ, Программная инженерия, 2026-2030. С сентября 2026: стажировка или неполная занятость.",
        "experience": "Опыт",
        "skills": "Технологии",
    },
    "en": {
        "contact": "Moscow / remote  ·  razakov.misha@mail.ru  ·  t.me/Micodiy  ·  github.com/Misha1302",
        "status": "HSE University, Software Engineering, 2026-2030. Open to internship or part-time work from September 2026.",
        "experience": "Experience",
        "skills": "Technologies",
    },
}

PROFILES = {
    "Mikhail_Razakov_Compiler_RU.pdf": {
        "lang": "ru",
        "title": "Михаил Разаков",
        "role": "Разработчик компиляторов и сред исполнения",
        "summary": "С 2024 года развиваю Wist2: лексер, парсер и AST, байткод/AIR, интерпретатор и CIL-бэкенд. На стажировке МЦСТ реализую графовые алгоритмы на C++23.",
        "evidence": ["1-е место среди 49 решений и 104/104 тестов в отборе МЦСТ", "Wist2: Bytecode/AIR, Interpreter, CIL", "C++23, C17, C#/.NET, Linux"],
        "experience": [
            ("МЦСТ · стажёр, июль-август 2026", ["RPO с поиском циклов, Дейкстра, Dinic max flow, Tarjan SCC.", "CMake, тесты .in/.out, -Werror, ASan/UBSan, clang-tidy."]),
            ("Wist2 · автор и основной разработчик, 2024-сейчас", ["Описание диалектов, Lexer, Parser/AST, Bytecode/AIR, оптимизаторы, Interpreter и CIL через DynamicMethod.", "Публичный API, NuGet, документация, примеры и тесты эквивалентности."]),
            ("Анализатор зависимостей памяти · C17", ["Нормализация, диапазоны, сравнения по модулю, НОД и точный анализ аффинных случаев.", "1-е место среди 49 решений; 104/104 тестов."]),
        ],
        "skills": "C++23, C17, C#, Python, CMake, Git, Linux, ASan/UBSan, clang-tidy, Lexer/Parser/AST, Bytecode/AIR, IR/SSA, CIL/DynamicMethod",
    },
    "Mikhail_Razakov_Compiler_EN.pdf": {
        "lang": "en",
        "title": "Mikhail Razakov",
        "role": "Compiler and Runtime Developer",
        "summary": "Since 2024, I have been building Wist2: lexer, parser and AST, bytecode/AIR, interpreter and CIL backend. At MCST, I implement graph algorithms in C++23.",
        "evidence": ["Ranked 1st among 49 submissions; 104/104 tests in MCST selection", "Wist2: Bytecode/AIR, Interpreter, CIL", "C++23, C17, C#/.NET, Linux"],
        "experience": [
            ("MCST · Software Engineering Intern, Jul-Aug 2026", ["RPO with cycle detection, Dijkstra, Dinic maximum flow and Tarjan SCC.", "CMake, .in/.out tests, -Werror, ASan/UBSan and clang-tidy."]),
            ("Wist2 · Author and main developer, 2024-present", ["Dialect configuration, Lexer, Parser/AST, Bytecode/AIR, optimizers, Interpreter and DynamicMethod-based CIL.", "Public API, NuGet packages, documentation, examples and equivalence tests."]),
            ("Memory-dependence analyzer · C17", ["Normalization, ranges, modular checks, GCD checks and exact affine cases.", "Ranked 1st among 49 submissions; 104/104 tests."]),
        ],
        "skills": "C++23, C17, C#, Python, CMake, Git, Linux, ASan/UBSan, clang-tidy, Lexer/Parser/AST, Bytecode/AIR, IR/SSA, CIL/DynamicMethod",
    },
    "Mikhail_Razakov_Backend_RU.pdf": {
        "lang": "ru",
        "title": "Михаил Разаков",
        "role": ".NET-бэкенд-разработчик",
        "summary": "Разрабатываю VpnMediator и CompilationLabLMS. Работаю с подписками, платежами, ролями, устройствами, PostgreSQL/SQLite, миграциями и фоновым восстановлением операций.",
        "evidence": ["3 проекта: VPN, LMS и клиентский API лицензирования", "Платежи: вебхуки, идемпотентность, возвраты, outbox", "Linux: Docker Compose, nginx, systemd, backup/restore"],
        "experience": [
            ("VpnMediator / Razaltush VPN · 2026-сейчас", ["Подписки, доступы, устройства, Telegram-интерфейс и выдача конфигурации.", "Платежи, outbox, журнал операций, миграции, backup/restore и откат."]),
            ("CompilationLabLMS · 2026-сейчас", ["Роли, группы, занятия, домашние задания, уведомления и чат.", "PostgreSQL, реестр балансов, ЮKassa, вебхуки, возвраты, cookie auth и CSRF."]),
            ("Клиентский API лицензирования · 2023", ["Выпуск и проверка ключей, статусы активации, административные операции.", "OpenAPI/Swagger и модель ошибок."]),
        ],
        "skills": "C#, ASP.NET Core, REST, OpenAPI/Swagger, PostgreSQL, SQLite, миграции, транзакции, outbox, Docker Compose, nginx, systemd, Linux",
    },
    "Mikhail_Razakov_Backend_EN.pdf": {
        "lang": "en",
        "title": "Mikhail Razakov",
        "role": ".NET Backend Developer",
        "summary": "I develop VpnMediator and CompilationLabLMS. My work includes subscriptions, payments, roles, devices, PostgreSQL/SQLite, migrations and background operation recovery.",
        "evidence": ["3 projects: VPN, LMS and client licensing API", "Payments: webhooks, idempotency, refunds and outbox", "Linux: Docker Compose, nginx, systemd and backup/restore"],
        "experience": [
            ("VpnMediator / Razaltush VPN · 2026-present", ["Subscriptions, access rights, devices, Telegram interface and configuration delivery.", "Payments, outbox, operation log, migrations, backup/restore and rollback."]),
            ("CompilationLabLMS · 2026-present", ["Roles, groups, lessons, homework, notifications and chat.", "PostgreSQL, balance ledger, YooKassa, webhooks, refunds, cookie auth and CSRF."]),
            ("Client licensing API · 2023", ["Key issuance and validation, activation states and administrative operations.", "OpenAPI/Swagger and error responses."]),
        ],
        "skills": "C#, ASP.NET Core, REST, OpenAPI/Swagger, PostgreSQL, SQLite, migrations, transactions, outbox, Docker Compose, nginx, systemd, Linux",
    },
    "Mikhail_Razakov_EdTech_RU.pdf": {
        "lang": "ru",
        "title": "Михаил Разаков",
        "role": ".NET-разработчик · EdTech",
        "summary": "С 2021 года преподаю программирование; работал примерно с 50 учениками. В CompilationLabLMS разрабатывал роли, группы, занятия, домашние задания, уведомления и платежи; в Diploma.school исправлял мобильную навигацию и отображение материалов.",
        "evidence": ["Преподавание с 2021 года; около 50 учеников", "CompilationLabLMS: учебные процессы и платежи", "Diploma.school: адаптивный интерфейс и материалы"],
        "experience": [
            ("Преподаватель программирования · 2021-сейчас", ["C/C++, C#, Python, Unity и алгоритмы.", "Диагностика знаний, подбор задач, ревью кода и отладка проектов."]),
            ("CompilationLabLMS · 2026-сейчас", ["Роли, группы, занятия, зачисления, домашние задания, уведомления и чат.", "PostgreSQL, баланс, ЮKassa, вебхуки, возвраты, cookie auth и CSRF."]),
            ("Diploma.school · 2026", ["Мобильная и десктопная навигация, адаптивный интерфейс, PDF-превью и Telegram-интеграции."]),
        ],
        "skills": "C#, ASP.NET Core, PostgreSQL, SQLite, REST, OpenAPI, ЮKassa, Docker Compose, nginx, C/C++, Python, Unity, алгоритмы, ревью кода",
    },
    "Mikhail_Razakov_EdTech_EN.pdf": {
        "lang": "en",
        "title": "Mikhail Razakov",
        "role": ".NET Developer · EdTech",
        "summary": "I have taught programming since 2021 and worked with about 50 students. In CompilationLabLMS, I built roles, groups, lessons, homework, notifications and payments; at Diploma.school, I fixed mobile navigation and learning-material views.",
        "evidence": ["Programming tutor since 2021; about 50 students", "CompilationLabLMS: learning workflows and payments", "Diploma.school: responsive UI and learning materials"],
        "experience": [
            ("Programming tutor · 2021-present", ["C/C++, C#, Python, Unity and algorithms.", "Knowledge assessment, exercise selection, code review and project debugging."]),
            ("CompilationLabLMS · 2026-present", ["Roles, groups, lessons, enrollments, homework, notifications and chat.", "PostgreSQL, balance ledger, YooKassa, webhooks, refunds, cookie auth and CSRF."]),
            ("Diploma.school · 2026", ["Mobile and desktop navigation, responsive UI, PDF previews and Telegram integrations."]),
        ],
        "skills": "C#, ASP.NET Core, PostgreSQL, SQLite, REST, OpenAPI, YooKassa, Docker Compose, nginx, C/C++, Python, Unity, algorithms, code review",
    },
}

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCV", fontName="CV-Bold", fontSize=23, leading=26, textColor=TEXT, spaceAfter=2))
styles.add(ParagraphStyle(name="RoleCV", fontName="CV", fontSize=12.5, leading=15, textColor=ACCENT, spaceAfter=6))
styles.add(ParagraphStyle(name="MetaCV", fontName="CV", fontSize=7.8, leading=10, textColor=MUTED, spaceAfter=3))
styles.add(ParagraphStyle(name="SummaryCV", fontName="CV", fontSize=9.2, leading=12.2, textColor=TEXT, spaceAfter=7))
styles.add(ParagraphStyle(name="SectionCV", fontName="CV-Bold", fontSize=10.5, leading=13, textColor=ACCENT, spaceBefore=5, spaceAfter=4))
styles.add(ParagraphStyle(name="HeadCV", fontName="CV-Bold", fontSize=9.1, leading=11, textColor=TEXT, spaceAfter=1))
styles.add(ParagraphStyle(name="BodyCV", fontName="CV", fontSize=8.1, leading=10.3, textColor=TEXT, leftIndent=8, firstLineIndent=-5, spaceAfter=1.1))
styles.add(ParagraphStyle(name="SmallCV", fontName="CV", fontSize=7.7, leading=9.6, textColor=MUTED))


def build(filename, profile):
    common = COMMON[profile["lang"]]
    doc = SimpleDocTemplate(str(OUT / filename), pagesize=A4, rightMargin=14 * mm, leftMargin=14 * mm, topMargin=12 * mm, bottomMargin=10 * mm, title=profile["title"])
    story = [
        Paragraph(profile["title"], styles["TitleCV"]),
        Paragraph(profile["role"], styles["RoleCV"]),
        Paragraph(common["contact"], styles["MetaCV"]),
        Paragraph(common["status"], styles["MetaCV"]),
        Spacer(1, 4),
        Paragraph(profile["summary"], styles["SummaryCV"]),
    ]
    table = Table([[Paragraph(item, styles["SmallCV"]) for item in profile["evidence"]]], colWidths=[(A4[0] - 28 * mm) / 3] * 3, hAlign="LEFT")
    table.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, BORDER), ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    story.extend([table, Paragraph(common["experience"], styles["SectionCV"])])
    for heading, bullets in profile["experience"]:
        block = [Paragraph(heading, styles["HeadCV"])]
        block.extend(Paragraph("• " + bullet, styles["BodyCV"]) for bullet in bullets)
        story.extend([KeepTogether(block), Spacer(1, 2)])
    story.extend([Paragraph(common["skills"], styles["SectionCV"]), Paragraph(profile["skills"], styles["SmallCV"])])
    doc.build(story)


for output_name, profile in PROFILES.items():
    build(output_name, profile)
