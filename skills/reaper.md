# /reaper — Staleness Reaper

Kill all staleness: ghost error logs, stale errors, bloated logs, crashed agents.

## Steps

1. **Run reaper**
```bash
python3 ~/.mirrordna/scripts/staleness_reaper.py 2>&1
```

Runs automatically every 30 minutes via LaunchAgent `ai.mirrordna.staleness-reaper`.

## What it does
- Clears error logs for agents that aren't loaded (ghost errors)
- Clears error logs older than 24h (stale noise)
- Rotates logs over 1MB to archive/
- Restarts crashed KeepAlive agents
- Deletes archived logs older than 7 days
- Reports via MirrorSignal
