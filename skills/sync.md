# /sync — Synchronize State Across All Clients

Read all state files, reconcile, and report current system status.

## Steps

1. **Read MirrorDNA State**
```bash
echo "=== STATE ===" && cat ~/.mirrordna/state.json 2>/dev/null | jq . || echo "No state file"
```

2. **Read Current Handoff**
```bash
echo "=== HANDOFF ===" && cat ~/.mirrordna/handoff.json 2>/dev/null | jq . || echo "No handoff"
```

3. **Check Today's Completions**
```bash
echo "=== COMPLETIONS ===" && ls -la ~/.mirrordna/completions/$(date +%Y-%m-%d)/ 2>/dev/null || echo "No completions today"
```

4. **Check Recent Ledger Entries**
```bash
echo "=== LEDGER (last 10) ===" && tail -10 ~/.mirrordna/ledger.md 2>/dev/null || echo "No ledger"
```

5. **Check MirrorBrain**
```bash
echo "=== MIRRORBRAIN ===" && curl -s http://localhost:8081/api/system/state 2>/dev/null | jq . || echo "MirrorBrain offline"
```

6. **Check Git Status**
```bash
echo "=== GIT STATUS ===" && cd ~/.mirrordna && git status --short 2>/dev/null || echo "Not a git repo"
```

## Output Format

Summarize to human:
- **Last action:** [from handoff]
- **Pending:** [from handoff]
- **Last client:** [from handoff]
- **Services:** [up/down]
- **Git:** [clean/dirty]

## Example Response

```
⟡ State Sync Complete

Last action: Fixed tier pills in ActiveMirror v3
Pending: Add transparency widget
Last client: claude_desktop
Services: MirrorBrain ✅ | Inference ❌ | UI ✅
Git: Clean (last commit 2h ago)

Ready to continue. What's next?
```
