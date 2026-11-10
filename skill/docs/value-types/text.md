# Value type: text

Text. The `parsing` field is optional (often absent in official exports — default parsing then).

## Format
```json
{ "type": "text", "text": "Hello, %player%!", "parsing": "plain" }
```
- `parsing`: `plain` — no color codes; `legacy` — with `&` codes;
- without `parsing`, hex codes like `&#a6ff6e` are available (see economy.json).

## Examples
```json
{ "type": "text", "text": "&6&lMATCH OVER!", "parsing": "legacy" }
{ "type": "text", "text": "%var_local(rx),%var_local(ry),%var_local(rz)" }
```

## Inside array
```json
{ "type": "array", "values": [ { "type": "text", "text": "set" }, { "type": "text", "text": "add" } ] }
```

- Placeholders in text: `%var(name)`, `%var_local(name)`, `%var_save(name)`, `%player%`, `%math(...)` — WITHOUT closing `%` for variable functions, WITH `%` for system values.
- An empty optional text slot is `{}`.
