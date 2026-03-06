# /services — Manage MirrorDNA Services

List, start, or stop MirrorDNA services. Shows LaunchAgent status and offers control.

## Arguments

`/services` — List all services and status
`/services start [name]` — Start a service
`/services stop [name]` — Stop a service
`/services restart [name]` — Restart a service

## Steps

### List Services
1. **Check LaunchAgents**
```bash
echo "=== LaunchAgents ==="
ls ~/Library/LaunchAgents/ai.mirrordna.*.plist 2>/dev/null || echo "No MirrorDNA LaunchAgents"
```

2. **Check Running Status**
```bash
echo "=== Running ==="
launchctl list 2>/dev/null | grep mirrordna || echo "None running via launchctl"
```

3. **Check Known Ports**
```bash
echo "=== Port Check ==="
for port in 8081 8086 8087; do
  echo -n "Port $port: "
  lsof -i :$port -P -n 2>/dev/null | head -2 || echo "free"
done
```

4. **Check Ollama**
```bash
echo -n "Ollama: "
pgrep -x ollama >/dev/null && echo "running" || echo "stopped"
```

### Start Service
```bash
# If LaunchAgent exists:
launchctl load ~/Library/LaunchAgents/ai.mirrordna.[name].plist

# If manual start needed:
# MirrorBrain: cd ~/repos/mirrorbrain-mcp && npm start &
# Inference: cd ~/repos/ActiveMirrorOS/apps/activemirror-v3 && python3 router.py &
# UI: cd ~/repos/ActiveMirrorOS/apps/activemirror-v3 && python3 -m http.server 8087 &
# Ollama: ollama serve &
```

### Stop Service
```bash
# If LaunchAgent:
launchctl unload ~/Library/LaunchAgents/ai.mirrordna.[name].plist

# If manual:
# Find PID and kill
lsof -i :[port] -t | xargs kill
```

## Output

```
⟡ Services

| Service | Status | Port | PID | LaunchAgent |
|---------|--------|------|-----|-------------|
| MirrorBrain | ✅ Running | 8081 | 1234 | Yes |
| Inference | ❌ Stopped | 8086 | — | No |
| ActiveMirror UI | ✅ Running | 8087 | 5678 | No |
| Ollama | ✅ Running | 11434 | 9012 | Yes |
| Memory Bus | ✅ Available | — | — | — |

Commands:
  /services start inference
  /services restart mirrorbrain
```
