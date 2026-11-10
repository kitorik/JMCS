# Game values
> **Enum macros:** {TF} = TRUE / FALSE; {TFN} = TRUE / FALSE / NOT_SET; {ANY_ALL} = ANY / ALL; {ITEM_MATCH} = EXACT / IGNORE_NAME_DURABILITY / IGNORE_NAME_DURABILITY_ENCHANTMENTS / CUSTOM_TAGS_CONTAINS / MINECRAFT_TAG / ITEM_TYPE; {DEG_RAD} = DEGREES / RADIANS; {CMP} = EXACTLY / IGNORE_STACK_SIZE / IGNORE_DURABILITY_AND_STACK_SIZE / TYPE_ONLY. Icon column omitted.


|  ID  |  Name  |  Description  |  Category  |  Return type  |  Works with  |  Status  |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
|  absorption_health  |  Absorption health  |  Gets the amount of absorption (golden) health of the target.  |  Statistics  |  number  |    |    |
|  active_item_used_time  |  Item use time  |  Gets the current item use time in hand.  |  Statistics  |  number  |    |    |
|  age  |  Target age  |  Gets the age of the target in ticks.  |  Statistics  |  number  |    |    |
|  all_entities_names  |  All entity names  |  Gets the names of all entities in the world.  |  World  |  array<text>  |    |    |
|  all_entities_uuids  |  All entity UUIDs  |  Gets the UUIDs of all entities in the world.  |  World  |  array<text>  |    |    |
|  all_players_names  |  All player names  |  Gets the names of all players in the world.  |  World  |  array<text>  |    |    |
|  all_players_uuids  |  All player UUIDs  |  Gets the UUIDs of all players in the world.  |  World  |  array<text>  |    |    |
|  anticheat_check  |  Anticheat check  |  Gets the name of the anticheat check that caught the player.  |  Event  |  text  |  The "Anticheat flagged player" event  |    |
|  anticheat_violations  |  Anticheat triggers  |  Gets the number of the player anticheat check triggers.  |  Event  |  number  |  The "Anticheat flagged player" event  |    |
|  armor_items  |  Armor items  |  Gets the items in the target armor slots.  |  Item  |  array<item>  |    |    |
|  armor_points  |  Armor points  |  Gets the amount of the target armor points changeable by items.  |  Statistics  |  number  |    |    |
|  armor_toughness  |  Armor toughness  |  Gets the amount of the target armor toughness changeable by items.  |  Statistics  |  number  |    |    |
|  arrows_in_body  |  Arrow count in body  |  Gets the number of arrows in the target body.  |  Statistics  |  number  |    |    |
|  attached_leads  |  Leashed entities  |  Gets the UUIDs of entities leashed to the target.  |  Info  |  array<text>  |    |    |
|  attack_cooldown_strength  |  Attack cooldown  |  Gets the target current attack cooldown.  |  Statistics  |  number  |    |    |
|  attack_cooldown_ticks  |  Attack cooldown in ticks  |  Gets the target current attack cooldown in ticks.  |  Statistics  |  number  |    |    |
|  attack_damage  |  Attack damage  |  Gets the amount of the target attack damage changeable by items.  |  Statistics  |  number  |    |    |
|  attack_speed  |  Attack speed  |  Gets the target attack speed changeable by items.  |  Statistics  |  number  |    |    |
|  block_beneath  |  Block location under target  |  Gets the location of the block under the target.  |  Location  |  location  |    |    |
|  blocks_beneath  |  Blocks under target  |  Gets the locations of all blocks under the target.  |  Location  |  array<location>  |    |    |
|  body_yaw  |  Body rotation  |  Gets the target body rotation.  |  Location  |  number  |    |    |
|  cape_location  |  Cape location  |  Gets the player cloak location.  |  Location  |  location  |  Players  |    |
|  cardinal_direction  |  Cardinal direction  |  Gets the target cardinal direction (north, west, south, east).  |  Location  |  text  |    |    |
|  chat_visibility  |  Chat visibility  |  Gets the player chat visibility status.  |  Info  |  text  |  Players  |    |
|  client_brand_name  |  Player client name  |  Gets the player client name.  |  Info  |  text  |  Players  |    |
|  client_view_distance  |  Player render distance  |  Gets the player render distance set in the game settings.  |  Statistics  |  number  |  Players  |    |
|  clientside_locale  |  Player client language  |  Gets the player client language.  |  Info  |  text  |  Players  |    |
|  cpu_usage  |  CPU usage percentage  |  Gets the percentage of the server CPU load by the world.  |  World  |  number  |    |    |
|  currency_transaction_amount  |  Emerald amount in transaction  |  Gets the number of emeralds spent in the transaction.  |  Event  |  text  |  The "Player makes transaction" event  |    |
|  currency_transaction_reason  |  Transaction request reason  |  Gets the reason of the emerald transaction request.  |  Event  |  text  |  The "Player makes transaction" event  |    |
|  currency_transaction_result  |  Transaction result  |  Gets the result of the completed transaction.  |  Event  |  text  |  The "Player makes transaction" event  |    |
|  current_health  |  Current health  |  Gets the remaining amount of the target health.  |  Statistics  |  number  |    |    |
|  current_input_list  |  Currently pressed movement keys  |  Gets the currently pressed movement keys.  |  Info  |  array<text>  |  Players  |    |
|  cursor_item  |  Cursor item  |  Gets the item on the target cursor (used when moving items in the inventory).  |  Item  |  item  |    |    |
|  custom_inventory_items  |  Item list in open inventory  |  Returns the list containing the items in the currently open inventory menu.  |  Item  |  array<item>  |    |    |
|  death_screen_score  |  Score amount  |  Gets the score amount shown on the death screen.  |  Statistics  |  number  |  Players  |    |
|  delay_reload_count  |  World freeze duration  |  Gets the current time the world is frozen for.  |  World  |  number  |    |    |
|  direction_of_view  |  Direction of view  |  Gets the target look direction vector.  |  Location  |  vector  |    |    |
|  display_entity_left_rotation  |  Display left rotation  |  Gets the display left rotation as a vector.  |  Info  |  vector  |  Displays  |    |
|  display_entity_right_rotation  |  Display right rotation  |  Gets the display right rotation as a vector.  |  Info  |  vector  |  Displays  |    |
|  display_entity_scale  |  Display scale  |  Gets the display scale as a vector.  |  Info  |  vector  |  Displays  |    |
|  display_entity_translation  |  Display offset  |  Gets the display translation as a vector.  |  Info  |  vector  |  Displays  |    |
|  display_name  |  Display name  |  Gets the target display name.  |  Info  |  text  |    |    |
|  enchantment_seed  |  Current enchantment seed  |  Gets the player current enchantment seed.  |  Statistics  |  number  |    |    |
|  entity_fuse_ticks  |  Fuse time  |  Gets the entity time until explosion.  |  Statistics  |  number  |  Creepers<br/>TNT<br/>Firework rockets  |    |
|  entity_height  |  Hitbox height  |  Gets the target hitbox size on the Y axis.  |  Statistics  |  number  |    |    |
|  entity_item  |  Entity item  |  Gets the target item form.  |  Item  |  item  |    |    |
|  entity_pathfinder_point_index  |  Path point index  |  Gets the mob current path point index it is walking along.  |  Statistics  |  number  |    |    |
|  entity_pathfinder_points  |  Current path  |  Gets the list of all points making up the mob current path.  |  Info  |  array<location>  |    |    |
|  entity_pick_item_stack  |  Entity received item  |  Gets the item obtained by middle-clicking (MMB) an entity.  |  Item  |  item  |    |    |
|  entity_ticks_lived  |  Target lifetime  |  Gets the number of ticks the target has existed.  |  Statistics  |  number  |    |    |
|  entity_type  |  Entity type  |  Gets the target entity type.  |  Info  |  text  |    |    |
|  entity_width_x  |  Hitbox width  |  Gets the target hitbox size on the X axis.  |  Statistics  |  number  |    |    |
|  entity_width_z  |  Hitbox length  |  Gets the target hitbox size on the Z axis.  |  Statistics  |  number  |    |    |
|  event_added_items  |  Distributed items  |  Yields the map of items distributed into slots via LMB/RMB or duplicated via the mouse wheel.  |  Event  |  map<number, item>  |  The "Player drags item in inventory" event  |    |
|  event_advancement_tab_name  |  Achievement tab name  |  Gets the event current advancements tab name.  |  Event  |  text  |  The "Player switched achievements menu tab" event  |  deprecated  |
|  event_anvil_damage_state  |  New anvil damage state  |  Gets the new anvil break state.  |  Event  |  text  |  The "Player damages anvil" event  |    |
|  event_anvil_rename_input  |  New item name  |  Gets the new item name in the anvil.  |  Event  |  text  |  The "Player renames item" event  |    |
|  event_block  |  Event block  |  Gets the ID of the block associated with the event.  |  Event  |  text  |    |    |
|  event_block_break_progress  |  Block breaking progress  |  Gets the break progress of the block associated with the event.  |  Event  |  number  |  Player block breaking update<br/>Entity block breaking update  |    |
|  event_block_face  |  Event block face  |  Gets the block face affected in the event as a direction.  |  Event  |  text  |  Interaction events<br/>Block place or break events<br/>The "Player projectile hits" event<br/>Piston events  |    |
|  event_block_location  |  Event block location  |  Gets the block location in the event.  |  Event  |  location  |    |    |
|  event_blocks_involved  |  Event affected blocks  |  Gets the list of locations of all blocks involved in the event.  |  Event  |  array<location>  |  Explosion events<br/>Piston events  |    |
|  event_chat_message  |  Chat message  |  Gets the message sent by the target in the event.  |  Event  |  text  |  The "Player writes chat message" event  |    |
|  event_close_inventory_cause  |  Inventory close reason  |  Gets the reason the target open inventory was closed in the event.  |  Event  |  text  |  The "Player closes inventory" event  |    |
|  event_combust_duration  |  Entity burn duration  |  Gets the entity burn duration from the event.  |  Event  |  number  |  The "Player ignites" event<br/>The "Entity ignites" event  |    |
|  event_combust_reason  |  Entity burn reason  |  Gets the entity burn reason from the event.  |  Event  |  text  |  The "Player ignites" event<br/>The "Entity ignites" event  |    |
|  event_custom_click_dialog_view_data  |  Dialog data  |  Gets the data entered by the player in the dialog window.  |  Event  |  any  |  The "Player triggers custom click" event  |    |
|  event_custom_click_key  |  Custom click ID  |  Gets the custom click ID in the dialog window or chat.  |  Event  |  text  |  The "Player triggers custom click" event  |    |
|  event_damage  |  Damage dealt  |  Gets the amount of damage dealt in the event.  |  Event  |  number  |    |    |
|  event_damage_cause  |  Damage received reason  |  Gets the reason or type of damage received in the event.  |  Event  |  text  |    |    |
|  event_death_screen_message  |  Death message  |  Gets the message shown on the death screen.  |  Event  |  text  |  The "Player dies" event  |    |
|  event_drag_type  |  Inventory drag type  |  Gets the drag type of items across the target open inventory in the event.  |  Event  |  text  |  The "Player drags item in inventory" event  |    |
|  event_enchantment_bonus  |  Bookshelf count  |  Gets the number of bookshelves associated with the event.  |  Event  |  number  |  The "Player chooses enchantment" event  |    |
|  event_enchantment_hint  |  Suggested enchantment  |  Gets the name of the offered enchantment in the enchanting table.  |  Event  |  text  |  The "Player enchants item" event  |    |
|  event_enchantment_level_hint  |  Required enchantment experience level  |  Gets the required experience level for the chosen enchantment.  |  Event  |  number  |  The "Player enchants item" event  |    |
|  event_enchantment_offers  |  Event suggested enchantments  |  Gets the list of enchantments offered to the player, associated with the event.  |  Event  |  array<text>  |  The "Player chooses enchantment" event  |    |
|  event_enchantments_to_add  |  Received enchantments  |  Gets the map of the item received enchantments.  |  Event  |  map<text, number>  |  The "Player enchants item" event  |    |
|  event_entity_unleash_reason  |  Entity untie reason  |  Gets the reason the entity was untied.  |  Event  |  text  |  Untie events  |    |
|  event_equipment_slot  |  Affected slot type  |  Gets the type of the target slot involved in the event.  |  Event  |  text  |    |    |
|  event_exhaustion_amount  |  Event exhaustion  |  Gets the amount of exhaustion received.  |  Event  |  number  |  The "Player exhausts" event  |    |
|  event_exhaustion_reason  |  Exhaustion reason  |  Gets the reason of exhaustion.  |  Event  |  text  |  The "Player exhausts" event  |    |
|  event_experience  |  Event experience amount  |  Gets the amount of experience in the event.  |  Event  |  number  |    |    |
|  event_fail_move_reason  |  Failed movement reason  |  Gets the reason of a failed movement.  |  Event  |  text  |  The "Player failed to move" event  |    |
|  event_final_damage  |  Final damage  |  Gets the final amount of damage dealt in the event.  |  Event  |  number  |    |    |
|  event_fish_state  |  Fishing event reason  |  Gets the fishing event reason.  |  Event  |  text  |  The "Player fishes" event  |    |
|  event_food_level  |  Event hunger restored  |  Gets the amount of hunger restored.  |  Event  |  number  |  The "Player hunger level change" event  |    |
|  event_from_location  |  Old player location  |  Gets the player old location.  |  Event  |  location  |    |    |
|  event_gamemode  |  Event game mode  |  Gets the game mode associated with the event.  |  Event  |  text  |  The "Player requested game mode menu" event  |    |
|  event_hanging_break_cause  |  Hanging entity removal reason  |  Gets the reason the hanging entity (painting, frame) was removed.  |  Event  |  text  |  The "Hanging entity broken" event  |    |
|  event_heal_amount  |  Health restored amount  |  Gets the amount of health restored in the event.  |  Event  |  number  |  The "Player regains health" event<br/>The "Entity regains health" event  |    |
|  event_heal_cause  |  Healing reason  |  Gets the reason of health restoration in the event.  |  Event  |  text  |  The "Player regains health" event<br/>The "Entity regains health" event  |    |
|  event_hotbar_slot  |  Event hotbar slot  |  Gets the current hotbar slot number in the event.  |  Event  |  number  |    |    |
|  event_input_list  |  Pressed movement key list  |  Gets the list of pressed movement keys of the event.  |  Event  |  array<text>  |  The "Player changes movement keys" event<br/>The "Player moves on vehicle" event<br/>The "Player jumps on vehicle" event  |    |
|  event_interaction  |  Event interaction type  |  Gets the target interaction type in the event.  |  Event  |  text  |  The "Player right-clicks" event<br/>The "Player left-clicks" event<br/>The "Player interacts with world" event  |    |
|  event_inventory_action  |  Inventory click action  |  Gets the current action in the inventory menu when clicking it.  |  Event  |  text  |    |    |
|  event_inventory_click_type  |  Inventory click type  |  Gets the click type on the target open inventory in the event.  |  Event  |  text  |    |    |
|  event_item  |  Event item  |  Gets the item in the event.  |  Event  |  item  |    |    |
|  event_item_cooldown  |  Event item cooldown  |  Gets the event item cooldown.  |  Event  |  number  |  The "Player uses item with cooldown" event<br/>The "Player gets item group cooldown" event  |    |
|  event_item_cooldown_group  |  Item group on cooldown  |  Gets the item group the event cooldown applies to.  |  Event  |  text  |  The "Player uses item with cooldown" event<br/>The "Player gets item group cooldown" event  |    |
|  event_item_damage  |  Item damage dealt  |  Gets the amount of damage dealt to the item.  |  Event  |  number  |  The "Player damages item" event  |    |
|  event_items  |  Event items  |  Gets all items in the event.  |  Event  |  array<item>  |    |    |
|  event_knockback_cause  |  Knockback reason  |  Gets the knockback reason in the event.  |  Event  |  text  |  The "Player is knocked back" event<br/>The "Entity is knocked back" event  |    |
|  event_knockback_event_type  |  Knockback type  |  Gets the knockback type in the event.  |  Event  |  text  |  The "Player is knocked back" event<br/>The "Entity is knocked back" event  |    |
|  event_knockback_vector  |  Knockback vector  |  Gets the knockback vector in the event.  |  Event  |  vector  |  The "Player is knocked back" event<br/>The "Entity is knocked back" event  |    |
|  event_message  |  Event message  |  Gets the system message sent in the event.  |  Event  |  text  |    |    |
|  event_new_equipments  |  Equipment  |  Gets the equipment from the event.  |  Event  |  map<text, item>  |  The "Player changes equipment" event<br/>The "Entity changes equipment" event  |    |
|  event_new_fishing_hook_state  |  New bobber state  |  Gets the bobber new state.  |  Event  |  text  |  The "Fishing bobber changes state" event  |    |
|  event_new_location  |  New player location  |  Gets the player new location.  |  Event  |  location  |    |    |
|  event_new_potion_effect  |  New effect  |  Gets the event new effect.  |  Event  |  potion  |  The "Player gets splash potion effect" event  |    |
|  event_new_vault_state  |  New vault state  |  Gets the vault new state.  |  Event  |  text  |  The "Vault changes state" event<br/>The "Player changes vault state" event  |    |
|  event_old_equipments  |  Previous event equipment  |  Gets the event previous equipment.  |  Event  |  map<text, item>  |  The "Player changes equipment" event<br/>The "Entity changes equipment" event  |    |
|  event_old_item  |  Old event item  |  Gets the old item in the event.  |  Event  |  item  |  The "Player inventory slot updates" event  |    |
|  event_old_vault_state  |  Previous vault state  |  Gets the vault previous state.  |  Event  |  text  |  The "Vault changes state" event<br/>The "Player changes vault state" event  |    |
|  event_power  |  Draw power percentage  |  Gets the event execution power percentage (bow tension, horse jump).  |  Event  |  number  |  The "Player shoots" event<br/>The "Player jumps on horse" event  |    |
|  event_projectile_item  |  Event projectile item  |  Gets the event projectile item.  |  Event  |  item  |  The "Player shoots" event  |    |
|  event_query_info  |  Debug info  |  Gets the debug information of the target block or entity.  |  Event  |  text  |  The "Player receives block info" event<br/>The "Player receives entity info" event  |    |
|  event_replaced_block  |  Replaced block  |  Gets the event replaced block ID.  |  Event  |  text  |  The "Player places block" event  |    |
|  event_sign_lines  |  Sign lines  |  Gets the sign lines as a list.  |  Event  |  array<text>  |  The "Player edits sign" event  |    |
|  event_sign_side  |  Sign side  |  Gets the sign face as text.  |  Event  |  text  |  The "Player edits sign" event  |    |
|  event_slot  |  Event slot  |  Yields the slot number in the event.  |  Event  |  number  |    |    |
|  event_slot_type  |  Click slot type  |  Gets the current inventory menu slot type when clicking it.  |  Event  |  text  |    |    |
|  event_slots_involved  |  Affected slots  |  Gets the list of all involved slots of the target open inventory in the event.  |  Event  |  array<number>  |  The "Player drags item in inventory" event  |    |
|  event_teleport_cause  |  Teleport reason  |  Gets the teleportation reason in the event.  |  Event  |  text  |  The "Player teleported" event<br/>The "Enderman escapes" event  |    |
|  event_ticks_held_for  |  Item use tick count  |  Gets the number of item use ticks.  |  Event  |  number  |  The "Player stops using item" event  |    |
|  event_time_skip_amount  |  Time skip tick count  |  Gets the number of world time skip ticks.  |  Event  |  number  |  The "Time skip" event  |    |
|  event_time_skip_reason  |  Time skip reason  |  Gets the reason of the world time skip.  |  Event  |  text  |  The "Time skip" event  |    |
|  event_transform_reason  |  Entity replacement reason  |  Gets the event entity replacement reason.  |  Event  |  text  |  The "Entity replaced by another entity" event  |    |
|  event_transformed_entities  |  Event replaced entities  |  Gets the event replaced entities.  |  Event  |  array<text>  |  The "Entity replaced by another entity" event  |    |
|  event_tree_type  |  Tree type  |  Gets the tree type in the event.  |  Event  |  text  |  The "Player grows tree" event<br/>The "Tree grows" event  |    |
|  event_velocity  |  Velocity vector  |  Gets the velocity vector in the event.  |  Event  |  vector  |  The "Player changed velocity vector" event  |    |
|  experience_level  |  Experience level  |  Gets the number of the target experience levels.  |  Statistics  |  number  |    |    |
|  experience_progress  |  Experience progress  |  Gets the percentage progress of the target current experience level.  |  Statistics  |  number  |    |    |
|  eye_location  |  Eye location  |  Gets the target location at eye height.  |  Location  |  location  |    |    |
|  fall_distance  |  Fall distance  |  Gets the target fall distance in blocks.  |  Statistics  |  number  |    |    |
|  fire_ticks  |  Burn time  |  Gets the remaining target burn ticks.  |  Statistics  |  number  |    |    |
|  flying_speed  |  Flight speed  |  Gets the target current flying speed (attribute).  |  Statistics  |  number  |    |    |
|  food_exhaustion  |  Exhaustion level  |  Gets the target exhaustion level, which grows from the player performed actions.  |  Statistics  |  number  |    |    |
|  food_level  |  Hunger level  |  Gets the remaining amount of the target food points.  |  Statistics  |  number  |    |    |
|  food_saturation  |  Saturation level  |  Gets the amount of the target food saturation, depending on the kinds of food eaten.  |  Statistics  |  number  |    |    |
|  freeze_ticks  |  Freeze time  |  Gets the target current freeze time.  |  Statistics  |  number  |    |    |
|  gamemode  |  Game mode  |  Gets the player current game mode.  |  Info  |  text  |  Players  |    |
|  held_slot  |  Selected hotbar slot  |  Gets the target selected hotbar slot.  |  Statistics  |  number  |    |    |
|  hitbox_midpoint_location  |  Hitbox center  |  Gets the target hitbox center location.  |  Location  |  location  |    |    |
|  hotbar_items  |  Hotbar items  |  Gets the items in the target hotbar.  |  Item  |  array<item>  |    |    |
|  idle_duration  |  Idle duration  |  Gets the player current idle duration.  |  Statistics  |  number  |    |    |
|  inventory_items  |  Inventory items  |  Gets the items in the target inventory (including the hotbar).  |  Item  |  array<item>  |    |    |
|  invulnerability_ticks  |  Invulnerability time  |  Gets the remaining target invulnerability ticks.  |  Statistics  |  number  |    |    |
|  item_usage_progress  |  Item use progress  |  Gets the percentage progress of the target using the item in hand, e.g. food.  |  Statistics  |  number  |    |    |
|  last_damage_cause  |  Last damage reason  |  Gets the target last damage reason.  |  Info  |  text  |    |    |
|  last_death_location  |  Last death location  |  Gets the player last death location.  |  Location  |  location  |    |    |
|  lead_holder  |  Guide  |  Gets the UUID of the entity leading the target on a leash.  |  Info  |  text  |    |    |
|  location  |  Location  |  Gets the target location.  |  Location  |  location  |    |    |
|  main_hand  |  Main hand  |  Gets the player main hand.  |  Info  |  text  |  Players  |    |
|  main_hand_item  |  Main hand item  |  Gets the item in the target main hand.  |  Item  |  item  |    |    |
|  max_health  |  Max health  |  Gets the maximum amount of the target health.  |  Statistics  |  number  |    |    |
|  max_invulnerability_ticks  |  Total invulnerability time  |  Gets the number of ticks the target invulnerability was granted for.  |  Statistics  |  number  |    |    |
|  merchant_recipe_count  |  Villager trade count  |  Gets the number of the Villager trades.  |  Statistics  |  number  |    |    |
|  name  |  Name  |  Gets the target name.  |  Info  |  text  |    |    |
|  off_hand_item  |  Off-hand item  |  Gets the item in the target offhand.  |  Item  |  item  |    |    |
|  open_inventory_custom_id  |  Open inventory custom ID  |  Gets the custom ID of the target open inventory.  |  Info  |  text  |  Players  |    |
|  open_inventory_size  |  Open inventory size  |  Gets the size of the currently open inventory.  |  Statistics  |  number  |  Players  |    |
|  open_inventory_title  |  Open inventory title  |  Gets the title of the target open inventory.  |  Info  |  text  |  Players  |    |
|  open_inventory_type  |  Open inventory type  |  Gets the type of the target open inventory.  |  Info  |  text  |  Players  |    |
|  origin  |  First spawn location  |  Gets the target first spawn location.  |  Location  |  location  |    |    |
|  owner_uuid  |  World owner UUID  |  Gets the world owner UUID.  |  World  |  text  |    |    |
|  particle_cpu_usage  |  Particle CPU usage percentage  |  Gets the percentage of the server CPU load by particle creation.  |  World  |  number  |    |    |
|  particle_visibility  |  Particle visibility  |  Gets the player particle visibility setting value.  |  Info  |  text  |  Players  |    |
|  passengers  |  Passengers  |  Gets the UUIDs of the entities riding the target.  |  Info  |  array<text>  |    |    |
|  ping  |  Player ping  |  Gets the player-server latency in milliseconds.  |  Statistics  |  number  |    |    |
|  pitch  |  Vertical rotation  |  Gets the target vertical (up/down) rotation (pitch).  |  Location  |  number  |    |    |
|  player_count  |  Player count in world  |  Gets the number of players in the world.  |  World  |  number  |    |    |
|  player_ender_pearls  |  Ender pearl list  |  Gets the list of the player unlanded ender pearls.  |  Info  |  array<text>  |  Players  |    |
|  player_enderchest_items  |  Ender chest items  |  Gets the items in the target ender chest.  |  Item  |  array<item>  |  Players  |    |
|  pose  |  Entity pose  |  Gets the entity pose.  |  Info  |  text  |    |    |
|  potion_effects  |  Potion effects  |  Gets the target active potion effects.  |  Info  |  array<potion>  |    |    |
|  projectile_owner_uuid  |  Projectile owner UUID  |  Gets the projectile owner UUID.  |  Info  |  text  |  Any projectiles  |    |
|  projectile_power  |  Projectile motion vector  |  Gets the projectile motion vector.  |  Statistics  |  vector  |  Fireballs<br/>Dragon charges<br/>Wither skulls  |    |
|  protocol_version  |  Client protocol version  |  Gets the player client protocol version.  |  Statistics  |  number  |    |    |
|  remaining_air  |  Remaining air  |  Gets the remaining target air ticks.  |  Statistics  |  number  |    |    |
|  response_headers  |  Web response headers  |  Gets the response headers of the sent web request.  |  Event  |  map<text, any>  |  The "Server response" event  |    |
|  saddle_item  |  Saddle item  |  Gets the saddle or carpet equipped on the target.  |  Item  |  item  |  Pigs<br/>Horses<br/>Llamas  |    |
|  saturated_regen_rate  |  Saturation regeneration speed  |  Gets the player saturated regeneration rate.  |  Statistics  |  number  |    |    |
|  selection_size  |  Selected target count  |  Gets the number of targets in the selection.  |  World  |  number  |    |    |
|  selection_target_names  |  Selected target names  |  Gets the name of each target in the selection.  |  World  |  array<text>  |    |    |
|  selection_target_uuids  |  Selected target UUIDs  |  Gets the UUID of each target in the selection.  |  World  |  array<text>  |    |    |
|  server_current_tick  |  Current server time  |  Gets the current server time in ticks.  |  World  |  number  |    |    |
|  server_tps  |  Server TPS  |  Gets the Ticks Per Second (TPS) the server can process.  |  World  |  number  |    |    |
|  spawn_location  |  World spawn location  |  Gets the world spawn point location.  |  Location  |  location  |    |    |
|  spawn_reason  |  Spawn reason  |  Gets the target spawn reason.  |  Info  |  text  |    |    |
|  start_reload_tick  |  World freeze start time  |  Gets the world freeze start time in ticks.  |  World  |  number  |    |    |
|  starvation_rate  |  Starvation speed  |  Gets the target starvation rate.  |  Statistics  |  number  |    |    |
|  steer_forward  |  Vehicle forward speed  |  Gets the vehicle forward or backward movement value.  |  Statistics  |  number  |    |    |
|  steer_sideways  |  Vehicle sideways speed  |  Gets the vehicle left or right movement value.  |  Statistics  |  number  |    |    |
|  target_block_face  |  Target block face  |  Gets the direction of the block face the target is looking at.  |  Location  |  text  |    |    |
|  target_block_location  |  Target block location  |  Gets the location of the block the target is looking at.  |  Location  |  location  |    |    |
|  target_fluid_location  |  Target fluid location  |  Gets the location of the fluid the target is looking at.  |  Location  |  location  |    |    |
|  targeted_entity  |  Attack target  |  Gets the mob current attack target.  |  Info  |  text  |    |    |
|  timestamp  |  UNIX time  |  Gets the current time as a single number in milliseconds.  |  World  |  number  |    |    |
|  unsaturated_regen_rate  |  Regeneration speed without saturation  |  Gets the player unsaturated regeneration rate.  |  Statistics  |  number  |    |    |
|  url  |  Web request URL  |  Gets the web request URL.  |  Event  |  text  |  The "Server response" event  |    |
|  url_response  |  Web request response  |  Gets the response to the sent web request.  |  Event  |  text  |  The "Server response" event  |    |
|  url_response_code  |  Web response code  |  Gets the response code of the sent web request.  |  Event  |  number  |  The "Server response" event  |    |
|  user_locale  |  Player server language  |  Gets the player current server language.  |  Info  |  text  |  Players  |    |
|  uuid  |  UUID  |  Gets the target universally unique identifier (UUID).  |  Info  |  text  |    |    |
|  vehicle  |  Vehicle  |  Gets the UUID of the entity the target is riding.  |  Info  |  text  |    |    |
|  velocity  |  Velocity vector  |  Gets the target velocity motion vector (not walking, but external forces).  |  Info  |  vector  |    |    |
|  walking_speed  |  Walk speed  |  Gets the target current walking speed (attribute).  |  Statistics  |  number  |    |    |
|  world_clear_weather_duration  |  World clear weather duration  |  Gets the current clear weather duration in the world.  |  World  |  number  |    |    |
|  world_game_time  |  World age  |  Gets the world existence time in ticks.  |  World  |  number  |    |    |
|  world_id  |  World ID  |  Gets the world identifier.  |  World  |  text  |    |    |
|  world_moon_phase  |  Current moon phase  |  Gets the current moon phase in the world.  |  World  |  text  |    |    |
|  world_size  |  World size  |  Gets the current world size in chunks.  |  World  |  number  |    |    |
|  world_thunder_duration  |  Rain duration in the world  |  Gets the current rain duration in the world.  |  World  |  number  |    |    |
|  world_time  |  Current world time  |  Gets the current world time in ticks.  |  World  |  number  |    |    |
|  world_weather  |  Current world weather  |  Gets the current world weather type.  |  World  |  text  |    |    |
|  world_weather_duration  |  Duration of the current world weather  |  Gets the current world weather duration.  |  World  |  number  |    |    |
|  x_coordinate  |  Coordinate X  |  Gets the target location X coordinate.  |  Location  |  number  |    |    |
|  y_coordinate  |  Coordinate Y  |  Gets the target location Y coordinate.  |  Location  |  number  |    |    |
|  yaw  |  Horizontal rotation  |  Gets the target horizontal (left/right) rotation (yaw).  |  Location  |  number  |    |    |
|  z_coordinate  |  Coordinate Z  |  Gets the target location Z coordinate.  |  Location  |  number  |    |    |

