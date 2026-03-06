# /regression — Detect Performance Regressions

Compare current system performance against historical baselines. Flag anything that got worse.

## Steps

1. **Load historical benchmarks**
```bash
tail -10 ~/.mirrordna/health/benchmarks.jsonl 2>/dev/null
```

2. **Load recent self-scores**
```bash
tail -10 ~/.mirrordna/bus/self_scores.jsonl
```

3. **Load calibration history**
```bash
cat ~/.mirrordna/kernel/substrates/data/calibration.json
```

4. **Compare against baselines**:
   - Grade trend (last 10 sessions): improving/declining/stable
   - Ship velocity trend: accelerating/slowing
   - Tool call rate: increasing (thrashing?) or stable
   - Rabbit hole count: increasing (bad) or decreasing
   - Ship ratio: increasing (productive) or decreasing (exploring too much)
   - Service uptime: any new failures in heal log

5. **Flag regressions**: anything that's measurably worse than 7 days ago

6. **Propose fixes**: for each regression, suggest what changed and how to fix

## Output Format
```
REGRESSION CHECK — [date]
  Grade:        65 → 55 REGRESSED (was 70 baseline)
  Ship velocity: 3.2/day → 2.1/day REGRESSED
  Ship ratio:   78% → 82% IMPROVED
  Rabbit holes: 0 → 2 REGRESSED
  Services:     41/41 STABLE

  Action: [specific fix for each regression]
```
