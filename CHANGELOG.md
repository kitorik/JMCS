# Changelog

All notable changes to the JAI skill. The current version lives in `skill/SKILL.md` and `skill/VERSION.md` (kept in sync); full history below and inside `skill/VERSION.md`.

## [1.0.0] — 2026-11-10

### Stable release

- **Version numbering reset to 1.0.0** (stable release version).
- Skill sources synced from [kitorik/JMCS_archive](https://github.com/kitorik/JMCS_archive) — the freshest full copy (includes all 3.1.0–3.2.1 changes below).
- Strict-semver CI machinery removed (`scripts/check_version.py`, `version-check.yml`, `VERSIONING.md`) — the repo is now Markdown-only; GitHub language detection fixed.

## [3.2.1] — 2026-11-10

- Removed the skill-authored examples `breakblock.json` and `randombox.json`; only official in-game exports remain (EditSession, Essentials, Economy).

## [3.2.0] — 2026-11-09

### MINOR (new sources + compact rewrite)

- Compact reference tables (`docs/actions/*.md`, `docs/events/events.md`, `docs/values/values.md`): Icon column and empty columns removed; repeated enum sets replaced with macros — `{TF}`, `{TFN}`, `{ANY_ALL}`, `{ITEM_MATCH}`, `{DEG_RAD}`, `{CMP}`. Tables ~26% smaller, meaning and IDs unchanged.
- Scope-suffix rule in SKILL.md for `%var`/`%length`/`%index`/`%entry`.
- Chat shorthand legend (explanations only; JSON always uses full official syntax).
- Mode check rule: "Сжатый" (Compressed) vs "Полный" (Full), default "Полный".

## [3.1.0] — 2026-11-08

- `parameter` value type expanded (`docs/value-types/parameter.md`): `type_key` (`singular`/`plural`), strict `value_type`, `default_value` as escaped JSON, grid 0–54, `%var_line(name)` access, call-time injection via `args`.
