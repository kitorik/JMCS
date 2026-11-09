#!/usr/bin/env python3
"""Strict semver checker for JAI (JMCS).

Rules (see VERSIONING.md):
  - SKILL.md frontmatter version == VERSION.md current version
  - valid semver only (X.Y.Z)
  - version must increase vs the previous tag
  - bump level must match the change size:
      >= 50 changed table rows  -> MAJOR (+1.0.0)
      any new file / new section -> at least MINOR (+0.1.0)
      <= 5 changed rows         -> PATCH (+0.0.1) allowed
  - CHANGELOG.md must contain an entry for the new version
"""
import os, re, subprocess, sys

TAG = os.environ.get("PREV_VERSION", "")

def fail(msg):
    print("::error::" + msg)
    sys.exit(1)

def semver(v):
    return re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", v or "")

def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True).stdout

def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""

skill = read("skill/SKILL.md")
m = re.search(r"^version:\s*(\S+)\s*$", skill, re.M)
v_skill = m.group(1) if m else None
vfile = read("skill/VERSION.md")
m = re.search(r"Current version:\s*\*\*?([0-9.]+)", vfile) or re.search(r"Current version:\s*([0-9.]+)", vfile)
v_ver = m.group(1) if m else None
if not (semver(v_skill) and semver(v_ver)):
    fail(f"versions must be strict semver X.Y.Z (SKILL.md={v_skill!r}, VERSION.md={v_ver!r})")
if v_skill != v_ver:
    fail(f"SKILL.md ({v_skill}) and VERSION.md ({v_ver}) versions differ")

if TAG:
    if not semver(TAG):
        fail(f"PREV_VERSION invalid: {TAG!r}")
    a = tuple(map(int, v_skill.split(".")))
    b = tuple(map(int, TAG.split(".")))
    if a <= b:
        fail(f"version {v_skill} must be higher than previous {TAG}")

added_rows = removed_rows = new_files = changed = 0
diff = git("diff", "-U0", "HEAD~1", "--", "skill/")
for line in diff.splitlines():
    if line.startswith("+") and not line.startswith("+++"):
        if line.lstrip("+").lstrip().startswith("|"):
            added_rows += 1
        changed += 1
    elif line.startswith("-") and not line.startswith("---"):
        if line.lstrip("-").lstrip().startswith("|"):
            removed_rows += 1
        changed += 1
names = git("diff", "--name-status", "HEAD~1", "--", "skill/")
for n in names.splitlines():
    if n.startswith("A"):
        new_files += 1

if changed == 0:
    print("No skill changes detected; version check passed trivially.")
    sys.exit(0)

ma, mi, pa = map(int, v_skill.split("."))
prev = tuple(map(int, TAG.split("."))) if TAG and semver(TAG) else (ma, mi, max(pa - 1, 0))
row_delta = added_rows + removed_rows
print(f"changed lines={changed}, table rows={row_delta}, new files={new_files}")

if row_delta >= 50 or changed >= 500:
    if ma <= prev[0]:
        fail(f"mass change ({row_delta} rows / {changed} lines) requires a MAJOR bump (+1.0.0); version is {v_skill}")
    print("MAJOR bump OK")
elif new_files > 0:
    if (ma, mi, 0) <= (prev[0], prev[1], 0):
        fail(f"new sources ({new_files} new files) require a MINOR bump (+0.1.0); version is {v_skill}")
    print("MINOR bump OK")
else:
    if row_delta > 5 and (ma, mi, 0) == (prev[0], prev[1], 0):
        print(f"::warning::{row_delta} changed rows with only a PATCH bump - consider MINOR")
    print("PATCH bump OK")

if ("## [" + v_skill + "]") not in read("CHANGELOG.md"):
    fail(f"CHANGELOG.md has no '## [{v_skill}]' entry")

print(f"Strict version check passed for {v_skill}")