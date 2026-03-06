# /benchmark — System Performance Benchmarks

Run quantitative benchmarks across the entire stack. Track over time. Detect regression.

## Arguments

`/benchmark [--full] [--compare YYYY-MM-DD]`

## Steps

1. **Kernel latency** — time a round-trip primitive call
```bash
time curl -s -X POST http://localhost:8892/execute -H "Content-Type: application/json" -d '{"primitive": "EVALUATE", "args": {"claim": "benchmark test"}}' 2>/dev/null
```

2. **Ollama inference speed** — tokens/sec on local model
```bash
time curl -s http://localhost:11434/api/generate -d '{"model": "llama3.2:3b", "prompt": "What is 2+2?", "stream": false}' 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'{d.get(\"eval_count\",0)} tokens in {d.get(\"eval_duration\",1)/1e9:.2f}s = {d.get(\"eval_count\",0)/(d.get(\"eval_duration\",1)/1e9):.1f} tok/s')"
```

3. **OpenMemory search speed**
```bash
time curl -s "http://localhost:8765/api/v1/memories/?user_id=mirror-admin&app_id=claude-code&query=test" 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'{len(d.get(\"results\",[]))} results')"
```

4. **Vault search speed** — grep across 5000+ notes
```bash
time grep -rl "MirrorGate" ~/MirrorDNA-Vault/ 2>/dev/null | wc -l
```

5. **Disk I/O**
```bash
dd if=/dev/zero of=/tmp/bench_test bs=1m count=100 2>&1 | tail -1; rm /tmp/bench_test
```

6. **Network latency** — to key services
```bash
for host in activemirror.ai api.anthropic.com api.groq.com; do echo -n "$host: "; ping -c 3 -q $host 2>/dev/null | grep avg | awk -F'/' '{print $5 "ms"}'; done
```

7. **Ship velocity** — ships per day over last 7d
```bash
python3 ~/.mirrordna/kernel/substrates/calibrate.py 7d 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Ship velocity: {d[\"metrics\"][\"ship_velocity\"]}/day ({d[\"metrics\"][\"ships_in_window\"]} in 7d)')"
```

8. **Session efficiency** — from self-scores
```bash
tail -5 ~/.mirrordna/bus/self_scores.jsonl | python3 -c "
import sys,json
scores = [json.loads(l) for l in sys.stdin if l.strip()]
if scores:
    avg_grade = sum(s['grade'] for s in scores)/len(scores)
    avg_ratio = sum(s['ship_ratio'] for s in scores)/len(scores)
    avg_cpm = sum(s['calls_per_min'] for s in scores)/len(scores)
    print(f'Avg grade: {avg_grade:.0f} | Ship ratio: {avg_ratio:.0%} | Calls/min: {avg_cpm:.1f}')
"
```

9. **Save results** to `~/.mirrordna/health/benchmarks.jsonl` (append, track over time)

10. **If --compare**: load previous benchmark, show delta for each metric, flag regressions

## Output Format
```
BENCHMARK — [date]
  Kernel latency:     [N]ms
  Ollama (3b):        [N] tok/s
  OpenMemory search:  [N]ms ([N] results)
  Vault grep:         [N]ms ([N] files)
  Disk I/O:           [N] MB/s
  Network (Anthropic):[N]ms
  Ship velocity:      [N]/day
  Session efficiency:  grade [N], ship ratio [N]%

  vs last benchmark: [improved/regressed/stable]
```
