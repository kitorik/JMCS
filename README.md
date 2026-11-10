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

Initial release of the JAI skill: SKILL.md, VERSION.md, full reference docs (actions, events, values, 13 value-types incl. `parameter`), rules, cheatsheet and official example modules (EditSession, Essentials, Economy).

---

## Плоский читаемый формат — JAI.md

Если инструмент или модель не может распаковать `JAI.zip`, используйте **`JAI.md`** в корне репозитория: все файлы навыка слиты в один текстовый файл (сборка автоматическая, тем же воркфлоу).

- Читать на GitHub: https://github.com/kitorik/JMCS/blob/main/JAI.md
- Raw: https://raw.githubusercontent.com/kitorik/JMCS/main/JAI.md
