# /status — Quick Status Check

Lightweight status check — bus phase, inbox count, pending items, git dirty count. Faster than `/health`.

## Steps

1. **Bus Phase**
```bash
~/.mirrordna/bin/bus read 2>/dev/null | head -5 || echo "Bus: OFFLINE"
```

2. **Inbox Count**
```bash
echo -n "Inbox: "
ls ~/MirrorDNA-Vault/00_INBOX/*.md 2>/dev/null | wc -l | tr -d ' '
echo " items"
```

3. **Pending Items**
```bash
echo "=== Pending ==="
cat ~/.mirrordna/handoff.json 2>/dev/null | jq -r '.pending' || echo "none"
```

4. **Git Dirty Count**
```bash
echo -n "Git dirty: "
DIRTY=0
for dir in ~/.mirrordna ~/MirrorDNA-Vault ~/repos/*; do
  if [ -d "$dir/.git" ]; then
    COUNT=$(cd "$dir" && git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    if [ "$COUNT" -gt 0 ]; then
      DIRTY=$((DIRTY + COUNT))
      echo -n "$(basename $dir):$COUNT "
    fi
  fi
done
[ $DIRTY -eq 0 ] && echo "clean" || echo "(total: $DIRTY)"
```

5. **Overnight Queue**
```bash
echo -n "Overnight: "
cat ~/.mirrordna/overnight-queue.json 2>/dev/null | jq '.tasks | length' 2>/dev/null || echo "0"
echo " tasks queued"
```

## Output

```
⟡ Status

Phase: [from bus]
Inbox: [N] items
Pending: [from handoff]
Git: [clean or N dirty files]
Overnight: [N] queued

[One-line recommendation if issues found]
```
