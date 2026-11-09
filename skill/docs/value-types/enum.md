# Value type: enum

An enumeration — a fixed option from the list defined by the action's argument.

## Format
```json
{ "type": "enum", "enum": "TRUE" }
```

## Examples
```json
{ "type": "enum", "enum": "SPACES" }
{ "type": "enum", "enum": "NO_TARGET" }
{ "type": "enum", "enum": "PROGRESS" }
```

## Rules
- Valid options depend on the specific argument (see the action reference).
- Typical sets: `TRUE`/`FALSE`, `TICKS`/`SECONDS`, `SPACES`/`CONCATENATION`/`SEPARATE_LINES`, selection modes `DEFAULT`/`CURRENT`/`EMPTY`/`FOR_EACH`.
