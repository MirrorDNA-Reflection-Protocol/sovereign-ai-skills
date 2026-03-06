# /beacon — Manage Beacon Blog

Create, publish, and manage beacon blog posts for truth-first-beacon.

## Arguments
- `/beacon new "Title"` — Create new post
- `/beacon list` — List recent posts
- `/beacon publish` — Build and deploy

## Steps

1. **List recent posts**
```bash
ls -lt ~/repos/truth-first-beacon/content/reflections/ | head -10
```

2. **Build site**
```bash
cd ~/repos/truth-first-beacon && hugo --minify 2>&1 | tail -5
```
