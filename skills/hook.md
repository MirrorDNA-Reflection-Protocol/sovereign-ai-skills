# /hook — Generate Viral Video Hooks

Uses Ollama to generate 10 attention-grabbing hooks for YouTube videos. Tested against viral formulas (curiosity gap, contrarian take, number-driven, story-driven).

## Arguments
- `/hook` — Generate hooks from today's ships
- `/hook "topic"` — Generate hooks for specific topic

## Steps

1. **Read today's context**
```bash
# Get today's ships from SHIPLOG
grep -A 20 "$(date +%Y-%m-%d)" ~/.mirrordna/SHIPLOG.md | head -20
```

2. **Generate hooks via Ollama**
Send to Ollama with prompt:
```
Generate 10 YouTube video hooks for a solo developer building sovereign AI. Today's work: [ships]. 
Each hook must be under 10 words and use one of these formulas:
1. Curiosity gap: "I built X and Y happened"
2. Contrarian: "Why X is wrong about Y"
3. Number: "N things I learned building X"
4. Challenge: "Can one person build X?"
5. Behind scenes: "What really happens when X"
```

3. **Output** the top 10 hooks ranked by viral potential.
