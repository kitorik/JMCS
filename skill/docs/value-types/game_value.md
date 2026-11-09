# Value type: game_value

A game value — data of a target or event (location, name, ping, etc.). Full list in `docs/values/values.md`.

## Format
```json
{ "type": "game_value", "game_value": "location", "selection": "null" }
```
- `selection` — target: `"null"` (no target), `"{\\"type\\":\\"default\\"}"` (event's default target), `"{\\"type\\":\\"current\\"}"` (current selection).
- A game value with no target → `selection: "null"` (that's normal and expected).

## Examples
```json
{ "type": "game_value", "game_value": "event_block_location", "selection": "null" }
{ "type": "game_value", "game_value": "name", "selection": "{\\"type\\":\\"default\\"}" }
{ "type": "game_value", "game_value": "world_size", "selection": "null" }
```

## Rules
- `game_value` can be embedded directly into an `array` of text messages (see essentials.json).
- Some game values only work in events (`event_*`) or for players.
