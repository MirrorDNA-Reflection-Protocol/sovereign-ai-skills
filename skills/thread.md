# /thread — Turn Build Log into Social Thread

Converts today's build log into a viral Bluesky/X thread with hooks, visuals, and CTA.

## Arguments
- `/thread` — Today's build log
- `/thread --date 2026-03-06` — Specific date
- `/thread --platform bluesky|x|mastodon` — Target platform

## Steps

1. **Read today's ships from SHIPLOG**
2. **Read today's session reports**
3. **Generate thread via Ollama** using format:
   - Post 1: Hook (curiosity gap)
   - Posts 2-8: One ship per post with context
   - Post 9: Stack/tools used
   - Post 10: CTA (follow, subscribe, link)
4. **Post to Bluesky** via AT Protocol (secrets.env has BLUESKY_HANDLE + BLUESKY_APP_PASSWORD)
5. **Report** thread URL and post count.
