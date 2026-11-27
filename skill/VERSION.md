# JAI skill version

**Current version: 2.1.1**

*Last updated: 2026-11-27*

## Instruction for AI agents

Before answering a user question about JustMc:

1. Read the version of your skill copy — the `version:` field in the SKILL.md frontmatter.
2. Compare it with the version in this file (VERSION.md).
3. **If the versions differ (lower or higher) — tell the user FIRST**, then answer:
   > ⚠️ My JAI skill version in SKILL.md is **X**, but VERSION.md says **Y**. Files are out of sync: the skill is outdated or corrupted. Download a fresh `JAI.zip` from https://github.com/kitorik/JMCS.
4. If the versions match — proceed as usual.

## 2.1.1
Год: SKILL.md slimmed — removed dead example names, duplicated bullets, stale notes, redundant best-practice items; removed the mode system (Сжатый/Полный) — one full-syntax answer style; removed negative "how-not-to" guidance in favor of positive rules (anti-memorization section, anti-patterns section and self-check item 12, Skip column, negative cheatsheet warnings); versions history shortened in SKILL.md (full history stays here and in CHANGELOG.md).

## 2.1.0
static data stays inline (no variables for build-time items/locations/texts); slot-filling exception for non-storing player actions; version check — ANY mismatch reported and update requested; Quick ref for all 8 action files (args, fixed parser bug), events and values (with frequency marks); common value literals in the docs map; answer discipline (no quoting reference, batch clarifications, blueprint before JSON); structure skeletons in cheatsheet; flat JAI.md build for models that cannot read zip; handler notes from community examples; anti-bias rule — never default the start method to item interaction; removed unidok link, dead example refs, obsolete intents.md. FULL RESYNC of all 10 reference docs with the updated official assets (2026-11 format), rebuilt quick refs, real JSON handler example, JSON-validity self-check item, anti-patterns section.

## 2.0.1
conversation-start Discord greeting (once per conversation, localized); router SKILL.md + new docs/syntax.md; Quick ref sections in all 8 action files; frequency marks (0-10) + common mistakes in docs/lookup.md; pre-answer self-check in rules.md; handler notes from community examples in cheatsheet.md (notes, not style); anti-bias rule — never default the game start to item interaction; removed unidok link, dead example refs and obsolete intents.md.

## 2.0.0 (2026-11-10)
- **Поколение (+1.0.0) — answer-quality update:**
- **Hard rule:** fill EVERY argument the reference table lists for an action. An empty slot is allowed only after verifying against the table — when in doubt, fill it. Empty item/block/sound slots are almost always a bug (the "missing items" failure).
- **New `docs/lookup.md`** — intent → most likely actions/events/conditions/values index.
- **`if_variable_not_equals` restored on the server** — deprecated mark removed; alternative: `if_variable_equals` + `is_inverted: true`.

## Versioning scheme
- **Поколение (+1.0.0):** only when the update improves performance, answer quality, or cuts the cost per request by 45% or more.
- **Десятилетие (+0.1.0):** when the skill's knowledge changes — new, removed or updated knowledge about actions, events, values, types.
- **Год (+0.0.1):** small fixes and a bit of new knowledge, plus instruction updates that change no essential knowledge and do not reach the 45% threshold.

## Merging rule
Consecutive updates of the SAME tier merge into ONE entry — no double increment. The next version bump happens only for a different tier or a new label from the user.

<details>
<summary>Older versions (1.x)</summary>

## 1.2.1 (2026-11-10)
- **Rule:** always read a variable's value through the %var family — %var(name), %var_local(name), %var_line(name), %var_save(name). A bare variable name in a slot is plain text; the same applies inside %math().
- **Versioning:** «Год» (+0.0.1) now also covers small fixes and a bit of new knowledge.

## 1.2.0 (2026-11-10)
- %math(): raw variable names auto-resolve scope (line → local → game → save); disambiguate with %var_line()/%var_local()/%var_save(); there is no %var_game() — game scope is bare %var().
- Trailing else after a chain of independent if-s fires whenever only the LAST if fails — never a fallback.
- Mid-air jump key: poll input (if_player_has_input JUMP / player_input_event) — player_jump is not guaranteed while airborne.

## 1.1.0 (2026-11-10)
- Default build location: world spawn (spawn_location game value, selection "null") with Y lowered by 1 when the player gave no coordinates.

## 1.0.3 (2026-11-10)
- Never zero-initialize or "declare" variables; clear via set_variable_remove / set_variable_purge; check game start with if_variable_exists.

## 1.0.2 (2026-11-10)
- Added the missing docs/value-types/parameter.md; cheatsheet: removed dead references (breakblock.json / randombox.json) and the imposed start method.

## 1.0.1 (2026-11-10)
- No imposed mini-game start method; function parameters surfaced in SKILL.md; call_function only; delays rule (min 1 tick, integers TICKS, cpu_usage pattern); prefer inline location; narrowest scope.

## 1.0.0 (2026-11-10)
- Initial release — complete starter set.

</details>
