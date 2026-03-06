# /health — System Health Check

Check all MirrorDNA services and report status.

## Steps

1. **MirrorBrain MCP (Port 8081)**
```bash
echo -n "MirrorBrain: "
curl -s -o /dev/null -w "%{http_code}" http://localhost:8081/api/system/state --max-time 2 2>/dev/null || echo "OFFLINE"
```

2. **Inference Router (Port 8086)**
```bash
echo -n "Inference Router: "
curl -s -o /dev/null -w "%{http_code}" http://localhost:8086/health --max-time 2 2>/dev/null || echo "OFFLINE"
```

3. **ActiveMirror UI (Port 8087)**
```bash
echo -n "ActiveMirror UI: "
curl -s -o /dev/null -w "%{http_code}" http://localhost:8087 --max-time 2 2>/dev/null || echo "OFFLINE"
```

4. **Ollama**
```bash
echo -n "Ollama: "
ollama list 2>/dev/null | head -3 || echo "OFFLINE"
```

5. **SC1 Pixel Bridge**
```bash
echo -n "Pixel (SC1): "
curl -s http://100.74.95.99:5000/ping --max-time 3 2>/dev/null || echo "OFFLINE"
```

6. **SC1 OnePlus Bridge**
```bash
echo -n "OnePlus (SC1): "
curl -s http://100.91.11.72:5000/ping --max-time 3 2>/dev/null || echo "OFFLINE"
```

7. **State Directory**
```bash
echo -n "State Dir: "
ls ~/.mirrordna/state.json 2>/dev/null && echo "OK" || echo "MISSING"
```

8. **Git Status**
```bash
echo -n "State Git: "
cd ~/.mirrordna && git status --short 2>/dev/null | wc -l | xargs -I{} echo "{} uncommitted"
```

## Output Format

```
⟡ Health Check

| Service | Status | Notes |
|---------|--------|-------|
| MirrorBrain | ✅ 200 | Port 8081 |
| Inference | ❌ OFFLINE | Port 8086 |
| UI | ✅ 200 | Port 8087 |
| Ollama | ✅ 3 models | gpt-oss:20b, llama3.2, etc |
| Pixel | ✅ alive | 100.74.95.99 |
| OnePlus | ❌ timeout | 100.91.11.72 |
| State | ✅ OK | Git clean |

Action needed: Start Inference Router
```

## If Services Down

Suggest startup commands:
```bash
# MirrorBrain
cd ~/repos/mirrorbrain-mcp && npm start &

# Inference Router
cd /Users/mirror-admin/repos/ActiveMirrorOS/apps/activemirror-v3 && python3 router.py &

# ActiveMirror UI
cd /Users/mirror-admin/repos/ActiveMirrorOS/apps/activemirror-v3 && python3 -m http.server 8087 &

# Ollama
ollama serve &
```
