# Language review — v16

## Общий результат

Проверены 13 HTML-файлов: 6 русских CV, 6 английских CV и стартовая страница.

- Заголовки профиля сформулированы профессионально, без слова «начинающий» и без искусственного завышения уровня.
- В русских версиях переведены обычные слова и описательные конструкции; сохранены точные названия технологий, API и устойчивые термины.
- Неудачная формулировка «Разработка и эксплуатация сервисов с состоянием» заменена на профессиональное «Разработка и сопровождение продуктовых .NET-систем».
- Записи опыта используют активные, проверяемые формулировки: «спроектировал», «реализовал», «поддерживал», «разбирал», «документировал».
- Английские версии избегают буквальных русских калек и используют `ownership`, `post-launch support`, `recovery paths`, `client delivery` только там, где они подтверждены содержанием.
- Формулировки об образовании синхронизированы: «официально зачислен» / `officially admitted`, без преждевременного `student` до начала обучения.
- Bash отсутствует во всём HTML и PDF.

## Пофайловый статус

| Файл | Статус | Основной результат |
|---|---|---|
| `ru-backend.html` | PASS | Опыт продукта, клиента, стажировки и поддержки показан отдельно и конкретно. |
| `ru-compiler.html` | PASS | Compiler-профиль дополнен production backend и преподаванием без размывания специализации. |
| `ru-platform.html` | PASS | Естественное позиционирование в надёжности приложений, без неподтверждённого SRE/cloud-опыта. |
| `ru-devtools.html` | PASS | Инструменты описаны через интерфейс, диагностику, тесты и сопровождение. |
| `ru-edtech.html` | PASS | Преподавание и разработка LMS соединены с более широкой инженерной практикой. |
| `ru-master.html` | PASS | Полная история опыта читается как единая траектория. |
| `en-backend.html` | PASS | Natural backend positioning with explicit delivery formats and no self-lowering title. |
| `en-compiler.html` | PASS | Idiomatic compiler/runtime language with credible cross-domain experience. |
| `en-platform.html` | PASS | Reliability and operations wording matches application-level experience. |
| `en-devtools.html` | PASS | Developer workflow, diagnostics and maintenance are concrete. |
| `en-edtech.html` | PASS | Teaching and engineering experience reinforce each other without inflated claims. |
| `en-master.html` | PASS | Consistent terminology and chronology. |
| `index.html` | PASS | Selector descriptions foreground experience rather than technology lists only. |

`EVIDENCE_STATUS: VERIFIED` for visible text in the delivered files.
