# /replay — Replay Session from Witness Chain

Reconstruct what happened in a previous session using the witness chain and event logs.

## Arguments

`/replay [session-id|date|latest]`

## Steps

1. **Find session events**
```bash
cat ~/.mirrordna/kernel/substrates/data/witness_chain.jsonl | python3 -c "
import sys,json
entries = [json.loads(l) for l in sys.stdin if l.strip()]
for e in entries[-20:]:
    print(f'{e.get(\"timestamp\",\"?\")[:19]} | {e.get(\"event\",\"?\")} | {e.get(\"details\",\"\")[:60]}')
"
```

2. **Find matching self-critique**
```bash
grep "$SESSION_ID" ~/.mirrordna/self_critique.jsonl 2>/dev/null || tail -3 ~/.mirrordna/self_critique.jsonl
```

3. **Find matching self-score**
```bash
grep "$SESSION_ID" ~/.mirrordna/bus/self_scores.jsonl 2>/dev/null || tail -3 ~/.mirrordna/bus/self_scores.jsonl
```

4. **Reconstruct timeline**: events in chronological order with what was built, what broke, what was fixed

5. **Report**: session timeline, ships, failures, grade, lessons
