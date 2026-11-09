# Value type: item

An item. **All `block` slots (game_set_block etc.) take an item value** — "where there is block, there is an item".

## Rule: items are ALWAYS encoded as an NBT string
`Count` + `id` (with the `minecraft:` prefix) + optional `tag:{...}` for extra data (custom name, enchantments, lore...).

## Format
```json
{ "type": "item", "item": "{Count:1b,id:\\"minecraft:iron_block\\"}" }
```

## Examples
Simple item:
```json
{ "type": "item", "item": "{Count:1b,id:\\"minecraft:diamond\\"}" }
{ "type": "item", "item": "{Count:1b,id:\\"minecraft:air\\"}" }
```
Full item with NBT tag (icon from the official economy.json export):
```json
{ "type": "item", "item": "{Count:1b,id:\\"minecraft:gold_ingot\\",tag:{display:{Name:'{\\"italic\\":false,\\"color\\":\\"yellow\\",\\"text\\":\\"Eco.take\\"}'}}}" }
```

## Empty item `"{}"`
- `"item": "{}"` — **valid syntax** (empty item). Official exports use it as the default icon for hidden functions.
- Where a real item is meant, put a real item, not the empty one.

## Rules
- The `id` inside the NBT string always carries the `minecraft:` prefix.
- Legacy modules (skill ≤ 2.9.2) may use bare ids like `"mace"` — accept them when reading, but always generate the NBT form.
- An item can be stored in a variable (`set_variable_value`) and passed by reference `{"type":"variable",...}` into an item slot.
