# /self-knowledge — Self-Knowledge Accuracy Benchmark

Test what the Twin actually knows about its own system vs what it hallucinates. 50 questions across 5 categories, scored against FACTS.md ground truth.

## Arguments

`/self-knowledge [--category hardware|services|identity|architecture|history] [--compare]`

## Steps

1. **Answer all 50 questions from memory — do NOT read FACTS.md, INFRASTRUCTURE.md, or SHIPLOG.md**

Get the question list:
```bash
python3 ~/.mirrordna/bin/self-knowledge-benchmark
```

2. **Answer each question** — write your answers into a JSON object keyed by question ID.

CRITICAL: Answer from your current knowledge. The whole point is measuring what you know without looking things up. Do not use Read, Grep, or Bash to check answers.

3. **Score your answers**
```bash
echo '{...your answers...}' | python3 ~/.mirrordna/bin/self-knowledge-benchmark --score
```

4. **Analyze results** — identify patterns in what you got wrong:
   - Wrong category = knowledge gap in that area
   - Common wrong values = hallucination pattern
   - Right on everything = bus/state system is working

5. **If --compare**: load previous results from `~/.mirrordna/health/self_knowledge_results.jsonl` and show trend

## Output Format
```
SELF-KNOWLEDGE BENCHMARK — [date]

Category         Score
hardware         [N]/10
services         [N]/10
identity         [N]/10
architecture     [N]/10
history          [N]/10

Total: [N]/50 ([N]%)

Hallucination patterns:
  - [what you consistently get wrong]

Knowledge gaps:
  - [categories where you score low]

vs previous: [improved/declined/stable]
```

## Why This Matters

Regular Claude scores 0/50 — it has zero knowledge of this system.
The Twin should score 40+/50 because of bus state, FACTS.md, and accumulated context.
The delta IS the value of the MirrorDNA system.
