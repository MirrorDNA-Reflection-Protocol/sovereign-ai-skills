# /shorts — Generate YouTube Shorts from Recordings

Auto-clip daily recordings into 55-second vertical Shorts with text overlays, upload to YouTube.

## Arguments
- `/shorts` — Generate from today's recordings
- `/shorts --date 2026-03-06` — Specific date
- `/shorts --max-shorts 5` — Limit clip count
- `/shorts --dry-run` — Preview clip selection

## Steps

1. **Run generator**
```bash
python3 ~/.mirrordna/scripts/shorts_generator.py $ARGUMENTS
```

2. **Report**
List each Short title and YouTube URL.
