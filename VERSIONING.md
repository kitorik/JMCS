# Versioning policy (strict semver)

JAI follows **strict semantic versioning** `MAJOR.MINOR.PATCH` with hard rules on which change bumps which digit. CI enforces them (see `scripts/check_version.py` and `.github/workflows/version-check.yml`).

## Bump rules

| Change | Bump | Example |
|--------|------|---------|
| **Куча новых данных / mass changes** — bulk additions or rewrites of reference tables (≥ 50 changed table rows), re-structuring of docs, breaking changes to formats, rules or JSON syntax | **+1.0.0** (MAJOR) | full re-generation of `docs/actions/*.md`; change of the item NBT format |
| **Новые источники (new sources)** — a new documentation file, value type, example module, rules section, or a new category of actions/values/events | **+0.1.0** (MINOR) | new `docs/value-types/xyz.md`; new `docs/examples/foo.json` |
| **Один предмет (one item)** — a single added/changed/fixed entry (one action, value, event row), typo fixes, formatting fixes | **+0.0.1** (PATCH) | fix one action description; add one game value |

## Hard requirements (CI fails otherwise)

1. `version:` in `skill/SKILL.md` frontmatter **must equal** the version in `skill/VERSION.md`.
2. Versions must be valid semver (`X.Y.Z`, no pre-release/build suffixes).
3. Any change under `skill/**` **must bump the version** versus the latest `vX.Y.Z` tag — no unchanged-version pushes.
4. The bump level **must match the change size** (row-count and new-file heuristics in `scripts/check_version.py`).
5. `CHANGELOG.md` **must have an entry** for the new version, with the bump level and a change summary.
6. Tags are `vX.Y.Z`, created after CI passes.

## Workflow

1. Make changes under `skill/`.
2. Bump `version:` in `skill/SKILL.md` and the current version in `skill/VERSION.md` (keep them equal), add a dated entry to `skill/VERSION.md`.
3. Add the version to `CHANGELOG.md`.
4. Push — CI validates everything above, `build-zip.yml` rebuilds `JAI.zip`.
5. After CI passes, tag `vX.Y.Z` (optionally via a GitHub Release).
