# /device — Device Status Dashboard

Check reachability and status of all devices in the mesh.

## Steps

1. **Ping all devices**
```bash
echo "OnePlus (EDGE):"; ping -c 1 -t 3 100.91.11.72 2>&1 | grep -E "bytes from|100%"
echo "Pixel (SHIELD):"; ping -c 1 -t 3 100.74.95.99 2>&1 | grep -E "bytes from|100%"
echo "Red Mac (RED TEAM):"; ping -c 1 -t 3 100.106.113.28 2>&1 | grep -E "bytes from|100%"
echo "MacBook Air (REMOTE):"; ping -c 1 -t 3 100.74.145.58 2>&1 | grep -E "bytes from|100%"
```

2. **Check ADB devices**
```bash
adb devices 2>/dev/null
```

3. **Check Termux SSH (OnePlus)**
```bash
nc -z -w 3 100.91.11.72 8022 2>&1 && echo "Termux SSH: UP" || echo "Termux SSH: DOWN"
```

4. **Check Tasker (Pixel)**
```bash
curl -s --max-time 3 http://100.74.95.99:8081/status 2>/dev/null || echo "Tasker: unreachable"
```

5. **Report**: device name, role, IP, reachable, services available

## Output Format
```
DEVICE MESH — [timestamp]
  | Device       | Role      | Tailscale      | Status    | Services       |
  |-------------|-----------|----------------|-----------|----------------|
  | OnePlus 15  | EDGE      | 100.91.11.72   | UP        | SSH:8022       |
  | Pixel 9 Pro | SHIELD    | 100.74.95.99   | UP        | Tasker:8081    |
  | Red Mac     | RED TEAM  | 100.106.113.28 | DOWN      | —              |
  | MacBook Air | REMOTE    | 100.74.145.58  | DOWN      | —              |
```
