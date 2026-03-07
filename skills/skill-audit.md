# /skill-audit — Skill Coverage Audit

Test which of the 100+ skills actually work end-to-end.

## Steps

1. **Structure check** (fast)
```bash
~/.mirrordna/bin/skill-coverage-audit
```

2. **Deep check** (verifies binaries/scripts exist)
```bash
~/.mirrordna/bin/skill-coverage-audit --deep
```

## What It Checks
- Skill file has valid structure (## Steps + ```bash blocks)
- Referenced binaries/scripts exist and are executable
- Coverage percentage of working vs broken skills

## Output
```
Total skills:    [N]
Valid structure:  [N]
Missing steps:   [N]
Broken:          [N]
Coverage:        [N]%
```
