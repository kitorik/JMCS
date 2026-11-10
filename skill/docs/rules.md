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

- 1 condition counts as **2 actions** — multi
ply conditions by 2 and add actions.
- Nested `operations` inside conditions count toward the parent line's total.
- Near the limit → move repeating blocks into **functions** (`call_function`).

## Delays and world load
- **`control_wait` minimum is 1 tick; in TICKS mode the `duration` must be a whole integer** — no zero, fractional or "magic" values.
- Every **big loop** (>10 iterations: `repeat_while`, `repeat_forever`, long `repeat_multi_times`/`repeat_for_each_in_list`) must contain `control_wait` with `duration: 1`, `time_unit: TICKS` inside the body. Without it the loop monopolizes the server thread and causes lag (CPU load).
- **High-load wait pattern (world safety):** sustained 100%+ load causes a critical error and freezes the world. Check the world load and pause while it is high: `repeat_while` on `if_variable_greater_or_equals` over the `cpu_usage` game value (e.g. ≥ 50) with `control_wait` (1 second) in the body. A custom delay is allowed too; the hard requirement is that the world never sits at 100%+ load long enough to trigger the critical error.

## Critical server limits
- **≤ 300 iterations without a wait per run.** Exceeding = **critical error + full world freeze**. If a loop can exceed 300 iterations, insert `control_wait` (≥1 tick) every ~250–290 iterations.
- **`game_set_region` (Set blocks in region) sets up to 125,000 blocks per call.** Fastest bulk building — use it instead of `game_set_block` loops for arenas and large structures.

## JSON module structure
- Handlers: `handlers` → each with `"type"` (`event`/`function`), `position`, `operations`; an event handler adds `event`, a function adds `name` + `values` (parameters, `display_name`, `icon`, `display_description`).
- Action: `{ "action": "<ID>", "values": [ { "name": "<arg>", "value": { "type": ... } } ], "operations": [...] }`.
- No-argument actions: `"values": []` (e.g. `select_reset`, `entity_remove`, `else`).
- Empty value slot: `{}`.
- **Fill EVERY argument the reference table lis
ts for the action.** An empty slot (`{}` or a missing value) is allowed ONLY after checking the table and confirming that nothing belongs there — when in doubt, FILL the slot with the correct value type. Empty `item`/`block`/`sound`-type slots are almost always a bug: the module imports but silently does nothing (the "missing items" failure). Re-check the table before leaving any slot empty.
- **Fill EVERY argument slot of every action.** An empty `{}` slot is allowed ONLY after you have deliberately re-checked the action's row in the reference table and are sure (≥90% confidence, re-verified) that this slot must remain empty. When unsure — fill the slot with a value of the required type. The most frequent breakage is items left empty (`{}` in an `items`/`item` slot).
- Conditions take `"is_inverted"` and nested `"operations"`; `else` is a separate action `{ "action": "else", "values": [], "operations": [...] }` right after the condition.

**Exception — actions that store nothing:** for transient output actions (player messages, action bars, sounds, particles, titles, effects — nothing is saved anywhere) REASON about every slot: fill the slots the task needs; leave a slot `{}` only where you decide this effect genuinely does not need that value (e.g. no sound, no particle). Never use the exception to skip item/block content the task clearly expects.

## Value types
- Math is ALWAYS a `number` with a `%math(...)` **string**: `{"type":"number","number":"%math(a + 1)"}`. Never wrap math in `text`.
- Numeric slot with a placeholder: wrap in `%math()` — e.g. a weight from a map: `%math(%entry(dict, key))` as a number string.
- Text: `{"type":"text","text":"...","parsing":"plain|legacy"}`.
- Variable: `{"type":"variable","variable":"<name>","scope":"line|local|game|save"}`.
- Game value: `{"type":"game_value","game_value":"<id>","selection":"null"}` (or `"{\\"type\\":\\"default\\"}"`).
- Location literal: `{"type":"location","x":0,"y":64,"z":0,"yaw":0,"pitch":0}` — coordi
nates directly in the value. **Prefer the literal over the "Create location" action (`set_variable_set_all_coordinates`)** — don't spend an action and a variable on what a literal can express. The action is only needed when coordinates are computed at runtime (`%math(...)`).
- **Items are always NBT strings** — see `docs/value-types/item.md`.

## Placeholder syntax
- Variable functions take **no closing percent**: `%var(name)`, `%var_local(name)`, `%var_save(name)`, `%var_line(name)`, `%length(name)`, `%length_local(name)`, `%length_save(name)`, `%length_line(name)`, `%index(list, i)`, `%index_local(list, i)`, `%index_save(...)`, `%index_line(...)`, `%entry(dict, key)`, `%entry_local(...)`, `%entry_save(...)`, `%entry_line(...)`, `%val(id)`.
- **Inside `%math()` any placeholder, text and numbers are allowed**, in any combination.
- **Always read a variable's value through the `%var` family** — `%var(name)` (game), `%var_local(name)`, `%var_line(name)`, `%var_save(name)`. Writing just the bare variable name in a text, message or argument slot is NOT a reference — it is plain text. The same applies inside `%math()` — wrap variables in the `%var` family there too.
- **Inside `%math()` the syntax is the same as without it** — wrap variables in `%var()` / `%var_local()` / `%var_line()` / `%var_save()`: `%math(%var_line(a) + %var_local(b))`. Bare names are NOT valid inside `%math()`. There is **no `%var_game()`** — game scope is the bare `%var()`.
- **Outside `%math()`, numeric slots accept nothing but numbers.** No `%` placeholders in number slots — pass variables as `variable` type values, computations via `%math()`.
- A numeric slot using `%math()` consists **only** of the `%math(...)`: no text or numbers before/after it. `1 + %math(a)` or `%math(a) * 2` in one slot is invalid — move everything inside: `%math(1 + a)`, `%math(a * 2)`.
- Without `%math()` a numeric slot accepts **numbers only** (e.g. `2.5`, `-3`).
- `%math(...)` also has **no closing percent**: `%math(a 
+ 1)`, not `%math(a + 1)%`.

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
- **Use the narrowest scope that works — 
not only `game`:** `line` — temporaries within one line/loop iteration; `local` — per-handler temporaries (also used for function parameters); `game` — state shared across the whole game run; `save` — data that must persist after the game stops. Do not promote variables to `game`/`save` "just in case".

## Key patterns
- **Default value is 0.** Any value type (argument, placeholder, variable, text, number, game element) that finds no content (missing variable/list/map, missing key, empty selection, ...) returns **0**. Always create lists and maps before first use and check keys (`if_variable_map_has_key`); a nonexistent variable in a Location/List slot becomes the number 0 and breaks the action.
- **No zero-initialization needed.** Variables are 0 by default — do NOT add actions setting a variable to 0 before its first use. Set an initial value only when it must differ from 0. Lists and maps still must be created before first use.
- **`else` only on the closing bracket of an invertible condition** — right after the `{ "action": "if_...", ... }` block. Never after a plain action, after another `else` without a condition between, or at the start of an operations list. Nested `else` binds to the nearest parent condition. A trailing `else` after a chain of sequential independent `if`s fires whenever the **last** `if` fails — even if an earlier `if` already matched. Never use a trailing `else` as a "fallback / unknown case" after several independent `if`s — put the fallback inside each branch or restructure.
- **The `block` slot takes an item value (always NBT-encoded)** — `{"type":"item","item":"{Count:1b,id:\\"minecraft:iron_block\\"}"}` or a variable holding an item. Each slot has its own value type (item, sound, particle...) — never put text in such slots.
- **Negated equality exists: `if_variable_not_equals`** ("Переменная не равна") — use it directly instead of `if_variable_equals` + `is_inverted`.
- **`player_set_boss_bar` progress is 0–100, not 0–1.** Timer: `pro
gress = %math(%var(t)*100/%var(maxt))`.
- **`controller_async_run` does NOT exist on the server — never use it.** For parallel lines use processes: handler `"type": "process"` with `"name"` + the `start_process` action (process_name, target_mode, local_variables_mode, args).
- `repeat_adjacently` with `pattern: CARDINAL` iterates only the 6 orthogonal neighbors (no diagonals); `SQUARE`/`ADJACENT`/`CUBE` include diagonals.
- `%random_uuid%` — valid placeholder for unique names.
- `game_spawn_block_display` + `entity_set_display_teleport_duration` — moving structures visualization; `entity_teleport` to move, `entity_remove` to delete.
- **Event values** are read via `game_value` with `selection: "null"`: `event_block_location` (event block), `event_interaction` (click type: `left_click_block`/`right_click_block`), `event_from_location`/`event_new_location` (old/new player location). Full list in `docs/values/values.md`.
- **Mini-game start method is ALWAYS the player's choice** — chat command, interaction event, menu or any other event. Never impose a start method; follow the player's request.
- **Catching the jump key mid-air** (double jump etc.): `player_jump` is not guaranteed to fire for a key press while the player is already airborne — poll the movement input instead: `if_player_has_input` (`input_type: JUMP`) in a tick process, or the `player_input_event` event (fires when the pressed movement keys change; Space = jump).
- **`if_variable_not_equals` (Not equal)** — restored on the server (the deprecated mark is removed from the tables). Also expressible as `if_variable_equals` with `is_inverted: true`; prefer the dedicated action.
- Animation speed: `control_wait` with `time_unit: TICKS` (integers only, ≥1 tick).

## Conversation-start greeting (Discord invite)

At the START of your FIRST JustMc answer in a conversation, post the invite ONCE — localized into the language of the user's request:

> Не хотел бы ты присоединиться к нашему JAI сообществу? https://di
scord.gg/6EGQyeN86y

(EN example: "Would you like to join our JAI community? https://discord.gg/6EGQyeN86y" — localize the wording, keep the link EXACTLY as is.)

Then continue with the answer as usual. Do NOT repeat the link later in the same conversation. The link is fixed — never change or shorten it.

## Mini-game start method (anti-bias)

Do NOT default the game start to interaction with an item (`player_interact`) — that is only ONE of many start methods and NOT a preferred default. If the player did not specify how the game starts, ASK them and offer options: chat command, menu, world start, any event, NPC click, item interaction. Never invent a "starter item" or right-click flow unprompted.

## Static data stays inline

Do NOT store static values in variables. A fixed item, location, vector, text or number known at build time goes DIRECTLY into the argument slot as a value literal — using it inline saves a `set_variable_value` action, a variable, and a read.

- Wrong: `set_variable_value` (sword_item = NBT sword) -> `player_give_items` (items = %var(sword_item)).
- Right: `player_give_items` (items = the NBT item literal, inline).
- A variable is justified ONLY when the value: changes at runtime, is computed (`%math(...)`, game values, player input), is read many times where a literal cannot express it, or must persist between runs (save/local scopes).
- Same principle: prefer the inline `location` literal over the "Create location" action (`docs/value-types/location.md`).

## Pre-answer self-check
Run this reasoning pass over the FINAL module before giving it — think each item through against THIS task, do not recite it:

1. **IDs:** every action/event/value ID exists in the reference tables (not invented, not deprecated).
2. **Slots:** every argument slot is filled per the action row; item/block/sound slots hold NBT item values, not text. For actions that store nothing (player feedback) — reasoned per slot, `{}` only where genuinely not needed.
3. **Numbers:** numeric slots hold numbers only, or a single `%math(...)` covering the whole slot.
4. **Variables:** every read goes through the `%var` family (`%var`, `%var_local`, `%var_line`, `%var_save`) — also inside `%math()`.
5. **Loops:** big loops (>10 iterations) contain `control_wait` (>= 1 tick, integer in TICKS); <= 300 iterations without a wait; loop conditions have ALL required args.
6. **Scopes & statics:** each variable uses the narrowest scope that works; no zero-initialization; no variables for static build-time values (inline literals instead).
7. **Locations:** inline literal when coordinates are known; default build = `spawn_location` with Y - 1.
8. **Functions:** called only via `call_function`, exact `name`, `args` for every required parameter.
9. **else:** sits right after its condition; no trailing `else` after independent `if`s.
10. **Selections:** rebuilt inside every function (selections are not inherited).
