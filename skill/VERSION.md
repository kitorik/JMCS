# JAI skill version

**Current version: 1.0.0**

*Last updated: 2026-11-10*

## Instruction for AI agents

Before answering a user question about JustMc:

1. Read the version of your skill copy — the `version:` field in the SKILL.md frontmatter.
2. Compare it with the version in this file (VERSION.md).
3. **If the versions differ (lower or higher) — tell the user FIRST**, then answer:
   > ⚠️ My JAI skill version in SKILL.md is **X**, but VERSION.md says **Y**. Files are out of sync: the skill is outdated or corrupted. Download a fresh `JAI.zip` from https://github.com/kitorik/JMCS.
4. If the versions match — proceed as usual.

## 1.0.0 (2026-11-10)
- **Initial release — complete starter set:**
  - `SKILL.md` — placeholders, %math() expressions, docs map, version check, mode check ("Сжатый"/"Полный", default "Полный"), chat shorthand legend (explanations only).
  - `docs/rules.md` — module rules, line limits, critical server limits.
  - `docs/actions/` (8 files), `docs/events/events.md`, `docs/values/values.md` — full reference tables with enum macros (`{TF}`, `{ITEM_MATCH}`, …).
  - `docs/value-types/` — 13 types including `parameter`.
  - `docs/examples/` — official in-game exports (EditSession, Essentials, Economy) + cheatsheet.

The version changes with every skill update: new rules, value types, examples and fixes. An outdated copy may generate broken modules (banned actions, wrong value formats).
