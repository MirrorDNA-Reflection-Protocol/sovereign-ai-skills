# /auto-publish — Syndicate Content to All Platforms

Publishes beacon blog posts to Bluesky, Mastodon, dev.to, Hashnode, and Telegram.

## Arguments
- `/auto-publish` — Run now
- `/auto-publish --dry-run` — Preview what would be posted

## Steps

1. **Run publisher**
```bash
python3 ~/.mirrordna/scripts/auto_publish.py $ARGUMENTS 2>&1 | tail -20
```

2. **Check results**
```bash
tail -30 ~/.mirrordna/logs/auto-publish.log
```
