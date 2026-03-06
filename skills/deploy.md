# /deploy — Deploy LaunchAgents

Create, load, and verify LaunchAgents following MirrorDNA hardening standards.

## Arguments

`/deploy [service-name]` — Create and load a LaunchAgent
`/deploy list` — List deployed agents
`/deploy remove [service-name]` — Unload and remove agent

## Steps

### List Deployed
```bash
echo "=== Deployed LaunchAgents ==="
ls ~/Library/LaunchAgents/ai.mirrordna.*.plist 2>/dev/null || echo "None"
echo ""
echo "=== Running ==="
launchctl list 2>/dev/null | grep mirrordna || echo "None active"
```

### Deploy New Service
1. **Gather Service Info**
Determine from service name:
- Binary/script path
- Working directory
- Arguments
- Environment variables
- Log path

2. **Create Plist**
```bash
cat > ~/Library/LaunchAgents/ai.mirrordna.[service-name].plist << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>ai.mirrordna.[service-name]</string>
    <key>ProgramArguments</key>
    <array>
        <string>[binary-path]</string>
        [additional args]
    </array>
    <key>WorkingDirectory</key>
    <string>[working-dir]</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/mirror-admin/.mirrordna/logs/[service-name].log</string>
    <key>StandardErrorPath</key>
    <string>/Users/mirror-admin/.mirrordna/logs/[service-name]-error.log</string>
</dict>
</plist>
EOF
```

3. **Ensure Log Directory**
```bash
mkdir -p ~/.mirrordna/logs
```

4. **Load Agent**
```bash
launchctl load ~/Library/LaunchAgents/ai.mirrordna.[service-name].plist
```

5. **Verify**
```bash
sleep 2
launchctl list | grep mirrordna.[service-name]
```

### Remove Service
```bash
launchctl unload ~/Library/LaunchAgents/ai.mirrordna.[service-name].plist
rm ~/Library/LaunchAgents/ai.mirrordna.[service-name].plist
```

## Output

```
⟡ Deployed: [service-name]

Plist: ~/Library/LaunchAgents/ai.mirrordna.[service-name].plist
Log: ~/.mirrordna/logs/[service-name].log
Status: Running (PID [pid])
KeepAlive: Yes

Verify: launchctl list | grep mirrordna
```
