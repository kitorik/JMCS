# Changelog

All notable changes to the JAI skill. Format based on [Keep a Changelog](https://keepachangelog.com/); versioning follows [VERSIONING.md](VERSIONING.md) (strict semver: куча данных = MAJOR, новые источники = MINOR, один предмет = PATCH).

## [3.2.0] — 2026-11-09

### MINOR (new sources + compact rewrite)

- Compact reference tables (`docs/actions/*.md`, `docs/events/events.md`, `docs/values/values.md`): Icon column and empty columns removed; repeated enum sets replaced with macros — `{TF}`, `{TFN}`, `{ANY_ALL}`, `{ITEM_MATCH}`, `{DEG_RAD}`, `{CMP}`. Tables ~26% smaller, meaning and IDs unchanged.
- Scope-suffix rule in SKILL.md for `%var`/`%length`/`%index`/`%entry`.
- Chat shorthand legend (explanations only; JSON always uses full official syntax).
- Mode check rule: "Сжатый" (Compressed) vs "Полный" (Full), default "Полный".

*Imported from [kitorik/JMCS_archive](https://github.com/kitorik/JMCS_archive) at 3.2.0 — initial state of the strict-versioning repository.*
