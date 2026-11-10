# JAI — JustMc module rules (summary)

Mandatory rules for building JustMc Creative+ JSON modules. Server version: **26.2 (Paper)**. Use together with the action/value/event references.

## Selections & entities
- **Selections are NOT inherited by functions**: each function builds its own (`select_reset` / a creation action + `select_add_*` inside the function). Never rely on the event's or calling line's selection.
- **`select_add_*` only works on an existing selection**: create it first with a creation action (`select_reset`, `select_entity_by_name`, `select_last_entity`, `select_all_entities`, `select_all_players`, `select_all_mobs`, ...).
- **Entities do NOT include players.** Use the player/mob variants (`select_all_players`/`select_all_mobs`, `select_player_by_name`/`select_mob_by_name`, `select_add_all_players`/`select_add_all_mobs`); never `select_*_entity_*` for players, and vice versa.
- **Entity names must be unique.** If an entity is addressed by name, all names in the construction (armor stand, shulker, display) must be unique — e.g. base `fb_<uuid>` with suffixes `_st`/`_sh`/`_dp`.

## Code shortening
- Shorten code when it doesn't hurt the result: for several entities use a creation action for the first (`select_entity_by_name`) and minimal `select_add_*` for the rest.
- Don't put `select_reset` before actions that **create a selection themselves** (`select_last_entity`, `select_entity_by_name`, `select_all_*`) — that's wasted actions.

## Display entities
- Displays spawn **from the bottom-right-back corner of the coordinate** (block displays have a built-in offset from the spawn point). Spawning at the cell corner aligns the render to the block.

## Line limits
A **line** is one linear code flow (line-scope), without function branches.

| Limit | Value |
|---|---|
| Conditions (`if_*` / `else`) per line | **≤ 33** |
| Actions per line | **≤ 67** |
| Total line content (conditions + actions) | **≤ 67** |

- 1 condition counts as **2 actions** — multiply conditions by 2 and add actions.
- Nested `operations` inside conditions count toward the parent line's total.
- Near the limit → move repeating blocks into **functions** (`call_function`).

## Delays and world load
- **`control_wait` minimum is 1 tick; in TICKS mode the `duration` must be a whole integer** — no zero, fractional or "magic" values.
- Every **big loop** (>10 iterations: `repeat_while`, `repeat_forever`, long `repeat_multi_times`/`repeat_for_each_in_list`) must contain `control_wait` with `duration: 1`, `time_unit: TICKS` inside the body. Without it the loop monopolizes the server thread and causes lag (CPU load).
- **High-load wait pattern (world safety):** sustained 100%+ load causes a critical error and freezes the world. Check the world load and pause while it is high: `repeat_while` on `if_variable_greater_or_equals` over the `cpu_usage` game value (e.g. ≥ 50) with `control_wait` (1 second) in the body — see the `wait` function in `docs/examples/editsession.json`. A custom delay is allowed too; the hard requirement is that the world never sits at 100%+ load long enough to trigger the critical error.

## Critical server limits
- **≤ 300 iterations without a wait per run.** Exceeding = **critical error + full world freeze**. If a loop can exceed 300 iterations, insert `control_wait` (≥1 tick) every ~250–290 iterations.
- **`game_set_region` (Set blocks in region) sets up to 125,000 blocks per call.** Fastest bulk building — use it instead of `game_set_block` loops for arenas and large structures.

## JSON module structure
- Handlers: `handlers` → each with `"type"` (`event`/`function`), `position`, `operations`; an event handler adds `event`, a function adds `name` + `values` (parameters, `display_name`, `icon`, `display_description`).
- Action: `{ "action": "<ID>", "values": [ { "name": "<arg>", "value": { "type": ... } } ], "operations": [...] }`.
- No-argument actions: `"values": []` (e.g. `select_reset`, `entity_remove`, `else`).
- Empty value slot: `{}`.
- Conditions take `"is_inverted"` and nested `"operations"`; `else` is a separate action `{ "action": "else", "values": [], "operations": [...] }` right after the condition.

## Value types
- Math is ALWAYS a `number` with a `%math(...)` **string**: `{"type":"number","number":"%math(a + 1)"}`. Never wrap math in `text`.
- Numeric slot with a placeholder: wrap in `%math()` — e.g. a weight from a map: `%math(%entry(dict, key))` as a number string.
- Text: `{"type":"text","text":"...","parsing":"plain|legacy"}`.
- Variable: `{"type":"variable","variable":"<name>","scope":"line|local|game|save"}`.
- Game value: `{"type":"game_value","game_value":"<id>","selection":"null"}` (or `"{\\"type\\":\\"default\\"}"`).
- Location literal: `{"type":"location","x":0,"y":64,"z":0,"yaw":0,"pitch":0}` — coordinates directly in the value. **Prefer the literal over the "Create location" action (`set_variable_set_all_coordinates`)** — don't spend an action and a variable on what a literal can express. The action is only needed when coordinates are computed at runtime (`%math(...)`).
- **Items are always NBT strings** — see `docs/value-types/item.md`.

## Placeholder syntax
- Variable functions take **no closing percent**: `%var(name)`, `%var_local(name)`, `%var_save(name)`, `%var_line(name)`, `%length(name)`, `%length_local(name)`, `%length_save(name)`, `%length_line(name)`, `%index(list, i)`, `%index_local(list, i)`, `%index_save(...)`, `%index_line(...)`, `%entry(dict, key)`, `%entry_local(...)`, `%entry_save(...)`, `%entry_line(...)`, `%val(id)`.
- **Inside `%math()` any placeholder, text and numbers are allowed**, in any combination.
- **Raw variable names in `%math()`** (`%math(a + b)`) auto-resolve the scope by locality: line → local → game → save. If the same name exists in several scopes, disambiguate with an explicit placeholder: `%math(%var_line(a) + %var_local(b))`. There is **no `%var_game()`** — game scope is the bare `%var()`.
- **Outside `%math()`, numeric slots accept nothing but numbers.** No `%` placeholders in number slots — pass variables as `variable` type values, computations via `%math()`.
- A numeric slot using `%math()` consists **only** of the `%math(...)`: no text or numbers before/after it. `1 + %math(a)` or `%math(a) * 2` in one slot is invalid — move everything inside: `%math(1 + a)`, `%math(a * 2)`.
- Without `%math()` a numeric slot accepts **numbers only** (e.g. `2.5`, `-3`).
- `%math(...)` also has **no closing percent**: `%math(a + 1)`, not `%math(a + 1)%`.

## Loop conditions (`repeat_while`)
- The condition's arguments go in the loop's common `"values"`; `"conditional"` holds only `{ "action": "<if_...>", "is_inverted": <bool> }`.
- Every condition needs **all** its required args: e.g. `if_variable_list_is_empty` requires `list` **and** `compare_type` (ANY/ALL), else import/export breaks.
- `if_variable_equals`/`if_variable_list_contains_value`: `compare`/`values` is an **array**; `if_variable_greater`/`if_variable_less`: single `number` in `compare`.

## Function calls
- `call_function`: `{"name":"function_name","value":{"type":"text","text":"<Name>","parsing":"plain"}}` + `args` of type `map`, where **keys are the stringified JSON of the parameter name**: `"{\\"type\\":\\"text\\",\\"text\\":\\"loc\\",\\"parsing\\":\\"plain\\"}": { ...value... }`.
- The name must exactly match the function's `"name"`.
- **NEVER call a function via `start_process`.** `start_process` starts a process code line (parallel/reusable lines); functions are called ONLY via `call_function`.

## Default build location
- **If the player did not give coordinates where to build the map, build by default at the world spawn** — the world center where players spawn. Take the `spawn_location` game value (`selection: "null"`) and **lower the Y coordinate by 1** (`%math(%var(y)-1)` or `set_variable_change` with −1), so the build sits on the ground under the spawn point instead of floating at the spawn block.
- Use exact coordinates only when the player explicitly gave them.
## Function parameters (the `"Parameter"` value)
A function handler declares its parameters in `values`: a single entry named `parameters` of type `array`, where each element is a value of type `parameter`:

```json
"values": [
  {
    "name": "parameters",
    "value": {
      "type": "array",
      "values": [
        {
          "type": "parameter",
          "type_key": "singular",
          "name": "loc",
          "value_type": "location",
          "is_required": "true",
          "default_value": "{}",
          "slot": 0,
          "description_slot": 9,
          "description": "{\"translations\":{},\"fallback\":{\"rawText\":\"Местоположение\",\"parsingType\":\"LEGACY\"}}"
        }
      ]
    }
  }
]
```
- `type_key`: `singular` (one value) or `plural` (list of values).
- `value_type`: the value type of the parameter (`location`, `number`, `text`, `item`, `vector`, ...). Strictly enforced — wrong type breaks the action.
- `slot` / `description_slot`: editor grid cells (0–54, description usually `slot + 9`) — plain numbers. For plural parameters use `slots` / `description_slots`: comma-separated numbers as **strings**. Slots must not overlap between parameters and must not exceed 54.
- `description`: stringified JSON text component (`translations` + `fallback` with `rawText` and `parsingType`).
- In the function body the parameter is read as a variable: `%var_line(name)` (or `%var_local(name)`, depending on the call).
- Each `call_function` must pass `args` (a `map`) for every required parameter — see Function calls above; the game injects the values into the parameters before running the function code.

## Variables: no zero-initialization, no fake "declaration"
- **Never create variables just to hold 0 or to "declare" them.** An unset variable already reads as 0 (and as empty for text/list/map checks). Do not zero-initialize variables at game/world start.
- **To clear or reset a variable, use one of the two "Clear variables" actions** — never assign 0:
  - `set_variable_remove` — pass the variable itself in the `variables` slot;
  - `set_variable_purge` — pass the variable **name as text** in `names`, plus `scope` (GAME/SAVE/LOCAL/LINE) and `match` (EQUALS/NAME_CONTAINS/...).
- **Game-start / state checks: don't create marker variables** — check whether the variable exists with `if_variable_exists` instead of pre-creating it with a zero value.
## Variable scopes
- **Use the narrowest scope that works — not only `game`:** `line` — temporaries within one line/loop iteration; `local` — per-handler temporaries (also used for function parameters); `game` — state shared across the whole game run; `save` — data that must persist after the game stops. Do not promote variables to `game`/`save` "just in case".

## Key patterns
- **Default value is 0.** Any value type (argument, placeholder, variable, text, number, game element) that finds no content (missing variable/list/map, missing key, empty selection, ...) returns **0**. Always create lists and maps before first use and check keys (`if_variable_map_has_key`); a nonexistent variable in a Location/List slot becomes the number 0 and breaks the action.
- **No zero-initialization needed.** Variables are 0 by default — do NOT add actions setting a variable to 0 before its first use. Set an initial value only when it must differ from 0. Lists and maps still must be created before first use.
- **`else` only on the closing bracket of an invertible condition** — right after the `{ "action": "if_...", ... }` block. Never after a plain action, after another `else` without a condition between, or at the start of an operations list. Nested `else` binds to the nearest parent condition. A trailing `else` after a chain of sequential independent `if`s fires whenever the **last** `if` fails — even if an earlier `if` already matched. Never use a trailing `else` as a "fallback / unknown case" after several independent `if`s — put the fallback inside each branch or restructure.
- **The `block` slot takes an item value (always NBT-encoded)** — `{"type":"item","item":"{Count:1b,id:\\"minecraft:iron_block\\"}"}` or a variable holding an item. Each slot has its own value type (item, sound, particle...) — never put text in such slots.
- **`player_set_boss_bar` progress is 0–100, not 0–1.** Timer: `progress = %math(%var(t)*100/%var(maxt))`.
- **`controller_async_run` does NOT exist on the server — never use it.** For parallel lines use processes: handler `"type": "process"` with `"name"` + the `start_process` action (process_name, target_mode, local_variables_mode, args).
- `repeat_adjacently` with `pattern: CARDINAL` iterates only the 6 orthogonal neighbors (no diagonals); `SQUARE`/`ADJACENT`/`CUBE` include diagonals.
- `%random_uuid%` — valid placeholder for unique names.
- `game_spawn_block_display` + `entity_set_display_teleport_duration` — moving structures visualization; `entity_teleport` to move, `entity_remove` to delete.
- **Event values** are read via `game_value` with `selection: "null"`: `event_block_location` (event block), `event_interaction` (click type: `left_click_block`/`right_click_block`), `event_from_location`/`event_new_location` (old/new player location). Full list in `docs/values/values.md`.
- **Mini-game start method is ALWAYS the player's choice** — chat command, interaction event, menu or any other event. Never impose a start method; follow the player's request.
- **Catching the jump key mid-air** (double jump etc.): `player_jump` is not guaranteed to fire for a key press while the player is already airborne — poll the movement input instead: `if_player_has_input` (`input_type: JUMP`) in a tick process, or the `player_input_event` event (fires when the pressed movement keys change; Space = jump).
- Animation speed: `control_wait` with `time_unit: TICKS` (integers only, ≥1 tick).
