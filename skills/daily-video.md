# /daily-video — Compile & Upload Daily Build Log Video

Compile today's screen recordings into a YouTube video, upload, SEO optimize, generate Shorts, and cross-post everywhere.

## Arguments
- `/daily-video` — Run for today
- `/daily-video --date 2026-03-06` — Specific date
- `/daily-video --dry-run` — Preview without uploading

## Steps

1. **Run the pipeline**
```bash
python3 ~/.mirrordna/scripts/daily_video.py $ARGUMENTS
```

2. **Verify upload**
Check `~/.mirrordna/logs/daily-video.log` for the YouTube URL and cross-post confirmations.

3. **Report**
```
Done: Daily video uploaded
YouTube: [url]
Cross-posts: Bluesky, Mastodon, Beacon, dev.to, Telegram
SEO: Optimized
Shorts: [N] generated
```
