# /standup — Morning Standup

Generate a concise briefing: what happened since last session, current state, today's priorities.

## Steps

1. **Read Bus State**
```bash
~/.mirrordna/bin/bus read 2>/dev/null
```

2. **Check Overnight Completions**
```bash
ls ~/.mirrordna/completions/$(date +%Y-%m-%d)/ 2>/dev/null
```

3. **Inbox Status**
```bash
ls ~/MirrorDNA-Vault/00_INBOX/*.md 2>/dev/null | wc -l
```

4. **Git Activity** — commits in last 12 hours across all repos

5. **Pending Work** — from handoff

6. **Dirty Repos** — uncommitted changes

## Output

```
⟡ Standup — [date]

Since Last Session:
  - [activity]

Current State:
  Phase: [from bus]
  Inbox: [N] items
  Pending: [from handoff]
  Dirty repos: [list or "all clean"]

Today's Priorities:
  1. [most important]
  2. [second]
  3. [third]

Blockers: [any or "None"]
```
