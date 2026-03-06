# /wire-check — Verify All AI Components Are Connected

End-to-end connectivity check across the full AI mesh: kernel, Ollama, OpenMemory, MirrorPulse, hooks, bus, models.

## Steps

1. **Cognitive Kernel**
```bash
curl -s http://localhost:8892/health | python3 -m json.tool
```

2. **Ollama**
```bash
curl -s http://localhost:11434/api/tags | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'{len(d.get(\"models\",[]))} models loaded')"
```

3. **OpenMemory**
```bash
curl -s "http://localhost:8765/api/v1/memories/?user_id=mirror-admin&app_id=claude-code" 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'{len(d.get(\"results\",[]))} memories')" 2>/dev/null || echo "OpenMemory: check endpoint"
```

4. **MirrorPulse**
```bash
cat ~/.mirrordna/mirrorpulse/state/pulse_state.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Health: {d.get(\"health_score\",\"?\")}% | Services: {d.get(\"services_up\",\"?\")}/{d.get(\"services_total\",\"?\")}')"
```

5. **Session Context Hook**
```bash
ls -la ~/.activemirror/bin/session_context.sh && echo "Hook: present" || echo "Hook: MISSING"
```

6. **Conscience Loop**
```bash
cat ~/.mirrordna/kernel/substrates/data/conscience_state.json 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Conscience grade: {d.get(\"grade\",\"?\")} | nudges: {len(d.get(\"nudges\",[]))}')" 2>/dev/null || echo "Conscience: no state"
```

7. **Witness Chain**
```bash
wc -l < ~/.mirrordna/kernel/substrates/data/witness_chain.jsonl 2>/dev/null || echo "0"
```

8. **Bus**
```bash
ls ~/.mirrordna/bus/ | wc -l
```

9. **Compaction Distill**
```bash
cat ~/.mirrordna/bus/compaction_distill.md 2>/dev/null | head -5 || echo "No distill checkpoint"
```

10. **Report connectivity matrix**: which components can reach which, any broken links

## Output Format

```
WIRE CHECK — AI Mesh Connectivity
  Kernel (8892):     [UP/DOWN] — [N] primitives
  Ollama (11434):    [UP/DOWN] — [N] models
  OpenMemory (8765): [UP/DOWN] — [N] memories
  MirrorPulse:       [UP/DOWN] — [health]%
  Session Hook:      [OK/MISSING]
  Conscience:        [grade] — [N] nudges
  Witness Chain:     [N] entries — [intact/broken]
  Bus:               [N] files
  Compaction:        [fresh/stale/missing]

Mesh status: [FULLY CONNECTED / N BROKEN LINKS]
```
