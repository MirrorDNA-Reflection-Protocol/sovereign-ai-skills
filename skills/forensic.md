# /forensic — Full-Stack System Forensic

Deep 10-layer scan across the entire MirrorDNA stack. Supersedes health, status, pulse, smoke for comprehensive audits.

## Arguments

`/forensic [--quick] [--layer X]`

- No args: full forensic (all 10 layers)
- `--quick`: skip slow checks (deps, SSL, API keys)
- `--layer X`: run only one layer (services, network, kernel, integrity, infra, deps, vault, security, continuity, drift)

## Steps

1. **Run the forensic script**
```bash
python3 ~/.mirrordna/scripts/forensic.py $ARGUMENTS
```

2. **Read the report**
```bash
cat ~/.mirrordna/health/forensic_report.json | python3 -m json.tool
```

3. **For each FAIL finding**: propose a fix and ask Paul before executing
4. **For each WARN finding**: note it, fix if trivial, flag if not
5. **Report grade and layer summary**

## Output Format

```
FORENSIC REPORT — [timestamp]
Grade: [A-F] ([score]/100)

  [+] Services         41 up, 0 down
  [!] Network          4/4 domains, 2/3 devices
  [+] Kernel           grade:C, witness:37
  [+] Integrity        FACTS:2h
  [+] Infrastructure   disk:122GB free, logs:45MB
  [-] Dependencies     skipped
  [+] Vault            5200 notes, inbox:3
  [-] Security         skipped
  [!] Continuity       heartbeat:120s
  [+] Drift            reg:12, loaded:83

Action needed: [list fixes]
```
