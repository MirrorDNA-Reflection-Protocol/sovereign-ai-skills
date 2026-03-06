# /youtube-seo — AI-Native YouTube SEO Optimizer

Uses Ollama to generate optimized titles, descriptions, and tags for YouTube videos. Runs automatically after daily uploads.

## Arguments
- `/youtube-seo <video_id>` — Optimize single video
- `/youtube-seo --recent` — Optimize last 5 uploads
- `/youtube-seo --channel-audit` — Audit all recent videos
- `/youtube-seo --dry-run <video_id>` — Preview changes

## Steps

1. **Run optimizer**
```bash
python3 ~/.mirrordna/scripts/youtube_seo.py $ARGUMENTS
```

2. **Report changes**
Show before/after title, tag count, and confirmation.
