# /ffmpeg-reaper — Kill Zombie FFmpeg Processes

Kills ffmpeg screen recording processes older than 4 hours to prevent CPU exhaustion.

## Steps

1. **Run reaper**
```bash
python3 ~/.mirrordna/scripts/ffmpeg_reaper.py 2>&1
```

2. **Check for survivors**
```bash
ps aux | grep ffmpeg | grep -v grep | wc -l
```
