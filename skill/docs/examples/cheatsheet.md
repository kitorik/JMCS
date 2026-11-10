# 📋 JustMc Creative+ cheatsheet (JSON modules)

Quick reference: value formats, common errors, ready patterns. Full per-type docs in `docs/value-types/` (file = type ID).

## Value formats

| Type | JSON format | Example |
|-----|-------------|--------|
| text | `{"type":"text","text":"...","parsing":"plain\|legacy"}` | `{"type":"text","text":"Hi, %player%!","parsing":"legacy"}` |
| number | `{"type":"number","number":...}` — plain number, `%math(...)` string, or variable ref | `{"type":"number","number":"%math(%var(x)*100/%var(max))"}` |
| variable | `{"type":"variable","variable":"name","scope":"line\|local\|game\|save"}` | `{"type":"variable","variable":"bb.t","scope":"game"}` |
| item | `{"type":"item","item":"{Count:1b,id:\"minecraft:mace\"}"}` — **always an NBT string** (`minecraft:` inside NBT); `block` slots take item too! | `{"type":"item","item":"{Count:1b,id:\"minecraft:iron_block\"}"}` |
| vector | `{"type":"vector","x":0,"y":1,"z":0}` | `{"type":"vector","x":2,"y":2,"z":2}` |
| enum | `{"type":"enum","enum":"VALUE"}` | `{"type":"enum","enum":"SPACES"}` |
| array | `{"type":"array","values":[...]}` | `{"type":"array","values":[{"type":"variable","variable":"x","scope":"game"}]}` |
| map | `{"type":"map","values":{}}` — function/process args | `{"type":"map","values":{}}` |
| location | `{"type":"location","x":0,"y":64,"z":0,"yaw":0,"pitch":0}` — prefer over "Create location" action | `{"type":"location","x":128,"y":70,"z":-200,"yaw":0,"pitch":0}` |
| game_value | `{"type":"game_value","game_value":"...","selection":"..."}` | `{"type":"game_value","game_value":"spawn_location","selection":"null"}` |

## Key rules (short)

- Any value that finds no content (missing variable/key) **returns 0** — create lists/maps before first use, check `if_variable_map_has_key`. **Don't zero-initialize variables: unset already reads as 0.**
- `else` **only** on the closing bracket of an invertible condition, never as a standalone action.
- Boss bar: `progress` is a **0–100** scale.
- `controller_async_run` does **not exist** on the server. Parallel line = handler `"type":"process"` + `start_process`.
- The `block` slot in `game_set_block` etc. takes an **item** value (NBT string).
- Static coordinates → `type: location` literal in the slot, not "Create location" + variable.
- Line budget: ≤67 (a condition = 2 actions), ≤33 conditions; loop >10 iterations → `control_wait` ≥1 tick.
- **≤300 iterations without a wait per run** — beyond that, critical error + full world freeze. `game_set_region` sets up to 125,000 blocks per call.
- Placeholders WITHOUT closing `%` (`%var(x)`, `%math(...)`, `%entry(m,k)`); system values WITH `%` (`%player%`, `%random_uuid%`).
- Selections are not inherited by functions: rebuild inside the function with a creation action (`select_entity_by_name` etc.), then `select_add_*`.

## Common errors

| Error | Cause | Fix |
|--------|---------|------|
| "expected Location, got Number" | nonexistent variable → 0 in a location slot | create/check the variable before the action |
| `else` won't insert | `else` placed after a plain action | place right after the condition's closing bracket |
| Action "not found" on import | `controller_async_run` doesn't exist | use a process + `start_process` |
| Boss bar always full/empty | progress as 0–1 fraction | rescale to 0–100 |
| Block not placed by game_set_block | text passed to the block slot | pass an item value (NBT) or item-variable |
| Lags/crash in a loop | no `control_wait` in a long loop | add wait ≥1 tick |
| Nothing happens to an entity | `select_add` into a nonexistent selection | create the selection first |

## Ready patterns

### 1. Timer with boss bar (process)
The BB.timer process runs in parallel; a token guards against stale timers:
```json
{ "action": "start_process", "values": [ { "name": "process_name", "value": { "type": "text", "text": "BB.timer", "parsing": "plain" } }, { "name": "target_mode", "value": { "type": "enum", "enum": "NO_TARGET" } }, { "name": "local_variables_mode", "value": { "type": "enum", "enum": "DONT_COPY" } }, { "name": "args", "value": { "type": "map", "values": {} } } ] }
```
Inside the process: save `tok = token`, loop `repeat_while (t >= 0)` with `control_wait` 20 ticks; if `token != tok` → `control_end_thread`; boss bar `progress = %math(%var(t)*100/%var(maxt))`.

### 2. Stale-thread invalidation (token)
Before every thread/process start: `token = token + 1`; inside the thread save `ttok = token`; in the loop `if_variable_equals [token] vs ttok, is_inverted=true` → `control_end_thread`.

### 3. Leaderboard (map + save)
`bb.score` — map (player → points): `set_variable_map_put` on change; top via `repeat_for_each_map_entry` + `player_send_message`. Balances — save-vars `%player%_balance`.

### 4. Axe zone selection
`player_interact` + `event_interaction` (`left_click_block`/`right_click_block`) + `if_game_event_item_equals` (TYPE_ONLY, wooden axe) → points `p1`/`p2` into game vars, cancel the event (`cancel_event`).

### 5. Chat command
`player_chat` + `if_player_chat_message_equals` (ignore_case TRUE) → `cancel_event` → `call_function`. Prefix `@` or `\`.
> ⚠️ Chat commands are for admin commands and syntax demos. **Start mini-games via interaction** (item RMB with `if_game_event_item_equals`, plate, menu), see randombox.json.

### 6. Block coordinates (corners)
JustMc gives coordinates from the block CENTER; a display spawns from the corner: `cl = center − 0.5` per axis (`set_variable_get_all_coordinates` → `set_variable_set_all_coordinates` with `%math(x-0.5)`).

### 7. Unique entity names
`fb_%random_uuid%` — base name; add construction-part suffixes. Never name two entities the same.

### 8. Random pick
`rnd = %math(floor(random*10))` + an `if_variable_less` / else chain. Or `repeat_on_grid` with a random point inside p1..p2 (see breakblock.json).
