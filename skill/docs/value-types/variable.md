# Value type: variable

A reference to a variable. Not a value but a pointer: the action will read/write the variable with this name.

## Format
```json
{ "type": "variable", "variable": "bb.score", "scope": "game" }
```
- `scope`: `line` (current line-flow) | `local` (function call) | `game` (world) | `save` (persistent).

## Examples
```json
{ "type": "variable", "variable": "bb.token", "scope": "game" }
{ "type": "variable", "variable": "%player%_balance", "scope": "save" }
{ "type": "variable", "variable": "bb.g%var_local(gid).locs", "scope": "game" }
```

## Rules
- Variable names may contain placeholders (`%player%_balance`, `bb.g%var_local(gid).locs`).
- A variable without a value in a source slot → 0 (breaks location/list slots).
- A nonexistent save variable reads as 0 — check `if_variable_exists` before reading.
