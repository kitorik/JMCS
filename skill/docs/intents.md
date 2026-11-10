# JAI intent lookup (mini-AI)

Quick router: what the player asks for → the most probable actions / events / conditions. Always verify the exact arguments and enum values in the reference tables (`docs/actions/`, `docs/events/events.md`, `docs/values/values.md`) before writing the module.

| The player wants... | Most likely tools |
|---|---|
| Teleport / move a player | `player_teleport`; location via `location` literal or the `spawn_location` game value |
| Push / impulse / launch | `player_set_velocity` (vector value) |
| Double jump / mid-air key press | `player_input_event` (pressed keys change), `if_player_has_input` (`input_type: JUMP`), `player_set_velocity` |
| Give / take items | `player_give_items`, `player_remove_items` — items are ALWAYS NBT strings `{Count:1b,id:"minecraft:..."}` |
| Inventory menu (GUI) | `player_show_inventory_menu` |
| Boss bar (timer, health, progress) | `player_set_boss_bar` (progress 0–100) + the timer process pattern (see cheatsheet) |
| Titles / on-screen messages | `player_send_title`, `player_send_message` |
| Sounds | `player_play_sound` |
| Change game mode | `player_set_gamemode`, condition `if_player_gamemode_equals` |
| Chat command handling | event `player_chat` + `if_player_chat_message_equals` |
| Interaction (click) start | event `player_interact` (+ `if_game_event_item_equals` for the item) |
| Death logic | event `player_death` |
| Join handling | event `player_join` |
| Build arenas / large structures | `game_set_region` (up to 125,000 blocks), `game_set_block` for single blocks |
| Cancel the triggering event | `game_cancel_event` |
| Compare a variable (negated) | `if_variable_not_equals` ("Переменная не равна") — NOT `if_variable_equals` + inversion |
| Random pick | `set_variable_get_map_random_entry` (map), or `%random%` + `%math(floor(random*N))` (index) |
| Timers / periodic code | `repeat_while` + `control_wait` (≥1 tick); under heavy load the `cpu_usage` wait pattern |
| Reusable code | functions: `parameter` type + `call_function`; parallel: process handler + `start_process` |
| Moving structures (visualization) | `game_spawn_block_display`, `entity_teleport`, `entity_remove`, `entity_set_display_teleport_duration` |
| Unique names | `%random_uuid%` |
| Select targets | `select_player_by_name` / `select_all_players` / `select_all_mobs` / `select_reset` (selections are NOT inherited by functions) |

## How to route
1. Identify the intent category → take the candidate IDs from the table.
2. Open the reference file and read the full row of each candidate (arguments, types, enums).
3. Pick the row that fits; fill EVERY argument slot with a value of the correct type.
4. Still unsure between two actions → prefer the one whose table row matches the required arguments exactly.
