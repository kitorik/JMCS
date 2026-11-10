# JAI lookup — what to use (intent → likely actions/events/values)

Pick candidates here, then check the EXACT arguments in `docs/actions/*.md`, `docs/events/events.md`, `docs/values/values.md`. Only verified IDs are listed.

**Frequency marks (N/10):** 0 = almost never used, 10 = used most often. Prefer high-mark actions first; for low-mark (<=3) IDs double-check the table row and consider a more common alternative before using them.

## Items & inventory
| Intent | Use |
|---|---|
| Give items | `player_give_items` (9/10) (+ `amount`) |
| Check inventory | `if_player_has_item` (8/10), `if_player_has_item_in_slot` (5/10), `if_player_cursor_item_equals` (4/10) |
| Event item check | `if_game_event_item_equals` (8/10) |
| Item encoding | items are ALWAYS NBT strings — `docs/value-types/item.md` (9/10 rule) |

## Communication & UI
| Message | `player_send_message` (9/10) |
| Boss bar | `player_set_boss_bar` (7/10) (progress 0-100) |
| Menu | `player_show_inventory_menu` (6/10) |
| Dialog | `player_show_dialog_menu_from_nbt` (4/10) |
| Sounds | `player_stop_sound` (3/10), `player_stop_sounds_by_source` (2/10) |
| Scoreboard | `player_show_scoreboard` (5/10), scoreboard actions in `docs/actions/world.md` |

## Movement & world
| Teleport | `player_teleport` (8/10) (keep_rotation / keep_velocity / dismount) |
| Teleport path | `player_teleport_sequence` (3/10) |
| Spectate | `player_spectate_target` (2/10) |
| Bulk blocks | `game_set_region` (8/10) (<= 125,000 blocks) |
| Single block | `game_set_block` (8/10) |
| Natural break | `game_break_block` (4/10) |
| Weather / border | `player_set_weather` (3/10), `player_set_world_border` (2/10), `player_shift_world_border` (1/10) |

## Entities
| Damage | `entity_damage` (6/10) |
| Remove | `entity_remove` (7/10) |
| Move / rotate | `entity_teleport` (7/10), `entity_face_location` (5/10) |
| Disguise | `entity_disguise_as_block` / `_entity` / `_item` / `_player` (3/10) |
| Attributes | `entity_get_attribute` (4/10) |
| Custom tags | `entity_get_custom_tag` (4/10) (+ set analog in the table) |
| Select | `select_*` family (7/10) — creation action first, then `select_add_*` |

## Events (triggers)
| Chat command | `player_chat` (8/10) + `if_player_chat_message_equals` (7/10) |
| Join / quit | `player_join` (7/10) / `player_quit` (5/10) |
| Interaction | `player_interact` (8/10) + `if_game_event_item_equals` |
| Movement keys | `player_input_event` (6/10), `if_player_has_input` (6/10) (JUMP for double jump mid-air) |
| Jump | `player_jump` (5/10) (from the ground) |
| World lifecycle | `world_start` (6/10), `world_stop` (3/10), `world_reload` (2/10) |
| Web | events `world_web_response` (2/10), `world_web_exception` (1/10) |

## Conditions & variables
| Compare | `if_variable_equals` (9/10), `if_variable_not_equals` (7/10), `if_variable_greater(_or_equals)` (8/10), `if_variable_less(_or_equals)` (7/10) |
| List / map | `if_variable_list_contains_value` (6/10), `if_variable_map_has_key` (6/10), `if_variable_list_is_empty` (5/10) |
| Text | `if_variable_text_contains` (6/10), `_starts_with` (4/10), `_ends_with` (3/10), `_matches` (RegEx) (4/10) |
| Assign | `set_variable_value` (9/10); computations inside %math() with %var_*() placeholders |
| Random | `%random%` + `%math()` (7/10), `set_variable_get_map_random_entry` (3/10), `set_variable_randomize_map_order` (2/10) |
| Clear | `set_variable_remove` (6/10), `set_variable_purge` (4/10) |

## Flow control
| Wait | `control_wait` (9/10) (>= 1 tick, integers in TICKS; high load -> cpu_usage wait pattern) |
| Loops | `repeat_*` family (8/10); `repeat_while` + `conditional` |
| Function | `call_function` (8/10) (+ `args` = declared parameters) |
| Process | `start_process` (5/10) (NOT for calling functions) |
| Label / error / timing | `controller_label` (3/10), `controller_exception` (2/10), `controller_measure_time` (2/10) |

## Game values (event data)
| Event data | `event_block_location` (7/10), `event_interaction` (6/10), `event_from_location` (4/10), `event_new_location` (4/10) |
| Spawn | `spawn_location` (6/10) (default build point, Y - 1) |
| Load | `cpu_usage` (5/10) |
| Online | `online`, `global_online`, `player_amount` (4/10) |

## Common mistakes (symptom -> fix)
| Symptom | Cause -> Fix |
|---|---|
| Module imports but items/blocks/effects are missing | empty `{}` item/block/sound slot -> fill it with a value of the exact type (items = NBT strings) |
| Message shows the variable NAME, not the value | bare name in a text slot -> read via `%var()` family (also inside %math()) |
| Math result is 0 / wrong / placeholder shown as text | bare name inside %math(), or text around a %math() in a numeric slot -> move the whole expression inside ONE `%math(...)` |
| World freeze + critical error | loop over 300 iterations without a wait -> `control_wait` every ~250-290 iterations |
| Server lags while a loop runs | big loop (>10 iterations) without `control_wait` in the body -> add `control_wait` (1 tick, TICKS) |
| Function never runs | called via `start_process` or name mismatch -> `call_function` with the exact `name` + `args` for every required parameter |
| Fallback branch fires at the wrong time | trailing `else` after independent `if`s -> put the fallback inside each branch or restructure |
| Empty selection inside a function | selections are NOT inherited -> rebuild the selection inside the function |
| Location becomes 0 / action breaks | nonexistent variable in a Location slot -> create the variable first; prefer the inline location literal when coordinates are known |
| Boss bar never fills / overflows | progress is 0-100, not 0-1 -> `%math(%var(t)*100/%var(maxt))` |
| Condition breaks the module on import | missing required args (e.g. `compare_type` in `if_variable_list_is_empty`) -> fill ALL arguments of the condition |

> The lookup only POINTS at likely IDs — always confirm the exact arguments and enum values in the reference tables before writing JSON.
