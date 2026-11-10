# Controller actions
> **Enum macros:** {TF} = TRUE / FALSE; {TFN} = TRUE / FALSE / NOT_SET; {ANY_ALL} = ANY / ALL; {ITEM_MATCH} = EXACT / IGNORE_NAME_DURABILITY / IGNORE_NAME_DURABILITY_ENCHANTMENTS / CUSTOM_TAGS_CONTAINS / MINECRAFT_TAG / ITEM_TYPE; {DEG_RAD} = DEGREES / RADIANS; {CMP} = EXACTLY / IGNORE_STACK_SIZE / IGNORE_DURABILITY_AND_STACK_SIZE / TYPE_ONLY. Icon column omitted.


|  ID  |  Name  |  Description  |  Category/Subcategory  |  Arguments  |  Additional info  |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
|  controller_do_not_run  |  Ignore execution  |  Ignores the code inside the brackets during execution.  |  controller  |    |    |
|  controller_exception  |  Catch error  |  Catches an error in the code inside the pistons and assigns its identifier to a variable (example: function_not_found).  |  controller  |  variable: variable  |  Does not catch global and critical errors.  |
|  controller_isolated_selection  |  Isolate selection  |  Isolates the selection inside the brackets.  |  controller  |  selection_mode: enum<br/>&nbsp;&nbsp;- DEFAULT<br/>&nbsp;&nbsp;- CURRENT<br/>&nbsp;&nbsp;- EMPTY<br/>&nbsp;&nbsp;- FOR_EACH  |  A selection created inside is active only within the brackets.  |
|  controller_label  |  Mark code  |  Marks the code between the pistons with the given name and allows interrupting it.  |  controller  |  label: text  |  Works together with the "Exit labeled block" action  |
|  controller_measure_time  |  Measure execution time  |  Measures the execution time of the code inside the pistons and assigns the result to a variable.  |  controller  |  variable: variable<br/>duration: enum<br/>&nbsp;&nbsp;- NANOSECONDS<br/>&nbsp;&nbsp;- MICROSECONDS<br/>&nbsp;&nbsp;- MILLISECONDS  |  Accounts for "Wait" blocks.  |

## Quick ref
> Argument **names and types only**, one line per action/condition — scan this first. Exact enum values and extra info: see the full table row above. ⚠ deprecated = do not use.

- `controller_do_not_run` — (no arguments)
- `controller_exception` — variable: variable
- `controller_isolated_selection` — selection_mode: enum
- `controller_label` — label: text
- `controller_measure_time` — variable: variable, duration: enum
