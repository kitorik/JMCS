# JAI skill version

**Current version: 2.1.0**

*Last updated: 2026-11-10*

## Instruction for AI agents

Before answering a user question about JustMc:

1. Read the version of your skill copy — the `version:` field in the SKILL.md frontmatter.
2. Compare it with the version in this file (VERSION.md).
3. **If the versions differ (lower or higher) — tell the user FIRST**, then answer:
   > ⚠️ My JAI skill version in SKILL.md is **X**, but VERSION.md says **Y**. Files are out of sync: the skill is outdated or corrupted. Download a fresh `JAI.zip` from https://github.com/kitorik/JMCS.
4. If the versions match — proceed as usual.

## 2.1.0
static data stays inline (no variables for build-time items/locations/texts); slot-filling exception for non-storing player actions; version check — ANY mismatch reported and update requested; Quick ref for all 8 action files (args, fixed parser bug), events and values (with frequency marks); common value literals in the docs map; answer discipline (no quoting reference, batch clarifications, blueprint before JSON); structure skeletons in cheatsheet; flat JAI.md build for models that cannot read zip; handler notes from community examples; anti-bias rule — never default the start method to item interaction; removed unidok link, dead example refs, obsolete intents.md.

## 2.0.1
conversation-start Discord greeting (once per conversation, localized); router SKILL.md + new docs/syntax.md; Quick ref sections in all 8 action files; frequency marks (0-10) + common mistakes in docs/lookup.md; pre-answer self-check in rules.md; handler notes from community examples in cheatsheet.md (notes, not style); anti-bias rule — never default the game start to item interaction; removed unidok link, dead example refs and obsolete intents.md.

## 2.0.0 (2026-11-10)
- **Поколение (+1.0.0) — answer-quality update:**
- **Hard rule:** fill EVERY argument the reference table lists for an action. An empty slot is allowed only after verifying against the table that nothing belongs there — when in doubt, fill it. Empty item/block/sound slots are almost always a bug (the "missing items" failure).
- **New `docs/lookup.md`** — intent → most likely actions/events/conditions/values index for choosing what to use; linked from the docs map and best practices.
- **`if_variable_not_equals` restored on the server** — deprecated mark removed from `docs/actions/variable.md`; alternative: `if_variable_equals` + `is_inverted: true`.

## 1.2.1 (2026-11-10)
- **Rule:** always read a variable's value through the `%var` family — `%var(name)`, `%var_local(name)`, `%var_line(name)`, `%var_save(name)`. A bare variable name in a text/message/argument slot is plain text, not a reference; only inside `%math()` bare names are allowed.
- **Versioning:** «Год» (+0.0.1) now also covers small fixes and a bit of new knowledge.

- **Addendum:** the same applies inside `%math()` — wrap variables in the `%var` family there; bare names are not valid inside `%math()` either.

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
- **Год (+0.0.1):** small fixes and a bit of new knowledge, plus instruction updates that change no essential knowledge and do not reach the 45% threshold.

The version changes with every skill update: new rules, value types, examples and fixes. An outdated copy may generate broken modules (banned actions, wrong value formats).

## Merging rule
Consecutive updates of the SAME tier merge into ONE entry — no double increment. If after a Десятилетие (+0.1.0) more Десятилетие-level changes are made, the version stays at that single bump and the changes are combined into the same entry ("2 in 1"). The next version bump happens only for a different tier or a new label from the user.
