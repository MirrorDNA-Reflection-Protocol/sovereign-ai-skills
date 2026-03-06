# /thumbnail — AI-Generate Video Thumbnails

Generate click-worthy thumbnails using terminal screenshots + text overlays + contrast optimization.

## Arguments
- `/thumbnail "Title Text"` — Generate thumbnail
- `/thumbnail --video-id <id>` — Generate and upload for existing video

## Steps

1. **Capture terminal screenshot** or use latest recording frame
2. **Apply thumbnail formula** via ffmpeg:
   - High contrast background (darken terminal)
   - Large bold text (title, 3-5 words max)
   - Accent color border (yellow/green on dark)
   - Face/avatar overlay if available
3. **Generate 3 variants** for A/B testing
4. **Output** paths to generated thumbnails
