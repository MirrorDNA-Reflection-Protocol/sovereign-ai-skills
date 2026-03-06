# /demo — MirrorBrain Mobile App Demo

Run the full end-to-end MirrorBrain mobile demo on the Pixel. Navigates all 5 panes, dismisses the seed modal, and opens a live action tile.

## Arguments

`/demo [fresh|quick] [--record]`

- `fresh`: Force fresh install state (pm clear + relaunch) — seed modal + all post-pm-clear dialogs will appear. **WARNING: wipes installed model — model must be reinstalled manually via phone touch before running.**
- `quick`: Skip reset, just navigate from current app state
- No arg: defaults to **`quick`** (force-stop + relaunch, model preserved)

## Pre-Demo Checklist

Before running: verify model is loaded AND set up ADB reverse.
```bash
# 1. ADB reverse — routes phone's 127.0.0.1:8097 to Mac's graph router
adb -s 46281FDAS005DS reverse tcp:8097 tcp:8097
# Verify: output should be "8097"

# 2. Verify model loaded
adb -s 46281FDAS005DS exec-out screencap -p > /tmp/check.png
# Read /tmp/check.png — ASK pane must NOT show "No local model loaded"
# If it does: physically tap Install on the phone, wait for download, then continue

# 3. Screen recording (optional — start before Step 1, pull after demo)
adb -s 46281FDAS005DS shell screenrecord --time-limit 120 /sdcard/demo_run.mp4 &
# Pull after: adb -s 46281FDAS005DS pull /sdcard/demo_run.mp4 /tmp/demo_run.mp4
```

**Never use `fresh` before a demo unless showing first-run experience.
Standard demo = force-stop + relaunch only.**
- `--record`: Record device screen during the tour → `/tmp/demo_recording.mp4`

## demo_runner.py (Python automation)

```bash
# Full tour, fresh install, screen recorded:
python3 scripts/demo_runner.py --mode tour --fresh --record

# Full tour, current state, no recording:
python3 scripts/demo_runner.py --mode tour

# Full tour, fresh, no recording:
python3 scripts/demo_runner.py --mode tour --fresh
```

## Device

Pixel 9 Pro XL · 1008×2244 (High res mode, default) · Package: `com.mirrorbrainmobile`
Native: 1344×2992 · ADB serial: `46281FDAS005DS`

## Confirmed Coordinates (tap-verified 2026-02-26)

```
SEED MODAL
  Skip for now:     (504, 1990)   # bounds [46,1936][962,2044] clickable=true

NAV DOTS  (DOT_Y = 2167)
  STATUS  (pulse):  (374, 2167)   ✓ verified 2026-02-26
  NOW:              (440, 2167)   ✓ verified 2026-02-26
  ASK:              (505, 2167)   ✓ verified 2026-02-26
  VAULT:            (570, 2167)   ✓ verified 2026-02-26
  ACTIONS:          (635, 2167)   ✓ verified 2026-02-26

ACTIONS TILES
  Mirror Controls:  (182, 405)
  Factory:          (756, 405)    ✓ verified 2026-02-26
  Moment:           (182, 690)
  Briefing:         (756, 690)
  Focus Mode:       (182, 935)
  Relationships:    (756, 935)
  Weekly Digest:    (182, 1180)
  Mesh Chat:        (756, 1180)

PANELS
  Close X (bottom sheet):   (924, 1032)   # bounds [886,982][962,1082] ✓ UI-dump verified 2026-02-26
  Close X (full screen):    (926, 278)    # bounds [891,231][961,325]

DIALOGS (after pm clear only)
  Android compat warning — Don't Show Again: (708, 2108)   # bounds [545,2057][871,2160]
  Calendar Allow:           (504, 1253)   # bounds [177,1215][831,1292]
```

## Steps

### RULE: Screenshot before EVERY tap. No exceptions.

### SCREENSHOT PROTOCOL

Use `mobile_screenshot` — now returns 288×641px (fixed: mobile-mcp patched to use device density for scaling, density 560 → scale 3.5 → 1008/3.5=288, 2244/3.5=641). Well under the 2000px limit.

### 1. Reset app

**NOTE: mobile_init fails when multiple ADB devices are connected. Use direct ADB with -s flag throughout.**

```bash
# STANDARD (quick/default) — preserves installed model:
adb -s 46281FDAS005DS shell am force-stop com.mirrorbrainmobile
adb -s 46281FDAS005DS shell am start -n com.mirrorbrainmobile/.MainActivity

# FRESH ONLY (first-run experience) — WIPES model, requires manual reinstall:
adb -s 46281FDAS005DS shell am force-stop com.mirrorbrainmobile
adb -s 46281FDAS005DS shell pm clear com.mirrorbrainmobile
adb -s 46281FDAS005DS shell am start -n com.mirrorbrainmobile/.MainActivity
```

Wait 3s, then screenshot.

### 2. Handle calendar permission (only after pm clear)

Screenshot → if calendar dialog visible ("Allow MirrorBrain to access Calendar?"):
- Tap Allow button at (504, 1253)

Screenshot again to confirm dismissed.

### 3. Dismiss seed modal

**NOTE: Modal appears with a ~2-3s delay after launch — it overlays on top of STATUS pane. Take screenshot after waiting, not immediately.**

Screenshot → confirm "Mirror Seed" modal visible (bottom sheet with Paste JSON / Create New / Skip for now).

Tap: (504, 1990)

Screenshot → confirm modal dismissed, full STATUS pane visible.

If modal still present: tap (504, 1990) once more. If stuck → `adb -s 46281FDAS005DS shell uiautomator dump /sdcard/ui.xml` then pull and parse for "Skip" bounds.

### 4. PANE 1 — STATUS

Screenshot → narrate:
- Mirror: **Online** / Offline + **SAFE** / ACTIVE badge
- Policy version + Router version (e.g. Policy pv0.1.0 · Router v0.3.0)
- Cortex Link: Router Tailscale · Mesh Tailscale
- Sensor row: Eyes · Mouth · Hands · TOPT-TERMINAL-0 (green dots = active)
- Stats: Runs / Evidence / Retry Rate
- Skill Reliability: vault_read / twin_invoke (progress bars)
- Device Actions: recent device events
- Quick Actions: Runs / Voice / Shield
- Factory Theatre card (scrolled below)

### 5. PANE 2 — NOW

Tap: (440, 2167)

Screenshot → narrate:
- Location + weather (e.g. Goa, 30°, Partly cloudy)
- MAC MINI M4: X/6 Services · X% Memory · XXXG Free
- Calendar: upcoming events or "No upcoming events"

Expected: 6/6 services, ~100% memory, ~135G free

### 6. PANE 3 — ASK

Tap: (505, 2167)

Screenshot → narrate:
- "Mirror is ready. Speak naturally." (confirms local model loaded)
- "Hold to talk" blue button
- Model pills: **Mirror** (local) · Claude · Codex
- Input bar: Ask Mirror... with mic + sparkle icons

If "No local model loaded" appears: **STOP. Do not continue demo. Model must be reinstalled on-device.**

### 7. PANE 4 — VAULT

Tap: (570, 2167)

Wait 2s. Screenshot → confirm VAULT pane visible (search bar + filter pills).

**GALAXY button tap is mandatory — galaxy does NOT auto-load reliably.**

Tap Galaxy button: **(808, 330)**   ← estimated; verify from screenshot

Wait 10s for galaxy to render (fetches 2420 nodes from graph router via ADB reverse).

Screenshot → narrate:
- "Vault ready" badge
- Galaxy: 2420+ nodes floating as knowledge constellation — Paul's 10 months of thinking
- Toggle buttons: Graph (force-directed) / Galaxy (orbital) views available
- Bottom tiles: Share / Obsidian / Backup

**If galaxy shows empty after 10s:** tap (808, 330) once more, wait another 10s.
Note: first load after fresh relaunch can take up to 30s (network warm-up). Subsequent loads hit AsyncStorage cache and are instant.

### 8. PANE 5 — ACTIONS

Tap: (635, 2167)

Screenshot → narrate:
- All 8 tiles visible:
  - Mirror Controls — Ambient toggles, permissions, and safety stops
  - Factory — Launch Mac swarm and show live progress
  - Moment — Capture screen + clipboard (+ screenshot/OCR)
  - Briefing — Context summary and next steps
  - Focus Mode — Deep work with auto-reply
  - Relationships — Who needs a follow-up
  - Weekly Digest — Weekly reflection and trends
  - Mesh Chat — Talk to agents on your Mac

### 9. Tap Factory tile

Tap: (756, 405)

Wait 3s for Factory sheet to load (shows spinner briefly).

Screenshot → narrate:
- Factory bottom sheet opens
- Run: `factory-YYYY-MM-DD-HHMM` (e.g. factory-2026-02-26-1200)
- Endpoint: Tailscale
- Auto Refresh: ON (polls every 2s)
- Tasks: X/5 done · Y running · Z pending
- Task list (MirrorDNA Organism, Living Today Demo Runner, MirrorGate Human Review Console, Kavach Safety Stack, ...)

Close sheet: tap (924, 1032)

### 10. Report

```
MIRRORBRAIN DEMO — Complete

Device: Pixel 9 Pro XL · 1008×2244
App: com.mirrorbrainmobile
Run: <timestamp>

Panes navigated:
  ✓ STATUS  — Mirror Online, SAFE, X runs, Y evidence
  ✓ NOW     — Mac Mini X/6 services, X% memory, XXXG free
  ✓ ASK     — Mirror ready, local model loaded
  ✓ VAULT   — Vault ready
  ✓ ACTIONS — 8 tiles, Factory live (X/5 tasks)

Seed modal: dismissed at (504, 1990)
Factory run: <run_id>
```

## Confirmed Coordinates — VAULT Galaxy/Graph buttons

```
VAULT HEADER BUTTONS  (row at ~y=330, above search bar)
  Graph button:         (720, 330)   ← estimated
  Galaxy button:        (808, 330)   ← estimated — ALWAYS tap after entering VAULT
```
**Verification**: if galaxy doesn't appear after tap, take screenshot and estimate from actual button position. These are approximate because uiautomator can't dump VAULT pane (animated/live).

## Screen Recording

```bash
# Start before demo:
adb -s 46281FDAS005DS shell screenrecord --time-limit 120 /sdcard/demo_run.mp4 &

# Pull after demo:
adb -s 46281FDAS005DS pull /sdcard/demo_run.mp4 /tmp/demo_run.mp4
open /tmp/demo_run.mp4
```

## Notes

- **Two ADB devices connected** — always use `adb -s 46281FDAS005DS` explicitly. `mobile_init` will fail without it.
- **ADB reverse required for vault galaxy** — run `adb -s 46281FDAS005DS reverse tcp:8097 tcp:8097` before every demo. Resets on USB reconnect. Without it, galaxy hangs for minutes.
- **Galaxy root cause (fixed in app build 2026-02-26)** — AbortController.abort() broken in RN/Hermes (GH#50015). LAN endpoint (192.168.0.115) would hang TCP for minutes. Fixed with Promise.race() timeout.
- **uiautomator can't dump live panes** — STATUS and ACTIONS have continuous polling/animations, so `uiautomator dump` returns "could not get idle state". Use screencap + Read for visual verification. UI dumps only work on static screens (seed modal, Factory sheet).
- The displayed screenshot in chat is scaled — use UI dump bounds for coord truth, not visual estimation
- Nav dots are small targets at y=2167 — if a tap misses, screenshot and verify before retrying
- Seed modal appears ~2-3s after app launch, overlaying on STATUS pane
- After `pm clear`, a calendar permission dialog always appears before the seed modal
- MacStatusWidget polls port 8100 every 30s — if memory shows 0%, the mirrorbrain-api may be down
- Factory sheet run ID format: `factory-YYYY-MM-DD-HHMM` (not DEMO-YYYYMMDD)
- Factory sheet close X: (924, 1032) — NOT at the visual header position — use verified coord only
