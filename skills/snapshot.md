# /snapshot — System Snapshot

Capture a full system snapshot: services, ports, disk, memory, processes.

## Steps

1. **Run snapshot**
```bash
python3 ~/.mirrordna/scripts/system_snapshot.py 2>&1
```

2. **Read latest**
```bash
cat ~/.mirrordna/snapshots/latest.json 2>/dev/null | python3 -m json.tool | head -30
```
