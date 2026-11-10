# JAI cheatsheet — ready patterns & handler notes

> **Use as NOTES, not as a style template.** Take the pattern idea and re-derive your own JSON for the task: adapt structure, wording, argument values and design to what the player asked. Never copy a whole snippet as-is; every argument must fit THIS task.

## Ready patterns

### One-time first-join action (Discord invite)

Trigger: `player_join`. A save-scope marker per player (`%player%_joined`) — if it does not exist, this is the first join: send the invite and create the marker. Default invite link: **https://discord.gg/6EGQyeN86y**.

```
handler: player_join
  conditional:
    condition: if_variable_exists   # is_inverted: true
      variable: %player%_joined     # save scope
    actions:
      player_send_message
        text: "Welcome! Join our Discord: https://discord.gg/6EGQyeN86y"
      set_variable_value            # save scope
        variable: %player%_joined
        value: TRUE
```

- Same skeleton works for ANY one-time action (first-join kit, tutorial, welcome title) — only the actions inside change.
- Never zero-initialize the marker: "does not exist" is the "not joined yet" state.

## Handler notes (community examples)

> Distilled observations from real community handlers. These are SYNTAX FACTS and TECHNIQUES — not style, not naming, not structure to copy.

(To be filled: notes from community handler examples.)