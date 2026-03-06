# /pr — Create Pull Request

Generate PR title and body from commits, create via `gh pr create`.

## Arguments

`/pr [base-branch]`

Default base: `main`. Uses current branch as head.

## Steps

1. **Check Current Branch**
```bash
BRANCH=$(git branch --show-current)
echo "Current branch: $BRANCH"
```

2. **Verify Not on Main**
```bash
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
  echo "ERROR: Already on main branch. Create a feature branch first."
  exit 1
fi
```

3. **Get Commits Since Branch Point**
```bash
BASE="${1:-main}"
git log --oneline $BASE..HEAD
```

4. **Get Full Diff**
```bash
git diff $BASE...HEAD --stat
```

5. **Generate PR Title and Body**
Based on commits and diff:
- Title: concise summary of all changes (<70 chars)
- Body: structured summary with sections

6. **Push Branch**
```bash
git push -u origin $BRANCH
```

7. **Create PR**
```bash
gh pr create --title "[generated title]" --body "$(cat <<'EOF'
## Summary
[bullet points of changes]

## Changes
[list of modified files/areas]

## Testing
[how to verify]

## Notes
[any context or caveats]

---
*Created via /pr — Claude Code*
EOF
)"
```

## Output

```
⟡ PR Created

Title: [title]
Branch: [branch] → [base]
URL: [github PR url]
Commits: [N]
Files changed: [N]

Review at: [URL]
```
