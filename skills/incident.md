# /incident — Post-Mortem Generator

Generate a structured post-mortem from recent failures, heal logs, and pulse state.

## Steps

1. **Collect evidence**
```bash
tail -20 ~/.mirrordna/mirrorpulse/logs/heal.jsonl 2>/dev/null
cat ~/.mirrordna/mirrorpulse/state/pulse_state.json 2>/dev/null
tail -20 ~/.mirrordna/logs/smoke_test.log 2>/dev/null
cat ~/.mirrordna/health/proactive_alerts.json 2>/dev/null
```

2. **Identify incident**: what broke, when, impact, duration
3. **Root cause**: trace from symptom to cause using heal logs and event chain
4. **Resolution**: what fixed it (auto-heal or manual)
5. **Prevention**: what hook/guard/agent would prevent recurrence
6. **Write post-mortem** to `~/.mirrordna/incidents/INC-YYYYMMDD-NNN.md`

## Output Format
```
INCIDENT POST-MORTEM — INC-[date]-[seq]
  What: [one line]
  When: [timestamp] — Duration: [Xm]
  Impact: [what was affected]
  Root cause: [why it happened]
  Resolution: [how it was fixed]
  Prevention: [what to automate]
  Status: [resolved/monitoring]
```
