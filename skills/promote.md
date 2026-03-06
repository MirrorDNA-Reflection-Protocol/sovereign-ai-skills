# /promote — Promote Script to Managed Service

Take a standalone script and wire it into the full service stack: LaunchAgent + SERVICE_REGISTRY + health check.

## Arguments

`/promote <script-path> [--interval Ns] [--port N] [--keepalive]`

## Steps

1. **Read the script** to understand what it does
2. **Determine run mode**:
   - `--keepalive`: long-running daemon (KeepAlive=true)
   - `--interval Ns`: periodic job (StartInterval=N)
   - Default: RunAtLoad only
3. **Generate LaunchAgent plist** at `~/Library/LaunchAgents/ai.mirrordna.<name>.plist`
4. **Add to SERVICE_REGISTRY.json** with label, port (if applicable), health_url
5. **Load the agent**: `launchctl load <plist>`
6. **Verify**: check exit code, health endpoint if applicable
7. **Register in SHIPLOG** via ship_register.py

## Safety

- Never overwrite existing plist without confirmation
- Always verify the script runs standalone first
- Add log paths for stdout/stderr
