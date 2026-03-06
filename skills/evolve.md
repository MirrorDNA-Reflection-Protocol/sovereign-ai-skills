# /evolve — Self-Improvement Cycle

Run a full self-improvement cycle: calibrate, identify weaknesses, propose improvements, implement if safe.

## Steps

1. **Calibrate** — get current grade and metrics
```bash
python3 ~/.mirrordna/kernel/substrates/calibrate.py 7d
```

2. **Read recurring failures** from self-critique
```bash
python3 -c "
import json
from pathlib import Path
critiques = []
for line in Path.home().joinpath('.mirrordna/self_critique.jsonl').read_text().splitlines()[-10:]:
    if line.strip():
        critiques.append(json.loads(line))
recurring = {}
for c in critiques:
    for r in c.get('recurring', []):
        recurring[r] = recurring.get(r, 0) + 1
for pattern, count in sorted(recurring.items(), key=lambda x: -x[1]):
    print(f'  [{count}x] {pattern}')
"
```

3. **Read MISTAKES.md** for scar tissue
```bash
head -50 ~/.mirrordna/MISTAKES.md
```

4. **Identify improvement targets**:
   - Recurring failures with count >= 3 → need automation (hook/guard)
   - Grade < B → identify weakest metric
   - Win rate < 0.7 → analyze character_failures
   - Ship velocity < 2/day → check for blockers

5. **Propose improvements** — concrete actions, not vague suggestions:
   - New hook to catch pattern X
   - New guard in session_context.sh for Y
   - New LaunchAgent to automate Z
   - Kernel primitive enhancement for W

6. **If improvement is safe (hook, guard, config)**: implement it immediately
7. **If improvement is risky (kernel change, service change)**: propose and wait for Paul

## Output Format
```
EVOLVE — Self-Improvement Cycle
  Current: Grade [X], [N] recurring failures

  Improvements applied:
    [+] Added hook for [pattern] → prevents [failure]
    [+] Updated guard for [X]

  Improvements proposed (needs Paul):
    [?] Kernel change: [description]
    [?] Service change: [description]

  Next calibration target: Grade [Y]
```
