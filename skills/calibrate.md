# /calibrate — Self-Benchmarking on Demand

Run the cognitive kernel CALIBRATE primitive and show twin performance metrics.

## Steps

1. **Run calibration**
```bash
python3 ~/.mirrordna/kernel/substrates/calibrate.py 7d
```

2. **Read calibration state**
```bash
cat ~/.mirrordna/kernel/substrates/data/calibration.json
```

3. **Read recent self-critiques for context**
```bash
tail -5 ~/.mirrordna/self_critique.jsonl
```

4. **Report**:
   - Grade (A-F) with score breakdown
   - Trend (improving/stable/declining)
   - Ship velocity (ships/day)
   - Accuracy score (hallucination rate)
   - Character win rate
   - Recurring failures (if any)
   - Recommendation

## Output Format

```
CALIBRATION — [window]
Grade: [letter]
  Session score: [avg] ([trend])
  Ship velocity: [N]/day ([ships] in window)
  Accuracy: [score] ([samples] samples)
  Win rate: [rate] ([wins]W / [fails]F)
  Recurring: [count] patterns

Recommendation: [one-line]
```
