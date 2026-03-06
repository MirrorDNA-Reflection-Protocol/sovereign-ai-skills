# /review — Review Changes

Review a PR or local uncommitted changes. Show diff summary, flag issues, suggest improvements.

## Arguments

`/review [PR-number|local]`

- PR number: review that GitHub PR
- `local`: review uncommitted changes in current repo
- No arg: defaults to `local`

## Steps

### If PR Number
1. **Fetch PR Details**
```bash
gh pr view [number] --json title,body,additions,deletions,files,commits
```

2. **Get PR Diff**
```bash
gh pr diff [number]
```

### If Local
1. **Get Uncommitted Changes**
```bash
git diff
git diff --cached
git status --short
```

### Analysis (Both Paths)

3. **Analyze Changes**
For each changed file:
- What type of change (new, modified, deleted)
- Size of change (lines added/removed)
- Complexity assessment

4. **Flag Issues**
Check for:
- **Security**: hardcoded secrets, SQL injection, XSS vectors
- **Quality**: missing error handling, unused variables, console.logs
- **Style**: inconsistent naming, missing types, dead code
- **Logic**: potential null refs, race conditions, edge cases

5. **Suggest Improvements**
For each flagged issue, provide:
- File and line
- Issue description
- Suggested fix

## Output

```
⟡ Review: [PR #N or "Local Changes"]

Files: [N] changed (+[additions] -[deletions])

Summary:
  [1-2 sentence overview of what changed]

Issues Found:
  🔴 [Critical issues]
  🟡 [Warnings]
  🟢 [Suggestions]

Details:
  [file:line] — [issue description]
    Suggestion: [how to fix]

Overall: [LGTM / Needs changes / Blocked]
```
