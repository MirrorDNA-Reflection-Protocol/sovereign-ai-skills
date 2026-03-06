# /signal — Send Notification via MirrorSignal

Send a notification to macOS + OnePlus + Pixel via the sovereign MirrorSignal service (port 8890).

## Arguments
- `/signal "message"` — Send notification
- `/signal --title "Title" "message"` — With custom title

## Steps

1. **Send via MirrorSignal**
```bash
curl -s -X POST http://127.0.0.1:8890/signal -H "Content-Type: application/json" -d '{"title": "$TITLE", "message": "$MESSAGE", "priority": 3}'
```
