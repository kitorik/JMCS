# Value type: sound

A sound with pitch and volume modifiers. Format confirmed by the official economy.json export.

## Format
```json
{ "type": "sound", "sound": "minecraft:entity.experience_orb.pickup", "pitch": 1.0, "volume": 1.0 }
```

## Examples
```json
{ "type": "sound", "sound": "minecraft:block.lava.extinguish", "pitch": 2.0, "volume": 0.5 }
```

## Rules
- Sound id is the standard `minecraft:<sound>`.
- `pitch` — tone (1.0 = normal), `volume` — volume (0–1+, 1.0 = normal).
- Typical slots: the `sound` argument of `player_play_sound`, `entity_set_arrow_hit_sound`.
