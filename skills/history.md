# /history — Session History

Show session history from ledger and memory bus. Who did what, when.

## Arguments

`/history [N]`

Show last N sessions. Default: 10.

## Steps

1. **Read Bus History**
```bash
~/.mirrordna/bin/bus history 2>/dev/null || echo "Bus history unavailable"
```

2. **Read Ledger**
```bash
echo "=== LEDGER ==="
tail -${1:-20} ~/.mirrordna/ledger.md 2>/dev/null || echo "No ledger found"
```

3. **Read Recent Completions**
```bash
echo "=== RECENT COMPLETIONS ==="
for day in $(ls -r ~/.mirrordna/completions/ 2>/dev/null | head -3); do
  echo "--- $day ---"
  ls ~/.mirrordna/completions/$day/ 2>/dev/null
done
```

4. **Read Recent Handoffs**
```bash
echo "=== HANDOFF HISTORY ==="
ls -lt ~/MirrorDNA-Vault/Superagent/handoffs/ 2>/dev/null | head -10
```

5. **Synthesize Timeline**
Merge all sources into a chronological view.

## Output

```
⟡ Session History (last [N])

| Time | Client | Action | Status |
|------|--------|--------|--------|
| 2026-01-27 14:30 | claude_code | Vault triage + spec creation | Completed |
| 2026-01-27 10:15 | claude_desktop | Strategy review | Handed off |
| 2026-01-26 23:00 | claude_code | Overnight CSS refactor | Completed |
| 2026-01-26 18:30 | human | Manual review | — |

Completions today: [N]
Total sessions this week: [N]
```
