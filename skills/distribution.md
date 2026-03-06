# /distribution — Full Distribution Pipeline

Run the complete content distribution pipeline for today's content.

## Steps

1. **Daily video**: `daily_video.py` (if not run)
2. **SEO optimize**: `youtube_seo.py --recent`
3. **Generate Shorts**: `shorts_generator.py`
4. **Auto-publish**: `auto_publish.py`
5. **Social thread**: Generate and post Bluesky thread
6. **Quote cards**: Generate 3 shareable images
7. **Newsletter segment**: Write weekly section
8. **Report** all URLs and metrics
