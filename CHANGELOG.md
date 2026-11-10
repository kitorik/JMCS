# Changelog

All notable changes to the JAI skill. The current version lives in `skill/SKILL.md` and `skill/VERSION.md` (kept in sync).

## [1.2.0] — 2026-11-10

### New knowledge & rules

- %math(): raw variable names auto-resolve scope (line → local → game → save); disambiguate same names with `%var_line()` / `%var_local()` / `%var_save()`; there is no `%var_game()` — game scope is the bare `%var()`.
- A trailing `else` after a chain of independent `if`s fires whenever only the last `if` fails — never use it as a fallback.
- Mid-air jump key: poll input (`if_player_has_input` JUMP / `player_input_event`); `player_jump` is not guaranteed to fire while airborne.

## [1.1.0] — 2026-11-10

### New knowledge

- Default build location: when the player gives no coordinates, build at the world spawn (`spawn_location` game value, `selection: "null"`) with Y lowered by 1.

## [1.0.3] — 2026-11-10

### New rules (variables)

- Never zero-initialize or "declare" variables: an unset variable already reads as 0.
- Clear variables only via the two "Clear variables" actions: `set_variable_remove` (takes the variable) or `set_variable_purge` (takes the name as text, plus scope and match).
- Check game start via variable existence (`if_variable_exists`), not by pre-created marker variables.

## [1.0.2] — 2026-11-10

### Fixes

- Added the missing `docs/value-types/parameter.md` (the `parameter` value type was documented only inside rules.md).
- Cheatsheet: removed dead references to `breakblock.json` / `randombox.json`, removed the imposed mini-game start method (per 1.0.1 rule).

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
