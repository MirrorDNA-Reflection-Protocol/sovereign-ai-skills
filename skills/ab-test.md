# /ab-test — A/B Test Video Titles & Thumbnails

Test different titles and thumbnails on existing videos to optimize CTR.

## Arguments
- `/ab-test <video_id>` — Run A/B test on video

## Steps

1. **Get current stats** via YouTube Data API
2. **Generate 3 title variants** via Ollama
3. **Generate 3 thumbnail variants**
4. **Schedule rotation**: Change title every 24h, track impressions/CTR
5. **Report** winner after 72h
