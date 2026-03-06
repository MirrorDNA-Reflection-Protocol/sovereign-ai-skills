# /note — Quick Capture to Inbox

Create a timestamped note in `00_INBOX/` with proper frontmatter for later triage.

## Arguments

`/note [title] [body text]`

First word(s) before any newline or `--` become the title. Rest is body.

## Steps

1. **Parse Arguments**
Extract title and body from input.

2. **Generate Metadata**
```bash
ID="N-$(date +%Y%m%d)-$(date +%H%M%S)"
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
FILENAME="$(date +%Y%m%d)-$(echo '[title]' | tr ' ' '-' | tr '[:upper:]' '[:lower:]').md"
```

3. **Create Note**
```bash
cat > ~/MirrorDNA-Vault/00_INBOX/$FILENAME << EOF
---
id: $ID
title: "[title]"
created: $TIMESTAMP
captured_by: claude_code
status: inbox
tags: []
---

# [title]

[body text]

---
*Captured via /note — $(date '+%Y-%m-%d %H:%M')*
EOF
```

4. **Confirm**
```bash
ls -la ~/MirrorDNA-Vault/00_INBOX/$FILENAME
```

## Output

```
⟡ Note Captured

Title: [title]
File: ~/MirrorDNA-Vault/00_INBOX/[filename]
ID: N-20260127-143022

Run `/triage` to classify and move to proper layer.
Inbox count: [N] items pending triage.
```
