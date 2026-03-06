# /factory — Visual Orchestration Demo

Spawn multiple Claude Code agents in separate Terminal windows, each building a different component in parallel. One orchestrator managing the factory floor.

## Arguments

`/factory [manifest|demo]`

- `manifest`: Path to a manifest.json with build tasks
- `demo`: Run the default demo manifest (today's phone-pull bundles)

## Steps

### 1. Generate Manifest (if `demo` or no manifest)

Create a manifest JSON at `/tmp/mirror-factory/manifest.json` with build tasks. Each task needs:
- `id`: short identifier
- `title`: display name for Terminal tab
- `prompt`: full Claude Code prompt for the build
- `cwd`: working directory

Example manifest:
```json
{
  "run_id": "factory-YYYY-MM-DD-HHMM",
  "agents": [
    {
      "id": "forge",
      "title": "MirrorForge",
      "prompt": "Initialize MirrorForge CLI: cd runtime && source .venv/bin/activate && python mirrorforge_cli.py init && python mirrorforge_cli.py simulate examples/intent_01.json. Report what happened.",
      "cwd": "~/MirrorDNA-Vault/01_ACTIVE/SovereignFactory/MirrorForge_v1/MirrorForge_v1_Bundle"
    }
  ]
}
```

### 2. Spawn Agents

```bash
~/.mirrordna/scripts/factory_spawn.sh /tmp/mirror-factory/manifest.json
```

This opens a Terminal window for each agent. Each window:
- Shows the agent title
- Runs Claude Code with the build prompt
- Streams output in real-time
- Writes status to `/tmp/mirror-factory/<run_id>/<agent_id>.status`
- Logs to `/tmp/mirror-factory/<run_id>/<agent_id>.log`

### 3. Monitor Progress

Open a separate Terminal tab for the live dashboard:
```bash
~/.mirrordna/scripts/factory_monitor.sh <run_id>
```

Or monitor from this session by checking status files:
```bash
for f in /tmp/mirror-factory/<run_id>/*.status; do echo "$(basename $f .status): $(cat $f)"; done
```

### 4. Collect Results

When all agents complete:
- Read each agent's log file
- Compile into an orchestration report
- Save to `~/MirrorDNA-Vault/SessionReports/`

### 5. Report

```
SOVEREIGN FACTORY — Run Complete

Run ID: factory-2026-02-14-1230
Duration: Xm Ys
Agents: N spawned, N completed

| Agent | Title | Status | Duration | Output |
|-------|-------|--------|----------|--------|
| forge | MirrorForge | DONE | 45s | Genome initialized |
| ... | ... | ... | ... | ... |

Logs: /tmp/mirror-factory/<run_id>/
Report: ~/MirrorDNA-Vault/SessionReports/SR-<date>-Factory.md
```

## Notes

- Each Terminal window is a separate Claude Code process
- The orchestrator (this session) does NOT run the builds — it only spawns and monitors
- For recording, use macOS screen recording (Cmd+Shift+5) to capture all windows
- The visual: 6 Terminal windows pop open simultaneously, all building in parallel
- Factory monitor shows live status dashboard in a 7th window
- All evidence, logs, and results land in the vault
