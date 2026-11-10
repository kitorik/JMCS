# Value type: number

A number. Three valid ways to fill the slot:
1. Plain number: `"number": 10`
2. Full math slot (string): `"number": "%math(...)"`
3. Reference to a number variable: a `variable` value.

## Format
```json
{ "type": "number", "number": 10 }
{ "type": "number", "number": "%math(%var(bb.t)*100/%var(bb.maxt))" }
```

## Rules
- ALWAYS wrap math in `number` with a `%math(...)` string, never in `text`.
- A numeric slot with a placeholder is wrapped in `%math()`: e.g. a weight from a map — `%math(%entry(dict, key))`.
- A nonexistent variable/key in a number slot → 0.
- Exports write numbers as `0.0`, `1.0`, `2.0` — floating format is normal.
