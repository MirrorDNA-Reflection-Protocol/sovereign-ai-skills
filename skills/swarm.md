# /swarm — Swarm Coordinator Status & Control

Check concurrent agent sessions, detect conflicts, view swarm state.

## Arguments
- `/swarm` — Show status
- `/swarm sessions` — List active sessions
- `/swarm conflicts` — Check for conflicts

## Steps

1. **Check swarm health**
```bash
curl -s http://127.0.0.1:8791/health 2>/dev/null | python3 -m json.tool || echo "Swarm coordinator not responding"
```

2. **List sessions**
```bash
curl -s http://127.0.0.1:8791/swarm 2>/dev/null | python3 -m json.tool
```

3. **Check conflicts**
```bash
curl -s http://127.0.0.1:8791/conflicts 2>/dev/null | python3 -m json.tool
```
