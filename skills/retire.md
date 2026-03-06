# /retire — Gracefully Disable a Service

Stop a service, unload its LaunchAgent, move plist to disabled/, update SERVICE_REGISTRY.

## Arguments

`/retire <service-label>`

Example: `/retire ai.mirrordna.old-service`

## Steps

1. **Verify service exists**
```bash
launchctl list | grep "$LABEL"
ls ~/Library/LaunchAgents/$LABEL.plist
```

2. **Stop and unload**
```bash
launchctl unload ~/Library/LaunchAgents/$LABEL.plist
```

3. **Move plist to disabled**
```bash
mkdir -p ~/Library/LaunchAgents/disabled
mv ~/Library/LaunchAgents/$LABEL.plist ~/Library/LaunchAgents/disabled/
```

4. **Update SERVICE_REGISTRY.json** — remove or mark as disabled

5. **Kill any lingering process** on the service's port

6. **Verify**: confirm not in `launchctl list`, port freed

7. **Report**: what was disabled, port freed, registry updated
