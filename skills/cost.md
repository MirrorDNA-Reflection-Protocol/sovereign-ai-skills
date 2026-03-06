# /cost — API Spend & Resource Tracking

Track API costs, token usage, and compute spend across all AI services.

## Steps

1. **Anthropic spend** — Check if cost tracker exists
```bash
cat ~/.mirrordna/bus/cost_tracking.json 2>/dev/null || echo "No cost tracker"
```

2. **Self-score history** — proxy for session intensity
```bash
tail -10 ~/.mirrordna/bus/self_scores.jsonl 2>/dev/null | python3 -c "
import sys,json
scores = [json.loads(l) for l in sys.stdin if l.strip()]
total_calls = sum(s.get('total_calls',0) for s in scores)
total_min = sum(s.get('duration_min',0) for s in scores)
print(f'Last {len(scores)} sessions: {total_calls} tool calls, {total_min:.0f} min')
"
```

3. **Ollama compute** — local model usage is free but uses hardware
```bash
curl -s http://localhost:11434/api/tags | python3 -c "
import sys,json
d=json.load(sys.stdin)
models = d.get('models',[])
total_gb = sum(m.get('size',0) for m in models) / 1e9
print(f'{len(models)} models, {total_gb:.1f}GB VRAM allocated')
"
```

4. **Groq usage** — check if tracking exists
```bash
cat ~/.mirrordna/bus/groq_usage.json 2>/dev/null || echo "No Groq tracker"
```

5. **Disk cost** — storage consumed by AI components
```bash
du -sh ~/.mirrordna/ ~/repos/ ~/.ollama/models/ 2>/dev/null
```

6. **Report total estimated spend and resource usage**

## Output Format

```
COST REPORT — [date]
  Anthropic: [estimated spend or "OAuth — no direct billing"]
  Groq: [spend or "free tier"]
  Ollama: [N] models, [X]GB disk, $0 (local)
  Storage: ~/.mirrordna [X]GB, repos [X]GB, models [X]GB
  Sessions: [N] in last 7d, [total calls] tool calls
```
