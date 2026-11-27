#!/usr/bin/env python3
"""Sync JAI skill docs with official JustMc assets (realDosed/justmc-assets, ru_RU).

For every mapped file: download the upstream markdown, insert the "Source" note
after the title, and regenerate the "Quick ref" section. Hand-written relevance
scores like [6/10] are preserved by ID. skill/VERSION.md and skill/SKILL.md are
never touched.
"""
import datetime
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG = "ru_RU"
BASE = f"https://raw.githubusercontent.com/realDosed/justmc-assets/master/documentation/{LANG}"

ACTIONS = ["code", "controller", "entity", "player", "repeat", "select", "variable", "world"]
FILES = {f"actions/{a}.md": f"skill/docs/actions/{a}.md" for a in ACTIONS}
FILES["events.md"] = "skill/docs/events/events.md"
FILES["values.md"] = "skill/docs/values/values.md"

ACTIONS_NOTE = ("> Argument **names and types only**, one line per action/condition — scan this first. "
                "Exact enum values: see the full table row above. ⚠ deprecated = do not use.")
EVENTS_NOTE = ("> Event IDs + slots they provide. Modern items may exist in table but not be listed here — "
               "check the full table. [N/10] = how often this event is relevant.")
VALUES_NOTE = ("> Value IDs — what each returns. [N/10] = how often used. "
               "Full descriptions and types: see the table above.")

SCORE_RE = re.compile(r"^- `([^`]+)` .*?( \[\d+/10\])")


def fetch(path):
    with urllib.request.urlopen(f"{BASE}/{path}", timeout=60) as r:
        return r.read().decode("utf-8")


def rows(md):
    for line in md.splitlines():
        if line.startswith("| ![") or (line.startswith("| ") and not line.startswith("| ---")
                                         and not line.startswith("| Icon")):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 9:
                yield cells


def args_of(cell):
    out = []
    for part in cell.split("<br/>"):
        part = part.strip()
        if not part or part.startswith("&nbsp;"):
            continue
        out.append(part)
    return ", ".join(out) if out else "(no arguments)"


def build(upstream, kind, scores, date_tag):
    lines = upstream.rstrip("\n").split("\n")
    note = (f"> Source: official JustMc assets (documentation/{LANG}) — updated {date_tag}. "
            "Icon column references the original repo icons — ignore the links.")
    body = [lines[0], note] + lines[1:]
    qr = []
    for c in rows(upstream):
        rid, args_cell, status = c[1], c[5], c[8]
        if kind == "actions":
            line = f"- `{rid}` — {args_of(args_cell)}"
        else:
            line = f"- `{rid}` — (no arguments)"
        if status == "deprecated":
            line += " ⚠ deprecated"
        line += scores.get(rid, "")
        qr.append(line)
    header = {"actions": ACTIONS_NOTE, "events": EVENTS_NOTE, "values": VALUES_NOTE}[kind]
    return "\n".join(body) + "\n\n## Quick ref\n" + header + "\n\n" + "\n".join(qr) + "\n"


def main():
    changed = []
    for src, dst in FILES.items():
        dst_path = ROOT / dst
        old = dst_path.read_text(encoding="utf-8") if dst_path.exists() else ""
        m = re.search(r"— updated (\S+)\. Icon", old)
        old_tag = m.group(1) if m else None
        scores = {}
        for l in old.splitlines():
            sm = SCORE_RE.match(l)
            if sm:
                scores[sm.group(1)] = sm.group(2)
        kind = "events" if src == "events.md" else "values" if src == "values.md" else "actions"
        upstream = fetch(src)
        # Keep the old date tag if content is otherwise identical, so no-op runs stay no-op.
        candidate = build(upstream, kind, scores, old_tag or datetime.date.today().strftime("%Y-%m"))
        if candidate != old:
            candidate = build(upstream, kind, scores, datetime.date.today().strftime("%Y-%m"))
            dst_path.write_text(candidate, encoding="utf-8")
            changed.append(dst)
    print("changed:", ", ".join(changed) if changed else "nothing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
