# /emergency — Emergency Triage Protocol

Trigger Part XXV emergency triage. Freeze content creation, clear inbox, bulk park stale Active files.

## Arguments

`/emergency [reason]`

Reason is logged in the emergency record.

## Steps

1. **Announce Emergency Mode**
```
⟡ EMERGENCY TRIAGE ACTIVATED
Reason: [reason]
Freezing all content creation...
```

2. **Create Emergency Lock**
```bash
cat > ~/MirrorDNA-Vault/.emergency-lock << EOF
{
  "activated": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "reason": "[reason]",
  "activated_by": "claude_code",
  "status": "active"
}
EOF
```

3. **Clear Inbox — Force Triage Everything**
```bash
for f in ~/MirrorDNA-Vault/00_INBOX/*.md; do
  [ -f "$f" ] || continue
  # Quick classify: if older than 7 days → Archive, else → Reference
  AGE=$(( ($(date +%s) - $(stat -f %m "$f")) / 86400 ))
  if [ $AGE -gt 7 ]; then
    mv "$f" ~/MirrorDNA-Vault/04_ARCHIVE/emergency-parked/
  else
    mv "$f" ~/MirrorDNA-Vault/03_REFERENCE/emergency-triaged/
  fi
done
```

4. **Park Stale Active Files**
```bash
mkdir -p ~/MirrorDNA-Vault/04_ARCHIVE/emergency-parked
for f in ~/MirrorDNA-Vault/02_ACTIVE/*.md; do
  [ -f "$f" ] || continue
  AGE=$(( ($(date +%s) - $(stat -f %m "$f")) / 86400 ))
  if [ $AGE -gt 30 ]; then
    mv "$f" ~/MirrorDNA-Vault/04_ARCHIVE/emergency-parked/
  fi
done
```

5. **Log Emergency Action**
```bash
cat >> ~/MirrorDNA-Vault/emergency_log.md << EOF

## Emergency Triage — $(date +%Y-%m-%d)
- **Reason:** [reason]
- **Inbox cleared:** [N] files moved
- **Active parked:** [N] files moved
- **Lock created:** Yes
- **Activated by:** claude_code
EOF
```

6. **Commit**
```bash
cd ~/MirrorDNA-Vault && git add -A && git commit -m "⟡ EMERGENCY TRIAGE: [reason] — via Claude Code"
```

7. **Remove Lock After Completion**
```bash
rm ~/MirrorDNA-Vault/.emergency-lock
```

## Output

```
⟡ EMERGENCY TRIAGE COMPLETE

Reason: [reason]

Actions:
  Inbox cleared: [N] files → Archive/Reference
  Active parked: [N] stale files → Archive
  Lock: Created and released

The Vault is now clean:
  INBOX: 0 files
  ACTIVE: [N] files (all <30 days)
  Content creation: FROZEN until manual unfreeze

To resume normal operations:
  Verify state, then run `/audit` to confirm health.
```
