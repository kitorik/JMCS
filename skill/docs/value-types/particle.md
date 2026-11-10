# Value type: particle

A particle effect with count, spread and size parameters.

## Format
```json
{ "type": "particle", "particle_type": "", "count": 10, "first_spread": 0, "second_spread": 0, "size": 1 }
```

## Fields
- `particle_type` — particle id (no `minecraft:` prefix);
- `count` — particle count;
- `first_spread` / `second_spread` — spread;
- `size` — size.

## Where used
- `trail: particle` — projectile trail (`entity_launch_projectile`);
- `particle: particle` — particle effect for a player (`player_display_particle`).

## Rules
- Never put text in a particle slot — only a particle value or a particle variable.
