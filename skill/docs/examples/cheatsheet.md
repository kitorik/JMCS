# JAI cheatsheet — ready patterns & handler notes

> **Use as NOTES, not as a style template.** Take the pattern idea and re-derive your own JSON for the task: adapt structure, wording, argument values and design to what the player asked. Never copy a whole snippet as-is; every argument must fit THIS task.

## Ready patterns

### One-time first-join action

Trigger: `player_join`. A save-scope marker per player (e.g. `%player%_joined`) — if it does not exist, this is the first join: run the one-time actions and create the marker.

```
handler: player_join
  conditional:
    condition: if_variable_exists   # is_inverted: true
      variable: %player%_joined     # save scope
    actions:
      player_send_message
        text: "Welcome!"          # any one-time action(s) here
      set_variable_value            # save scope
        variable: %player%_joined
        value: TRUE
```

- Works for ANY one-time action (first-join kit, tutorial, welcome title) — only the actions inside change.
- Never zero-initialize the marker: "does not exist" is the "not joined yet" state.

## Handler notes (community examples, merged)

> Distilled from two real community handlers (a gifts/NPC module on `world_start` and an NPC control-panel module on `player_right_click_entity`). Syntax facts and techniques ONLY — not style, not naming, not structure to copy.

### Value literals & parsing
- `text` values carry a `parsing` mode: `"plain"` (literal) or `"legacy"` (color codes, hex like `&#A6FF6E`, placeholders). Use legacy for player-facing colored text.
- Actions can carry a `selection` object directly, no separate select action needed: `{"type":"all_entities"}`, `{"type":"all_players"}`, `{"type":"default_player"}`, `{"type":"victim_entity"}`.
- In `game_value` values the `selection` field is a STRINGIFIED selection literal: `"selection":"{\"type\":\"default\"}"`.
- `call_function` `args` map keys are STRINGIFIED value literals of the parameter names: key = `"{\"type\":\"text\",\"text\"
:\"npcName\",\"parsing\":\"plain\"}"`, value = the passed value literal. Non-obvious but real.
- `if_variable_equals` `compare` may be an ARRAY — the check passes if ANY of the compare values matches.

### Functions
- Functions declare `parameters` (array of `parameter` values: `name`, `value_type`, `is_required`, `default_value`, `slot`) and `is_hidden` (enum TF).
- `control_return_function` — early return from a function.
- Feedback helper pattern: a small "deny" function (action bar + sound + early return) reused everywhere.

### Verified actions seen in real use
`set_variable_multiple` (set many variables in one action), `set_variable_format_timestamp`, `set_variable_get_list_random_value`, `set_variable_get_item_component`, `set_variable_set_item_model_data` / `_set_item_name` / `_set_item_custom_tag` / `_set_item_max_stack_size`, `player_set_item_cooldown`, `game_spawn_item`, `repeat_forever`, `player_send_action_bar`, `player_send_title`, `player_display_particle`, `player_play_sound`, `game_cancel_event`, `select_filter_by_conditional`, `select_entity_by_name`, `set_variable_clamp`, `set_variable_add`.

### Techniques
- **NPC as control panel:** `game_cancel_event` FIRST in the event handler (block vanilla behavior) -> `entity_get_custom_tag` on the `victim_entity` selection (args `name`, `default`) -> route via `if_variable_equals` -> `call_function`.
- **Count a selection:** `set_variable_get_list_length` with `list` = game value `selection_target_uuids`, then `if_variable_greater_or_equals` on the length.
- **Polling loop:** `repeat_forever` + `control_wait` (20 ticks) inside, throttled by a size check — never spin without a wait.
- **Batch start on `world_start`:** `entity_remove` on all entities + `set_variable_multiple` reset + `call_function` / `start_process`. `start_process` args: `process_name`, `local_variables_mode` (e.g. `DONT_COPY`), `target_mode` (e.g. `NO_TARGET`).

> Caveat: one handler used `%math(1-breaker_on)` with a bare name inside — do
 NOT adopt that; keep the rule: wrap variables in the %var family inside %math().

## Structure skeletons

> Minimal structure skeletons — take the shape, fill with task content. Full JSON syntax: `docs/rules.md`.

### Event handler with condition + else
```
handler: <event>
  conditional:
    condition: <if_...>          # is_inverted where needed
    operations: [ ...actions... ]
    else: [ ...fallback actions... ]   # sits right after ITS condition
```

### Function with parameters
```
function <name>
  parameters: [ {parameter: name, value_type, is_required, default_value, slot} ]
  is_hidden: FALSE
  ...actions...                  # read params as %var_line(name)
  control_return_function        # early return if needed
```

### Loop with wait (safe)
```
repeat_forever / repeat_while:
  ...body actions...
  control_wait  duration: 1  time_unit: TICKS   # every big loop body
```

### Cancel-event handler (block vanilla behavior)
```
handler: <event>
  game_cancel_event
  ...then custom logic...
```
