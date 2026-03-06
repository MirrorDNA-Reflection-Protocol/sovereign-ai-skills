# /dream — Run Dream Engine

Trigger the sovereign dream engine — processes vault notes, generates insights, creates new connections while Paul sleeps.

## Steps

1. **Run dream cycle**
```bash
python3 ~/.mirrordna/scripts/dreaming_daemon.py --once 2>&1 | tail -20
```

2. **Check dream output**
```bash
ls -lt ~/.mirrordna/dreams/ 2>/dev/null | head -5
```
