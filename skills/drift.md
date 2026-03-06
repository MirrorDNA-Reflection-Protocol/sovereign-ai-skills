# /drift — Detect Configuration Drift

Compare all sources of truth against reality. Find where config says one thing but the system does another.

## Steps

1. **SERVICE_REGISTRY vs LaunchAgents**
```bash
python3 -c "
import json
from pathlib import Path
reg = json.loads(Path.home().joinpath('.mirrordna/SERVICE_REGISTRY.json').read_text())
svcs = reg.get('services', [])
reg_labels = {s['label'] for s in svcs if isinstance(s, dict) and 'label' in s}
import subprocess
out = subprocess.run(['launchctl', 'list'], capture_output=True, text=True).stdout
loaded = {l.split()[-1] for l in out.splitlines() if 'ai.mirrordna' in l}
print('In registry, not loaded:', sorted(reg_labels - loaded)[:10])
print('Loaded, not in registry:', sorted({l for l in loaded if l.startswith('ai.mirrordna')} - reg_labels)[:10])
"
```

2. **twin_state.json vs kernel reality**
```bash
curl -s http://localhost:8892/health
cat ~/.mirrordna/twin_state.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d.get('kernel',{}), indent=2))"
```

3. **INFRASTRUCTURE.md vs actual**
   - Check Ollama models listed vs `ollama list`
   - Check disk free vs actual
   - Check Tailscale IPs vs `tailscale status`

4. **FACTS.md vs reality** — run verify_claims if target file given

5. **Report all drift items with severity (cosmetic/functional/critical)**
