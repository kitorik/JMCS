# World actions
> **Enum macros:** {TF} = TRUE / FALSE; {TFN} = TRUE / FALSE / NOT_SET; {ANY_ALL} = ANY / ALL; {ITEM_MATCH} = EXACT / IGNORE_NAME_DURABILITY / IGNORE_NAME_DURABILITY_ENCHANTMENTS / CUSTOM_TAGS_CONTAINS / MINECRAFT_TAG / ITEM_TYPE; {DEG_RAD} = DEGREES / RADIANS; {CMP} = EXACTLY / IGNORE_STACK_SIZE / IGNORE_DURABILITY_AND_STACK_SIZE / TYPE_ONLY. Icon column omitted.


|  ID  |  Name  |  Description  |  Category/Subcategory  |  Arguments  |  Works with  |  Additional info  |  Status  |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
|  game_add_custom_cooking_recipe  |  Add smelting recipe  |  Adds a custom furnace or smoker recipe to the game  |  game/recipe  |  name: text<br/>input: item<br/>result: item<br/>experience: number<br/>cooking_time: number<br/>replace_vanilla: enum<br/>{TF}<br/>input_match: enum<br/>{ITEM_MATCH}<br/>recipe_type: enum<br/>&nbsp;&nbsp;- FURNACE<br/>&nbsp;&nbsp;- BLASTING<br/>&nbsp;&nbsp;- SMOKING<br/>&nbsp;&nbsp;- CAMPFIRE<br/>category: enum<br/>&nbsp;&nbsp;- FOOD<br/>&nbsp;&nbsp;- BLOCKS<br/>&nbsp;&nbsp;- MISC  |    |    |    |
|  game_add_custom_crafting_recipe  |  Add crafting recipe  |  Adds a custom crafting recipe to the world.  |  game/recipe  |  name: text<br/>items: item<br/>result: item<br/>replace_vanilla: enum<br/>{TF}<br/>recipe_match_slot_1: enum<br/>{ITEM_MATCH}<br/>recipe_match_slot_2: enum<br/>{ITEM_MATCH}<br/>recipe_match_slot_3: enum<br/>{ITEM_MATCH}<br/>recipe_match_slot_4: enum<br/>{ITEM_MATCH}<br/>recipe_match_slot_5: enum<br/>{ITEM_MATCH}<br/>recipe_match_slot_6: enum<br/>{ITEM_MATCH}<br/>recipe_match_slot_7: enum<br/>{ITEM_MATCH}<br/>recipe_match_slot_8: enum<br/>{ITEM_MATCH}<br/>recipe_match_slot_9: enum<br/>{ITEM_MATCH}<br/>recipe_type: enum<br/>&nbsp;&nbsp;- SHAPED<br/>&nbsp;&nbsp;- SHAPELESS<br/>category: enum<br/>&nbsp;&nbsp;- BUILDING<br/>&nbsp;&nbsp;- REDSTONE<br/>&nbsp;&nbsp;- EQUIPMENT<br/>&nbsp;&nbsp;- MISC  |    |    |    |
|  game_add_custom_smithing_transform_recipe  |  Add smithing upgrade recipe  |  Adds a custom smithing upgrade recipe in the smithing table  |  game/recipe  |  name: text<br/>template: item<br/>base: item<br/>addition: item<br/>result: item<br/>replace_vanilla: enum<br/>{TF}<br/>template_match: enum<br/>{ITEM_MATCH}<br/>base_match: enum<br/>{ITEM_MATCH}<br/>recipe_match: enum<br/>{ITEM_MATCH}<br/>copy_data_components: enum<br/>{TF}  |    |    |    |
|  game_add_custom_smithing_trim_recipe  |  Add smithing trim recipe  |  Adds a custom armor trim recipe in the smithing table  |  game/recipe  |  name: text<br/>template: item<br/>base: item<br/>addition: item<br/>trim: item<br/>replace_vanilla: enum<br/>{TF}<br/>template_match: enum<br/>{ITEM_MATCH}<br/>base_match: enum<br/>{ITEM_MATCH}<br/>addition_match: enum<br/>{ITEM_MATCH}<br/>copy_data_components: enum<br/>{TF}  |    |    |    |
|  game_add_custom_stonecutting_recipe  |  Add stonecutter recipe  |  Adds a custom stonecutter block-cutting recipe  |  game/recipe  |  name: text<br/>input: item<br/>result: item<br/>replace_vanilla: enum<br/>{TF}<br/>input_match: enum<br/>{ITEM_MATCH}  |    |    |    |
|  game_add_custom_transmute_recipe  |  Add transmutation recipe  |  Adds a custom item transmutation recipe to the world.  |  game/recipe  |  name: text<br/>input: item<br/>material: item<br/>result: item<br/>replace_vanilla: enum<br/>{TF}<br/>input_match: enum<br/>{ITEM_MATCH}<br/>material_match: enum<br/>{ITEM_MATCH}<br/>category: enum<br/>&nbsp;&nbsp;- BUILDING<br/>&nbsp;&nbsp;- REDSTONE<br/>&nbsp;&nbsp;- EQUIPMENT<br/>&nbsp;&nbsp;- MISC  |    |    |    |
|  game_block_growth  |  Set block growth stage  |  Sets the growth stage for the block at the chosen location.  |  game/block  |  location: location<br/>growth_stage: number<br/>growth_type: enum<br/>&nbsp;&nbsp;- STAGE_NUMBER<br/>&nbsp;&nbsp;- PERCENTAGE  |    |    |    |
|  game_bloom_skulk_catalyst  |  Extend sculk infection to location  |  Extends the sculk infection towards the location.  |  game/block  |  location: location<br/>bloom_location: location<br/>charge: number  |  Sculk catalysts  |    |    |
|  game_bone_meal_block  |  Fertilize block  |  Fertilizes the block at the chosen location.  |  game/block  |  location: location<br/>count: number  |    |    |    |
|  game_break_block  |  Break block  |  Breaks the blocks at the given locations as if a survival-mode player did it with the proper tool.  |  game/block  |  locations: location<br/>tool: item<br/>drop_exp: enum<br/>{TF}  |    |    |    |
|  game_cancel_event  |  Cancel event  |  Cancels the initial event that triggered this code.  |  game/event  |    |    |    |    |
|  game_chunk_get_custom_tag  |  Get chunk custom tag  |  Gets the chunk custom tag and assigns the result to a variable.  |  game/block  |  variable: variable<br/>location: location<br/>tag_name: text<br/>default_value: any  |    |    |    |
|  game_chunk_get_custom_tags  |  Get chunk custom tags  |  Gets the chunk custom tags and assigns the result to a variable.  |  game/block  |  variable: variable<br/>location: location  |    |    |    |
|  game_chunk_remove_custom_tag  |  Remove chunk custom tag  |  Removes the given chunk custom tags.  |  game/block  |  location: location<br/>tag_names: text  |    |    |    |
|  game_chunk_remove_custom_tags  |  Remove chunk custom tags  |  Removes all chunk custom tags.  |  game/block  |  location: location  |    |    |    |
|  game_chunk_set_custom_tag  |  Set chunk custom tag  |  Sets the given chunk custom tags.  |  game/block  |  location: location<br/>tag_names: text<br/>tag_values: text  |    |    |    |
|  game_clear_container  |  Clear container  |  Removes all items from the container at the chosen location.  |  game/block  |  location: location  |  Any containers  |    |    |
|  game_clear_container_items  |  Clear items in container  |  Clears the given items from the container.  |  game/block  |  location: location<br/>items: item  |  Any containers  |    |    |
|  game_clear_custom_recipes  |  Clear custom recipes  |  Clears all custom recipes.  |  game/recipe  |    |    |    |    |
|  game_clear_exploded_blocks  |  Clear exploded blocks  |  Restores the exploded blocks to their original state.  |  game/event  |  location: location  |  The "Entity explodes" event<br/>The "Block explodes" event  |    |    |
|  game_clear_region  |  Clear region  |  Removes all blocks in the region.  |  game/block  |  pos_1: location<br/>pos_2: location  |    |    |    |
|  game_clear_scoreboard_scores  |  Clear scoreboard values  |  Clears all values of the given scoreboard.  |  game/scoreboard  |  id: text  |    |    |    |
|  game_clone_region  |  Clone region blocks  |  Clones the region to the chosen location.  |  game/block  |  pos_1: location<br/>pos_2: location<br/>target_pos: location<br/>paste_pos: location<br/>ignore_air: enum<br/>{TF}<br/>copy_entity: enum<br/>{TF}  |    |    |    |
|  game_create_explosion  |  Create explosion  |  Creates an explosion at the given location.  |  game/entity  |  location: location<br/>power: number<br/>name_or_uuid: text<br/>fire: enum<br/>{TF}<br/>break_blocks: enum<br/>{TF}  |    |    |    |
|  game_create_scoreboard  |  Create scoreboard  |  Creates a scoreboard with the given ID. To show the scoreboard to the player, use the "Show scoreboard" action.  |  game/scoreboard  |  id: text<br/>display_name: text  |    |    |    |
|  game_fill_container  |  Fill container  |  Fills the container at the chosen location with the given items.  |  game/block  |  location: location<br/>items: item  |  Any containers  |    |    |
|  game_generate_tree  |  Create tree  |  Creates a tree at the chosen location.  |  game/block  |  location: location<br/>tree_type: enum<br/>&nbsp;&nbsp;- TREE<br/>&nbsp;&nbsp;- ACACIA<br/>&nbsp;&nbsp;- BIG_TREE<br/>&nbsp;&nbsp;- BIRCH<br/>&nbsp;&nbsp;- BROWN_MUSHROOM<br/>&nbsp;&nbsp;- CHORUS_PLANT<br/>&nbsp;&nbsp;- COCOA_TREE<br/>&nbsp;&nbsp;- CRIMSON_FUNGUS<br/>&nbsp;&nbsp;- DARK_OAK<br/>&nbsp;&nbsp;- JUNGLE<br/>&nbsp;&nbsp;- JUNGLE_BUSH<br/>&nbsp;&nbsp;- MEGA_REDWOOD<br/>&nbsp;&nbsp;- REDWOOD<br/>&nbsp;&nbsp;- RED_MUSHROOM<br/>&nbsp;&nbsp;- SMALL_JUNGLE<br/>&nbsp;&nbsp;- SWAMP<br/>&nbsp;&nbsp;- TALL_BIRCH<br/>&nbsp;&nbsp;- TALL_REDWOOD<br/>&nbsp;&nbsp;- WARPED_FUNGUS<br/>&nbsp;&nbsp;- AZALEA<br/>&nbsp;&nbsp;- MANGROVE<br/>&nbsp;&nbsp;- TALL_MANGROVE<br/>&nbsp;&nbsp;- CHERRY<br/>&nbsp;&nbsp;- MEGA_PINE<br/>&nbsp;&nbsp;- PALE_OAK_CREAKING<br/>&nbsp;&nbsp;- PALE_OAK  |    |    |    |
|  game_get_tile_block_custom_tags  |  Get block entity custom tags  |  Gets the block entity custom tags and assigns the result to a variable.  |  game/block  |  variable: variable<br/>location: location  |  Block entities (chests, signs, barrels, etc.)  |    |    |
|  game_hide_event_message  |  Remove event message  |  Suppresses the event message of the event that triggered this code.  |  game/event  |  hide: enum<br/>{TF}  |  The "Player joins world" event<br/>The "Player leaves world" event<br/>The "Player dies" event  |    |    |
|  game_launch_firework  |  Create firework  |  Launches a firework at the given location.  |  game/entity  |  firework: item<br/>location: location<br/>movement: enum<br/>&nbsp;&nbsp;- UPWARDS<br/>&nbsp;&nbsp;- DIRECTIONAL<br/>instant: enum<br/>{TF}  |    |    |    |
|  game_launch_projectile  |  Launch projectile  |  Launches a projectile at the given location.  |  game/entity  |  projectile: item<br/>location: location<br/>speed: number<br/>inaccuracy: number<br/>custom_name: text<br/>trail: particle  |    |    |    |
|  game_random_tick_block  |  Trigger random tick  |  Triggers a random tick at the chosen location.  |  game/block  |  location: location<br/>times: number  |    |    |    |
|  game_remove_container_items  |  Remove items from container  |  Removes the given items from the container at the chosen location.  |  game/block  |  location: location<br/>items: item  |  Any containers  |    |    |
|  game_remove_custom_recipe  |  Remove custom recipe  |  Removes a custom recipe from the world.  |  game/recipe  |  names: text<br/>remove_vanilla: enum<br/>{TF}  |    |    |    |
|  game_remove_scoreboard  |  Remove scoreboard  |  Removes the given scoreboard.  |  game/scoreboard  |  id: text  |    |    |    |
|  game_remove_scoreboard_score_by_name  |  Remove scoreboard value by text  |  Removes the value of the given scoreboard row.  |  game/scoreboard  |  id: text<br/>text: text  |    |    |    |
|  game_remove_scoreboard_score_by_score  |  Remove scoreboard value by score  |  Removes the value of the given scoreboard by score.  |  game/scoreboard  |  id: text<br/>score: number  |    |    |    |
|  game_remove_tile_block_custom_tag  |  Remove block entity custom tag  |  Removes the given block entity custom tag at the location.  |  game/block  |  location: location<br/>tag_name: text  |  Block entities (chests, signs, barrels, etc.)  |    |    |
|  game_remove_tile_block_custom_tags  |  Remove block entity custom tags  |  Removes all block entity custom tags.  |  game/block  |  location: location  |  Block entities (chests, signs, barrels, etc.)  |    |    |
|  game_replace_blocks_in_region  |  Replace blocks in region  |  Replaces some blocks with others in the chosen region.  |  game/block  |  old_block: block<br/>pos_1: location<br/>pos_2: location<br/>new_block: block  |    |    |    |
|  game_replace_container_items  |  Replace items in container  |  Replaces the given items in the container at the chosen location with a certain item.  |  game/block  |  items: item<br/>location: location<br/>replace: item<br/>count: number  |  Any containers  |    |    |
|  game_send_web_request  |  Send web request  |  Sends a web request with the chosen method and body to the chosen URL.  |  game/web  |  url: text<br/>content_body: text<br/>headers: map<br/>request_type: enum<br/>&nbsp;&nbsp;- GET<br/>&nbsp;&nbsp;- HEAD<br/>&nbsp;&nbsp;- POST<br/>&nbsp;&nbsp;- PUT<br/>&nbsp;&nbsp;- PATCH<br/>&nbsp;&nbsp;- DELETE<br/>content_type: enum<br/>&nbsp;&nbsp;- TEXT_PLAIN<br/>&nbsp;&nbsp;- APPLICATION_JSON  |    |    |    |
|  game_set_age  |  Set age  |  Sets the block age at the chosen location.  |  game/block  |  location: location<br/>tick: number  |  Any blocks that can have an age  |    |    |
|  game_set_block  |  Set block  |  Sets the chosen block type at the chosen locations.  |  game/block  |  block: block<br/>locations: location<br/>update_blocks: enum<br/>{TF}  |    |    |    |
|  game_set_block_analogue_power  |  Set redstone signal power  |  Sets the given signal strength at the chosen location.  |  game/block  |  location: location<br/>power_level: number  |  Activatable blocks  |    |    |
|  game_set_block_data  |  Set block properties  |  Sets block properties at the given location.  |  game  |  location: location<br/>block_data: text  |    |    |  deprecated  |
|  game_set_block_drops_enabled  |  Set block drops  |  Sets the world rule for block drops when blocks are broken.  |  game/settings  |  enable: enum<br/>{TF}  |    |    |    |
|  game_set_block_nbt  |  Set block entity NBT tags  |  Sets the given NBT tag on the block entity at the location.  |  game/block  |  location: location<br/>tag_names: text<br/>tag_values: text  |  Block entities  |  Only NBT tags supported by the target block entity can be set.  |    |
|  game_set_block_powered  |  Activate block  |  Activates the block at the chosen location.  |  game/block  |  location: location<br/>powered: enum<br/>{TF}  |  Activatable blocks  |    |    |
|  game_set_block_single_data  |  Set block property  |  Sets the given block property at the location to the given value.  |  game/block  |  location: location<br/>data: text<br/>value: text  |    |    |    |
|  game_set_brushable_block_item  |  Set item in suspicious block  |  Sets the item into the suspicious block (sand, gravel) at the chosen location.  |  game/block  |  location: location<br/>item: item  |  Suspicious sand<br/>Suspicious gravel  |    |    |
|  game_set_campfire_item  |  Set item in campfire  |  Sets the item into the campfire at the chosen location.  |  game/block  |  location: location<br/>item: item<br/>cooking_time: number<br/>slot: enum<br/>&nbsp;&nbsp;- FIRST<br/>&nbsp;&nbsp;- SECOND<br/>&nbsp;&nbsp;- THIRD<br/>&nbsp;&nbsp;- FOURTH  |  Campfires  |    |    |
|  game_set_container  |  Set items in container  |  Sets the given items into the container at the chosen location.  |  game/block  |  location: location<br/>items: item  |  Any containers  |    |    |
|  game_set_container_lock  |  Set container key  |  Sets the given key for the container at the chosen location.  |  game/block  |  location: location<br/>container_key: text  |    |  Any item with a specific name serves as the container key.  |    |
|  game_set_container_name  |  Set container name  |  Sets the container name at the chosen location.  |  game/block  |  location: location<br/>name: text  |  Any containers  |    |    |
|  game_set_copper_golem_statue_pose  |  Set copper golem statue pose  |  Sets the given pose for the copper golem statue at the given location.  |  game/block  |  location: location<br/>pose: enum<br/>&nbsp;&nbsp;- STANDING<br/>&nbsp;&nbsp;- SITTING<br/>&nbsp;&nbsp;- RUNNING<br/>&nbsp;&nbsp;- STAR  |  Copper golem statues  |    |    |
|  game_set_creaking_heart_natural  |  Set creeper vine naturalness  |  Sets whether the creaking heart at the given location is natural.  |  game/block  |  location: location<br/>natural: enum<br/>{TF}  |  Creeper vines  |  Creeper vine naturalness determines whether experience drops when it is destroyed.   |    |
|  game_set_creaking_heart_state  |  Set creeper vine state  |  Sets the state of the creaking heart at the given location.  |  game/block  |  location: location<br/>heart_state: enum<br/>&nbsp;&nbsp;- UPROOTED<br/>&nbsp;&nbsp;- DORMANT<br/>&nbsp;&nbsp;- AWAKE  |  Creeper vines  |    |    |
|  game_set_decorate_pot_sherd  |  Set vase decoration  |  Sets the given sherd on the chosen pot face at the given location.  |  game/block  |  location: location<br/>item: item<br/>side: enum<br/>&nbsp;&nbsp;- BACK<br/>&nbsp;&nbsp;- FRONT<br/>&nbsp;&nbsp;- LEFT<br/>&nbsp;&nbsp;- RIGHT  |  Vases  |    |    |
|  game_set_dried_ghast_hydration  |  Set dried ghast dampness  |  Sets the humidity of the dried ghast at the given location.  |  game/block  |  location: location<br/>hydration: number  |  Dried ghasts  |    |    |
|  game_set_event_anvil_damage_state  |  Set anvil damage state  |  Sets the anvil break state.  |  game/event  |  damage_state: enum<br/>&nbsp;&nbsp;- FULL<br/>&nbsp;&nbsp;- CHIPPED<br/>&nbsp;&nbsp;- DAMAGED<br/>&nbsp;&nbsp;- BROKEN  |  The "Player damages anvil" event  |    |    |
|  game_set_event_anvil_repair_cost  |  Set anvil action cost  |  Sets the cost of the action being performed in the anvil.  |  game/event  |  repair_cost: number<br/>repair_cost_type: enum<br/>&nbsp;&nbsp;- REPAIR_COST<br/>&nbsp;&nbsp;- REPAIR_ITEM_COUNT_COST<br/>&nbsp;&nbsp;- MAXIMUM_REPAIR_COST<br/>bypass_cost: enum<br/>{TF}  |  The "Player receives result" event  |    |    |
|  game_set_event_combust_duration  |  Set event burn time  |  Sets the burn time associated with this event.  |  game/event  |  duration: number  |  The "Player ignites" event<br/>The "Entity ignites" event  |    |    |
|  game_set_event_damage  |  Set event damage  |  Sets the damage associated with this event.  |  game/event  |  damage: number  |  Damage events<br/>The "Player damages item" event  |    |    |
|  game_set_event_death_screen_message  |  Set death message  |  Sets the death message shown on the death screen, associated with this event.  |  game/event  |  message: text  |  The "Player dies" event  |  If the passed value is empty, the default message is set.<br/>The message is limited to 256 characters.  |    |
|  game_set_event_enchantment_offers  |  Set event suggested enchantments  |  Sets the event offered enchantments.  |  game/event  |  enchantments: text<br/>levels: number<br/>costs: number  |  The "Player chooses enchantment" event  |    |    |
|  game_set_event_exhaustion  |  Set event exhaustion  |  Sets the exhaustion value associated with this event.  |  game/event  |  exhaustion: number  |  The "Player exhausts" event  |    |    |
|  game_set_event_experience  |  Set event experience  |  Sets the experience value associated with this event.  |  game/event  |  experience: number  |  The "Player fishes" event<br/>The "Player picks up experience orb" event<br/>Kill events  |    |    |
|  game_set_event_gamemode  |  Set event game mode  |  Sets the game mode associated with the event.  |  game/event  |  gamemode: enum<br/>&nbsp;&nbsp;- SURVIVAL<br/>&nbsp;&nbsp;- CREATIVE<br/>&nbsp;&nbsp;- ADVENTURE<br/>&nbsp;&nbsp;- SPECTATOR  |  The "Player requested game mode menu" event  |    |    |
|  game_set_event_heal  |  Set event healing  |  Sets the healing value associated with this event.  |  game/event  |  heal: number  |  The "Player regains health" event<br/>The "Entity heals" event  |    |    |
|  game_set_event_item  |  Set event item  |  Sets the item associated with this event.  |  game/event  |  item: item  |    |    |    |
|  game_set_event_item_cooldown  |  Set event item cooldown  |  Sets the item delay associated with this event.  |  game/event  |  cooldown: number  |  The "Player uses item with cooldown" event<br/>The "Player gets item group cooldown" event  |    |    |
|  game_set_event_items  |  Set event items  |  Sets the items associated with this event.  |  game/event  |  items: item  |    |    |    |
|  game_set_event_knockback_vector  |  Set event knockback vector  |  Sets the knockback vector associated with this event.  |  game/event  |  knockback: vector  |  The "Player is knocked back" event<br/>The "Entity is knocked back" event  |    |    |
|  game_set_event_move_allowed  |  Allow movement  |  Allows the movement if it failed.  |  game/event  |  allowed: enum<br/>{TF}  |  The "Player failed to move" event  |    |    |
|  game_set_event_projectile  |  Set event projectile  |  Replaces the projectile associated with this event.  |  game/event  |  projectile: item<br/>name: text  |    |    |    |
|  game_set_event_should_drop_leash  |  Set lead drop  |  Sets whether the leash associated with the event drops.  |  game/event  |  should_drop_leash: enum<br/>{TF}  |  Untie events  |    |    |
|  game_set_event_should_play_effect  |  Set event particle creation  |  Sets whether the particles associated with the event are created.  |  game/event  |  should_play_effect: enum<br/>{TF}  |  The "Block failed to drop item" event  |    |    |
|  game_set_event_sound  |  Set event sound  |  Sets the sound to play associated with this event, replacing the original.  |  game/event  |  sound: sound  |    |    |    |
|  game_set_event_source_slot  |  Set event initial slot  |  Sets the initial slot associated with this event.  |  game/event  |  source_slot: number  |  The "Player finds item in inventory" event  |    |    |
|  game_set_event_target_slot  |  Set event final slot  |  Sets the final slot associated with this event.  |  game/event  |  target: number  |  The "Player finds item in inventory" event  |    |    |
|  game_set_event_uery_info  |  Set tags in received info  |  Sets additional tags into the received debug information that will be copied to the clipboard if the event is not cancelled.  |  game/event  |  information: text  |  The "Player receives block info" event<br/>The "Player receives entity info" event  |  Changes affect additional info only.  |    |
|  game_set_event_velocity  |  Set event velocity vector  |  Sets the velocity vector associated with this event.  |  game/event  |  velocity: vector  |  The "Player changed velocity vector" event  |    |    |
|  game_set_furnace_cook_time  |  Set furnace cook time  |  Sets the furnace cook time at the chosen location.  |  game/block  |  location: location<br/>time: number  |  Furnaces<br/>Blast furnaces<br/>Smokers  |    |    |
|  game_set_hardcore  |  creative_plus.action.game_set_hardcore.name  |  creative_plus.action.game_set_hardcore.description  |  game  |  hardcore: enum<br/>{TF}  |    |    |  deprecated  |
|  game_set_item_in_container_slot  |  Set item in container slot  |  Sets the item into the given container slot at the chosen location.  |  game/block  |  location: location<br/>item: item<br/>slot: number  |  Any containers  |    |    |
|  game_set_lectern_book  |  Set book in lectern  |  Sets the book into the lectern at the chosen location.  |  game/block  |  location: location<br/>item: item<br/>page: number  |  Lecterns  |    |    |
|  game_set_player_head  |  Set player head  |  Sets the player head at the chosen location.  |  game/block  |  location: location<br/>name_or_uuid: text<br/>receive_type: enum<br/>&nbsp;&nbsp;- NAME_OR_UUID<br/>&nbsp;&nbsp;- VALUE  |  Player heads  |    |    |
|  game_set_potent_sulfur_state  |  Set active sulfur state  |  Sets the active sulfur state.  |  game/block  |  location: location<br/>state: enum<br/>&nbsp;&nbsp;- DRY<br/>&nbsp;&nbsp;- WET<br/>&nbsp;&nbsp;- DORMANT<br/>&nbsp;&nbsp;- ERUPTING<br/>&nbsp;&nbsp;- CONTINUOUS  |  Active sulfur  |    |    |
|  game_set_region  |  Set blocks in region  |  Sets the chosen block type across the whole chosen region.  |  game/block  |  block: block<br/>pos_1: location<br/>pos_2: location  |    |    |    |
|  game_set_scoreboard_line  |  Set scoreboard line  |  Sets a line in the scoreboard.  |  game/scoreboard  |  id: text<br/>line: text<br/>display: text<br/>score: number<br/>format_content: text<br/>format: enum<br/>&nbsp;&nbsp;- BLANK<br/>&nbsp;&nbsp;- FIXED<br/>&nbsp;&nbsp;- STYLED<br/>&nbsp;&nbsp;- RESET  |    |    |    |
|  game_set_scoreboard_line_display  |  Set scoreboard line display text  |  Sets the displayed text of the given scoreboard line.  |  game/scoreboard  |  id: text<br/>line: text<br/>display: text  |    |    |    |
|  game_set_scoreboard_line_format  |  Set scoreboard line text format  |  Sets the text formatting of the given scoreboard line.  |  game/scoreboard  |  id: text<br/>line: text<br/>format_content: text<br/>format: enum<br/>&nbsp;&nbsp;- BLANK<br/>&nbsp;&nbsp;- FIXED<br/>&nbsp;&nbsp;- STYLED<br/>&nbsp;&nbsp;- RESET  |    |    |    |
|  game_set_scoreboard_number_format  |  Set scoreboard value formatting  |  Sets the value formatting for the scoreboard.  |  game/scoreboard  |  id: text<br/>format_content: text<br/>format: enum<br/>&nbsp;&nbsp;- BLANK<br/>&nbsp;&nbsp;- FIXED<br/>&nbsp;&nbsp;- STYLED<br/>&nbsp;&nbsp;- RESET  |    |    |    |
|  game_set_scoreboard_score  |  Set scoreboard value  |  Sets the value for the given scoreboard row.  |  game/scoreboard  |  id: text<br/>text: text<br/>score: number  |    |    |    |
|  game_set_scoreboard_title  |  Change scoreboard title  |  Changes the title of the given scoreboard.  |  game/scoreboard  |  id: text<br/>title: text  |    |    |    |
|  game_set_sculk_shrieker_can_summon  |  Set sculk shrieker summon ability  |  Sets whether the given sculk shrieker can summon the Warden.  |  game/block  |  location: location<br/>can_summon: enum<br/>{TF}  |  Sculk shriekers  |    |    |
|  game_set_sculk_shrieker_shrieking  |  Set sculk shrieker state  |  Sets the state of the given sculk shrieker.  |  game/block  |  location: location<br/>shrieking: enum<br/>{TF}  |  Sculk shriekers  |    |    |
|  game_set_sculk_shrieker_warning_level  |  Set sculk shrieker danger level  |  Sets the warning level of the given sculk shrieker.  |  game/block  |  location: location<br/>warning_level: number  |  Sculk shriekers  |    |    |
|  game_set_sign_text  |  Set sign text  |  Sets the sign text at the chosen location.  |  game/block  |  location: location<br/>text: text<br/>line: number<br/>side: enum<br/>&nbsp;&nbsp;- FRONT<br/>&nbsp;&nbsp;- BACK<br/>&nbsp;&nbsp;- ALL  |  Signs  |    |    |
|  game_set_sign_text_color  |  Set sign text color  |  Sets the sign text color at the chosen location.  |  game/block  |  location: location<br/>side: enum<br/>&nbsp;&nbsp;- FRONT<br/>&nbsp;&nbsp;- BACK<br/>&nbsp;&nbsp;- ALL<br/>sign_text_color: enum<br/>&nbsp;&nbsp;- BLACK<br/>&nbsp;&nbsp;- BLUE<br/>&nbsp;&nbsp;- BROWN<br/>&nbsp;&nbsp;- CYAN<br/>&nbsp;&nbsp;- GRAY<br/>&nbsp;&nbsp;- GREEN<br/>&nbsp;&nbsp;- LIGHT_BLUE<br/>&nbsp;&nbsp;- LIGHT_GRAY<br/>&nbsp;&nbsp;- LIME<br/>&nbsp;&nbsp;- MAGENTA<br/>&nbsp;&nbsp;- ORANGE<br/>&nbsp;&nbsp;- PINK<br/>&nbsp;&nbsp;- PURPLE<br/>&nbsp;&nbsp;- RED<br/>&nbsp;&nbsp;- WHITE<br/>&nbsp;&nbsp;- YELLOW<br/>glowing: enum<br/>{TF}  |  Signs  |    |    |
|  game_set_sign_waxed  |  Set sign wax state  |  Sets whether the sign at the chosen location is waxed.  |  game/block  |  location: location<br/>waxed: enum<br/>{TF}  |  Signs  |    |    |
|  game_set_spawner_entity  |  Set spawner entity  |  Sets the entity inside the spawner at the chosen location.  |  game/block  |  location: location<br/>entity: item  |  Spawners  |    |    |
|  game_set_tile_block_custom_tag  |  Set block entity custom tag  |  Sets the given custom tag on the block entity at the location.  |  game/block  |  location: location<br/>tag_name: text<br/>tag_value: text  |  Block entities (chests, signs, barrels, etc.)  |    |    |
|  game_set_vault_displayed_item  |  Set vault displayed item  |  Sets the displayed item of the vault at the given location.  |  game/block  |  location: location<br/>item: item  |  Vaults  |  Calling the action again overwrites the displayed item.  |    |
|  game_set_vault_next_state_update_time  |  Set vault time to next state  |  Sets the time until the next state transition of the vault at the given location.  |  game/block  |  location: location<br/>time: number  |  Vaults  |  Set the exact time when the vault switches to the next state.<br/>Defaults to the maximum possible value.  |    |
|  game_set_world_difficulty  |  Set world difficulty  |  Sets the given difficulty in the world.  |  game/settings  |  difficulty: enum<br/>&nbsp;&nbsp;- EASY<br/>&nbsp;&nbsp;- HARD<br/>&nbsp;&nbsp;- NORMAL<br/>&nbsp;&nbsp;- PEACEFUL  |    |    |    |
|  game_set_world_gamerule  |  Set world game rule  |  Sets the given world game rule (gamerule).  |  game/settings  |  gamerule: enum<br/>&nbsp;&nbsp;- DISABLE_RAIDS<br/>&nbsp;&nbsp;- DO_DAYLIGHT_CYCLE<br/>&nbsp;&nbsp;- DO_ENTITY_DROPS<br/>&nbsp;&nbsp;- DO_FIRE_TICK<br/>&nbsp;&nbsp;- DO_IMMEDIATE_RESPAWN<br/>&nbsp;&nbsp;- DO_INSOMNIA<br/>&nbsp;&nbsp;- DO_MOB_LOOT<br/>&nbsp;&nbsp;- DO_MOB_SPAWNING<br/>&nbsp;&nbsp;- DO_PATROL_SPAWNING<br/>&nbsp;&nbsp;- DO_TILE_DROPS<br/>&nbsp;&nbsp;- DO_TRADER_SPAWNING<br/>&nbsp;&nbsp;- DO_WEATHER_CYCLE<br/>&nbsp;&nbsp;- DROWNING_DAMAGE<br/>&nbsp;&nbsp;- FALL_DAMAGE<br/>&nbsp;&nbsp;- FIRE_DAMAGE<br/>&nbsp;&nbsp;- FORGIVE_DEAD_PLAYERS<br/>&nbsp;&nbsp;- KEEP_INVENTORY<br/>&nbsp;&nbsp;- MOB_GRIEFING<br/>&nbsp;&nbsp;- PROJECTILES_CAN_BREAK_BLOCKS<br/>&nbsp;&nbsp;- SHOW_DEATH_MESSAGES<br/>&nbsp;&nbsp;- NATURAL_REGENERATION<br/>&nbsp;&nbsp;- UNIVERSAL_ANGER<br/>&nbsp;&nbsp;- PLAYERS_SLEEPING_PERCENTAGE<br/>&nbsp;&nbsp;- REDUCED_DEBUG_INFO<br/>&nbsp;&nbsp;- FREEZE_DAMAGE<br/>&nbsp;&nbsp;- RANDOM_TICK_SPEED<br/>&nbsp;&nbsp;- MAX_ENTITY_CRAMMING<br/>&nbsp;&nbsp;- SPAWN_RADIUS<br/>&nbsp;&nbsp;- LAVA_SOURCE_CONVERSION<br/>&nbsp;&nbsp;- WATER_SOURCE_CONVERSION<br/>&nbsp;&nbsp;- TNT_EXPLOSION_DROP_DECAY<br/>&nbsp;&nbsp;- BLOCK_EXPLOSION_DROP_DECAY<br/>&nbsp;&nbsp;- MOB_EXPLOSION_DROP_DECAY<br/>&nbsp;&nbsp;- DO_LIMITED_CRAFTING<br/>&nbsp;&nbsp;- PLAYERS_NETHER_PORTAL_DEFAULT_DELAY<br/>&nbsp;&nbsp;- PLAYERS_NETHER_PORTAL_CREATIVE_DELAY<br/>&nbsp;&nbsp;- SNOW_ACCUMULATION_HEIGHT<br/>&nbsp;&nbsp;- DO_WARDEN_SPAWNING<br/>&nbsp;&nbsp;- ENDER_PEARLS_VANISH_ON_DEATH<br/>&nbsp;&nbsp;- DO_VINES_SPREAD<br/>&nbsp;&nbsp;- TNT_EXPLODER<br/>&nbsp;&nbsp;- LOCATOR_BAR<br/>&nbsp;&nbsp;- SPAWN_MONSTERS<br/>&nbsp;&nbsp;- PVP<br/>&nbsp;&nbsp;- SPAWNER_BLOCKS_WORK<br/>value: text  |    |  Leave the "Value" argument empty to reset it to the default state.  |    |
|  game_set_world_simulation_distance  |  Set world simulation distance  |  Sets the chunk simulation distance for the world.  |  game/settings  |  distance: number  |    |    |    |
|  game_set_world_time  |  Set world time  |  Sets the world time in ticks.  |  game/settings  |  time: number  |    |    |    |
|  game_set_world_weather  |  Set world weather  |  Sets the world weather for a given duration.  |  game/settings  |  weather_type: enum<br/>&nbsp;&nbsp;- CLEAR<br/>&nbsp;&nbsp;- RAINING<br/>&nbsp;&nbsp;- THUNDER<br/>weather_duration: number  |    |  By default, if no duration is given, the weather will not change.  |    |
|  game_spawn_armor_stand  |  Spawn armor stand  |  Creates an armor stand at the given location.  |  game/entity  |  helmet: item<br/>chestplate: item<br/>leggings: item<br/>boots: item<br/>right_hand: item<br/>left_hand: item<br/>gravity: enum<br/>{TF}<br/>marker: enum<br/>{TF}<br/>small: enum<br/>{TF}<br/>show_arms: enum<br/>{TF}<br/>base_plate: enum<br/>{TF}<br/>invisible: enum<br/>{TF}<br/>location: location<br/>custom_name: text  |    |    |    |
|  game_spawn_block_display  |  Spawn block display  |  Creates a block display at the given location.  |  game/entity  |  spawn_location: location<br/>custom_name: text<br/>block: block  |    |    |    |
|  game_spawn_effect_cloud  |  Spawn lingering potion cloud  |  Creates a lingering potion cloud that inflicts effects on entities inside it.  |  game/entity  |  location: location<br/>effects: potion<br/>radius: number<br/>duration: number<br/>particle: particle<br/>custom_name: text  |    |    |    |
|  game_spawn_end_crystal  |  Spawn End crystal  |  Creates an End crystal at the given location.  |  game/entity  |  location: location<br/>custom_name: text<br/>show_bottom: enum<br/>{TF}  |    |    |    |
|  game_spawn_evoker_fangs  |  Spawn evoker fangs  |  Creates an evoker fangs at the given location.  |  game/entity  |  location: location<br/>custom_name: text  |    |    |    |
|  game_spawn_experience_orb  |  Spawn experience orb  |  Creates an experience orb at the given location with the chosen parameters.  |  game/entity  |  location: location<br/>experience_amount: number<br/>custom_name: text  |    |    |    |
|  game_spawn_eye_of_ender  |  Spawn Eye of Ender  |  Creates an Eye of Ender at the given location that moves towards its target.  |  game/entity  |  location: location<br/>destination: location<br/>lifespan: number<br/>custom_name: text<br/>end_of_lifespan: enum<br/>&nbsp;&nbsp;- DROP<br/>&nbsp;&nbsp;- SHATTER<br/>&nbsp;&nbsp;- RANDOM  |    |    |    |
|  game_spawn_falling_block  |  Spawn falling block  |  Creates a falling block at the given location.  |  game/entity  |  block: block<br/>location: location<br/>name: text<br/>should_expire: enum<br/>{TF}  |    |    |    |
|  game_spawn_interaction_entity  |  Spawn interaction entity  |  Creates an interaction entity at the given location.  |  game/entity  |  location: location<br/>custom_name: text<br/>width: number<br/>height: number<br/>responsive: enum<br/>{TF}  |    |    |    |
|  game_spawn_item  |  Spawn item  |  Creates an item at the given location with the chosen parameters.  |  game/entity  |  item: item<br/>location: location<br/>custom_name: text<br/>apply_motion: enum<br/>{TF}<br/>can_mob_pickup: enum<br/>{TF}<br/>can_player_pickup: enum<br/>{TF}  |    |    |    |
|  game_spawn_item_display  |  Spawn item display  |  Creates an item display at the given location.  |  game/entity  |  spawn_location: location<br/>custom_name: text<br/>displayed_item: item  |    |    |    |
|  game_spawn_item_frame  |  Spawn item frame  |  Creates an item frame at the given location.  |  game/entity  |  spawn_location: location<br/>item: item<br/>rotation: enum<br/>&nbsp;&nbsp;- NONE<br/>&nbsp;&nbsp;- CLOCKWISE_45<br/>&nbsp;&nbsp;- CLOCKWISE<br/>&nbsp;&nbsp;- CLOCKWISE_135<br/>&nbsp;&nbsp;- FLIPPED<br/>&nbsp;&nbsp;- FLIPPED_45<br/>&nbsp;&nbsp;- COUNTER_CLOCKWISE<br/>&nbsp;&nbsp;- COUNTER_CLOCKWISE_45<br/>block_face: enum<br/>&nbsp;&nbsp;- NORTH<br/>&nbsp;&nbsp;- EAST<br/>&nbsp;&nbsp;- SOUTH<br/>&nbsp;&nbsp;- WEST<br/>&nbsp;&nbsp;- UP<br/>&nbsp;&nbsp;- DOWN<br/>glowing: enum<br/>{TF}<br/>visible: enum<br/>{TF}<br/>fixed: enum<br/>{TF}  |    |    |    |
|  game_spawn_lightning_bolt  |  Spawn lightning  |  Creates a lightning bolt at the given location.  |  game/entity  |  location: location  |    |    |    |
|  game_spawn_mob  |  Spawn mob  |  Creates a mob at the given location with the chosen parameters.  |  game/entity  |  mob: item<br/>location: location<br/>health: number<br/>custom_name: text<br/>potion_effects: potion<br/>main_hand: item<br/>helmet: item<br/>chestplate: item<br/>leggings: item<br/>boots: item<br/>off_hand: item<br/>natural_equipment: enum<br/>{TF}  |    |    |    |
|  game_spawn_painting  |  Spawn painting  |  Creates a painting at the given location.  |  game/entity  |  spawn_location: location<br/>art: text<br/>block_face: enum<br/>&nbsp;&nbsp;- NORTH<br/>&nbsp;&nbsp;- EAST<br/>&nbsp;&nbsp;- SOUTH<br/>&nbsp;&nbsp;- WEST  |    |    |    |
|  game_spawn_primed_tnt  |  Spawn primed TNT  |  Creates primed TNT at the given location.  |  game/entity  |  location: location<br/>tnt_power: number<br/>fuse_duration: number<br/>custom_name: text<br/>block: block  |    |    |    |
|  game_spawn_shulker_bullet  |  Spawn shulker projectile  |  Creates a shulker bullet at the given location.  |  game/entity  |  location: location<br/>custom_name: text  |    |    |    |
|  game_spawn_text_display  |  Create text display  |  Creates a text display at the given location.  |  game/entity  |  spawn_location: location<br/>custom_name: text<br/>merging_mode: enum<br/>&nbsp;&nbsp;- SPACES<br/>&nbsp;&nbsp;- CONCATENATION<br/>&nbsp;&nbsp;- SEPARATE_LINES<br/>displayed_text: text  |    |    |    |
|  game_spawn_vehicle  |  Create vehicle  |  Creates a vehicle at the given location with the chosen parameters.  |  game/entity  |  vehicle: item<br/>location: location<br/>custom_name: text  |    |    |    |
|  game_uncancel_event  |  Event result  |  Returns whether the event that triggered this code is cancelled.  |  game/event  |    |    |    |    |
|  game_update_block  |  Update adjacent blocks  |  Updates the blocks adjacent to the given location if the block at the location is not air. The block at the location itself is not updated, but may update from its neighbors.  |  game/block  |  location: location  |    |    |    |
|  game_wobble_decorated_pot  |  Set pot wobble  |  Sets the given pot wobble type at the given location.  |  game/block  |  location: location<br/>style: enum<br/>&nbsp;&nbsp;- POSITIVE<br/>&nbsp;&nbsp;- NEGATIVE  |  Vases  |    |    |
|  if_game_block_equals  |  Block equals  |  Checks whether the block at the given location is a certain block type.  |  if_game  |  location: location<br/>blocks: block  |    |    |    |
|  if_game_block_powered  |  Block is powered by redstone  |  Checks whether the block at the given location is powered by redstone.  |  if_game  |  locations: location<br/>power_mode: enum<br/>&nbsp;&nbsp;- DIRECT<br/>&nbsp;&nbsp;- INDIRECT  |    |    |    |
|  if_game_chunk_has_custom_tag  |  Chunk has custom tag  |  Checks whether the chunk has the given custom tag.  |  if_game  |  location: location<br/>tag: text<br/>tag_value: text<br/>compare_type: enum<br/>&nbsp;&nbsp;- EQUALS<br/>&nbsp;&nbsp;- CONTAINS<br/>&nbsp;&nbsp;- STARTS_WITH<br/>&nbsp;&nbsp;- ENDS_WITH  |    |    |    |
|  if_game_chunk_is_loaded  |  Chunk loaded  |  Checks whether the chunk at the location is loaded.  |  if_game  |  location: location  |    |    |    |
|  if_game_container_has  |  Container has item  |  Checks whether the container at the given location has the given items in its inventory.  |  if_game  |  location: location<br/>items: item<br/>check_mode: enum<br/>{ANY_ALL}<br/>comparison_mode: enum<br/>{CMP}  |    |    |    |
|  if_game_container_has_room_for_item  |  Container has room for items  |  Checks whether the container at the given location has room for items in its inventory.  |  if_game  |  location: location<br/>items: item<br/>check_mode: enum<br/>{ANY_ALL}  |    |    |    |
|  if_game_damage_cause_equals  |  Event damage source equals  |  Checks whether the event damage source equals the chosen one.  |  if_game  |  cause: enum<br/>&nbsp;&nbsp;- BLOCK_EXPLOSION<br/>&nbsp;&nbsp;- CONTACT<br/>&nbsp;&nbsp;- CRAMMING<br/>&nbsp;&nbsp;- CUSTOM<br/>&nbsp;&nbsp;- DRAGON_BREATH<br/>&nbsp;&nbsp;- DROWNING<br/>&nbsp;&nbsp;- DRYOUT<br/>&nbsp;&nbsp;- ENTITY_ATTACK<br/>&nbsp;&nbsp;- ENTITY_EXPLOSION<br/>&nbsp;&nbsp;- ENTITY_SWEEP_ATTACK<br/>&nbsp;&nbsp;- FALL<br/>&nbsp;&nbsp;- FALLING_BLOCK<br/>&nbsp;&nbsp;- FIRE<br/>&nbsp;&nbsp;- FIRE_TICK<br/>&nbsp;&nbsp;- FLY_INTO_WALL<br/>&nbsp;&nbsp;- FREEZE<br/>&nbsp;&nbsp;- HOT_FLOOR<br/>&nbsp;&nbsp;- LAVA<br/>&nbsp;&nbsp;- LIGHTNING<br/>&nbsp;&nbsp;- MAGIC<br/>&nbsp;&nbsp;- MELTING<br/>&nbsp;&nbsp;- POISON<br/>&nbsp;&nbsp;- PROJECTILE<br/>&nbsp;&nbsp;- STARVATION<br/>&nbsp;&nbsp;- SUFFOCATION<br/>&nbsp;&nbsp;- SUICIDE<br/>&nbsp;&nbsp;- THORNS<br/>&nbsp;&nbsp;- VOID<br/>&nbsp;&nbsp;- WITHER<br/>&nbsp;&nbsp;- KILL<br/>&nbsp;&nbsp;- COMMAND<br/>&nbsp;&nbsp;- SONIC_BOOM<br/>&nbsp;&nbsp;- WORLD_BORDER<br/>&nbsp;&nbsp;- CAMPFIRE  |    |    |    |
|  if_game_event_attack_is_critical  |  The attack was critical  |  Checks whether the attack in the event was critical.  |  if_game  |    |    |    |    |
|  if_game_event_block_equals  |  Event block equals  |  Checks whether the current event block equals a certain block.  |  if_game  |  blocks: block<br/>locations: location  |    |    |    |
|  if_game_event_has_input  |  Movement key equals  |  Checks whether the movement key from the event is the chosen key.  |  if_game  |  input_type: enum<br/>&nbsp;&nbsp;- FORWARD<br/>&nbsp;&nbsp;- BACKWARDS<br/>&nbsp;&nbsp;- LEFT<br/>&nbsp;&nbsp;- RIGHT<br/>&nbsp;&nbsp;- JUMP<br/>&nbsp;&nbsp;- SNEAK<br/>&nbsp;&nbsp;- SPRINT  |  The "Player changes pressed movement keys" event  |    |    |
|  if_game_event_is_age_locked  |  Growth stopped  |  Checks whether growth is stopped in the event  |  if_game  |    |  Blocking growth with a golden dandelion  |    |    |
|  if_game_event_is_canceled  |  Event cancelled  |  Checks whether the event is cancelled.  |  if_game  |    |    |    |    |
|  if_game_event_item_equals  |  Event item equals  |  Checks whether the current event item equals a certain item.  |  if_game  |  items: item<br/>comparison_mode: enum<br/>{CMP}  |    |    |    |
|  if_game_has_custom_recipe  |  Recipe exists  |  Checks whether a custom recipe exists in the world.  |  if_game  |  names: text<br/>is_vanilla_recipe: enum<br/>{TF}<br/>compare_type: enum<br/>{ANY_ALL}  |    |    |    |
|  if_game_has_entity  |  Entity in world  |  Checks whether a certain entity exists in the world.  |  if_game  |  names_or_uuids: text<br/>check_mode: enum<br/>{ANY_ALL}  |    |    |    |
|  if_game_has_player  |  Player is in game  |  Checks whether the given player is in the game.  |  if_game  |  names_or_uuids: text<br/>check_mode: enum<br/>{ANY_ALL}  |    |    |    |
|  if_game_heal_cause_equals  |  Healing source equals  |  Checks whether the healing source equals the chosen one.  |  if_game  |  heal_cause: enum<br/>&nbsp;&nbsp;- CUSTOM<br/>&nbsp;&nbsp;- EATING<br/>&nbsp;&nbsp;- ENDER_CRYSTAL<br/>&nbsp;&nbsp;- MAGIC<br/>&nbsp;&nbsp;- MAGIC_REGEN<br/>&nbsp;&nbsp;- REGEN<br/>&nbsp;&nbsp;- SATIATED<br/>&nbsp;&nbsp;- WITHER<br/>&nbsp;&nbsp;- WITHER_SPAWN  |    |    |    |
|  if_game_ignite_cause_equals  |  Fire source equals  |  Checks whether the fire source equals the chosen one.  |  if_game  |  cause: enum<br/>&nbsp;&nbsp;- ARROW<br/>&nbsp;&nbsp;- ENDER_CRYSTAL<br/>&nbsp;&nbsp;- EXPLOSION<br/>&nbsp;&nbsp;- FIREBALL<br/>&nbsp;&nbsp;- FLINT_AND_STEEL<br/>&nbsp;&nbsp;- LAVA<br/>&nbsp;&nbsp;- LIGHTNING<br/>&nbsp;&nbsp;- SPREAD  |    |    |    |
|  if_game_instrument_equals  |  Tool equals  |  Checks whether the tool in the event equals the chosen one.  |  if_game  |  instrument: enum<br/>&nbsp;&nbsp;- BANJO<br/>&nbsp;&nbsp;- BASS_DRUM<br/>&nbsp;&nbsp;- BASS_GUITAR<br/>&nbsp;&nbsp;- BELL<br/>&nbsp;&nbsp;- BIT<br/>&nbsp;&nbsp;- CHIME<br/>&nbsp;&nbsp;- COW_BELL<br/>&nbsp;&nbsp;- DIDGERIDOO<br/>&nbsp;&nbsp;- FLUTE<br/>&nbsp;&nbsp;- GUITAR<br/>&nbsp;&nbsp;- IRON_XYLOPHONE<br/>&nbsp;&nbsp;- PIANO<br/>&nbsp;&nbsp;- PLING<br/>&nbsp;&nbsp;- SNARE_DRUM<br/>&nbsp;&nbsp;- STICKS<br/>&nbsp;&nbsp;- XYLOPHONE<br/>&nbsp;&nbsp;- ZOMBIE<br/>&nbsp;&nbsp;- SKELETON<br/>&nbsp;&nbsp;- CREEPER<br/>&nbsp;&nbsp;- WITHER_SKELETON<br/>&nbsp;&nbsp;- DRAGON<br/>&nbsp;&nbsp;- PIGLIN<br/>&nbsp;&nbsp;- CUSTOM_HEAD<br/>&nbsp;&nbsp;- TRUMPET<br/>&nbsp;&nbsp;- TRUMPET_EXPOSED<br/>&nbsp;&nbsp;- TRUMPET_OXIDIZED<br/>&nbsp;&nbsp;- TRUMPET_WEATHERED  |    |    |    |
|  if_game_location_in_block  |  Whether the location is inside a block  |  Checks whether the given location is inside a block.  |  if_game  |  location: location  |    |    |    |
|  if_game_sign_contains  |  Sign contains text  |  Checks whether the sign at the given location contains certain text.  |  if_game  |  location: location<br/>texts: text<br/>check_side: enum<br/>&nbsp;&nbsp;- ANY<br/>&nbsp;&nbsp;- FRONT<br/>&nbsp;&nbsp;- BACK<br/>check_mode: enum<br/>&nbsp;&nbsp;- CONTAINS<br/>&nbsp;&nbsp;- EQUALS<br/>lines: enum<br/>&nbsp;&nbsp;- FIRST<br/>&nbsp;&nbsp;- SECOND<br/>&nbsp;&nbsp;- THIRD<br/>&nbsp;&nbsp;- FOURTH<br/>&nbsp;&nbsp;- ALL  |    |    |    |
|  if_game_tile_block_has_custom_tag  |  Block entity has custom tag  |  Checks whether the block entity has the given custom tag.  |  if_game  |  location: location<br/>tag: text<br/>tag_value: text<br/>compare_type: enum<br/>&nbsp;&nbsp;- EQUALS<br/>&nbsp;&nbsp;- CONTAINS<br/>&nbsp;&nbsp;- STARTS_WITH<br/>&nbsp;&nbsp;- ENDS_WITH  |    |    |    |

## Quick ref
> Argument **names and types only**, one line per action/condition — scan this first. Exact enum values and extra info: see the full table row above. ⚠ deprecated = do not use.

- `game_add_custom_cooking_recipe` — name: text, input: item, result: item, experience: number, cooking_time: number, replace_vanilla: enum{TF}, input_match: enum{ITEM_MATCH}, recipe_type: enum, category: enum
- `game_add_custom_crafting_recipe` — name: text, items: item, result: item, replace_vanilla: enum{TF}, recipe_match_slot_1: enum{ITEM_MATCH}, recipe_match_slot_2: enum{ITEM_MATCH}, recipe_match_slot_3: enum{ITEM_MATCH}, recipe_match_slot_4: enum{ITEM_MATCH}, recipe_match_slot_5: enum{ITEM_MATCH}, recipe_match_slot_6: enum{ITEM_MATCH}, recipe_match_slot_7: enum{ITEM_MATCH}, recipe_match_slot_8: enum{ITEM_MATCH}, recipe_match_slot_9: enum{ITEM_MATCH}, recipe_type: enum, category: enum
- `game_add_custom_smithing_transform_recipe` — name: text, template: item, base: item, addition: item, result: item, replace_vanilla: enum{TF}, template_match: enum{ITEM_MATCH}, base_match: enum{ITEM_MATCH}, recipe_match: enum{ITEM_MATCH}, copy_data_components: enum{TF}
- `game_add_custom_smithing_trim_recipe` — name: text, template: item, base: item, addition: item, trim: item, replace_vanilla: enum{TF}, template_match: enum{ITEM_MATCH}, base_match: enum{ITEM_MATCH}, addition_match: enum{ITEM_MATCH}, copy_data_components: enum{TF}
- `game_add_custom_stonecutting_recipe` — name: text, input: item, result: item, replace_vanilla: enum{TF}, input_match: enum{ITEM_MATCH}
- `game_add_custom_transmute_recipe` — name: text, input: item, material: item, result: item, replace_vanilla: enum{TF}, input_match: enum{ITEM_MATCH}, material_match: enum{ITEM_MATCH}, category: enum
- `game_block_growth` — location: location, growth_stage: number, growth_type: enum
- `game_bloom_skulk_catalyst` — location: location, bloom_location: location, charge: number
- `game_bone_meal_block` — location: location, count: number
- `game_break_block` — locations: location, tool: item, drop_exp: enum{TF}
- `game_cancel_event` — (no arguments)
- `game_chunk_get_custom_tag` — variable: variable, location: location, tag_name: text, default_value: any
- `game_chunk_get_custom_tags` — variable: variable, location: location
- `game_chunk_remove_custom_tag` — location: location, tag_names: text
- `game_chunk_remove_custom_tags` — location: location
- `game_chunk_set_custom_tag` — location: location, tag_names: text, tag_values: text
- `game_clear_container` — location: location
- `game_clear_container_items` — location: location, items: item
- `game_clear_custom_recipes` — (no arguments)
- `game_clear_exploded_blocks` — location: location
- `game_clear_region` — pos_1: location, pos_2: location
- `game_clear_scoreboard_scores` — id: text
- `game_clone_region` — pos_1: location, pos_2: location, target_pos: location, paste_pos: location, ignore_air: enum{TF}, copy_entity: enum{TF}
- `game_create_explosion` — location: location, power: number, name_or_uuid: text, fire: enum{TF}, break_blocks: enum{TF}
- `game_create_scoreboard` — id: text, display_name: text
- `game_fill_container` — location: location, items: item
- `game_generate_tree` — location: location, tree_type: enum
- `game_get_tile_block_custom_tags` — variable: variable, location: location
- `game_hide_event_message` — hide: enum{TF}
- `game_launch_firework` — firework: item, location: location, movement: enum, instant: enum{TF}
- `game_launch_projectile` — projectile: item, location: location, speed: number, inaccuracy: number, custom_name: text, trail: particle
- `game_random_tick_block` — location: location, times: number
- `game_remove_container_items` — location: location, items: item
- `game_remove_custom_recipe` — names: text, remove_vanilla: enum{TF}
- `game_remove_scoreboard` — id: text
- `game_remove_scoreboard_score_by_name` — id: text, text: text
- `game_remove_scoreboard_score_by_score` — id: text, score: number
- `game_remove_tile_block_custom_tag` — location: location, tag_name: text
- `game_remove_tile_block_custom_tags` — location: location
- `game_replace_blocks_in_region` — old_block: block, pos_1: location, pos_2: location, new_block: block
- `game_replace_container_items` — items: item, location: location, replace: item, count: number
- `game_send_web_request` — url: text, content_body: text, headers: map, request_type: enum, content_type: enum
- `game_set_age` — location: location, tick: number
- `game_set_block` — block: block, locations: location, update_blocks: enum{TF}
- `game_set_block_analogue_power` — location: location, power_level: number
- `game_set_block_data` — location: location, block_data: text ⚠ deprecated
- `game_set_block_drops_enabled` — enable: enum{TF}
- `game_set_block_nbt` — location: location, tag_names: text, tag_values: text
- `game_set_block_powered` — location: location, powered: enum{TF}
- `game_set_block_single_data` — location: location, data: text, value: text
- `game_set_brushable_block_item` — location: location, item: item
- `game_set_campfire_item` — location: location, item: item, cooking_time: number, slot: enum
- `game_set_container` — location: location, items: item
- `game_set_container_lock` — location: location, container_key: text
- `game_set_container_name` — location: location, name: text
- `game_set_copper_golem_statue_pose` — location: location, pose: enum
- `game_set_creaking_heart_natural` — location: location, natural: enum{TF}
- `game_set_creaking_heart_state` — location: location, heart_state: enum
- `game_set_decorate_pot_sherd` — location: location, item: item, side: enum
- `game_set_dried_ghast_hydration` — location: location, hydration: number
- `game_set_event_anvil_damage_state` — damage_state: enum
- `game_set_event_anvil_repair_cost` — repair_cost: number, repair_cost_type: enum, bypass_cost: enum{TF}
- `game_set_event_combust_duration` — duration: number
- `game_set_event_damage` — damage: number
- `game_set_event_death_screen_message` — message: text
- `game_set_event_enchantment_offers` — enchantments: text, levels: number, costs: number
- `game_set_event_exhaustion` — exhaustion: number
- `game_set_event_experience` — experience: number
- `game_set_event_gamemode` — gamemode: enum
- `game_set_event_heal` — heal: number
- `game_set_event_item` — item: item
- `game_set_event_item_cooldown` — cooldown: number
- `game_set_event_items` — items: item
- `game_set_event_knockback_vector` — knockback: vector
- `game_set_event_move_allowed` — allowed: enum{TF}
- `game_set_event_projectile` — projectile: item, name: text
- `game_set_event_should_drop_leash` — should_drop_leash: enum{TF}
- `game_set_event_should_play_effect` — should_play_effect: enum{TF}
- `game_set_event_sound` — sound: sound
- `game_set_event_source_slot` — source_slot: number
- `game_set_event_target_slot` — target: number
- `game_set_event_uery_info` — information: text
- `game_set_event_velocity` — velocity: vector
- `game_set_furnace_cook_time` — location: location, time: number
- `game_set_hardcore` — hardcore: enum{TF} ⚠ deprecated
- `game_set_item_in_container_slot` — location: location, item: item, slot: number
- `game_set_lectern_book` — location: location, item: item, page: number
- `game_set_player_head` — location: location, name_or_uuid: text, receive_type: enum
- `game_set_potent_sulfur_state` — location: location, state: enum
- `game_set_region` — block: block, pos_1: location, pos_2: location
- `game_set_scoreboard_line` — id: text, line: text, display: text, score: number, format_content: text, format: enum
- `game_set_scoreboard_line_display` — id: text, line: text, display: text
- `game_set_scoreboard_line_format` — id: text, line: text, format_content: text, format: enum
- `game_set_scoreboard_number_format` — id: text, format_content: text, format: enum
- `game_set_scoreboard_score` — id: text, text: text, score: number
- `game_set_scoreboard_title` — id: text, title: text
- `game_set_sculk_shrieker_can_summon` — location: location, can_summon: enum{TF}
- `game_set_sculk_shrieker_shrieking` — location: location, shrieking: enum{TF}
- `game_set_sculk_shrieker_warning_level` — location: location, warning_level: number
- `game_set_sign_text` — location: location, text: text, line: number, side: enum
- `game_set_sign_text_color` — location: location, side: enum, sign_text_color: enum, glowing: enum{TF}
- `game_set_sign_waxed` — location: location, waxed: enum{TF}
- `game_set_spawner_entity` — location: location, entity: item
- `game_set_tile_block_custom_tag` — location: location, tag_name: text, tag_value: text
- `game_set_vault_displayed_item` — location: location, item: item
- `game_set_vault_next_state_update_time` — location: location, time: number
- `game_set_world_difficulty` — difficulty: enum
- `game_set_world_gamerule` — gamerule: enum, value: text
- `game_set_world_simulation_distance` — distance: number
- `game_set_world_time` — time: number
- `game_set_world_weather` — weather_type: enum, weather_duration: number
- `game_spawn_armor_stand` — helmet: item, chestplate: item, leggings: item, boots: item, right_hand: item, left_hand: item, gravity: enum{TF}, marker: enum{TF}, small: enum{TF}, show_arms: enum{TF}, base_plate: enum{TF}, invisible: enum{TF}, location: location, custom_name: text
- `game_spawn_block_display` — spawn_location: location, custom_name: text, block: block
- `game_spawn_effect_cloud` — location: location, effects: potion, radius: number, duration: number, particle: particle, custom_name: text
- `game_spawn_end_crystal` — location: location, custom_name: text, show_bottom: enum{TF}
- `game_spawn_evoker_fangs` — location: location, custom_name: text
- `game_spawn_experience_orb` — location: location, experience_amount: number, custom_name: text
- `game_spawn_eye_of_ender` — location: location, destination: location, lifespan: number, custom_name: text, end_of_lifespan: enum
- `game_spawn_falling_block` — block: block, location: location, name: text, should_expire: enum{TF}
- `game_spawn_interaction_entity` — location: location, custom_name: text, width: number, height: number, responsive: enum{TF}
- `game_spawn_item` — item: item, location: location, custom_name: text, apply_motion: enum{TF}, can_mob_pickup: enum{TF}, can_player_pickup: enum{TF}
- `game_spawn_item_display` — spawn_location: location, custom_name: text, displayed_item: item
- `game_spawn_item_frame` — spawn_location: location, item: item, rotation: enum, block_face: enum, glowing: enum{TF}, visible: enum{TF}, fixed: enum{TF}
- `game_spawn_lightning_bolt` — location: location
- `game_spawn_mob` — mob: item, location: location, health: number, custom_name: text, potion_effects: potion, main_hand: item, helmet: item, chestplate: item, leggings: item, boots: item, off_hand: item, natural_equipment: enum{TF}
- `game_spawn_painting` — spawn_location: location, art: text, block_face: enum
- `game_spawn_primed_tnt` — location: location, tnt_power: number, fuse_duration: number, custom_name: text, block: block
- `game_spawn_shulker_bullet` — location: location, custom_name: text
- `game_spawn_text_display` — spawn_location: location, custom_name: text, merging_mode: enum, displayed_text: text
- `game_spawn_vehicle` — vehicle: item, location: location, custom_name: text
- `game_uncancel_event` — (no arguments)
- `game_update_block` — location: location
- `game_wobble_decorated_pot` — location: location, style: enum
- `if_game_block_equals` — location: location, blocks: block
- `if_game_block_powered` — locations: location, power_mode: enum
- `if_game_chunk_has_custom_tag` — location: location, tag: text, tag_value: text, compare_type: enum
- `if_game_chunk_is_loaded` — location: location
- `if_game_container_has` — location: location, items: item, check_mode: enum{ANY_ALL}, comparison_mode: enum{CMP}
- `if_game_container_has_room_for_item` — location: location, items: item, check_mode: enum{ANY_ALL}
- `if_game_damage_cause_equals` — cause: enum
- `if_game_event_attack_is_critical` — (no arguments)
- `if_game_event_block_equals` — blocks: block, locations: location
- `if_game_event_has_input` — input_type: enum
- `if_game_event_is_age_locked` — (no arguments)
- `if_game_event_is_canceled` — (no arguments)
- `if_game_event_item_equals` — items: item, comparison_mode: enum{CMP}
- `if_game_has_custom_recipe` — names: text, is_vanilla_recipe: enum{TF}, compare_type: enum{ANY_ALL}
- `if_game_has_entity` — names_or_uuids: text, check_mode: enum{ANY_ALL}
- `if_game_has_player` — names_or_uuids: text, check_mode: enum{ANY_ALL}
- `if_game_heal_cause_equals` — heal_cause: enum
- `if_game_ignite_cause_equals` — cause: enum
- `if_game_instrument_equals` — instrument: enum
- `if_game_location_in_block` — location: location
- `if_game_sign_contains` — location: location, texts: text, check_side: enum, check_mode: enum, lines: enum
- `if_game_tile_block_has_custom_tag` — location: location, tag: text, tag_value: text, compare_type: enum
