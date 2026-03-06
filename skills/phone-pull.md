# /phone-pull — Pull & Triage Files from OnePlus

Pull files Paul has dropped into the phone's dedicated DROP zone, unzip archives, and triage into vault project folders.

**Drop zones (both scanned):**
- `/sdcard/DROP/` — **PRIMARY. Root of storage. One tap in any file manager.**
- `/sdcard/Obsidian/MirrorDNA-Vault/DROP/` — secondary (deep path, same purpose)

Paul drops files into either. NEVER pull from `00_INBOX/` — that folder contains Sonnet-generated noise and old accumulation. Only `DROP/` folders are authoritative.

## Arguments

`/phone-pull [date] [dry-run]`

- `date`: Optional date override (YYYY-MM-DD). Defaults to today.
- `dry-run`: If specified, show what would be pulled/moved without executing.

## Steps

1. **Verify Phone Connection**
```bash
adb devices
```
If no device attached, report and stop.

2. **Find Files — both DROP zones (maxdepth 1)**
```bash
adb -s 3C15AT00EBJ00000 shell "find /sdcard/DROP/ /sdcard/Obsidian/MirrorDNA-Vault/DROP/ -maxdepth 1 -type f 2>/dev/null"
```
Pull ALL files found in either DROP folder regardless of date or type. These are Paul's intentional drop zones.
Skip: `_INDEX.md`, `.DS_Store`, `.nomedia`, system files.
**NEVER scan or pull from `00_INBOX/` — only `DROP/` folders.**

3. **Pull Files**
```bash
mkdir -p ~/MirrorDNA-Vault/00_INBOX/phone-pull-[date]
adb -s 3C15AT00EBJ00000 pull [each file] ~/MirrorDNA-Vault/00_INBOX/phone-pull-[date]/
```
Pull individually (not the whole folder) to avoid pulling the entire inbox tree.

4. **Unzip Archives**
```bash
cd ~/MirrorDNA-Vault/00_INBOX/phone-pull-[date]
for z in *.zip; do unzip -o "$z" -d "${z%.zip%.ZIP}"; done
```

5. **Triage to Project Folders**
Read each bundle's README or contents to determine the right project folder. Use this mapping:

| Pattern | Destination |
|---------|-------------|
| MirrorBalance, MirrorSim, NetBird, mesh | `01_ACTIVE/MirrorBalance_v2/` |
| MirrorGate, Nanbeige, AgentKit, router | `01_ACTIVE/MirrorGate/` |
| MirrorForge, SovereignFactory, GSD, Factory | `01_ACTIVE/SovereignFactory/` |
| MirrorCast, podcast, audio | `01_ACTIVE/MirrorCast/` |
| MirrorBrain, graph, memory | `01_ACTIVE/MirrorBrain/` |
| MirrorIntake, intake, funnel | `01_ACTIVE/MirrorIntake/` |
| MirrorPulse, pulse, health | `01_ACTIVE/MirrorPulse/` |
| ActiveMirror, landing, marketing | `01_ACTIVE/ActiveMirror/` |
| Reference, concept, theory | `04_REFERENCE/` |
| Unknown / ambiguous | Leave in `00_INBOX/phone-pull-[date]/` |

Move extracted directories (not zip files) to destinations.

6. **Clean Up**
Remove zip files from the local pull folder after successful extraction.
```bash
rm ~/MirrorDNA-Vault/00_INBOX/phone-pull-[date]/*.zip
```
If pull folder is empty after triage, remove it.

**NEVER delete anything from the phone.** Pull only. The phone is the source of truth and backup. Do not clean the drop zone.

7. **Summarize Each Bundle**
For every triaged bundle, read the README.md (or main files if no README) and produce a 2-3 sentence summary covering:
- What it is (tool, spec, config, reference)
- What stage it's at (idea, spec, buildable, built, shipped)
- Key capabilities or purpose

8. **Build Action Plan**
Based on the summaries, create a prioritized action plan:
- For each bundle, determine: **BUILD** (has code, needs running/testing), **REVIEW** (spec or reference, needs reading), **CONFIGURE** (config/infra, needs setup), or **PARK** (not actionable now)
- Order by: BUILD items first (most actionable), then CONFIGURE, then REVIEW, then PARK
- For BUILD items, include the specific commands to run (from README or inferred from file structure)
- For CONFIGURE items, include what needs to be set up
- Estimate complexity: **quick** (< 5 min), **medium** (5-30 min), **deep** (30+ min)

9. **Write Intake Report**
Save to `~/MirrorDNA-Vault/SessionReports/SR-[date]-PhonePull.md`:
```markdown
---
mirror_id: SR-[date]-PULL
title: "Phone Pull — [date]"
layer: active
created: [timestamp]
tags: [phone-pull, intake, triage]
---

# Phone Pull — [date]

**Device:** [device ID]
**Pulled:** [N] files ([size])
**Bundles:** [N] triaged

## Triage

| Bundle | Destination | Files | Stage |
|--------|-------------|-------|-------|
| ... | ... | ... | ... |

## Summaries

### [Bundle Name]
[2-3 sentence summary]

## Action Plan

| # | Bundle | Action | Complexity | Command |
|---|--------|--------|------------|---------|
| 1 | MirrorForge_v1 | BUILD | medium | `cd runtime && python mirrorforge_cli.py init` |
| ... | ... | ... | ... | ... |

## Quick Start
To build everything in parallel:
```
/factory demo
```
Or pick one: [first BUILD item command]
```

10. **Bus Entry**
Write a bus changelog entry for the pull:
```bash
session commit "Phone pull: [N] files, [M] bundles triaged, [B] buildable"
```

11. **Report to Terminal**
```
⟡ Phone Pull Complete — [date]

Device: [device ID]
Pulled: [N] files ([size])

| Bundle | → Destination | Files | Action |
|--------|---------------|-------|--------|
| MirrorForge_v1 | SovereignFactory/ | 21 | BUILD |
| ... | ... | ... | ... |

Action Plan:
  1. BUILD MirrorForge_v1 — cd runtime && python mirrorforge_cli.py init
  2. BUILD GSD_SelfSteering — python3 gsd_runner.py examples/...
  3. CONFIGURE NetBird — bash provision_device.sh
  ...

Triaged: [N] | Buildable: [B] | Report: SessionReports/SR-[date]-PhonePull.md
Ready to build? Run: /factory demo
```

## Notes

- Fix double extensions (e.g. `.md.md` → `.md`) during triage
- Rename emoji-prefixed filenames to clean ASCII versions
- **NEVER delete anything from the phone — EVER. Pull only. Phone is source of truth.**
- If a destination folder doesn't exist, create it
- The action plan feeds directly into `/factory` — buildable items become factory agents
- If Paul says "build" after a pull, generate a factory manifest and run it
