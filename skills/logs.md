# /logs — View Service Logs

Tail MirrorDNA service logs for debugging and monitoring.

## Arguments

`/logs [service-name]` — Tail logs for a service
`/logs` — List available log files

## Steps

### List Logs (no argument)
```bash
echo "=== Available Logs ==="
ls -lh ~/.mirrordna/logs/ 2>/dev/null || echo "No log directory"
echo ""
echo "=== Recent Log Activity ==="
for f in ~/.mirrordna/logs/*.log; do
  [ -f "$f" ] || continue
  echo "$(basename $f): $(wc -l < "$f") lines, last modified $(stat -f '%Sm' -t '%Y-%m-%d %H:%M' "$f")"
done
```

### View Specific Log
1. **Find Log File**
```bash
LOG="$HOME/.mirrordna/logs/${1}.log"
if [ ! -f "$LOG" ]; then
  # Try partial match
  LOG=$(ls ~/.mirrordna/logs/*${1}*.log 2>/dev/null | head -1)
fi
```

2. **Show Recent Entries**
```bash
echo "=== Last 50 lines: $(basename $LOG) ==="
tail -50 "$LOG"
```

3. **Check for Errors**
```bash
echo ""
echo "=== Errors (last 24h) ==="
grep -i "error\|exception\|fatal\|crash" "$LOG" | tail -20
```

4. **Show Log Stats**
```bash
echo ""
echo "=== Stats ==="
echo "Total lines: $(wc -l < "$LOG")"
echo "Errors: $(grep -ic 'error' "$LOG")"
echo "Warnings: $(grep -ic 'warn' "$LOG")"
echo "Size: $(ls -lh "$LOG" | awk '{print $5}')"
```

## Output

```
⟡ Logs: [service]

Last 50 lines:
[log content]

Errors (last 24h): [N]
  [error lines if any]

Stats: [N] total lines, [size]
```
