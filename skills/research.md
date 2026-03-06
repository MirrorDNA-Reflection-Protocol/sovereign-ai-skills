# /research — Deep Research

Search web and Vault, synthesize findings, optionally create a Reference note.

## Arguments

`/research [topic]`
`/research [topic] --save` — Also save as Reference note

## Steps

1. **Search Vault First**
```bash
echo "=== Vault Matches ==="
grep -ril "[topic]" ~/MirrorDNA-Vault/ 2>/dev/null | head -10
```

2. **Read Vault Matches**
For each match, extract relevant sections and key points.

3. **Web Search**
Search the web for current information on the topic. Use multiple queries if needed:
- "[topic]" — general
- "[topic] 2026" — recent
- "[topic] technical" — depth

4. **Fetch Key Sources**
Read the top 3-5 most relevant web results for detailed content.

5. **Synthesize**
Combine Vault knowledge with web findings:
- What we already know (from Vault)
- What's new (from web)
- Key takeaways
- Open questions

6. **If --save, Create Reference Note**
```bash
ID="REF-$(date +%Y%m%d)-$(date +%H%M)"
FILENAME="research-$(echo '[topic]' | tr ' ' '-' | tr '[:upper:]' '[:lower:]').md"

cat > ~/MirrorDNA-Vault/03_REFERENCE/$FILENAME << EOF
---
id: $ID
title: "Research: [topic]"
layer: reference
created: $(date -u +%Y-%m-%dT%H:%M:%SZ)
researcher: claude_code
status: active
tags: [research, topic-tag]
sources: [list URLs]
---

# Research: [Topic]

## Summary
[2-3 sentence overview]

## Key Findings
[bullet points]

## Sources
[list with URLs and dates]

## Vault Connections
[links to related Vault files]

## Open Questions
[what remains unclear]

---
*Researched via /research — $(date +%Y-%m-%d)*
EOF
```

7. **Commit if saved**
```bash
cd ~/MirrorDNA-Vault && git add -A && git commit -m "⟡ Research: [topic] — via Claude Code"
```

## Output

```
⟡ Research: [topic]

From Vault ([N] related files):
  - [key point from vault]
  - [key point from vault]

From Web:
  - [finding 1 — source]
  - [finding 2 — source]
  - [finding 3 — source]

Synthesis:
  [combined understanding]

[If saved]: Reference note: ~/MirrorDNA-Vault/03_REFERENCE/[file]
[If not saved]: Run `/research [topic] --save` to persist.
```
