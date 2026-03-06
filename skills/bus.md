# /bus — Memory Bus Operations

Direct interface to the MirrorDNA Memory Bus — the single source of truth.

## Arguments

`/bus read` — Full state read
`/bus health` — Quick health check
`/bus history` — Session history (who wrote what)
`/bus intent` — Show binding constraints
`/bus write [message]` — Write to bus with message

Default (no args): `read`

## Steps

### Read
```bash
~/.mirrordna/bin/bus read
```

### Health
```bash
~/.mirrordna/bin/bus health
```

### History
```bash
~/.mirrordna/bin/bus history
```

### Intent
```bash
~/.mirrordna/bin/bus intent
```

### Write
```bash
echo '{"state":{"phase":"[inferred from context]"}}' | ~/.mirrordna/bin/bus write "[message]" --json
```

Or via Python for complex writes:
```python
from lib.memory_bus import MemoryBus
bus = MemoryBus()

with bus.write_transaction("[message]", writer="claude_code") as txn:
    txn.update_state({"phase": "[new phase]"})
    txn.remove_pending("[completed item]")
    txn.append_notes("[details]")
```

## Output

```
⟡ Bus: [subcommand]

[raw bus output, formatted]
```

## Notes

- The bus is the single source of truth — not handoff.json, not chat history
- Always read bus at session start
- Always write to bus before session ends
- Never write handoff.json directly — it's auto-generated from bus
