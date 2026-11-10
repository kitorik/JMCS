# JAI skill version

**Current version: 1.2.0**

*Last updated: 2026-11-10*

## Instruction for AI agents

Before answering a user question about JustMc:

1. Read the version of your skill copy — the `version:` field in the SKILL.md frontmatter.
2. Compare it with the version in this file (VERSION.md).
3. **If the versions differ (lower or higher) — tell the user FIRST**, then answer:
   > ⚠️ My JAI skill version in SKILL.md is **X**, but VERSION.md says **Y**. Files are out of sync: the skill is outdated or corrupted. Download a fresh `JAI.zip` from https://github.com/kitorik/JMCS.
4. If the versions match — proceed as usual.

## 1.2.0 (2026-11-10)
- **New knowledge (rules.md, SKILL.md):** raw variable names in `%math()` auto-resolve the scope (line → local → game → save); same-name variables are disambiguated with `%var_line()` / `%var_local()` / `%var_save()` placeholders; there is **no `%var_game()`** — game scope is the bare `%var()`.
- **Rule (rules.md → Key patterns):** a trailing `else` after a chain of independent `if`s fires whenever only the LAST `if` fails — never use it as a "fallback / unknown case".
- **New pattern:** to catch the jump key mid-air (double jump), poll input (`if_player_has_input` JUMP / `player_input_event`) — `player_jump` is not guaranteed to fire while airborne.

## 1.1.0 (2026-11-10)
- **New rule (rules.md → Default build location):** if the player did not give coordinates where to build the map, build by default at the world spawn — the point where players spawn. Use the `spawn_location` game value (`selection: "null"`) and lower the Y coordinate by 1, so the build sits on the ground under the spawn point.

## 1.0.3 (2026-11-10)
- **New rules for AI agents (rules.md → Variables):**
  - Never create variables with a zero value or "declare" them: an unset variable already reads as 0.
  - To clear a variable use one of the two "Clear variables" actions: `set_variable_remove` (variable in the `variables` slot) or `set_variable_purge` (variable name as text + scope + match).
  - To check game start, check variable existence with `if_variable_exists` instead of creating marker variables.

## 1.0.2 (2026-11-10)
- **Added the missing `docs/value-types/parameter.md`** — 1.0.0/1.0.1 claimed 13 value-types including `parameter`, but the reference file did not exist.
- **Cheatsheet fixed:** removed dead references to `breakblock.json` / `randombox.json` (deleted in 1.0.0) and removed the imposed start method, per the 1.0.1 rule.

## 1.0.1 (2026-11-10)
- **Fixed:** the skill no longer imposes a mini-game start method (was: "start via interaction/items") — the start method is always the player's choice.
- **Fixed:** function parameters surfaced in SKILL.md (docs map + best practices → `docs/value-types/parameter.md`, `docs/rules.md` → Function parameters).
- **Rule:** functions are called ONLY via `call_function`; `start_process` is for processes — never for calling functions.
- **Rule:** delays — `control_wait` minimum 1 tick, integers only in TICKS mode; high-load CPU-wait pattern added (rules.md → Delays and world load) so the world never enters the critical error caused by sustained 100%+ load.
- **Rule:** prefer the inline `location` value over the "Create location" action; use the narrowest variable scope (line → local → game → save), not only `game`.

## 1.0.0 (2026-11-10)
- **Initial release — complete starter set:** SKILL.md, `docs/rules.md`, 8 action references, events, values, 13 value-types (incl. `parameter`), cheatsheet, official examples (EditSession, Essentials, Economy).

## Versioning scheme
- **Поколение (+1.0.0):** only when the update improves performance, answer quality, or cuts the cost per request by 45% or more.
- **Десятилетие (+0.1.0):** when the skill's knowledge changes — new, removed or updated knowledge about actions, events, values, types.
- **Год (+0.0.1):** instruction updates that change no knowledge and do not reach the 45% threshold.

The version changes with every skill update: new rules, value types, examples and fixes. An outdated copy may generate broken modules (banned actions, wrong value formats).
