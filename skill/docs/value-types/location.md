# Value type: location

A location literal: coordinate fields live directly in the value.

## Format
```json
{ "type": "location", "x": 0, "y": 64, "z": 0, "yaw": 0, "pitch": 0 }
```

## Rules
- **Prefer this literal over the "Create location" action (`set_variable_set_all_coordinates`)** — it saves an action and a variable.
- The action is only needed when coordinates are computed at runtime (`%math(...)`) — a literal doesn't fit then.
- Block center: JustMc gives coordinates from the block CENTER; subtract 0.5 per axis for the corner.
