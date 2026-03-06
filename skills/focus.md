# /focus — Set Current Project Focus

Update bus state with active project. Subsequent commands scope to that project context.

## Arguments

`/focus [project-name]`
`/focus` — Show current focus
`/focus clear` — Clear focus

## Steps

### Show Current Focus
```bash
echo "=== Current Focus ==="
~/.mirrordna/bin/bus read 2>/dev/null | grep -i "focus\|project\|phase" || echo "No focus set"
```

### Set Focus
1. **Find Project**
```bash
# Check repos
ls -d ~/repos/*[project-name]* 2>/dev/null

# Check Vault active specs
grep -rl "[project-name]" ~/MirrorDNA-Vault/02_ACTIVE/ 2>/dev/null
```

2. **Update Bus State**
```bash
echo '{"state":{"focus":"[project-name]","focus_set":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}}' | ~/.mirrordna/bin/bus write "Focus set: [project-name]" --json
```

3. **Show Project Context**
```bash
# If repo exists, show recent activity
if [ -d ~/repos/[project-name] ]; then
  cd ~/repos/[project-name]
  echo "=== Recent Commits ==="
  git log --oneline -5
  echo "=== Status ==="
  git status --short
fi
```

4. **Log**
```bash
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | claude_code | FOCUS: [project-name]" >> ~/.mirrordna/ledger.md
```

### Clear Focus
```bash
echo '{"state":{"focus":null,"focus_set":null}}' | ~/.mirrordna/bin/bus write "Focus cleared" --json
```

## Output

```
⟡ Focus: [project-name]

Repo: ~/repos/[project-name]
Status: [N] uncommitted files
Last commit: [message] ([time ago])
Related specs: [list from Vault]

All subsequent commands will scope to this project.
Run `/focus clear` to reset.
```
