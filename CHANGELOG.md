# Changelog

All notable changes to the JAI skill. The current version lives in `skill/SKILL.md` and `skill/VERSION.md` (kept in sync).

## [1.0.1] — 2026-11-10

### Fixes & rules

- The skill no longer imposes a mini-game start method — the start method is always the player's choice.
- Function parameters surfaced in SKILL.md (docs map + best practices → `parameter` type, rules.md → Function parameters).
- Functions are called ONLY via `call_function`; `start_process` is for processes, never for calling functions.
- Delays: `control_wait` minimum 1 tick, integers only in TICKS mode; high-load CPU-wait pattern (`cpu_usage`) added so the world never enters the critical error caused by sustained 100%+ load.
- Prefer the inline `location` value over the "Create location" action; use the narrowest variable scope (line → local → game → save).

## [1.0.0] — 2026-11-10

### Initial release

Complete starter set: `SKILL.md`, `docs/rules.md`, 8 action references (`docs/actions/`), events, values, 13 value-types (incl. `parameter`), cheatsheet, official example modules (EditSession, Essentials, Economy).

## Versioning scheme

- **Поколение (+1.0.0):** the update improves performance, answer quality, or cuts the cost per request by 45% or more.
- **Десятилетие (+0.1.0):** the skill's knowledge changes — new, removed or updated knowledge about actions, events, values, types.
- **Год (+0.0.1):** instruction updates that change no knowledge and do not reach the 45% threshold.
