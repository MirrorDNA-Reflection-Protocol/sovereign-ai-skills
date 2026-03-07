# /viral — Autonomous Viral Distribution Pipeline

Run the full viral engine: detect new ships, generate multi-format content, optimize for SEO+AEO+AIO, distribute across all channels.

## Arguments

`/viral [--dry-run] [--force]`

- No args: normal run (only processes unposted ships)
- `--dry-run`: generate content but don't post
- `--force`: re-process all ships from last 3 days

## Steps

1. **Run viral engine**
```bash
python3 ~/.mirrordna/scripts/viral_engine.py
```

2. **Check results**
```bash
cat ~/.mirrordna/bus/viral_state.json | python3 -m json.tool
```

3. **Check recent content generated**
```bash
ls -lt ~/.mirrordna/viral/content/ | head -10
```

4. **Report**: ships detected, content generated, posts made, repos pushed, IndexNow submitted

## Automated Schedule

LaunchAgent `ai.mirrordna.viral-engine` runs every 2 hours. The pipeline:
1. Scans SHIPLOG for new SHIPPED entries (last 3 days)
2. Generates short post + thread + article hook + AIO description via Ollama
3. Posts to Bluesky and Mastodon with glyph signature
4. Updates llms.txt across all repos
5. Pushes repos with unpushed commits
6. Submits URLs to IndexNow for instant Bing/Yandex indexing

## The Three Optimization Layers

- **SEO**: meta tags, sitemaps, IndexNow, structured data
- **AEO**: FAQ schema, answer-first paragraphs, speakable markup
- **AIO**: llms.txt on every repo, machine-readable capability claims, provenance metadata

## Output Format
```
VIRAL ENGINE — [timestamp]
  Ships detected: [N]
  Content generated: [N] pieces
  Posted: Bluesky [N], Mastodon [N]
  Repos pushed: [N]
  IndexNow: [submitted/skipped]
  llms.txt: [N] repos updated
```
