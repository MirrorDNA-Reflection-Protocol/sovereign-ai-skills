# /overnight — Queue Background Agent Tasks

Set up tasks to run via Claude Code background agents while Paul sleeps/works on other things.

## Usage

`/overnight [task description]`

Or without argument to see current queue.

## Steps

### If Viewing Queue
```bash
echo "=== OVERNIGHT QUEUE ===" 
cat ~/.mirrordna/overnight-queue.json 2>/dev/null | jq . || echo "Queue empty"
```

### If Adding Task

1. **Parse Task**
Extract from human's description:
- What to do
- Which repo/files
- Success criteria
- Priority

2. **Add to Queue**
```bash
QUEUE=$(cat ~/.mirrordna/overnight-queue.json 2>/dev/null || echo '{"tasks":[]}')
TASK_ID="overnight-$(date +%Y%m%d-%H%M%S)"

NEW_TASK=$(cat << EOF
{
  "id": "$TASK_ID",
  "created": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "task": "[description]",
  "repo": "[path]",
  "success_criteria": "[what success looks like]",
  "priority": "[high|medium|low]",
  "status": "queued"
}
EOF
)

echo "$QUEUE" | jq ".tasks += [$NEW_TASK]" > ~/.mirrordna/overnight-queue.json
```

3. **Create Background Agent Command**
```bash
cat > ~/.mirrordna/overnight-scripts/${TASK_ID}.sh << EOF
#!/bin/bash
# Overnight task: $TASK_ID
# Created: $(date)

cd [repo]
claude --background --task "[task description]" --output ~/.mirrordna/completions/$(date +%Y-%m-%d)/${TASK_ID}-complete.md
EOF
chmod +x ~/.mirrordna/overnight-scripts/${TASK_ID}.sh
```

4. **Provide Launch Command**
```
To start overnight tasks:
  ~/.mirrordna/overnight-scripts/${TASK_ID}.sh &

Or start all queued:
  for f in ~/.mirrordna/overnight-scripts/*.sh; do bash "$f" & done
```

## Output

```
⟡ Overnight Task Queued

ID: overnight-20260116-2230
Task: Refactor ActiveMirror v3 CSS into modules
Repo: /Users/mirror-admin/repos/ActiveMirrorOS/apps/activemirror-v3/
Priority: medium

To launch now:
  claude --background "Refactor ActiveMirror v3 CSS into separate module files"

Or wait for LaunchAgent to pick it up at next scheduled run.

Queue: 1 task pending
```

## Background Agent Notes

Claude Code background agents:
- Run detached from terminal
- Write output to specified file
- Can be monitored via `claude --status`
- Will write completion when done

Paul can check status anytime:
```bash
claude --status  # See running agents
cat ~/.mirrordna/completions/$(date +%Y-%m-%d)/  # See completions
```
