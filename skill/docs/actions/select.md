# Select actions
> **Enum macros:** {TF} = TRUE / FALSE; {TFN} = TRUE / FALSE / NOT_SET; {ANY_ALL} = ANY / ALL; {ITEM_MATCH} = EXACT / IGNORE_NAME_DURABILITY / IGNORE_NAME_DURABILITY_ENCHANTMENTS / CUSTOM_TAGS_CONTAINS / MINECRAFT_TAG / ITEM_TYPE; {DEG_RAD} = DEGREES / RADIANS; {CMP} = EXACTLY / IGNORE_STACK_SIZE / IGNORE_DURABILITY_AND_STACK_SIZE / TYPE_ONLY. Icon column omitted.


|  ID  |  Name  |  Description  |  Category/Subcategory  |  Arguments  |
|  ---  |  ---  |  ---  |  ---  |  ---  |
|  select_add_all_entities  |  Add all entities  |  Adds all entities in the world to the selection.  |  select/add  |    |
|  select_add_all_mobs  |  Add all mobs  |  Adds all mobs in the world to the selection.  |  select/add  |    |
|  select_add_all_players  |  Add all players  |  Adds all players in the world to the selection.  |  select/add  |    |
|  select_add_entity_by_conditional  |  Add entity by condition  |  Adds entities matching the given condition.  |  select/add  |    |
|  select_add_entity_by_name  |  Add entity by name/UUID  |  Adds the entity with the given name/UUID to the selection.  |  select/add  |  name_or_uuid: text  |
|  select_add_event_target  |  Add event target  |  Adds the target that triggered the event to the selection.  |  select/add  |  selection_type: enum<br/>&nbsp;&nbsp;- DEFAULT<br/>&nbsp;&nbsp;- KILLER<br/>&nbsp;&nbsp;- DAMAGER<br/>&nbsp;&nbsp;- VICTIM<br/>&nbsp;&nbsp;- SHOOTER<br/>&nbsp;&nbsp;- PROJECTILE  |
|  select_add_last_entity  |  Add last spawned entity  |  Adds the last spawned entity in the world to the selection.  |  select/add  |    |
|  select_add_last_mob  |  Add last spawned mob  |  Adds the last spawned mob in the world to the selection.  |  select/add  |    |
|  select_add_mob_by_name  |  Add mob by name/UUID  |  Adds the mob with the given name/UUID to the selection.  |  select/add  |  name_or_uuid: text  |
|  select_add_player_by_conditional  |  Add player by condition  |  Adds players matching the given condition.  |  select/add  |    |
|  select_add_player_by_name  |  Add player by name/UUID  |  Adds the player with the given name/UUID to the selection.  |  select/add  |  name_or_uuid: text  |
|  select_add_random_entity  |  Add random entity  |  Adds a random entity from the world to the selection.  |  select/add  |    |
|  select_add_random_mob  |  Add random mob  |  Adds a random mob from the world to the selection.  |  select/add  |    |
|  select_add_random_player  |  Add random player  |  Adds a random player from the world to the selection.  |  select/add  |    |
|  select_all_entities  |  Select all entities  |  Selects all entities in the world.  |  select/creation  |    |
|  select_all_mobs  |  Select all mobs  |  Selects all mobs in the world.  |  select/creation  |    |
|  select_all_players  |  Select all players  |  Selects all players in the world.  |  select/creation  |    |
|  select_entity_by_conditional  |  Select entity by condition  |  Selects entities matching the given condition.  |  select/creation  |    |
|  select_entity_by_name  |  Select entity by name  |  Selects the entity or entities by name or UUID.  |  select/creation  |  name_or_uuid: text  |
|  select_event_target  |  Select event target  |  Selects the target that triggered the event.  |  select/creation  |  selection_type: enum<br/>&nbsp;&nbsp;- DEFAULT<br/>&nbsp;&nbsp;- KILLER<br/>&nbsp;&nbsp;- DAMAGER<br/>&nbsp;&nbsp;- VICTIM<br/>&nbsp;&nbsp;- SHOOTER<br/>&nbsp;&nbsp;- PROJECTILE  |
|  select_filter_by_conditional  |  Filter selection by condition  |  Keeps in the selection only the targets matching the chosen condition.  |  select/filter  |    |
|  select_filter_by_distance  |  Filter selection by distance  |  Keeps in the selection only the targets within a distance of the location.  |  select/filter  |  location: location<br/>selection_size: number<br/>ignore_y_axis: enum<br/>{TF}<br/>compare_mode: enum<br/>&nbsp;&nbsp;- NEAREST<br/>&nbsp;&nbsp;- FARTHEST  |
|  select_filter_by_raycast  |  Raycast filter  |  Keeps only the targets hit by a raycast. The beam width only affects entities (grows or shrinks their hitboxes).  |  select/filter  |  variable: variable<br/>origin: location<br/>max_distance: number<br/>ray_size: number<br/>selection_size: number<br/>consider_blocks: enum<br/>{TF}<br/>ignore_passable_blocks: enum<br/>{TF}<br/>fluid_collision_mode: enum<br/>&nbsp;&nbsp;- NEVER<br/>&nbsp;&nbsp;- SOURCE_ONLY<br/>&nbsp;&nbsp;- ALWAYS  |
|  select_filter_randomly  |  Filter selection randomly  |  Keeps the given number of random targets in the selection.  |  select/filter  |  size: number  |
|  select_invert  |  Invert selection  |  Creates a new selection containing all entities except the selected ones.  |  select/creation  |    |
|  select_last_entity  |  Select last spawned entity  |  Selects the last spawned entity in the world.  |  select/creation  |    |
|  select_last_mob  |  Select last spawned mob  |  Selects the last spawned mob in the world.  |  select/creation  |    |
|  select_mob_by_name  |  Select mob by name  |  Selects the mob or mobs by name or UUID.  |  select/creation  |  name_or_uuid: text  |
|  select_player_by_conditional  |  Select player by condition  |  Selects players matching the given condition.  |  select/creation  |    |
|  select_player_by_name  |  Select player by name  |  Selects the player or players by name or UUID.  |  select/creation  |  name_or_uuid: text  |
|  select_random_entity  |  Select random entity  |  Selects a random entity in the world.  |  select/creation  |    |
|  select_random_mob  |  Select random mob  |  Selects a random mob in the world.  |  select/creation  |    |
|  select_random_player  |  Select random player  |  Selects a random player in the world.  |  select/creation  |    |
|  select_reset  |  Reset selection  |  Resets the whole selection.  |  select/creation  |    |
