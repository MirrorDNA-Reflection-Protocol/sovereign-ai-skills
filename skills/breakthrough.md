# /breakthrough — Track & Generate Novel Capabilities

Identify what's genuinely new in the stack — things no one else has built. Track breakthroughs over time. Generate new ones.

## Arguments

`/breakthrough [list|generate|log]`

- `list`: Show all logged breakthroughs
- `generate`: Analyze current stack and propose next breakthroughs
- `log`: Record a new breakthrough

## Steps

### list
```bash
cat ~/.mirrordna/breakthroughs.jsonl 2>/dev/null | python3 -c "
import sys,json
for line in sys.stdin:
    b = json.loads(line.strip())
    print(f'[{b[\"date\"]}] {b[\"name\"]}')
    print(f'  Category: {b[\"category\"]} | Impact: {b[\"impact\"]}')
    print(f'  What: {b[\"description\"][:100]}')
    print()
" 2>/dev/null || echo "No breakthroughs logged yet. Run /breakthrough log to start."
```

### generate
1. Read current stack capabilities:
   - Kernel primitives and modes (temperature-as-architecture)
   - Conscience loop (DREAM -> CALIBRATE -> CONSCIENCE -> INJECT -> ACT -> WITNESS)
   - Witness chain (cryptographic provenance)
   - Self-healing (MirrorPulse playbook evolution)
   - Compaction survival (distill checkpoint)
   - 5 digital coworker roles
   - 184 scripts, 83 LaunchAgents

2. Identify what's novel (things that don't exist in standard AI infra):
   - Temperature as formal architecture (not just a parameter)
   - Conscience loop with self-nudging
   - Witness chain for AI session provenance
   - Self-scoring with automated regression detection
   - Context compaction survival via distill
   - Sovereign notification without cloud dependencies
   - Self-learning playbook (MirrorPulse)

3. Propose NEXT breakthroughs — what's achievable in the next session:
   - Cross-session learning (kernel learns from self-critique patterns)
   - Adversarial self-testing (Red Mac runs attacks on main system)
   - Autonomous paper generation from ship logs
   - Predictive intent (anticipate Paul's next request from patterns)
   - Self-replicating skills (skill that generates new skills)
   - Federated memory across all devices
   - Coworker runtime with real contract execution

### log
1. Ask for: name, category, description, impact level (incremental/significant/paradigm)
2. Append to `~/.mirrordna/breakthroughs.jsonl`
3. Update SHIPLOG if it's a shipped breakthrough

## Breakthrough Categories
- architecture: new structural pattern
- capability: new thing the system can do
- autonomy: system does something without being asked
- efficiency: does existing thing 10x better
- novelty: genuinely new in the field
- integration: connects things that weren't connected
