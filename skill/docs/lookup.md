# JAI lookup — what to use (intent → likely actions/events/values)

Pick candidates here, then check the EXACT arguments in `docs/actions/*.md`, `docs/events/events.md`, `docs/values/values.md`. Only verified IDs are listed.

## Items & inventory
| Intent | Use |
|---|---|
| Give items | `player_give_items` (+ `amount`) |
| Check inventory | `if_player_has_item`, `if_player_has_item_in_slot`, `if_player_cursor_item_equals` |
| Event item check | `if_game_event_item_equals` |
| Item encoding | items are ALWAYS NBT strings — `docs/value-types/item.md` |

## Communication & UI
| Message | `player_send_message` |
| Boss bar | `player_set_boss_bar` (progress 0–100) |
| Menu | `player_show_inventory_menu` |
| Dialog | `player_show_dialog_menu_from_nbt` |
| Sounds | `player_stop_sound`, `player_stop_sounds_by_source` |
| Scoreboard | `player_show_scoreboard`, scoreboard actions in `docs/actions/world.md` |

## Movement & world
| Teleport | `player_teleport` (keep_rotation / keep_velocity / dismount) |
| Teleport path | `player_teleport_sequence` |
| Spectate | `player_spectate_target` |
| Bulk blocks | `game_set_region` (≤ 125,000 blocks) |
| Single block | `game_set_block` |
| Natural break | `game_break_block` |
| Weather / border | `player_set_weather`, `player_set_world_border`, `player_shift_world_border` |

## Entities
| Damage | `entity_damage` |
| Remove | `entity_remove` |
| Move / rotate | `entity_teleport`, `entity_face_location` |
| Disguise | `entity_disguise_as_block` / `_entity` / `_item` / `_player` |
| Attributes | `entity_get_attribute` |
| Custom tags | `entity_get_custom_tag` (+ set analog in the table) |
| Select | `select_*` family — creation action first, then `select_add_*` |

## Events (triggers)
| Chat command | `player_chat` + `if_player_chat_message_equals` |
| Join / quit | `player_join` / `player_quit` |
| Interaction | `player_interact` + `if_game_event_item_equals` |
| Movement keys | `player_input_event`, `if_player_has_input` (JUMP for double jump mid-air) |
| Jump | `player_jump` (from the ground) |
| World lifecycle | `world_start`, `world_stop`, `world_reload` |
| Web | events `world_web_response`, `world_web_exception` |

## Conditions & variables
| Compare | `if_variable_equals`, `if_variable_not_equals`, `if_variable_greater(_or_equals)`, `if_variable_less(_or_equals)` |
| List / map | `if_variable_list_contains_value`, `if_variable_map_has_key`, `if_variable_list_is_empty` |
| Text | `if_variable_text_contains`, `_starts_with`, `_ends_with`, `_matches` (RegEx) |
| Assign | `set_variable_value`; computations inside `%math()` with `%var_*()` placeholders |
| Random | `%random%` + `%math()`, `set_variable_get_map_random_entry`, `set_variable_randomize_map_order` |
| Clear | `set_variable_remove`, `set_variable_purge` |

## Flow control
| Wait | `control_wait` (≥ 1 tick, integers in TICKS; high load → `cpu_usage` wait pattern) |
| Loops | `repeat_*` family; `repeat_while` + `conditional` |
| Function | `call_function` (+ `args` = declared parameters) |
| Process | `start_process` (NOT for calling functions) |
| Label / error / timing | `controller_label`, `controller_exception`, `controller_measure_time` |

## Game values (event data)
| Event data | `event_block_location`, `event_interaction`, `event_from_location`, `event_new_location` |
| Spawn | `spawn_location` (default build point, Y − 1) |
| Load | `cpu_usage` |
| Online | `online`, `global_online`, `player_amount` |

> ⚠️ The lookup only POINTS at likely IDs — always confirm the exact arguments and enum values in the reference tables before writing JSON.
