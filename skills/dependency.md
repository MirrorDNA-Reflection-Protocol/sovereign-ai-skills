# /dependency — Package & Dependency Audit

Run full dependency audit across brew, pip, npm, and Ollama. Includes vulnerability scanning.

## Arguments

`/dependency [--quick] [--json]`

## Steps

1. **Run dependency audit**
```bash
python3 ~/.mirrordna/scripts/dependency_audit.py $ARGUMENTS
```

2. **Read results**
```bash
cat ~/.mirrordna/health/dependency_audit.json | python3 -m json.tool
```

3. **Report**: outdated counts, vulnerability counts, recommendations
