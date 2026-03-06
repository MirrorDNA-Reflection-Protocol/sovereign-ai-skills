# /handoff — Write Handoff for Next Client

Write a detailed handoff so the next client (Claude Desktop, AG, or human) can continue seamlessly.

**IMPORTANT:** All handoffs go to `~/.mirrordna/handoff/` — NEVER to the vault.
See `~/.mirrordna/AGENT_GOVERNANCE.md` for full rules.

## Arguments

`/handoff [target: desktop|ag|human]`

Default: desktop

## Steps

1. **Gather Context**
```bash
# What files were modified this session?
git diff --name-only HEAD~1 2>/dev/null
```

2. **Determine Target**
- `desktop` → Claude Desktop (reflection, strategy)
- `ag` → Antigravity (heavy builds — output goes to sandbox)
- `human` → Paul (review, decisions)

3. **Write Handoff JSON** (active state)
```bash
cat > ~/.mirrordna/handoff.json << EOF
{
  "client": "claude_code",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "action": "[DETAILED: what you did]",
  "pending": "[SPECIFIC: what's left]",
  "files_modified": [
    "[list exact paths]"
  ],
  "verification": "[how to verify work]",
  "next_client": "[desktop|ag|human]",
  "notes": "[context, blockers, decisions needed]"
}
EOF
```

4. **If Target is AG, Write Pending Handoff**
```bash
ID="HO-$(date +%Y%m%d)-$(date +%H%M)"
cat > ~/.mirrordna/handoff/pending/${ID}.md << EOF
# HANDOFF: Claude Code → Antigravity

**ID:** $ID
**Priority:** MEDIUM
**Created:** $(date '+%Y-%m-%d %H:%M') IST
**Status:** PENDING

## BEFORE EXECUTING
1. Read ~/.gemini/GEMINI.md
2. Read ~/.mirrordna/AGENT_GOVERNANCE.md
3. ALL output goes to sandbox: ~/.mirrordna/sandbox/ag/
4. Code goes to ~/repos/ — docs go to sandbox (NOT vault)
5. Completion report goes to ~/.mirrordna/handoff/completed/

## TASK
[What AG needs to do]

## CONTEXT
[What Claude Code already did]

## REPO
[Path to relevant repo]

## DELIVERABLES
[What success looks like]

## WHEN COMPLETE
Write to: ~/.mirrordna/handoff/completed/${ID}-COMPLETE.md
EOF
```

5. **Append to Ledger**
```bash
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | claude_code | HANDOFF → [target]: [summary]" >> ~/.mirrordna/ledger.md
```

6. **Write to Bus**
```bash
cd ~/.mirrordna && python3 -c "
from lib.memory_bus import MemoryBus
bus = MemoryBus()
with bus.write_transaction('Handoff to [target]') as txn:
    txn.update_state({'last_action': '[summary]', 'next_action': '[what target should do]'})
    txn.append_notes('Handoff to [target]: [details]')
"
```

7. **Commit State**
```bash
cd ~/.mirrordna && git add -A && git commit -m "⟡ Handoff to [target]"
```

## Output

```
Handoff written for [target]

Action: [what you did]
Pending: [what's next]
Files: [count] modified

[If desktop]: Start new Claude Desktop chat and say "pickup" or "where were we?"
[If AG]: AG will read from ~/.mirrordna/handoff/pending/ and sandbox output to ~/.mirrordna/sandbox/ag/
[If human]: Ready for your review, Paul.
```

## Handoff Quality Checklist

Before writing, ensure:
- [ ] Action is specific (not "worked on stuff")
- [ ] Pending is actionable (not "continue work")
- [ ] Files list is complete
- [ ] Verification is testable
- [ ] Notes include any blockers or decisions needed
- [ ] Handoff written to ~/.mirrordna/handoff/ (NOT the vault)
- [ ] If AG target: sandbox instructions included in preamble
