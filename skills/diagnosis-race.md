# /diagnosis-race — Operational Diagnosis Race

Inject 10 real failures into the live system. Diagnose and fix each one. Measures operational knowledge.

## Steps

1. **Inject failures** (non-destructive, reversible)
```bash
~/.mirrordna/bin/diagnosis-race
```

2. **Diagnose each scenario** — identify root cause and fix

3. **Cleanup when done**
```bash
~/.mirrordna/bin/diagnosis-race --cleanup
```

## Scenarios
- Service down, port conflict, config corruption, stale PID
- DNS failure, disk pressure, missing model, launchd/supervisord conflict
- Git conflict, memory pressure

## Output
```
Diagnosed: [N]/10
Time: [N]s average per diagnosis
Rating: EXPERT | COMPETENT | NEEDS PRACTICE
```
