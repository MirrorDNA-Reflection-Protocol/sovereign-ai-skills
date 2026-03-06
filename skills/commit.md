# /commit — Smart Commit

Scan changes across repos, generate contextual commit message with ⟡ prefix. Does NOT push (use `/ship` for that).

## Arguments

`/commit [optional: message override]`

If no message provided, auto-generate from diff analysis.

## Steps

1. **Find Dirty Repos**
```bash
for dir in ~/.mirrordna ~/MirrorDNA-Vault ~/repos/*; do
  if [ -d "$dir/.git" ]; then
    cd "$dir"
    if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
      echo "DIRTY: $dir"
      git status --short
      echo "---"
    fi
  fi
done
```

2. **For Each Dirty Repo**
- Read the diff to understand changes
```bash
cd [repo]
git diff --stat
git diff --cached --stat
```

3. **Generate Commit Message**
Based on diff analysis:
- If adding new files: "Add [description]"
- If modifying: "Update [what changed]"
- If fixing: "Fix [what was broken]"
- If refactoring: "Refactor [what was reorganized]"
- Always prefix with ⟡

4. **Stage and Commit**
```bash
cd [repo]
git add -A
git commit -m "⟡ [generated or provided message] — via Claude Code"
```

5. **Repeat for Each Dirty Repo**

6. **Log to Ledger**
```bash
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | claude_code | COMMIT: [summary]" >> ~/.mirrordna/ledger.md
```

## Output

```
⟡ Committed

| Repo | Message | Files |
|------|---------|-------|
| mirrordna | ⟡ Update state after triage | 3 |
| MirrorDNA-Vault | ⟡ Add new spec document | 1 |

Total: [N] repos, [N] files
Not pushed. Run `/ship` to push all.
```
