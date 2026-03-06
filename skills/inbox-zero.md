# /inbox-zero — Clear All Pending

Process ALL pending items across every inbox until zero remains or everything is explicitly deferred.

## Inboxes

1. Vault `00_INBOX/`
2. Bus pending items
3. Git dirty repos
4. Overnight queue results
5. Stale handoffs

## Steps

1. **Inventory All Inboxes**
```bash
echo "Vault inbox: $(ls ~/MirrorDNA-Vault/00_INBOX/*.md 2>/dev/null | wc -l)"
~/.mirrordna/bin/bus read 2>/dev/null | grep -A 10 "pending"
for dir in ~/.mirrordna ~/MirrorDNA-Vault ~/repos/*; do
  [ -d "$dir/.git" ] && cd "$dir" && COUNT=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ') && [ "$COUNT" -gt 0 ] && echo "$(basename $dir): $COUNT dirty"
done
```

2. **Process Vault Inbox** — classify, add frontmatter, move to layer
3. **Process Bus Pending** — execute, defer, or clear each item
4. **Process Git Dirty** — commit with contextual messages
5. **Process Overnight Results** — verify completions, handle failures
6. **Clear Stale Handoffs** — archive if >24h old and no longer relevant
7. **Final Inventory** — recount everything
8. **Update Bus** — record inbox zero timestamp

## Output

```
⟡ Inbox Zero

Processed:
  Vault inbox: [N] → triaged
  Bus pending: [N] → resolved
  Git repos: [N] committed
  Overnight: [N] processed
  Handoffs: [cleared/flagged]

Deferred:
  - [item]: [reason]

Status: [ZERO / N deferred]
```
