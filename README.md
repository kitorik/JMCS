# JAI (JustMc AI)

A skill for AI agents that helps them understand coding on the **JustMc** Minecraft server (Creative+ mini-game).

## How to use

**Download one file — `JAI.zip`** — and hand it to your AI agent (unpack into its skills folder). That's it.

- Archive contents: `JAI/SKILL.md`, `JAI/VERSION.md` and `JAI/docs/`
- Before answering, the agent compares the version in `VERSION.md` with the `version:` field in the `SKILL.md` frontmatter and warns the user if they are out of sync

## Repository structure

- `JAI.zip` — ready-made skill archive (built automatically)
- `skill/` — skill sources (SKILL.md, VERSION.md, docs/)
- `.github/workflows/build-zip.yml` — GitHub Action: rebuilds `JAI.zip` on every change to `skill/**`

> ⚠️ Examples in the skill show syntax, not design: chat commands there are demos; start mini-games via interaction events.

## v1.0.0 (2026-11-10)

- **Version numbering reset to 1.0.0** (stable release).
- Synced with the skill sources: compact reference tables, `parameter` value type, chat shorthand legend, mode check ("Сжатый"/"Полный", default "Полный").
- Strict-semver CI machinery removed (repo is now Markdown-only).

<details><summary>History: v3.0.0 (2026-11-08)</summary>

</details>

- Skill renamed **justmc-ai → JAI**; the archive is now `JAI.zip` (internal folder `JAI/`).
- Skill core rewritten in compact English for faster model reading (doc structure unchanged).
- **Items are always encoded as NBT strings** (`{Count:1b,id:"minecraft:..."}`).
- **New rule: variables need no zero-initialization** — an unset variable already reads as 0.
