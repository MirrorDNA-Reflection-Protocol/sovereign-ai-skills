# /research-agents — Run MirrorResearch Intelligence Sweep

Collect RSS feeds, GitHub trending, and generate a daily research briefing.

## Steps

1. **Run sweep**
```bash
python3 ~/MirrorDNA-Vault/01_ACTIVE/MirrorResearchAgents/main.py 2>&1 | tail -20
```

2. **Read latest briefing**
```bash
ls -t ~/MirrorDNA-Vault/01_ACTIVE/MirrorResearchAgents/data/briefings/ | head -1
```
