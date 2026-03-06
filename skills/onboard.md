# /onboard — Generate Context Pack for New Agent

Create a minimal context pack so a new agent (Codex, Gemini, local model, digital coworker) can start working immediately.

## Arguments

`/onboard <agent-name> [--scope full|minimal|domain]`

## Steps

1. **Read identity anchors**
```bash
head -50 ~/.mirrordna/true-paul-seed.md
head -50 ~/.mirrordna/twin-character.md
```

2. **Read current state**
```bash
head -30 ~/.mirrordna/CONTINUITY.md
head -30 ~/.mirrordna/SHIPLOG.md
```

3. **Generate context pack** containing:
   - Who Paul is (condensed from true-paul-seed)
   - Current focus and phase
   - What's shipped (last 10 entries from SHIPLOG)
   - Key file paths
   - Communication style rules
   - Constraints (no auto-publish, no test-fire, facts from sources only)
   - OAuth scope for the agent

4. **Write pack** to `~/.mirrordna/handoff/onboard-<agent>-<date>.md`

5. **If agent is a digital coworker**: also include work contract schema and role spec from `~/MirrorDNA-Vault/01_ACTIVE/DigitalCoworkers/`
