# /clip — AI-Powered Highlight Clipper

Analyzes screen recordings to find the most visually interesting moments (fast typing, terminal output, UI changes) and extracts them as clips.

## Arguments
- `/clip` — Clip today's recordings
- `/clip --date 2026-03-06` — Specific date  
- `/clip --count 5` — Number of clips

## Steps

1. **Scan recordings** for visual activity (frame diff analysis via ffmpeg)
```bash
for f in ~/recordings/$(date +%Y-%m-%d)/*.mp4; do
  ffprobe -v quiet -show_entries format=duration -of json "$f" 2>/dev/null
done
```

2. **Find high-activity segments** using scene change detection:
```bash
ffmpeg -i INPUT -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep showinfo
```

3. **Extract top clips** as 15-60 second segments
4. **Add text overlay** with context from SHIPLOG
