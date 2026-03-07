# /decision-persistence — Decision Persistence Test

Proves decisions survive across sessions. Two-phase test: plant in session 1, verify in session 2.

## Steps

### Phase 1 (session 1):
```bash
python3 ~/.mirrordna/bin/decision-persistence-test --plant
```

### Phase 2 (NEW session):
```bash
python3 ~/.mirrordna/bin/decision-persistence-test --check
```
Answer from memory. Then score:
```bash
echo '{...}' | python3 ~/.mirrordna/bin/decision-persistence-test --score
```

## What It Tests
10 architectural and behavioral decisions. The Twin should respect all of them without being re-told. This has never been benchmarked for any AI system.

## Output
```
Score: [N]/10 ([N]%)
DECISIONS PERSIST | DECISION DRIFT DETECTED
```
