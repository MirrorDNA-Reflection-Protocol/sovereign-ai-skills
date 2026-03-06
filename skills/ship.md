# /ship — Commit, Push, and Complete

Finalize current work: commit all changes, push to remote, write completion.

## Arguments

`/ship [optional: task-id or description]`

If no argument, infer from recent work.

## Steps

1. **Identify Changed Repos**
```bash
# Check common locations for uncommitted changes
for dir in ~/.mirrordna ~/repos/* /Users/mirror-admin/repos/*; do
  if [ -d "$dir/.git" ]; then
    cd "$dir"
    if [ -n "$(git status --porcelain)" ]; then
      echo "DIRTY: $dir"
    fi
  fi
done
```

2. **For Each Dirty Repo, Commit**
```bash
cd [repo]
git add -A
git status --short
git commit -m "⟡ [contextual message based on changes] — via Claude Code"
```

3. **Push**
```bash
git push origin $(git branch --show-current)
```

4. **Verify Push Succeeded**
```bash
git log --oneline -1
git status
```

5. **Write Completion File**
```bash
TASK_ID="${1:-$(date +%H%M%S)}"
DATE=$(date +%Y-%m-%d)
mkdir -p ~/.mirrordna/completions/$DATE

cat > ~/.mirrordna/completions/$DATE/${TASK_ID}-complete.md << EOF
# ⟡ COMPLETION: $TASK_ID

**Completed:** $(date -u +%Y-%m-%dT%H:%M:%SZ)
**Client:** claude_code

## Commits
$(git log --oneline -3)

## Files Changed
$(git diff --name-only HEAD~1 2>/dev/null || echo "First commit")

## Verification
[Add verification steps]
EOF
```

6. **Update Handoff**
```bash
cat > ~/.mirrordna/handoff.json << EOF
{
  "client": "claude_code",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "action": "Shipped: [summary]",
  "pending": "none",
  "next_client": "human"
}
EOF
```

7. **Commit State**
```bash
cd ~/.mirrordna && git add -A && git commit -m "⟡ Shipped $TASK_ID" && git push 2>/dev/null || true
```

## Output

```
⟡ Shipped!

Commits:
- repo1: "⟡ Fix tier pills — via Claude Code"
- repo2: "⟡ Update state — via Claude Code"

Pushed to: origin/main
Completion: ~/.mirrordna/completions/2026-01-16/123456-complete.md

Ready for next task.
```
