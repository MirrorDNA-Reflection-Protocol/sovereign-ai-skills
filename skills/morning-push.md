# /morning-push — Send Morning Briefing to Devices

Reads the latest overnight report and pushes it to OnePlus + Pixel via MirrorSignal + ADB.

## Steps

1. **Run push**
```bash
python3 ~/.mirrordna/scripts/morning_push.py 2>&1
```

2. **Verify delivery**
```bash
tail -10 ~/.mirrordna/logs/morning-push.log
```
