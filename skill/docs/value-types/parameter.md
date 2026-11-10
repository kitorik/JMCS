# Value type: parameter

A function parameter declaration. Used only inside a function handler's `values` array: the single entry named `parameters` holds an `array`, and each of its elements is a value of type `parameter`. In the visual editor each parameter is a physical block in the function's interface grid.

## Format (singular — one value)
```json
{
  "type": "parameter",
  "type_key": "singular",
  "name": "loc",
  "value_type": "location",
  "is_required": "true",
  "default_value": "{}",
  "slot": 0,
  "description_slot": 9,
  "description": "{\"translations\":{},\"fallback\":{\"rawText\":\"Местоположение\",\"parsingType\":\"LEGACY\"}}"
}
```

## Format (plural — a parameter-array)
```json
{
  "type": "parameter",
  "type_key": "plural",
  "name": "locs",
  "value_type": "location",
  "is_required": "false",
  "default_value": "{}",
  "slots": "0,1,2",
  "description_slots": "9,10,11",
  "description": "{\"translations\":{},\"fallback\":{\"rawText\":\"Locations\",\"parsingType\":\"LEGACY\"}}"
}
```

## Fields
- `type`: fixed `"parameter"` — tells the game this is a parameter, not a variable.
- `type_key`: `"singular"` (single value, `slot`/`description_slot`) or `"plural"` (array of values, `slots`/`description_slots`).
- `name`: parameter name; in the function code it is read as a variable — `%var_line(loc)` (or `%var_local(loc)`, depending on how the call passes local variables).
- `value_type`: type of the value (`location`, `number`, `text`, `item`, `vector`, ...). The type is strictly enforced: passing text where a location is needed breaks the action (an empty value appears).
- `is_required`: whether the parameter must be passed at call time.
- `default_value`: default value as an escaped JSON string — `"{}"` for a location, `"{\"type\":\"number\",\"number\":0.0}"` for a number.
- `slot`: editor grid cell (0–54) where the parameter block sits (a number).
- `description_slot`: cell holding the parameter's description (usually `slot + 9`).
- `slots` / `description_slots` (plural only): comma-separated numbers as **strings**, e.g. `"0,1,2"`.
- `description`: stringified JSON text component (`translations` + `fallback` with `rawText` and `parsingType`).

## How it works on call
`call_function` passes data in its `args` argument (a value of type `map`). The game injects these values into the parameters and then executes the function code with the new values.

## Example (function handler `values`)
```json
"values": [
  {
    "name": "parameters",
    "value": {
      "type": "array",
      "values": [
        {
          "type": "parameter",
          "type_key": "singular",
          "name": "loc",
          "value_type": "location",
          "is_required": "true",
          "default_value": "{}",
          "slot": 0,
          "description_slot": 9,
          "description": "{\"translations\":{},\"fallback\":{\"rawText\":\"Местоположение\",\"parsingType\":\"LEGACY\"}}"
        }
      ]
    }
  }
]
```

## Rules
- The function handler's whole `values` array contains a single `parameters` entry; each element of its nested array is one parameter.
- `call_function` `args` keys must match the parameter names — see `docs/rules.md` → Function calls.
- Slots must not overlap between parameters and must not exceed 54 (grid range 0–54).
