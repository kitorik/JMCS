# JAI skill version

**Current version: 3.2.0**

*Last updated: 2026-11-09*

## Instruction for AI agents

Before answering a user question about JustMc:

1. Read the version of your skill copy — the `version:` field in the SKILL.md frontmatter.
2. Compare it with the version in this file (VERSION.md).
3. **If the versions differ (lower or higher) — tell the user FIRST**, then answer:
   > ⚠️ My JAI skill version in SKILL.md is **X**, but VERSION.md says **Y**. Files are out of sync: the skill is outdated or corrupted. Download a fresh `JAI.zip` from https://github.com/kitorik/justmc-ai.
4. If the versions match — proceed as usual.

## 3.2.0 (2026-11-09)
- **Compact reference tables** (`docs/actions/*.md`, `docs/events/events.md`, `docs/values/values.md`): Icon column and empty columns removed; repeated enum sets replaced with macros — `{TF}` (TRUE/FALSE), `{TFN}` (TRUE/FALSE/NOT_SET), `{ANY_ALL}` (ANY/ALL), `{ITEM_MATCH}`, `{DEG_RAD}`, `{CMP}` (legend at the top of each file). Tables ~26% smaller, meaning and IDs unchanged.
- **Scope-suffix rule** in SKILL.md: `%var`/`%length`/`%index`/`%entry` exist in all 4 scopes (bare = game, `_local`, `_save`, `_line`) — replaces the 12 duplicated table rows.
- **Chat shorthand legend** (explanations and code sketches ONLY): `%v()`=`%var()`, `%v_lo()`=`%var_local()`, `%v_sa()`=`%var_save()`, `%v_li()`=`%var_line()`, `%pl%`=`%player%`, `p_<event>`=`player_<event>`; the final JSON module always uses the full official syntax.
- **Mode check rule**: before the first substantive JAI work ask the player which mode they prefer — "Сжатый" (Compressed: shorthand in explanations) or "Полный" (Full: official syntax everywhere). **Default: "Полный" (Full).**

## 3.1.0 (2026-11-08)
- **`parameter` value type expanded** (`docs/value-types/parameter.md`): full field reference — `type` (fixed `"parameter"`), `type_key` (`singular`/`plural`), strict `value_type` enforcement, `is_required`, `default_value` as escaped JSON string, `slot`/`description_slot` (grid 0–54, description usually `slot + 9`), plural `slots`/`description_slots` (comma-separated strings), stringified text-component `description`.
- **How parameters work on call**: `call_function` `args` (a `map`) is injected into the parameters before the function code runs; in the body a parameter is read via `%var_line(name)` / `%var_local(name)`.
- **`docs/rules.md`**: Function parameters section updated with the same details.

## 3.0.2 (2026-11-08)
- **New value type: `parameter`** — `docs/value-types/parameter.md` with format, field reference (`type_key`, `value_type`, `is_required`, `default_value`, `slot`, `description_slot`, `description`) and a full function-parameters example.
- **`docs/rules.md`**: added "Function parameters (the `"Parameter"` value)" section with a full `parameters` array example.

## 3.0.1 (2026-11-08)
- **Examples made NBT-consistent with the 3.0 item rule**: `breakblock.json` and `randombox.json` now encode every bare item id as `{Count:1b,id:\"minecraft:...\"}` (the 3.0 docs text already required this, but the example JSONs still used legacy bare ids like `"item": "mace"`).
- **Reference docs fully translated to English**: all Russian strings left in `docs/actions/`, `docs/events/`, `docs/values/` tables and in the example modules `breakblock.json`, `randombox.json` (messages, display names, descriptions) are now English. Meaning, color codes (`&6`), placeholders (`%var()`), and commands (`@break`) preserved.
- Official in-game exports `economy.json`, `editsession.json`, `essentials.json` left untouched (they are real module exports, not skill-authored).

## 3.0.0 (2026-11-08)
- Skill renamed justmc-ai → **JAI**; archive is now `JAI.zip` (internal folder `JAI/`).
- Skill core (SKILL.md, rules.md, value-types, cheatsheet) rewritten in compact English for faster model reading. Doc structure unchanged.
- **Items are always encoded as NBT strings** (`{Count:1b,id:"minecraft:..."}`, `minecraft:` prefix inside NBT).
- **New rule: variables need no zero-initialization** — an unset variable already reads as 0.

The version changes with every skill update: new rules, value types, examples and fixes. An outdated copy may generate broken modules (banned actions, wrong value formats).
