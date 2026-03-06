# /carousel — Generate Social Media Carousel

Turn a build session into a swipeable carousel (images with text) for Instagram/LinkedIn/Bluesky.

## Arguments
- `/carousel` — Today's session
- `/carousel "topic"` — Specific topic

## Steps

1. **Extract 5-8 key points** from today's SHIPLOG entries
2. **Generate slides** via ffmpeg:
   - Slide 1: Hook/title (bold, contrasting)
   - Slides 2-7: One insight per slide with terminal screenshot background
   - Slide 8: CTA (activemirror.ai, follow)
3. **Output** as PNG sequence ready for upload
