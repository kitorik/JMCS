# Value type: parameter

Declares a function parameter inside a function handler's `parameters` array. In the function body the parameter is read as a variable: `%var_line(name)` (or `%var_local(name)`, depending on the call).

Full rules: `docs/rules.md` → Function parameters.

## Format
```json
{ "type": "parameter", "type_key": "singular", "name": "loc", "value_type": "location", "is_required": "true", "default_value": "{}", "slot": 0, "description_slot": 9, "description": "{\"translations\":{},\"fallback\":{\"rawText\":\"Location\",\"parsingType\":\"LEGACY\"}}" }
```

## Fields
- `type_key`: `singular` (one value) or `plural` (list of values; for plural use `slots` / `description_slots` — comma-separated numbers as **strings**).
- `name`: parameter name.
- `value_type`: the value type of the parameter (`location`, `number`, `text`, `item`, `vector`, ...). Strictly enforced — a wrong type breaks the action.
- `is_required` / `default_value`: whether the caller must pass the argument and what to use otherwise.
- `slot` / `description_slot`: editor grid cells (0-54, description usually `slot + 9`) — plain numbers. Slots must not overlap between parameters and must not exceed 54.
- `description`: stringified JSON text component (`translations` + `fallback` with `rawText` and `parsingType`).

## Rules
- Declared in the function handler's `values` as a single entry: `{"name":"parameters","value":{"type":"array","values":[ ...parameter values... ]}}`.
- Each `call_function` must pass `args` (a `map`) for every required parameter — keys are the stringified JSON of the parameter name; the game injects the values into the parameters before running the function code.
