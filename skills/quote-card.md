# /quote-card — Generate Quotable Image Cards

Extract memorable quotes from vault notes and build logs, render as shareable image cards.

## Arguments
- `/quote-card` — Random quote from vault
- `/quote-card "Custom quote"` — Specific text

## Steps

1. **Select/generate quote** from vault or Ollama
2. **Render card** via ffmpeg drawtext:
   - Dark background with subtle terminal texture
   - Quote in large serif font
   - Attribution: "— Paul Desai, activemirror.ai"
   - Subtle branding in corner
3. **Output** as 1080x1080 PNG (Instagram) and 1200x675 (Twitter/Bluesky)
