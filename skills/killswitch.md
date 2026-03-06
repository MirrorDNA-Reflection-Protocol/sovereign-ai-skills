# /killswitch — Emergency Kill Switch

Activate or check the sovereign kill switch. Stops all non-essential services.

## Arguments
- `/killswitch status` — Check current state
- `/killswitch activate` — ACTIVATE (requires confirmation)
- `/killswitch deactivate` — Restore services

## Steps

1. **Check status**
```bash
python3 ~/.mirrordna/scripts/killswitch.py status 2>&1
```

**WARNING: Activation stops all services. Only use in emergencies.**
