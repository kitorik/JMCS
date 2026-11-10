# Repeat actions
> **Enum macros:** {TF} = TRUE / FALSE; {TFN} = TRUE / FALSE / NOT_SET; {ANY_ALL} = ANY / ALL; {ITEM_MATCH} = EXACT / IGNORE_NAME_DURABILITY / IGNORE_NAME_DURABILITY_ENCHANTMENTS / CUSTOM_TAGS_CONTAINS / MINECRAFT_TAG / ITEM_TYPE; {DEG_RAD} = DEGREES / RADIANS; {CMP} = EXACTLY / IGNORE_STACK_SIZE / IGNORE_DURABILITY_AND_STACK_SIZE / TYPE_ONLY. Icon column omitted.


|  ID  |  Name  |  Description  |  Category/Subcategory  |  Arguments  |
|  ---  |  ---  |  ---  |  ---  |  ---  |
|  repeat_adjacently  |  Iterate adjacent blocks  |  Assigns the current location to the given variable among blocks adjacent to the given location.  |  repeat  |  variable: variable<br/>origin: location<br/>change_rotation: enum<br/>{TF}<br/>include_self: enum<br/>{TF}<br/>pattern: enum<br/>&nbsp;&nbsp;- CARDINAL<br/>&nbsp;&nbsp;- SQUARE<br/>&nbsp;&nbsp;- ADJACENT<br/>&nbsp;&nbsp;- CUBE  |
|  repeat_for_each_in_list  |  Iterate list  |  Iterates each element of the given list, yielding its index and value into the given variables.  |  repeat  |  index_variable: variable<br/>value_variable: variable<br/>list: array  |
|  repeat_for_each_map_entry  |  Iterate map  |  Iterates each entry of the given map, yielding its key and value into the given variables.  |  repeat  |  key_variable: variable<br/>value_variable: variable<br/>map: map  |
|  repeat_forever  |  Repeat forever  |  Repeats the code inside the pistons forever.  |  repeat  |    |
|  repeat_multi_times  |  Counted loop  |  Runs the code the given number of times.  |  repeat  |  variable: variable<br/>amount: number  |
|  repeat_on_circle  |  Iterate circle  |  Sequentially yields the location of each block of the circle with the given parameters.  |  repeat  |  variable: variable<br/>center: location<br/>radius: number<br/>circle_points: number<br/>perpendicular_to_plane: vector<br/>start_angle: number<br/>angle_unit: enum<br/>{DEG_RAD}  |
|  repeat_on_grid  |  Iterate region  |  Yields the location of each block in the given region into the given variable.  |  repeat  |  variable: variable<br/>start: location<br/>end: location  |
|  repeat_on_path  |  Iterate path  |  Walks from one location to another with a given step, assigning the current location to the given variable.  |  repeat  |  variable: variable<br/>step: number<br/>locations: location<br/>rotation: enum<br/>{TF}  |
|  repeat_on_range  |  Range loop  |  Assigns the current number from the given range with a given step into the given variable.  |  repeat  |  variable: variable<br/>start: number<br/>end: number<br/>interval: number  |
|  repeat_on_sphere  |  Iterate sphere  |  Sequentially yields the location of each point on the sphere with the given parameters.  |  repeat  |  variable: variable<br/>center: location<br/>radius: number<br/>points: number<br/>rotate_location: enum<br/>&nbsp;&nbsp;- NO_CHANGES<br/>&nbsp;&nbsp;- INWARDS<br/>&nbsp;&nbsp;- OUTWARDS  |
|  repeat_while  |  While loop  |  Runs the code as long as the chosen condition is true.  |  repeat  |    |
