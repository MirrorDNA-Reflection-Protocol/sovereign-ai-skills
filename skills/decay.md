# /decay — Check Staleness Thresholds

Check files against decay limits per Vault spec Part XX. List files exceeding staleness thresholds by layer.

## Arguments

`/decay [layer]`

Default: check all layers.

## Steps

1. **Define Decay Thresholds**
| Layer | Max Staleness | Action |
|-------|--------------|--------|
| INBOX | 7 days | Triage or archive |
| ACTIVE | 30 days | Review or demote to Reference |
| REFERENCE | 90 days | Review or archive |
| CANONICAL | Never decays | — |
| ARCHIVE | — | Already archived |

2. **Scan Each Layer**
```bash
NOW=$(date +%s)
for layer in 00_INBOX 02_ACTIVE 03_REFERENCE; do
  echo "=== $layer ==="
  find ~/MirrorDNA-Vault/$layer -name "*.md" -type f | while read f; do
    MOD=$(stat -f %m "$f" 2>/dev/null || stat -c %Y "$f" 2>/dev/null)
    AGE=$(( (NOW - MOD) / 86400 ))
    echo "$AGE days: $(basename $f)"
  done | sort -rn
done
```

3. **Flag Violations**
Compare each file's age against its layer threshold. Flag files exceeding limits.

4. **Generate Decay Report**
```bash
cat > ~/MirrorDNA-Vault/Decay_Report.md << EOF
# ⟡ Decay Report
**Generated:** $(date -u +%Y-%m-%dT%H:%M:%SZ)

## Violations
| File | Layer | Age (days) | Threshold | Action |
|------|-------|-----------|-----------|--------|
[list violations]

## Summary
- INBOX overdue: [N]
- ACTIVE stale: [N]
- REFERENCE aging: [N]
EOF
```

## Output

```
⟡ Decay Check

INBOX (7-day threshold):
  ⚠ old-note.md — 12 days (OVERDUE)
  ✓ new-idea.md — 2 days

ACTIVE (30-day threshold):
  ⚠ stale-spec.md — 45 days (OVERDUE)
  ⚠ draft-plan.md — 33 days (OVERDUE)
  ✓ current-project.md — 5 days

REFERENCE (90-day threshold):
  ✓ All within threshold

Violations: [N] files need attention
Run `/triage` to process overdue inbox items.
```
