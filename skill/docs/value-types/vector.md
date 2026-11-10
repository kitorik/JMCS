# Value type: vector

A vector (x, y, z) — direction, velocity, scale. Like location, but without yaw/pitch.

## Format
```json
{ "type": "vector", "x": 0, "y": 1, "z": 0 }
```

## Where used
- `velocity: vector` — launching an entity along a vector (`entity_set_location`);
- `axis_vector`/`direction`/`up` — display rotations (`entity_set_display_rotation_*`);
- `scale_vector`/`translation_vector` — display size and offset;
- `power: vector` — projectile motion vector (`entity_set_projectile_power`).

## Examples
```json
{ "type": "vector", "x": 0, "y": 1, "z": 0 }
{ "type": "vector", "x": 2, "y": 2, "z": 2 }
```

## Rules
- Player look direction: the `direction_of_view` game value (vector type).
- To change display scale use mode: SET/ADD of the corresponding action.
