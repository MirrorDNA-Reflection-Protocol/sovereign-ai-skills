# /pickup — Continue From Last Handoff

Read the last handoff and continue the pending work without asking.

## Steps

1. **Read Handoff**
```bash
HANDOFF=$(cat ~/.mirrordna/handoff.json 2>/dev/null)
echo "$HANDOFF" | jq .
```

2. **Extract Key Fields**
```bash
ACTION=$(echo "$HANDOFF" | jq -r '.action')
PENDING=$(echo "$HANDOFF" | jq -r '.pending')
FILES=$(echo "$HANDOFF" | jq -r '.files_modified[]?' 2>/dev/null)
NOTES=$(echo "$HANDOFF" | jq -r '.notes')
LAST_CLIENT=$(echo "$HANDOFF" | jq -r '.client')
```

3. **Acknowledge Context**
Say briefly:
```
⟡ Picking up from [LAST_CLIENT]:
   Done: [ACTION]
   Pending: [PENDING]
   Continuing now...
```

4. **Execute Pending Work**
- Don't ask for permission
- Don't re-explain what you're going to do
- Just start working on PENDING

5. **When Done, Write New Handoff**
Follow session end protocol in CLAUDE.md.

## Important

- If PENDING is "none" or empty, ask human what to work on
- If PENDING is unclear, check the files_modified for context
- If handoff is old (>24h), ask human to confirm it's still relevant

## Example

```
⟡ Picking up from claude_desktop:
   Done: Fixed tier pills, restored Sankey animation
   Pending: Add transparency widget to right panel
   Continuing now...

[proceeds to add widget without further discussion]
```
