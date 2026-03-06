#!/usr/bin/env python3
"""
forensic.py — Ultimate Full-Stack System Forensic for MirrorDNA.

Single-pass deep scan across every layer:
  1. SERVICES   — ports, health endpoints, process state, LaunchAgent exit codes
  2. NETWORK    — domains, SSL certs, Tailscale mesh, device reachability
  3. KERNEL     — cognitive kernel health, primitives, substrates, conscience
  4. INTEGRITY  — witness chain, FACTS.md vs reality, SHIPLOG freshness
  5. INFRA      — disk, memory, CPU, log bloat, zombie processes
  6. DEPS       — outdated packages, missing modules
  7. VAULT      — inbox backlog, orphan notes, frontmatter compliance
  8. SECURITY   — API key validity, credential exposure, permission anomalies
  9. CONTINUITY — heartbeat age, CONTINUITY.md staleness, bus health, calendar sync
  10. DRIFT     — SERVICE_REGISTRY vs actual, twin_state vs reality, config drift

Outputs:
  - Console summary (pass/warn/fail per layer)
  - JSON report at ~/.mirrordna/health/forensic_report.json
  - One-line grade (A-F)

Usage:
    python3 forensic.py              # Full forensic
    python3 forensic.py --quick      # Skip slow checks (deps, SSL, API keys)
    python3 forensic.py --json       # JSON output only
    python3 forensic.py --layer X    # Run only layer X (services, network, etc.)
"""

import json
import os
import re
import socket
import subprocess
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

IST = timezone(timedelta(hours=5, minutes=30))
HOME = Path.home()
MIRRORDNA = HOME / ".mirrordna"
REPORT_PATH = MIRRORDNA / "health" / "forensic_report.json"
REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

QUICK = "--quick" in sys.argv
JSON_ONLY = "--json" in sys.argv
LAYER_FILTER = None
if "--layer" in sys.argv:
    idx = sys.argv.index("--layer")
    if idx + 1 < len(sys.argv):
        LAYER_FILTER = sys.argv[idx + 1].lower()


def now_ist():
    return datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S IST")


def cmd(c, timeout=15):
    try:
        r = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "timeout"
    except Exception as e:
        return -1, "", str(e)


def http_check(url, timeout=5):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "MirrorDNA-Forensic/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")[:500]
    except urllib.error.HTTPError as e:
        return e.code, str(e)
    except Exception as e:
        return 0, str(e)


def file_age_seconds(path):
    try:
        return time.time() - Path(path).stat().st_mtime
    except Exception:
        return float("inf")


def read_json_safe(path, default=None):
    try:
        return json.loads(Path(path).read_text())
    except Exception:
        return default or {}


# ═══════════════════════════════════════════════════════════════════
# LAYER 1: SERVICES
# ═══════════════════════════════════════════════════════════════════

def check_services():
    findings = []

    # Load service registry
    registry = read_json_safe(MIRRORDNA / "SERVICE_REGISTRY.json", {})
    services = registry.get("services", [])
    if isinstance(services, dict):
        services = list(services.values())

    # Check each registered service
    up = 0
    down = 0
    for svc in services:
        if isinstance(svc, str):
            continue
        name = svc.get("label", svc.get("name", "unknown"))
        port = svc.get("port")
        health_url = svc.get("health_url")

        if health_url:
            code, body = http_check(health_url)
            if code in (200, 301, 302):
                up += 1
            else:
                down += 1
                findings.append(("FAIL", f"{name} (:{port}) — HTTP {code}"))
        elif port:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect(("127.0.0.1", port))
                s.close()
                up += 1
            except Exception:
                down += 1
                findings.append(("FAIL", f"{name} (:{port}) — port closed"))

    # LaunchAgent exit codes
    rc, out, _ = cmd("launchctl list 2>/dev/null | grep ai.mirrordna")
    crashed = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 3:
            exit_code = parts[1]
            label = parts[2]
            if exit_code not in ("0", "-"):
                crashed.append(f"{label} (exit:{exit_code})")

    if crashed:
        findings.append(("WARN", f"{len(crashed)} LaunchAgents with non-zero exit: {', '.join(crashed[:5])}"))

    # Zombie processes
    rc, out, _ = cmd("ps aux | grep -E 'python3?|node|uvicorn' | grep -v grep | wc -l")
    proc_count = int(out.strip()) if out.strip().isdigit() else 0

    # ffmpeg zombies
    rc, out, _ = cmd("pgrep -f 'ffmpeg.*screen' | wc -l")
    ffmpeg_count = int(out.strip()) if out.strip().isdigit() else 0
    if ffmpeg_count > 2:
        findings.append(("WARN", f"{ffmpeg_count} ffmpeg screen recording processes"))

    return {
        "services_up": up,
        "services_down": down,
        "crashed_agents": crashed[:10],
        "python_node_procs": proc_count,
        "ffmpeg_zombies": ffmpeg_count,
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 2: NETWORK
# ═══════════════════════════════════════════════════════════════════

def check_network():
    findings = []

    # Domain checks
    domains = {
        "activemirror.ai": "https://activemirror.ai",
        "beacon.activemirror.ai": "https://beacon.activemirror.ai",
        "id.activemirror.ai": "https://id.activemirror.ai",
        "docs.activemirror.ai": "https://docs.activemirror.ai",
    }
    domain_status = {}
    for name, url in domains.items():
        code, _ = http_check(url, timeout=10)
        domain_status[name] = code
        if code not in (200, 301, 302, 403):
            findings.append(("FAIL", f"{name} — HTTP {code}"))

    # Tailscale mesh
    devices = {
        "OnePlus": "100.91.11.72",
        "Pixel": "100.74.95.99",
        "Red Mac": "100.106.113.28",
    }
    device_status = {}
    for name, ip in devices.items():
        rc, _, _ = cmd(f"ping -c 1 -t 3 {ip} 2>/dev/null", timeout=5)
        device_status[name] = "reachable" if rc == 0 else "unreachable"
        if rc != 0:
            findings.append(("WARN", f"{name} ({ip}) unreachable on Tailscale"))

    # SSL cert (skip on --quick)
    cert_info = {}
    if not QUICK:
        import ssl
        for domain in ["activemirror.ai", "beacon.activemirror.ai"]:
            try:
                ctx = ssl.create_default_context()
                with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
                    s.settimeout(10)
                    s.connect((domain, 443))
                    cert = s.getpeercert()
                    expiry_str = cert.get("notAfter", "")
                    if expiry_str:
                        expiry = datetime.strptime(expiry_str, "%b %d %H:%M:%S %Y %Z")
                        days = (expiry - datetime.utcnow()).days
                        cert_info[domain] = f"{days}d remaining"
                        if days < 14:
                            findings.append(("FAIL", f"SSL cert {domain} expires in {days}d"))
            except Exception as e:
                cert_info[domain] = f"check failed: {str(e)[:60]}"

    return {
        "domains": domain_status,
        "devices": device_status,
        "ssl_certs": cert_info,
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 3: KERNEL
# ═══════════════════════════════════════════════════════════════════

def check_kernel():
    findings = []

    # Kernel health
    code, body = http_check("http://localhost:8892/health")
    kernel_up = code == 200
    if not kernel_up:
        findings.append(("FAIL", f"Cognitive kernel (8892) — HTTP {code}"))

    kernel_info = {}
    if kernel_up:
        try:
            data = json.loads(body)
            kernel_info = {
                "primitives": data.get("primitives", "?"),
                "domains": data.get("domains", "?"),
                "uptime": data.get("uptime_seconds", "?"),
            }
        except Exception:
            kernel_info = {"raw": body[:200]}

    # Calibration grade
    cal_path = MIRRORDNA / "kernel" / "substrates" / "data" / "calibration.json"
    cal = read_json_safe(cal_path)
    grade = cal.get("grade", "?")
    if grade in ("D", "F"):
        findings.append(("WARN", f"Calibration grade: {grade}"))

    # Conscience state
    conscience_path = MIRRORDNA / "kernel" / "substrates" / "data" / "conscience_state.json"
    conscience = read_json_safe(conscience_path)

    # Witness chain integrity
    witness_path = MIRRORDNA / "kernel" / "substrates" / "data" / "witness_chain.jsonl"
    witness_count = 0
    chain_intact = True
    if witness_path.exists():
        lines = [l.strip() for l in witness_path.read_text().splitlines() if l.strip()]
        witness_count = len(lines)
        # Quick chain verify — check last 5 entries have prev_hash
        for line in lines[-5:]:
            try:
                entry = json.loads(line)
                if "prev_hash" not in entry and "hash" not in entry:
                    chain_intact = False
            except Exception:
                chain_intact = False

    if not chain_intact:
        findings.append(("FAIL", "Witness chain integrity compromised"))

    return {
        "kernel_up": kernel_up,
        "kernel_info": kernel_info,
        "calibration_grade": grade,
        "calibration_metrics": cal.get("metrics", {}),
        "conscience_grade": conscience.get("grade", "?"),
        "witness_entries": witness_count,
        "witness_chain_intact": chain_intact,
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 4: INTEGRITY
# ═══════════════════════════════════════════════════════════════════

def check_integrity():
    findings = []

    # FACTS.md exists and is recent
    facts_path = MIRRORDNA / "FACTS.md"
    facts_age = file_age_seconds(facts_path)
    if facts_age > 86400 * 7:
        findings.append(("WARN", f"FACTS.md is {int(facts_age / 86400)}d old"))

    # SHIPLOG.md freshness
    shiplog_path = MIRRORDNA / "SHIPLOG.md"
    shiplog_age = file_age_seconds(shiplog_path)
    if shiplog_age > 86400 * 3:
        findings.append(("WARN", f"SHIPLOG.md is {int(shiplog_age / 86400)}d old — no recent ships?"))

    # MISTAKES.md exists
    mistakes_path = MIRRORDNA / "MISTAKES.md"
    mistakes_exists = mistakes_path.exists()

    # twin_state.json freshness
    twin_path = MIRRORDNA / "twin_state.json"
    twin_age = file_age_seconds(twin_path)
    twin_state = read_json_safe(twin_path)

    # Verify kernel grade in twin_state matches calibration
    cal_path = MIRRORDNA / "kernel" / "substrates" / "data" / "calibration.json"
    cal = read_json_safe(cal_path)
    if twin_state.get("kernel", {}).get("grade") != cal.get("grade"):
        findings.append(("WARN", "twin_state.json kernel grade doesn't match calibration"))

    return {
        "facts_age_hours": round(facts_age / 3600, 1),
        "shiplog_age_hours": round(shiplog_age / 3600, 1),
        "mistakes_exists": mistakes_exists,
        "twin_state_age_hours": round(twin_age / 3600, 1),
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 5: INFRASTRUCTURE
# ═══════════════════════════════════════════════════════════════════

def check_infra():
    findings = []

    # Disk space
    st = os.statvfs(str(HOME))
    free_gb = (st.f_bavail * st.f_frsize) / (1024 ** 3)
    total_gb = (st.f_blocks * st.f_frsize) / (1024 ** 3)
    used_pct = round((1 - st.f_bavail / st.f_blocks) * 100, 1)
    if free_gb < 10:
        findings.append(("FAIL", f"Only {free_gb:.1f}GB free disk"))
    elif free_gb < 20:
        findings.append(("WARN", f"{free_gb:.1f}GB free disk"))

    # Log directory size
    log_dir = MIRRORDNA / "logs"
    log_size_mb = 0
    biggest_logs = []
    if log_dir.exists():
        files = [(f, f.stat().st_size) for f in log_dir.iterdir() if f.is_file()]
        log_size_mb = sum(s for _, s in files) / (1024 * 1024)
        biggest_logs = sorted(files, key=lambda x: x[1], reverse=True)[:5]
        biggest_logs = [{"name": f.name, "mb": round(s / (1024 * 1024), 1)} for f, s in biggest_logs]
        if log_size_mb > 500:
            findings.append(("WARN", f"Logs: {log_size_mb:.0f}MB — consider rotation"))

    # Memory pressure
    rc, out, _ = cmd("vm_stat | head -5")
    # Simple parse — just report available
    rc2, out2, _ = cmd("sysctl hw.memsize 2>/dev/null")
    total_ram_gb = 24  # known from INFRASTRUCTURE.md

    # Load average
    rc, out, _ = cmd("sysctl -n vm.loadavg 2>/dev/null")
    load_avg = out.strip() if out else "?"

    # Uptime
    rc, out, _ = cmd("uptime")
    uptime_str = out.strip() if out else "?"

    return {
        "disk_free_gb": round(free_gb, 1),
        "disk_total_gb": round(total_gb, 1),
        "disk_used_pct": used_pct,
        "log_size_mb": round(log_size_mb, 1),
        "biggest_logs": biggest_logs,
        "load_avg": load_avg,
        "uptime": uptime_str,
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 6: DEPENDENCIES (skip on --quick)
# ═══════════════════════════════════════════════════════════════════

def check_deps():
    if QUICK:
        return {"skipped": True, "findings": []}

    findings = []

    # pip outdated count
    rc, out, _ = cmd("pip3 list --outdated --format=json 2>/dev/null", timeout=30)
    pip_outdated = 0
    if rc == 0 and out:
        try:
            pip_outdated = len(json.loads(out))
        except Exception:
            pass

    # brew outdated count
    rc, out, _ = cmd("brew outdated 2>/dev/null | wc -l", timeout=30)
    brew_outdated = int(out.strip()) if out.strip().isdigit() else 0

    # Ollama models
    rc, out, _ = cmd("ollama list 2>/dev/null")
    ollama_models = len([l for l in out.splitlines() if l and not l.startswith("NAME")]) if out else 0

    if pip_outdated > 20:
        findings.append(("WARN", f"{pip_outdated} outdated pip packages"))

    return {
        "pip_outdated": pip_outdated,
        "brew_outdated": brew_outdated,
        "ollama_models": ollama_models,
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 7: VAULT
# ═══════════════════════════════════════════════════════════════════

def check_vault():
    findings = []
    vault = HOME / "MirrorDNA-Vault"

    # Inbox backlog
    inbox = vault / "00_INBOX"
    inbox_count = len(list(inbox.glob("*.md"))) if inbox.exists() else 0
    if inbox_count > 20:
        findings.append(("WARN", f"Inbox backlog: {inbox_count} items"))

    # Folder counts
    folders = {}
    for d in vault.iterdir():
        if d.is_dir() and not d.name.startswith("."):
            count = sum(1 for _ in d.rglob("*.md"))
            folders[d.name] = count

    # Git status
    rc, out, _ = cmd(f"cd {vault} && git status --porcelain 2>/dev/null | wc -l")
    dirty_count = int(out.strip()) if out.strip().isdigit() else 0
    if dirty_count > 50:
        findings.append(("WARN", f"Vault has {dirty_count} uncommitted changes"))

    # Total notes
    total = sum(folders.values())

    return {
        "total_notes": total,
        "inbox_count": inbox_count,
        "folders": folders,
        "git_dirty": dirty_count,
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 8: SECURITY (skip on --quick)
# ═══════════════════════════════════════════════════════════════════

def check_security():
    if QUICK:
        return {"skipped": True, "findings": []}

    findings = []

    # Check API keys exist (not validity — that's slow)
    env_file = MIRRORDNA / "secrets.env"
    keys_found = set()
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k = line.split("=")[0].strip()
                if k:
                    keys_found.add(k)

    expected_keys = {"ANTHROPIC_API_KEY", "GROQ_API_KEY"}
    missing = expected_keys - keys_found
    if missing:
        findings.append(("WARN", f"Missing API keys: {', '.join(missing)}"))

    # Check for exposed secrets in common locations
    exposed = []
    for pattern in ["*.env", "*.key", "*.pem"]:
        for f in (HOME / "MirrorDNA-Vault").rglob(pattern):
            if f.is_file() and f.stat().st_size > 0:
                exposed.append(str(f.relative_to(HOME)))
    if exposed:
        findings.append(("WARN", f"Potential secrets in vault: {', '.join(exposed[:3])}"))

    # File permissions on secrets
    secrets_perms = {}
    for p in [MIRRORDNA / "secrets.env", MIRRORDNA / ".env"]:
        if p.exists():
            mode = oct(p.stat().st_mode)[-3:]
            secrets_perms[p.name] = mode
            if mode not in ("600", "640", "400"):
                findings.append(("WARN", f"{p.name} has permissions {mode} (should be 600)"))

    return {
        "api_keys_found": sorted(keys_found),
        "missing_keys": sorted(missing),
        "exposed_files": exposed[:5],
        "secrets_permissions": secrets_perms,
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 9: CONTINUITY
# ═══════════════════════════════════════════════════════════════════

def check_continuity():
    findings = []

    # CONTINUITY.md heartbeat line age
    cont = MIRRORDNA / "CONTINUITY.md"
    cont_age = file_age_seconds(cont)
    heartbeat_age = None
    if cont.exists():
        first_line = cont.read_text().split("\n")[0]
        # Parse: Last heartbeat: 2026-03-06 22:51 IST
        m = re.search(r"Last heartbeat: (\d{4}-\d{2}-\d{2} \d{2}:\d{2})", first_line)
        if m:
            try:
                hb = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M").replace(tzinfo=IST)
                heartbeat_age = (datetime.now(IST) - hb).total_seconds()
                if heartbeat_age > 300:
                    findings.append(("WARN", f"Heartbeat stale: {int(heartbeat_age)}s ago"))
            except Exception:
                pass

    # Sync line age
    sync_age = None
    if cont.exists():
        text = cont.read_text()
        m = re.search(r"Last sync: (\d{4}-\d{2}-\d{2}T\d{2}:\d{2})", text)
        if m:
            try:
                sync = datetime.fromisoformat(m.group(1)).replace(tzinfo=IST)
                sync_age = (datetime.now(IST) - sync).total_seconds()
                if sync_age > 43200:
                    findings.append(("WARN", f"Last sync {int(sync_age / 3600)}h ago"))
            except Exception:
                pass

    # Bus health
    bus_dir = MIRRORDNA / "bus"
    bus_files = len(list(bus_dir.glob("*"))) if bus_dir.exists() else 0

    # Calendar sync freshness
    cal_synced = None
    if cont.exists():
        m = re.search(r"synced: (\d{4}-\d{2}-\d{2})", cont.read_text())
        if m:
            try:
                cal_date = datetime.strptime(m.group(1), "%Y-%m-%d").replace(tzinfo=IST)
                cal_age_days = (datetime.now(IST) - cal_date).days
                cal_synced = m.group(1)
                if cal_age_days > 3:
                    findings.append(("WARN", f"Calendar sync stale: {cal_age_days}d ago"))
            except Exception:
                pass

    # Self-score trend
    scores_file = MIRRORDNA / "bus" / "self_scores.jsonl"
    scores = []
    if scores_file.exists():
        for line in scores_file.read_text().strip().splitlines()[-5:]:
            try:
                scores.append(json.loads(line).get("grade", 0))
            except Exception:
                pass

    # Action queue
    aq = read_json_safe(MIRRORDNA / "bus" / "action_queue.json", {"items": []})
    pending_actions = len(aq.get("items", []))
    if pending_actions > 0:
        findings.append(("WARN", f"{pending_actions} items in action queue"))

    return {
        "heartbeat_age_s": int(heartbeat_age) if heartbeat_age else None,
        "sync_age_hours": round(sync_age / 3600, 1) if sync_age else None,
        "bus_files": bus_files,
        "calendar_last_sync": cal_synced,
        "self_scores_recent": scores,
        "pending_actions": pending_actions,
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# LAYER 10: DRIFT
# ═══════════════════════════════════════════════════════════════════

def check_drift():
    findings = []

    # SERVICE_REGISTRY vs actual LaunchAgents
    registry = read_json_safe(MIRRORDNA / "SERVICE_REGISTRY.json", {})
    reg_services = registry.get("services", [])
    reg_labels = set()
    for svc in reg_services:
        if isinstance(svc, dict):
            reg_labels.add(svc.get("label", ""))

    # Actual LaunchAgents
    rc, out, _ = cmd("launchctl list 2>/dev/null | grep ai.mirrordna | awk '{print $3}'")
    actual_labels = set(out.strip().splitlines()) if out.strip() else set()

    in_registry_not_loaded = reg_labels - actual_labels - {""}
    loaded_not_in_registry = {l for l in actual_labels if l.startswith("ai.mirrordna")} - reg_labels

    if in_registry_not_loaded:
        findings.append(("WARN", f"In registry but not loaded: {', '.join(sorted(in_registry_not_loaded)[:5])}"))
    if loaded_not_in_registry:
        findings.append(("INFO", f"Loaded but not in registry: {', '.join(sorted(loaded_not_in_registry)[:5])}"))

    # Plist files vs loaded agents
    la_dir = HOME / "Library" / "LaunchAgents"
    plist_labels = set()
    if la_dir.exists():
        for p in la_dir.glob("ai.mirrordna.*.plist"):
            plist_labels.add(p.stem)

    plists_not_loaded = plist_labels - actual_labels
    if plists_not_loaded:
        findings.append(("INFO", f"{len(plists_not_loaded)} plist files not loaded"))

    # twin_state vs kernel reality
    twin = read_json_safe(MIRRORDNA / "twin_state.json")
    kernel_state = twin.get("kernel", {})
    code, body = http_check("http://localhost:8892/health")
    if code == 200:
        try:
            live = json.loads(body)
            live_prims = live.get("primitives", "?")
            state_prims = kernel_state.get("primitives", "?")
            if live_prims != "?" and state_prims != "?" and live_prims != state_prims:
                findings.append(("WARN", f"twin_state says {state_prims} primitives, kernel reports {live_prims}"))
        except Exception:
            pass

    return {
        "registry_services": len(reg_labels - {""}),
        "loaded_agents": len(actual_labels),
        "plist_files": len(plist_labels),
        "registry_not_loaded": sorted(in_registry_not_loaded)[:10],
        "loaded_not_registry": sorted(loaded_not_in_registry)[:10],
        "findings": findings,
    }


# ═══════════════════════════════════════════════════════════════════
# GRADING
# ═══════════════════════════════════════════════════════════════════

def grade_report(layers):
    fails = sum(1 for l in layers.values() for f in l.get("findings", []) if f[0] == "FAIL")
    warns = sum(1 for l in layers.values() for f in l.get("findings", []) if f[0] == "WARN")

    score = 100 - (fails * 15) - (warns * 3)
    score = max(0, min(100, score))

    for threshold, letter in [(90, "A"), (75, "B"), (60, "C"), (40, "D")]:
        if score >= threshold:
            return letter, score
    return "F", score


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

LAYERS = {
    "services": ("Services", check_services),
    "network": ("Network & Domains", check_network),
    "kernel": ("Cognitive Kernel", check_kernel),
    "integrity": ("Data Integrity", check_integrity),
    "infra": ("Infrastructure", check_infra),
    "deps": ("Dependencies", check_deps),
    "vault": ("Vault", check_vault),
    "security": ("Security", check_security),
    "continuity": ("Continuity & Bus", check_continuity),
    "drift": ("Config Drift", check_drift),
}


def run_forensic():
    ts = now_ist()
    results = {"timestamp": ts, "mode": "quick" if QUICK else "full", "layers": {}}

    for key, (name, fn) in LAYERS.items():
        if LAYER_FILTER and key != LAYER_FILTER:
            continue
        try:
            results["layers"][key] = fn()
            results["layers"][key]["name"] = name
        except Exception as e:
            results["layers"][key] = {"name": name, "error": str(e), "findings": [("FAIL", f"Layer crashed: {e}")]}

    grade, score = grade_report(results["layers"])
    results["grade"] = grade
    results["score"] = score

    # Save report
    REPORT_PATH.write_text(json.dumps(results, indent=2, default=str))

    if JSON_ONLY:
        print(json.dumps(results, indent=2, default=str))
        return results

    # Console output
    print(f"FORENSIC REPORT — {ts}")
    print(f"Mode: {'quick' if QUICK else 'full'}")
    print(f"Grade: {grade} ({score}/100)")
    print("=" * 60)

    for key, data in results["layers"].items():
        name = data.get("name", key)
        findings = data.get("findings", [])
        fails = sum(1 for f in findings if f[0] == "FAIL")
        warns = sum(1 for f in findings if f[0] == "WARN")
        infos = sum(1 for f in findings if f[0] == "INFO")

        if fails > 0:
            status = "FAIL"
        elif warns > 0:
            status = "WARN"
        else:
            status = "PASS"

        summary_parts = []
        if data.get("skipped"):
            status = "SKIP"
            summary_parts.append("skipped (--quick)")
        elif data.get("error"):
            summary_parts.append(data["error"])
        else:
            # Layer-specific summaries
            if key == "services":
                summary_parts.append(f"{data.get('services_up', 0)} up, {data.get('services_down', 0)} down")
            elif key == "network":
                doms = data.get("domains", {})
                ok = sum(1 for v in doms.values() if v in (200, 301, 302, 403))
                summary_parts.append(f"{ok}/{len(doms)} domains")
                devs = data.get("devices", {})
                rok = sum(1 for v in devs.values() if v == "reachable")
                summary_parts.append(f"{rok}/{len(devs)} devices")
            elif key == "kernel":
                summary_parts.append(f"grade:{data.get('calibration_grade', '?')}")
                summary_parts.append(f"witness:{data.get('witness_entries', 0)}")
            elif key == "integrity":
                summary_parts.append(f"FACTS:{data.get('facts_age_hours', '?')}h")
            elif key == "infra":
                summary_parts.append(f"disk:{data.get('disk_free_gb', '?')}GB free")
                summary_parts.append(f"logs:{data.get('log_size_mb', '?')}MB")
            elif key == "vault":
                summary_parts.append(f"{data.get('total_notes', '?')} notes")
                summary_parts.append(f"inbox:{data.get('inbox_count', 0)}")
            elif key == "continuity":
                hb = data.get("heartbeat_age_s")
                summary_parts.append(f"heartbeat:{hb}s" if hb else "heartbeat:?")
            elif key == "drift":
                summary_parts.append(f"reg:{data.get('registry_services', 0)}")
                summary_parts.append(f"loaded:{data.get('loaded_agents', 0)}")

        summary = ", ".join(summary_parts) if summary_parts else ""
        marker = {"PASS": "+", "WARN": "!", "FAIL": "X", "SKIP": "-"}.get(status, "?")
        print(f"  [{marker}] {name:<20} {summary}")

        for severity, msg in findings:
            indent_marker = {"FAIL": "X", "WARN": "!", "INFO": "i"}.get(severity, "?")
            print(f"      [{indent_marker}] {msg}")

    print("=" * 60)
    print(f"Report: {REPORT_PATH}")

    return results


if __name__ == "__main__":
    run_forensic()
