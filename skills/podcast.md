# /podcast — Extract Podcast Audio

Generate a podcast episode by extracting narration-worthy content and adding TTS.

## Arguments
- `/podcast` — This week's episode
- `/podcast "topic"` — Topic-focused episode

## Steps

1. **Generate script** via Ollama from week's work
2. **Generate TTS** via macOS `say` or Ollama voice model
3. **Add intro/outro** music markers
4. **Export** as MP3 with metadata
