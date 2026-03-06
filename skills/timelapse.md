# /timelapse — Create Coding Timelapse

Concatenate all day's recordings into a 60-90 second timelapse at 16x-32x speed with music-ready timing.

## Arguments
- `/timelapse` — Today
- `/timelapse --date 2026-03-06` — Specific date
- `/timelapse --speed 16` — Speed multiplier

## Steps

1. **Concatenate** all recordings from the date
2. **Speed up** with ffmpeg setpts filter
3. **Add progress bar** overlay showing time of day
4. **Export** as both landscape (YouTube) and vertical (Shorts)
