# JAI syntax — placeholders and %math() expressions

All placeholder tables and the full %math() reference. Value formats (item, location, ...) live in `docs/value-types/<type>.md`.

## Placeholders

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

> Scope suffixes: every variable function (`%var`, `%length`, `%index`, `%entry`) exists in all 4 scopes: game (bare, e.g. `%var(name)`), local (`%var_local(name)`), save (`%var_save(name)`), line (`%var_line(name)`) — likewise `%length_*`, `%index_*`, `%entry_*`.

> **Always read variable values via the %var family.** A bare variable name in a text, message or argument slot is plain text, NOT a value reference. The same applies inside %math() — wrap variables in the %var family there too.

### Chat shorthand (explanations only!)

> Shorthand is for chat explanations and code sketches ONLY (mode "Compressed"). The final JSON module must always use the FULL official syntax.

- `%v()` = `%var()`, `%v_lo()` = `%var_local()`, `%v_sa()` = `%var_save()`, `%v_li()` = `%var_line()` (also `%len_*`, `%idx_*`, `%ent_*`)
- `%pl%` = `%player%`, `%pl_uuid%` = `%player_uuid%`, `%e%` = `%entity%`, `%e_uuid%` = `%entity_uuid%`
- `p_<event>` = the `player_<event>` event family (e.g. `p_join` = `player_join`) — always expand to the real event ID in JSON
- Enum macros from the reference tables (`{TF}`, `{ITEM_MATCH}`, ...) — always expand to real enum values in JSON

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

## %math() expressions

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
- **Inside %math() the syntax is the same as without it** — wrap variables in `%var()` / `%var_local()` / `%var_line()` / `%var_save()`: `%math(%var(x) + 1)`, `%math(%var_line(a) + %var_local(b))`. Bare names are NOT valid inside %math(). There is **no %var_game()** — game scope is the bare `%var()`.
- %var() inside %math() is substituted as raw text. Wrap for correctness: `%math(%var(x) + 1)`

### Functions
| Function | Description | Example |
|----------|-------------|---------|
| `abs(x)` | Absolute value | `abs(-5) = 5` |
| `sign(x)` | Sign: -1, 0 or 1 | `sign(-3.5) = -1` |
| `min(a,b,...)` | Minimum (<=5 args) | `min(1,2,3) = 1` |
| `max(a,b,...)` | Maximum (<=5 args) | `max(1,2,3) = 3` |
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

> Angles: degrees for sin/cos, radians for sinr/cosr.

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
11. Ternary: `a ? b : c` — if a != 0 then b else c

> Logical operators return 0/1; bitwise operators work on 64-bit numbers; all math runs in BigDecimal with 10-digit precision; infinite-fraction ops (roots, logs, trig) use double.

---

## Usage examples

```
# Entity placeholders
%damager% dealt %damage% damage to %victim%
Your UUID: %player_uuid%
Hello, %display_name%!

# Math
%math(2 + 3 * 4) = 14
%math(sqrt(16) + pow(2, 3)) = 8
%math(clamp((%var(x) + %var(y)) * 2, 0, 100))
%math(%var(health) > 50 ? "Healthy" : "Wounded")

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
