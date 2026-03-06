# /reflect — Meta-Analysis Mode

Review recent work, identify patterns, suggest next moves. Reads bus history and recent handoffs.

## Steps

1. **Read Bus History**
```bash
~/.mirrordna/bin/bus history 2>/dev/null
```

2. **Read Recent Ledger**
```bash
tail -30 ~/.mirrordna/ledger.md 2>/dev/null
```

3. **Read Recent Completions**
```bash
for day in $(ls -r ~/.mirrordna/completions/ 2>/dev/null | head -7); do
  echo "=== $day ==="
  cat ~/.mirrordna/completions/$day/*.md 2>/dev/null | head -20
done
```

4. **Read Recent Handoffs**
```bash
ls -lt ~/MirrorDNA-Vault/Superagent/handoffs/ 2>/dev/null | head -5
for f in $(ls -t ~/MirrorDNA-Vault/Superagent/handoffs/*.md 2>/dev/null | head -3); do
  cat "$f"
done
```

5. **Check Current Vault State**
```bash
echo "Inbox: $(ls ~/MirrorDNA-Vault/00_INBOX/*.md 2>/dev/null | wc -l) items"
echo "Active: $(ls ~/MirrorDNA-Vault/02_ACTIVE/*.md 2>/dev/null | wc -l) items"
```

6. **Analyze Patterns**
Look for:
- **Velocity**: How much got done recently?
- **Focus drift**: Are tasks scattered or concentrated?
- **Completion rate**: How many items started vs finished?
- **Client mix**: Who's doing what (claude_code vs desktop vs human)?
- **Blockers**: Recurring issues or stuck items?
- **Gaps**: Areas with no recent activity

7. **Suggest Next Moves**
Based on patterns:
- What has momentum (continue)
- What's stalled (address or park)
- What's missing (start)
- What's overhead (automate or eliminate)

## Output

```
⟡ Reflection

Period: Last [N] days ([N] sessions)

Patterns:
  Velocity: [increasing/steady/decreasing] — [N] completions/week
  Focus: [concentrated on X / scattered across Y areas]
  Client mix: claude_code [N]% | desktop [N]% | human [N]%

What's Working:
  - [pattern that's producing results]
  - [effective workflow identified]

What's Not:
  - [bottleneck or recurring issue]
  - [stalled area]

Suggested Next Moves:
  1. [highest-leverage action]
  2. [second priority]
  3. [maintenance task]

Open Questions:
  - [strategic question worth considering]
```
