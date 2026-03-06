# /triage — Auto-Triage Inbox

Scan `00_INBOX/` in the Vault, classify each item by type and urgency, move to the correct layer.

## Arguments

`/triage [dry-run]`

If `dry-run`, show proposed moves without executing.

## Steps

1. **Scan Inbox**
```bash
ls -la ~/MirrorDNA-Vault/00_INBOX/
```

2. **For Each File, Classify**
Read each file and determine:
- **Type**: concept, reference, spec, content draft, log, task
- **Layer**: Canonical (core identity), Active (current work), Reference (external/research), Archive (historical)
- **Urgency**: immediate, normal, low

3. **Determine Target Location**
| Type | Target |
|------|--------|
| Core concept/identity | `01_CANONICAL/` |
| Active project/spec | `02_ACTIVE/` |
| Research/external ref | `03_REFERENCE/` |
| Old/completed/historical | `04_ARCHIVE/` |
| Content draft | `Content/[Platform]/drafts/` |
| Task/handoff | `Superagent/` |

4. **Add Frontmatter If Missing**
Ensure each file has:
```yaml
---
id: [generated if missing]
title: [from filename or content]
layer: [target layer]
created: [file date or now]
status: active
tags: []
---
```

5. **Move Files**
```bash
mv ~/MirrorDNA-Vault/00_INBOX/[file] ~/MirrorDNA-Vault/[target]/[file]
```

6. **Update Inbox Index**
```bash
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | TRIAGE | Moved [count] files" >> ~/MirrorDNA-Vault/00_INBOX/_triage_log.md
```

7. **Commit Vault**
```bash
cd ~/MirrorDNA-Vault && git add -A && git commit -m "⟡ Inbox triage: [count] items classified — via Claude Code"
```

## Output

```
⟡ Inbox Triage Complete

Processed: [N] files

| File | Type | → Layer | Notes |
|------|------|---------|-------|
| sovereignty-notes.md | concept | 01_CANONICAL | Core identity doc |
| react-patterns.md | reference | 03_REFERENCE | External research |
| old-draft.md | archive | 04_ARCHIVE | Stale >30 days |

Moved: [N] | Skipped: [N] | Errors: [N]
```
