# /chaos — Infrastructure Chaos Testing

Inject failures into the MirrorDNA stack, verify auto-recovery, produce scored results.

## Arguments

`/chaos [--scenario all|disable|stop|mixed|corrupt] [--rounds N]`

- No args: run full 50-round suite across all scenarios
- `--scenario disable`: only test config-disable recovery
- `--rounds 10`: override round count per scenario (default 10)

## Steps

1. **Pre-flight: verify system healthy before injecting chaos**
```bash
~/.mirrordna/bin/supervisor-boot-guard 2>/dev/null
supervisorctl -c ~/.mirrordna/supervisord.conf status 2>/dev/null | grep -c RUNNING
```

If fewer than 5 protected services running, abort — don't inject chaos into an already-broken system.

2. **Run chaos test suite**
```bash
~/.mirrordna/bin/supervisor-boot-guard-chaos-test 2>&1
```

This runs 50 iterations across 6 scenarios:
- **Round 1** (10x): All 5 services disabled → guard recovers
- **Round 2** (10x): Random single service disabled → guard recovers
- **Round 3** (10x): Random subset disabled → guard recovers
- **Round 4** (10x): Services stopped (configs intact) → guard restarts
- **Round 5** (5x): Everything healthy → guard is idempotent
- **Round 6** (5x): Mixed chaos (stop some + disable others)

3. **Parse results** — extract pass/fail counts per round

4. **If any failures**: analyze the failure pattern, check logs:
```bash
tail -20 ~/.mirrordna/logs/supervisor-boot-guard.log
for svc in semantic-cache skillrl kavach-v04 mcp-adapter opa; do
  tail -5 ~/.mirrordna/logs/$svc.err 2>/dev/null
done
```

5. **Save results** to `~/.mirrordna/health/chaos_results.jsonl`

6. **Post-flight: verify system healthy after chaos**
```bash
~/.mirrordna/bin/supervisor-boot-guard 2>/dev/null
```

## Output Format
```
CHAOS TEST — [date]

Scenario            Rounds  Pass  Fail
all-disabled           10    10     0
random-one-disabled    10    10     0
random-subset          10    10     0
stopped-not-disabled   10    10     0
idempotent              5     5     0
mixed-chaos             5     5     0

Total: [N]/50 passed
Rating: BULLETPROOF | HARDENING NEEDED
System status: [N]/5 services confirmed healthy post-test
```
