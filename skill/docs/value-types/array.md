# Value type: array

A list of values of any type. In official exports a list has a fixed capacity (e.g. 20 slots); unoccupied slots are empty `{}`.

## Format
```json
{ "type": "array", "values": [ { "type": "text", "text": "set" }, { "type": "text", "text": "add" }, {}, {}, {} ] }
```

## Examples
```json
{ "type": "array", "values": [ { "type": "variable", "variable": "bb.token", "scope": "game" } ] }
{ "type": "array", "values": [ { "type": "number", "number": 0 }, { "type": "text", "text": "1.0" }, { "type": "variable", "variable": "commands", "scope": "local" } ] }
```

## Rules
- Elements may be of mixed types (text, number, variable, game_value...).
- Empty element `{}` = unoccupied slot.
- A nonexistent list variable → 0 in a list slot → the action breaks: create lists before use.
