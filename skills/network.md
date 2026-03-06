# /network — Network Diagnostics

Check Tailscale, ports, SC1 bridges, DNS, and connectivity.

## Steps

1. **Tailscale Status**
```bash
tailscale status 2>/dev/null || echo "Not running"
```

2. **Internet**
```bash
curl -s -o /dev/null -w "%{http_code}" https://api.anthropic.com --max-time 5
```

3. **SC1 Bridges**
```bash
curl -s http://100.74.95.99:5000/ping --max-time 3 2>/dev/null || echo "OFFLINE"
curl -s http://100.91.11.72:5000/ping --max-time 3 2>/dev/null || echo "OFFLINE"
```

4. **Local Ports**
```bash
for port in 8081 8086 8087 11434 5000; do
  lsof -i :$port -P -n 2>/dev/null | grep LISTEN | head -1
done
```

5. **DNS**
```bash
dig +short api.anthropic.com github.com activemirror.ai
```

## Output

```
⟡ Network

Internet: ✅ Online
Tailscale: ✅ Connected ([N] peers)
  SC1 Pixel: [status]
  SC1 OnePlus: [status]

Ports:
  8081 (MirrorBrain): [status]
  8086 (Inference): [status]
  8087 (UI): [status]

DNS: ✅ resolving
```
