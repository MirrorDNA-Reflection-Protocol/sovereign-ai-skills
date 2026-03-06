# /draft — Draft Content for Publishing

Create a content draft for a specific platform with proper structure and frontmatter.

## Arguments

`/draft [topic] --platform [substack|x|linkedin]`

Default platform: substack.

## Steps

1. **Search Vault for Related Content**
```bash
grep -ril "[topic]" ~/MirrorDNA-Vault/01_CANONICAL/ ~/MirrorDNA-Vault/02_ACTIVE/ 2>/dev/null
```

2. **Read Related Files**
Pull key concepts, quotes, and frameworks from Vault matches.

3. **Determine Target Directory**
```bash
PLATFORM="${2:-substack}"
mkdir -p ~/MirrorDNA-Vault/Content/${PLATFORM}/drafts
```

4. **Create Draft**
```bash
ID="D-$(date +%Y%m%d)-$(date +%H%M)"
FILENAME="draft-$(echo '[topic]' | tr ' ' '-' | tr '[:upper:]' '[:lower:]').md"

cat > ~/MirrorDNA-Vault/Content/${PLATFORM}/drafts/$FILENAME << EOF
---
id: $ID
title: "[topic]"
platform: $PLATFORM
status: draft
created: $(date -u +%Y-%m-%dT%H:%M:%SZ)
author: Paul Desai
tags: []
vault_sources: [list related vault files]
---

# [Title]

## Hook
[Opening that grabs attention — 1-2 sentences]

## Core Argument
[Main thesis — draw from Vault canonical docs]

## Supporting Points
1. [Point 1 — with evidence/example]
2. [Point 2 — with evidence/example]
3. [Point 3 — with evidence/example]

## Key Quote / Framework
> [Pull from Vault if available]

## Call to Action
[What should the reader do/think/feel?]

## Platform Notes
- Target length: [word count for platform]
- Tone: [platform-appropriate tone]
- Hashtags/tags: [if applicable]

---
*Drafted via /draft — Sources from MirrorDNA Vault*
EOF
```

5. **Commit**
```bash
cd ~/MirrorDNA-Vault && git add -A && git commit -m "⟡ Draft: [topic] for $PLATFORM — via Claude Code"
```

## Output

```
⟡ Draft Created

Topic: [topic]
Platform: [platform]
File: ~/MirrorDNA-Vault/Content/[platform]/drafts/[filename]
Sources: [N] Vault files referenced

Next: Edit the draft, then publish when ready.
```
