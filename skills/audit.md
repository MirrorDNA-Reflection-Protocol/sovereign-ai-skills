# /audit — Vault Health Audit

Run vault audit, display dashboard, flag structural issues. Regenerate `Vault_Health.md`.

## Arguments

`/audit [layer]`

If layer specified (canonical, active, reference, archive), audit only that layer. Otherwise audit all.

## Steps

1. **Check Audit Script**
```bash
ls ~/MirrorDNA-Vault/vault_audit.py 2>/dev/null || echo "NO_SCRIPT"
```

2. **If Script Exists, Run It**
```bash
cd ~/MirrorDNA-Vault && python3 vault_audit.py
```

3. **If No Script, Manual Audit**
Check each layer:
```bash
# Count files per layer
for layer in 00_INBOX 01_CANONICAL 02_ACTIVE 03_REFERENCE 04_ARCHIVE; do
  echo "$layer: $(find ~/MirrorDNA-Vault/$layer -type f -name '*.md' 2>/dev/null | wc -l) files"
done
```

4. **Check Frontmatter Compliance**
For each `.md` file, verify:
- Has YAML frontmatter
- Has `id` field
- Has `title` field
- Has `layer` field matching its location
- Has `created` date

5. **Check for Issues**
- Files without frontmatter
- Duplicate IDs
- Layer mismatches (file in wrong directory vs frontmatter)
- Orphaned links (links to non-existent files)
- Files older than decay threshold without review

6. **Generate Vault_Health.md**
```bash
cat > ~/MirrorDNA-Vault/Vault_Health.md << EOF
# ⟡ Vault Health Report
**Generated:** $(date -u +%Y-%m-%dT%H:%M:%SZ)
**Auditor:** claude_code

## Summary
| Layer | Files | Issues | Health |
|-------|-------|--------|--------|
| INBOX | [n] | [n] | [status] |
| CANONICAL | [n] | [n] | [status] |
| ACTIVE | [n] | [n] | [status] |
| REFERENCE | [n] | [n] | [status] |
| ARCHIVE | [n] | [n] | [status] |

## Issues Found
[list each issue with file path and fix suggestion]

## Recommendations
[actionable next steps]
EOF
```

7. **Commit**
```bash
cd ~/MirrorDNA-Vault && git add Vault_Health.md && git commit -m "⟡ Vault audit — via Claude Code"
```

## Output

```
⟡ Vault Audit Complete

Total: [N] files across 5 layers
Issues: [N] found

Critical:
- [list critical issues]

Warnings:
- [list warnings]

Report: ~/MirrorDNA-Vault/Vault_Health.md
```
