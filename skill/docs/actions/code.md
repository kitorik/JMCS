# Code actions
> **Enum macros:** {TF} = TRUE / FALSE; {TFN} = TRUE / FALSE / NOT_SET; {ANY_ALL} = ANY / ALL; {ITEM_MATCH} = EXACT / IGNORE_NAME_DURABILITY / IGNORE_NAME_DURABILITY_ENCHANTMENTS / CUSTOM_TAGS_CONTAINS / MINECRAFT_TAG / ITEM_TYPE; {DEG_RAD} = DEGREES / RADIANS; {CMP} = EXACTLY / IGNORE_STACK_SIZE / IGNORE_DURABILITY_AND_STACK_SIZE / TYPE_ONLY. Icon column omitted.


|  ID  |  Name  |  Description  |  Category/Subcategory  |  Arguments  |  Works with  |  Additional info  |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
|  call_function  |  Call function  |  Calls a function code line.  |  call_function  |  function_name: text<br/>args: map  |    |    |
|  control_break_label  |  Exit labeled block  |  Interrupts the code marked with the given name.  |  control  |  label: text  |  the "Mark code" action  |    |
|  control_call_exception  |  Throw error  |  Throws the given error with the given ID and message.  |  control  |  id: text<br/>message: text<br/>type: enum<br/>&nbsp;&nbsp;- WARNING<br/>&nbsp;&nbsp;- ERROR<br/>&nbsp;&nbsp;- FATAL  |    |  Recommended to use inside the "Catch error" action.  |
|  control_end_thread  |  Stop sequence  |  Stops the current code block sequence. Any code after this block will not run.  |  control  |    |    |  If used inside a function, stops the parent line that called the function.  |
|  control_return_function  |  Return to call site  |  Stops the current code block sequence inside a function and returns to that function call block.  |  control  |    |    |  Returns to the call block of the current function in the parent line.  |
|  control_skip_iteration  |  Skip iteration  |  Skips one iteration of the current loop.  |  control  |    |    |    |
|  control_stop_repeat  |  Stop loop  |  Fully stops the current loop.  |  control  |    |    |    |
|  control_wait  |  Wait  |  Pauses the current code block sequence for the given time.  |  control  |  duration: number<br/>time_unit: enum<br/>&nbsp;&nbsp;- TICKS<br/>&nbsp;&nbsp;- SECONDS<br/>&nbsp;&nbsp;- MINUTES  |    |  Minimum delay is 1 tick; in Ticks mode only whole numbers are allowed.  |
|  else  |  Else  |  ...  |  else  |    |    |    |
|  start_process  |  Start process  |  Starts a process code line.  |  start_process  |  process_name: text<br/>target_mode: enum<br/>&nbsp;&nbsp;- CURRENT_TARGET<br/>&nbsp;&nbsp;- CURRENT_SELECTION<br/>&nbsp;&nbsp;- NO_TARGET<br/>&nbsp;&nbsp;- FOR_EACH_IN_SELECTION<br/>local_variables_mode: enum<br/>&nbsp;&nbsp;- DONT_COPY<br/>&nbsp;&nbsp;- COPY<br/>&nbsp;&nbsp;- SHARE<br/>args: map  |    |    |
