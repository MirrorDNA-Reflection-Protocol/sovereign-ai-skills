# /backup — Vault Backup Operations

Check backup age, run backup, verify integrity.

## Arguments

`/backup` — Check backup status
`/backup run` — Execute backup now
`/backup verify` — Verify latest backup integrity

## Steps

### Check Status
1. **Find Backup Location**
```bash
# Check common backup targets
echo "=== Backup Targets ==="
ls -la /Volumes/ 2>/dev/null | grep -v "^total"
ls -la ~/Backups/ 2>/dev/null
ls -la ~/.mirrordna/backups/ 2>/dev/null
```

2. **Check Last Backup**
```bash
LAST_BACKUP=$(ls -t ~/.mirrordna/backups/ 2>/dev/null | head -1)
if [ -n "$LAST_BACKUP" ]; then
  echo "Last backup: $LAST_BACKUP"
  echo "Age: $(( ($(date +%s) - $(stat -f %m ~/.mirrordna/backups/$LAST_BACKUP)) / 3600 )) hours"
else
  echo "No backups found"
fi
```

### Run Backup
1. **Create Backup Directory**
```bash
BACKUP_DIR="$HOME/.mirrordna/backups/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"
```

2. **Backup Vault**
```bash
rsync -av --exclude='.git' ~/MirrorDNA-Vault/ "$BACKUP_DIR/vault/"
```

3. **Backup State**
```bash
rsync -av ~/.mirrordna/bus/ "$BACKUP_DIR/bus/"
cp ~/.mirrordna/state.json "$BACKUP_DIR/" 2>/dev/null
cp ~/.mirrordna/handoff.json "$BACKUP_DIR/" 2>/dev/null
cp ~/.mirrordna/ledger.md "$BACKUP_DIR/" 2>/dev/null
```

4. **Create Manifest**
```bash
cat > "$BACKUP_DIR/manifest.json" << EOF
{
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "vault_files": $(find "$BACKUP_DIR/vault" -type f | wc -l | tr -d ' '),
  "total_size": "$(du -sh "$BACKUP_DIR" | cut -f1)",
  "created_by": "claude_code"
}
EOF
```

### Verify
1. **Compare File Counts**
```bash
VAULT_COUNT=$(find ~/MirrorDNA-Vault -type f -not -path '*/.git/*' | wc -l)
BACKUP_COUNT=$(find "$BACKUP_DIR/vault" -type f | wc -l)
echo "Vault: $VAULT_COUNT files, Backup: $BACKUP_COUNT files"
```

2. **Spot-Check Random Files**
```bash
# Compare checksums of 5 random files
find ~/MirrorDNA-Vault -type f -not -path '*/.git/*' | sort -R | head -5 | while read f; do
  REL=${f#$HOME/MirrorDNA-Vault/}
  ORIG=$(md5 -q "$f")
  BACK=$(md5 -q "$BACKUP_DIR/vault/$REL" 2>/dev/null || echo "MISSING")
  echo "$REL: $([ "$ORIG" = "$BACK" ] && echo '✓ match' || echo '✗ MISMATCH')"
done
```

## Output

```
⟡ Backup Status

Last backup: 2026-01-27 10:30
Age: [N] hours
Location: ~/.mirrordna/backups/20260127-103000
Size: [size]
Files: [N] vault, [N] state

Health: [OK / STALE / MISSING]
Recommendation: [backup now / OK / verify integrity]
```
