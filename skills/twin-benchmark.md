# /twin-benchmark — Twin vs Baseline Comparative Benchmark

The headline proof: same 25 tasks given to raw Claude (no context) vs Mirror Twin (full bus/state/facts). Measures the actual value of persistent AI identity.

## Arguments

`/twin-benchmark [--tasks all|continuity|accuracy|diagnosis|identity] [--compare]`

## Prerequisites

- `ANTHROPIC_API_KEY` in `~/.mirrordna/secrets.env` or environment
- Uses claude-sonnet-4-20250514 for both baseline and twin runs (cost-efficient, still proves the point)

## Steps

1. **Check API key**
```bash
grep ANTHROPIC_API_KEY ~/.mirrordna/secrets.env 2>/dev/null | head -1 | cut -c1-30
```

2. **Run the benchmark**
```bash
python3 ~/.mirrordna/bin/twin-vs-baseline --tasks all
```

This sends 25 tasks to Claude twice:
- **BASELINE**: Raw Claude, no system prompt, zero context
- **TWIN**: Claude with full Twin system prompt + FACTS.md + state + CONTINUITY.md

Each answer scored against ground truth keywords.

3. **Parse and display results**

The benchmark auto-saves to `~/.mirrordna/health/twin_vs_baseline.jsonl`

4. **If --compare**: load previous run, show improvement/regression

## Task Categories (25 total)

| Category | Tasks | What It Proves |
|----------|-------|---------------|
| Continuity (5) | Session memory, state awareness, decision persistence | Baseline = 0. Twin remembers across sessions. |
| Accuracy (5) | Hardware specs, model inventory, domain list, costs, device IPs | Baseline hallucinates. Twin is grounded in FACTS.md. |
| Diagnosis (5) | Port→service mapping, failure recovery, operational workflow | Baseline gives generic advice. Twin knows the actual system. |
| Identity (5) | Self-awareness, behavioral rules, mistake history, Paul-specific behavior | Baseline says "I'm Claude." Twin knows its role. |

## Expected Results

| Category | Baseline | Twin | Why |
|----------|----------|------|-----|
| Continuity | 0/5 | 5/5 | Baseline has no session memory |
| Accuracy | 0-1/5 | 4-5/5 | FACTS.md prevents hallucination |
| Diagnosis | 1-2/5 | 4-5/5 | Twin has operational context |
| Identity | 0/5 | 4-5/5 | Bus IS identity |
| **Total** | **1-3/25** | **17-25/25** | **~10x improvement** |

## Output Format
```
TWIN vs BASELINE — [date]

Category        Baseline      Twin     Delta
continuity          0/5       5/5       +5
accuracy            1/5       5/5       +4
diagnosis           1/5       4/5       +3
identity            0/5       5/5       +5

TOTAL               2/25     19/25     +17

Baseline: 8%  |  Twin: 76%

Tasks only Twin got right:
  C1: What was the last major thing shipped?
  A1: What are the exact hardware specs?
  D3: Services keep dying — what was the root cause?
  I1: Who are you in this system?
```

## Why This Is Game-Changing

This is the first quantitative proof that persistent state transforms a stateless LLM into something fundamentally more capable for its specific domain. The delta between baseline and twin IS the value proposition of MirrorDNA.

No other system measures this. No benchmark exists for persistent AI identity. We're creating the category.
