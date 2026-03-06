# /inventory — Full System Inventory

Complete inventory of everything in the MirrorDNA stack: scripts, agents, skills, ports, repos, models, devices.

## Steps

1. **Scripts**
```bash
echo "Scripts:"; ls ~/.mirrordna/scripts/*.py 2>/dev/null | wc -l; echo "Shell:"; ls ~/.mirrordna/scripts/*.sh 2>/dev/null | wc -l
```

2. **LaunchAgents**
```bash
ls ~/Library/LaunchAgents/ai.mirrordna.*.plist 2>/dev/null | wc -l
```

3. **Skills**
```bash
ls ~/.claude/commands/*.md 2>/dev/null | wc -l
```

4. **Repos**
```bash
ls -d ~/repos/*/.git 2>/dev/null | wc -l
```

5. **Ports in use**
```bash
cat ~/.mirrordna/SERVICE_REGISTRY.json | python3 -c "import sys,json; d=json.load(sys.stdin); svcs=[s for s in d.get('services',[]) if isinstance(s,dict)]; print(f'{len(svcs)} registered services'); [print(f'  :{s.get(\"port\",\"?\")} {s.get(\"label\",\"?\")}') for s in svcs[:20]]"
```

6. **Ollama models**
```bash
ollama list 2>/dev/null
```

7. **Kernel primitives**
```bash
curl -s http://localhost:8892/health 2>/dev/null | python3 -m json.tool
```

8. **Vault notes**
```bash
find ~/MirrorDNA-Vault -name "*.md" | wc -l
```

9. **Devices**
```bash
cat ~/.mirrordna/INFRASTRUCTURE.md | grep -A1 "Device\|Model"
```

10. **Report totals and breakdown**
