---
name: JAI
description: JustMc AI (JAI) — skill for coding on the JustMc Minecraft server (Creative+ mini-game). References for actions, game values, events, value types (text, number, item, location, vector, enum, array, map, variable, game_value, sound, particle), JSON module examples (EditSession, Essentials, Economy), cheatsheet, variable functions and %math() expressions.
version: 1.0.3
tags:
  - minecraft
  - justmc
  - creative-plus
  - jai
  - actions
  - game-values
  - math
  - variables
---

# JAI (JustMc AI)

Skill for the **JustMc AI** system — Minecraft server with the **Creative+** mini-game: actions, events, game values, variables, %math() and JSON modules.

> 🔍 **Version check (run before your first JustMc answer):** read `VERSION.md` next to this SKILL.md and compare its version with `version:` in the frontmatter above. If they **differ** (higher or lower), tell the user FIRST: "skill files out of sync: SKILL.md = X, VERSION.md = Y — the skill is outdated or corrupted; fresh version: JAI.zip from github.com/kitorik/JMCS". Ask whether to update the skill, then answer. If equal — answer without a warning.

> 🎛️ **Mode check (before the first substantive JAI work):** ask the player which mode they prefer — **"Сжатый" (Compressed)**: shorthand notation in explanations and code sketches (see the Chat shorthand section below), compact answers — or **"Полный" (Full)**: full official syntax everywhere, detailed answers. **Default if the player does not choose: "Полный" (Full).** In BOTH modes the final JSON module always uses the full official syntax.

**Server limits:** up to **300 iterations without a wait** per run (exceeding = critical error + full world freeze); **`game_set_region` sets up to 125,000 blocks per call**. Full details in `docs/rules.md`.

## 📚 Docs map (read on demand, relative to this skill's folder)

Before writing or editing a module, check `docs/rules.md` and the relevant reference file. Use exact action/event/value IDs from the tables.

### Rules
| File | Contents |
|------|-----------|
| `docs/rules.md` | Module rules: line limits (≤33 conditions, ≤67 actions, ≤67 total content units; 1 condition = 2 actions), JSON structure, placeholder syntax, delays & world-load safety, function calls & parameters, variable scopes, critical server limits |

### Actions (`docs/actions/`)
| File | Contents |
|------|-----------|
| `docs/actions/variable.md` | Variables: conditions (`if_variable_*`), assignments (`set_variable_*`) — numbers, texts, lists, maps, locations, vectors, items, stylable texts |
| `docs/actions/world.md` | World: blocks, containers, recipes, scoreboards, `game_*` events, entity spawn, world settings, web requests |
| `docs/actions/player.md` | Players: `if_player_*`, inventory, communication, motion, disguise, particles, parameters, menus |
| `docs/actions/entity.md` | Entities: parameters, motion, AI goals (`entity/goals`), disguise, displays (`display_entity`), settings, custom tags |
| `docs/actions/select.md` | Selections: create, add, filter (`select_*`) |
| `docs/actions/repeat.md` | Loops (`repeat_*`): list, map, region, circle, sphere, range, while |
| `docs/actions/code.md` | Code: function/process calls, flow control (`control_*`), `else`, wait |
| `docs/actions/controller.md` | Controllers: labels, selection isolation, error catching, timing, separate thread |

### Values (`docs/values/`) and value types (`docs/value-types/`)
| File | Contents |
|------|-----------|
| `docs/values/values.md` | All game values: stats, events, entity/world info — with return types |
| `docs/value-types/<type>.md` | One file per type — format, examples, rules: text, number, variable, item (**always NBT-encoded**), location, vector, enum, array, map, game_value, sound, particle, parameter (function parameter declaration) |

### Events (`docs/events/`)
| File | Contents |
|------|-----------|
| `docs/events/events.md` | All events: ID, name, description, category, cancellable, compatibility, extra info, status |

### Examples (`docs/examples/`)
| File | Contents |
|------|-----------|
| `editsession.json` | EditSession: `wait`, `openES`/`editES`/`closeES` (block-edit sessions, buffer 20000), `setRegionES`, `replaceRegionES`, `copyRegionES`, `randomSetES`; chat commands \set, \replace, \copy, \paste |
| `essentials.json` | Essentials: `worldinfo`, `playerinfo`, `gm`; MAPI module manifest (`mapi=essentials`), message prefix, join-date fixing |
| `economy.json` | Economy: `pay`, `balance` (set/take/add/show), `Eco.take` function; save-vars `%player%_balance`, balance boss bar, MAPI (`Mapi.commandConstructor`) |
| `cheatsheet.md` | Cheatsheet: value formats (item is NBT!), common errors + fixes, ready patterns (timer with boss bar, tokens, leaderboard, zone selection, chat commands, block corners, unique names, random pick) |

> ℹ️ **Examples show syntax, not design.** The mini-game start method (chat command, interaction event, menu, any event) is ALWAYS the player's choice — never impose one.

Examples show the real JSON syntax of JustMc modules: `handlers` → `operations`, value types (`variable`, `game_value`, `text`, `number`, `map`, `array`), variable scopes (`line`/`local`/`game`/`save`), function parameters, conditions (`conditional`, `is_inverted`), nested `else` blocks, function calls (`call_function`).

> ℹ️ Every reference table row contains: ID, name, description, category/subcategory, arguments with types and enum values (repeated enum sets are replaced with macros — see the legend at the top of each file), compatibility, extra info and status (deprecated/unused).

---

## 🎯 Placeholders

### Targets
| Placeholder | Description |
|-------------|-------------|
| `%player%` | Name of the player who triggered the event or was targeted in a "each target in selection" process |
| `%player_uuid%` | Player UUID (analog of %player%) |
| `%entity%` | Name of the entity that triggered/participated in the event. Can be a player |
| `%entity_uuid%` | Entity UUID (analog of %entity%) |
| `%uuid%` | Shortcut for %entity_uuid% |
| `%victim%` | Victim of the event (entity/player the action was performed on) |
| `%victim_uuid%` | Victim UUID |
| `%damager%` | Attacker name in the event |
| `%damager_uuid%` | Attacker UUID |
| `%shooter%` | Shooter name in the event |
| `%shooter_uuid%` | Shooter UUID |
| `%killer%` | Killer name in the death event |
| `%killer_uuid%` | Killer UUID |
| `%selected%` | Name of the first target in the current selection |
| `%selected_uuid%` | UUID of the first target in the current selection |
| `%display_name%` | Display name of the entity. For players — name with prefix and suffix |

### Variable functions

| Placeholder | Description |
|-------------|-------------|
| `%var(name)` | Value of the game variable `name` (game scope) |
| `%length(name)` | Length of list/map `name` |
| `%index(list, index)` | Value from list `list` at index `index` |
| `%entry(dict, key)` | Value from map `dict` by key `key` |
| `%val(id)` | Game value with ID `id` |

> ℹ️ **Scope suffixes:** every variable function (`%var`, `%length`, `%index`, `%entry`) exists in all 4 scopes: game (bare, e.g. `%var(name)`), local (`%var_local(name)`), save (`%var_save(name)`), line (`%var_line(name)`) — likewise `%length_*`, `%index_*`, `%entry_*`.

### Chat shorthand (explanations only!)

> ⚠️ Shorthand is for chat explanations and code sketches ONLY. The final JSON module must always use the FULL official syntax.

- `%v()` = `%var()`, `%v_lo()` = `%var_local()`, `%v_sa()` = `%var_save()`, `%v_li()` = `%var_line()` (also `%len_*`, `%idx_*`, `%ent_*`)
- `%pl%` = `%player%`, `%pl_uuid%` = `%player_uuid%`, `%e%` = `%entity%`, `%e_uuid%` = `%entity_uuid%`
- `p_<event>` = the `player_<event>` event family (e.g. `p_join` = `player_join`) — always expand to the real event ID in JSON
- Enum macros from the reference tables (`{TF}`, `{ITEM_MATCH}`, …) — always expand to real enum values in JSON

### System values
| Placeholder | Description |
|-------------|-------------|
| `%player_amount%` | Players in the world |
| `%entity_count%` | Entities in the world (excluding players) |
| `%entity_amount%` | Alias for %entity_count% |
| `%global_online%` | Players on the server |
| `%online%` | Shortcut for %global_online% |
| `%time%` | Server time, ISO-8601 |
| `%worlds%` | Number of online players' worlds |

### Misc
| Placeholder | Description |
|-------------|-------------|
| `%damage%` | Damage dealt in the event |
| `%random%` | Random number in [0, 1) |
| `%random_uuid%` | Randomly generated UUID |
| `%empty%` | Empty string |
| `%space%` | Space |

---

## ➗ %math() expressions

### Number formats
- Decimal: `1`, `2.5`, `-3.14`
- Exponent: `1e10`, `1.2E-3`, `-5e+2`
- Binary: `0b01`, `0b101010`
- Octal: `0o01234567`
- Hex: `0x0123456789ABCDEF`, `0xFF`

### Constants
| Constant | Meaning | Value |
|----------|----------|---------|
| `PI` | Pi | 3.141592653589793 |
| `E` | Euler's number | 2.718281828459045 |

### Variables in expressions
- Naming: letters, digits (not first), `_`, `$` (Java-style).
- Variable scope is auto-resolved by locality: 1) line → 2) local → 3) game → 4) save.
- `%math(a + b)` adds variables `a` and `b`, picking the most local available.

> ⚠️ %var() inside %math() is substituted as raw text. Wrap for correctness: `%math(%var(x) + 1)`

### Functions
| Function | Description | Example |
|----------|-------------|---------|
| `abs(x)` | Absolute value | `abs(-5) = 5` |
| `sign(x)` | Sign: -1, 0 or 1 | `sign(-3.5) = -1` |
| `min(a,b,...)` | Minimum (≤5 args) | `min(1,2,3) = 1` |
| `max(a,b,...)` | Maximum (≤5 args) | `max(1,2,3) = 3` |
| `clamp(x,min,max)` | Clamp to [min, max] | `clamp(5,1,3) = 3` |
| `wrap(x,min,max)` | Wrap to [min, max) | `wrap(5,1,3) = 1` |
| `round(x,a)` | Round to precision a | `round(3.1415,2) = 3.14` |
| `ceil(x,a)` | Round up, precision a | `ceil(3.1415,2) = 3.15` |
| `floor(x,a)` | Round down, precision a | `floor(3.1415,2) = 3.14` |
| `pow(x,a)` | Power | `pow(2,3) = 8` |
| `sqrt(x)` | Square root | `sqrt(16) = 4` |
| `cbrt(x)` | Cube root | `cbrt(27) = 3` |
| `root(x,a)` | Root of degree a | `root(16,4) = 2` |
| `log(a,x)` | Log base a | `log(10,100) = 2` |
| `ln(x)` | Natural log | `ln(E) = 1` |
| `sin(x)` | Sine (degrees) | `sin(90) = 1` |
| `cos(x)` | Cosine (degrees) | `cos(0) = 1` |
| `sinr(x)` | Sine (radians) | `sinr(PI/2) = 1` |
| `cosr(x)` | Cosine (radians) | `cosr(0) = 1` |
| `asin(x)` | Arcsine (radians) | `asin(1) = PI/2` |
| `acos(x)` | Arccosine (radians) | `acos(1) = 0` |
| `atan2(y,x)` | Arctangent (radians) | `atan2(1,1) = PI/4` |

> ⚠️ Angles: degrees for sin/cos, radians for sinr/cosr.

### Operators (by precedence)
1. `(x)` — grouping
2. `^` — power (`2^3 = 8`)
3. Unary: `+x`, `-x`, `!x` (logical not), `~x` (bitwise not)
4. `*`, `/`, `%` (remainder), `//` (integer division)
5. `+`, `-`
6. Bit shifts: `<<`, `>>`, `>>>`
7. Comparison: `>`, `>=`, `<`, `<=`
8. Equality: `==`, `!=`
9. Bitwise: `&`, `~` (XOR), `|`
10. Logical: `&&`, `||`
11. Ternary: `a ? b : c` — if a ≠ 0 then b else c

> ℹ️ Logical operators return 0/1; bitwise operators work on 64-bit numbers; all math runs in BigDecimal with 10-digit precision; infinite-fraction ops (roots, logs, trig) use double.

---

## 🎯 Usage examples

```
# Entity placeholders
%damager% dealt %damage% damage to %victim%
Your UUID: %player_uuid%
Hello, %display_name%!

# Math
%math(2 + 3 * 4) = 14
%math(sqrt(16) + pow(2, 3)) = 8
%math(clamp((x + y) * 2, 0, 100))
%math(health > 50 ? "Healthy" : "Wounded")

# Variables
Health: %var(health)
First item: %index(my_list, 0)   Length: %length(my_list)
By key: %entry(my_dict, key)

# Trig & random
%math(sin(45)) = 0.7071      %math(asin(0.5) * 180/PI) = 30
Random: %random%              %math(random * 100)

# Time & online
Now: %time%    Online: %online% of %player_amount%
```

---

## 🔗 Resources
- [JustMC Assets — documentation (RU)](https://github.com/realDosed/justmc-assets/tree/master/documentation/ru_RU)
- [unidok/modules](https://github.com/unidok/modules) — module collection
- [jmc-commandtree](https://github.com/White-145/jmc-commandtree) — command tree example

## 💡 Best practices
1. Prefer %math() over %var() for computations where possible.
2. Split complex expressions into simple parts.
3. Validate inputs before computing.
4. Use %empty% and %space% for output formatting.
5. Remember variable resolution order (line → local → game → save).
6. **Call functions ONLY via `call_function`** (exact function `name` + `args` for every required parameter). `start_process` starts a process code line — NEVER use it to call a function.
7. **Prefer the inline `location` value literal** over the "Create location" action when coordinates are known — see `docs/value-types/location.md`.
8. **Use the narrowest variable scope that works** (`line` → `local` → `game` → `save`) — do not default everything to `game`. Function parameters are read as `%var_line(name)`.
9. **Delays:** `control_wait` minimum is 1 tick, integers only in TICKS mode. Under heavy world load use the CPU-wait pattern (`rules.md` → Delays and world load) — the world must never reach the critical error caused by sustained 100%+ load.

---

## 📝 Versions
- **1.0.3** — New variable rules: never zero-initialize or "declare" variables (unset = 0); clear variables only via `set_variable_remove` / `set_variable_purge`; check game start with `if_variable_exists`, not marker variables.
- **1.0.2** — Added the missing `parameter` value-type reference (`docs/value-types/parameter.md`); removed dead references to deleted example files in cheatsheet.md.
- **1.0.0** — Initial release: complete starter set (SKILL.md, rules, 8 action references, events, values, 13 value-types incl. `parameter`, cheatsheet, official examples EditSession/Essentials/Economy).

---

## ℹ️ About JustMc
**JustMc** — Minecraft server with the **Creative+** mini-game for creative building and gameplay.
