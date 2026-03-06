Run a MirrorPulse health check and report results.

1. Run the MirrorPulse engine: `python3 ~/.mirrordna/mirrorpulse/engine.py`
2. Read the state: `~/.mirrordna/mirrorpulse/state/pulse_state.json`
3. Read recent heals: `~/.mirrordna/mirrorpulse/logs/heal.jsonl` (last 10 lines)
4. Report:
   - Health score with trend (compare to previous readings in health_history)
   - Services up/down with names
   - Any auto-heals that happened
   - Playbook stats (lifetime heals, learned fixes)
   - Any issues that need human attention
5. If health < 50%, flag as critical and list all down services
6. To launch the TUI dashboard: `python3 ~/.mirrordna/mirrorpulse/dashboard.py`
