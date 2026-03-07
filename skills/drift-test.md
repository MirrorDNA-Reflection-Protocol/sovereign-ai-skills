# /drift-test — Identity Drift Detector

Same 20 questions asked weekly. Consistency scored over time. Detects identity degradation.

## Steps

1. **Answer 20 identity questions**
```bash
python3 ~/.mirrordna/bin/drift-detector --generate
```

2. **Record answers**
```bash
echo '{...}' | python3 ~/.mirrordna/bin/drift-detector --record
```

3. **View drift report** (after 2+ snapshots)
```bash
python3 ~/.mirrordna/bin/drift-detector --report
```

## Categories
Identity, philosophy, behavior, architecture, emotional, strategy

## Output
```
IDENTITY DRIFT REPORT — [N] snapshots
Overall: [N]% stable, [N]% drifted
DRIFTED ANSWERS:
  DQ08: What was your biggest mistake?
    Was: "2 errata in published papers"
    Now: "port conflicts" ← DRIFT
```
