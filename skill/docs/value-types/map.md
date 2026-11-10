# Value type: map

A key → value dictionary. Used for function (`call_function`) and process (`start_process`) arguments, and for data storage (`set_variable_create_map`).

## Format
```json
{ "type": "map", "values": {} }
```

## Examples
```json
{ "name": "args", "value": { "type": "map", "values": {} } }
```

## Rules
- A call without arguments → empty map `"values": {}`.
- Map variable ops: `set_variable_create_map`, `set_variable_map_put`, `%entry(map, key)`, `if_variable_map_has_key`, iteration `repeat_for_each_map_entry`.
- Default for a missing key is 0: check the key before reading.
