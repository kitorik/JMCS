# Changelog

All notable changes to the JAI skill. The current version lives in `skill/SKILL.md` and `skill/VERSION.md` (kept in sync).

## [2.1.1] — 2026-11-27 · Год
- SKILL.md почищен: из frontmatter-description убраны мёртвые примеры (EditSession/Essentials/Economy — в docs/examples только cheatsheet.md)
- Удалены дубли: буллет про start method (дубль hard rule 8), абзац про серверные лимиты (живёт в rules.md), буллет «Cheatsheet first» (дубль docs map)
- Удалена устаревшая заметка о формате таблиц (описывала ДО-ресинхронный формат)
- Best practices сжаты с 12 до 7 (убраны общие/дублирующие пункты)
- История версий в SKILL.md сокращена до последних записей (полная — в VERSION.md/CHANGELOG.md); старые 1.x перенесены в свёрнутый блок VERSION.md
- Новые строки: ~13.4k → ~8.9k символов (−33%)

## [2.1.0] — 2026-11-10 · Десятилетие
- Статичные данные — inline-литералы, не переменные (предметы/локации/тексты, известные при сборке)
- Исключение в правиле слотов для «ненакопительных» действий (сообщения, звуки, частицы — рассуждать по слоту)
- Проверка версии: любая несостыковка (выше/ниже) → сообщить и просить обновить
- Quick ref во всех 8 файлах действий (починен парсер: аргументы теперь видны), в events.md и values.md (+ метки частоты 0–10)
- Частые литералы типов прямо в docs map SKILL.md
- Дисциплина ответа: не цитировать справочник, вопросы — одним пакетом, чертёж перед JSON
- Скелеты структур в cheatsheet
- Плоский JAI.md для моделей, не читающих zip
- Заметки из комьюнити-хендлеров (заметки, не стиль)
- Анти-биас: никогда не начинать мини-игру через взаимодействие по умолчанию
- Чистка: unidok, мёртвые ссылки на примеры, intents.md
- Правило слияния: однотипные последовательные обновления объединяются в одну запись без двойного бампа
- Полная ресинхронизация всех 10 справочных файлов с обновлёнными ассетами (2026-11), пересобранные quick refs, настоящий JSON-пример хендлера, пункт самопроверки на валидность JSON, секция анти-паттернов

[2.0.1] — 2026-11-10 · Год
- Приветствие Discord в начале первого ответа (один раз за диалог, с локализацией) — https://discord.gg/6EGQyeN86y
- SKILL.md → роутер; плейсхолдеры и %math() → новый docs/syntax.md
- Quick ref (компактные аргументы) во всех 8 файлах действий
- Метки частоты 0–10 и частые ошибки в docs/lookup.md
- Pre-answer self-check в rules.md
- Заметки из комьюнити-хендлеров в cheatsheet.md (заметки, не стиль)
- Анти-биас: никогда не начинать мини-игру через взаимодействие по умолчанию
- Удалены: ссылка на unidok, мёртвые ссылки на примеры, устаревший intents.md

[2.0.0] — 2026-11-10

### Поколение — answer-quality update

- Hard rule: fill every action argument from the reference table; an empty slot only after verifying against the table (empty item/block/sound slots are almost always a bug — "missing items").
- New docs/lookup.md: intent → most likely actions/events/conditions/values, then confirm exact arguments in the tables.
- if_variable_not_equals restored on the server — deprecated mark removed; alternative if_variable_equals + is_inverted: true.

## [1.2.1] — 2026-11-10
- Always read variable values via the %var family (%var, %var_local, %var_line, %var_save) — bare names are plain text, also inside %math().
- Versioning: «Год» (+0.0.1) also covers small fixes and minor new knowledge.

## [1.2.0] — 2026-11-10
- %math(): raw variable names auto-resolve scope; disambiguate with %var_line()/%var_local()/%var_save(); no %var_game() exists.
- Trailing else after independent if-s fires when only the last fails — never a fallback.
- Mid-air jump key: poll input (if_player_has_input JUMP / player_input_event).

## [1.1.0] — 2026-11-10
- Default build location: world spawn (spawn_location, selection "null") with Y − 1 when no coordinates given.

## [1.0.3] — 2026-11-10
- No zero-initialization/declaration; clear via set_variable_remove / set_variable_purge; game start via if_variable_exists.

## [1.0.2] — 2026-11-10
- Added missing docs/value-types/parameter.md; cheatsheet dead references removed.

## [1.0.1] — 2026-11-10
- No imposed start method; function parameters surfaced; call_function only; delays rule + cpu_usage pattern; inline location preference; narrowest scope.

## [1.0.0] — 2026-11-10
- Initial release: SKILL.md, docs/rules.md, 8 action references, events, values, 13 value-types, cheatsheet, example modules.

## Versioning scheme

- **Поколение (+1.0.0):** the update improves performance, answer quality, or cuts the cost per request by 45% or more.
- **Десятилетие (+0.1.0):** the skill's knowledge changes — new, removed or updated knowledge about actions, events, values, types.
- **Год (+0.0.1):** small fixes and a bit of new knowledge, plus instruction updates that change no essential knowledge and do not reach the 45% threshold.
