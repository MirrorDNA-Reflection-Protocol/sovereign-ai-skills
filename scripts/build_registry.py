#!/usr/bin/env python3
"""Build the sovereign-ai-skills registry from skill markdown files.

Scans all .md files in skills/, extracts metadata, and outputs:
  - registry/skills.json    (flat array of skill objects)
  - registry/categories.json (skills grouped by category with counts)

Usage:
    python3 scripts/build_registry.py
"""

import json
import os
import re
import sys
from pathlib import Path

# Resolve paths relative to this script's repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
REGISTRY_DIR = REPO_ROOT / "registry"

# Category keyword maps — order matters (first match wins within priority tiers)
# Each entry: (category, keywords, weight)
# Higher-weight categories are checked first to avoid mis-classification
CATEGORY_RULES = [
    # Highly specific categories first
    ("security", [
        "killswitch", "kill switch", "adversarial", "red team", "security",
        "threat", "attack", "auth", "credential", "forensic", "incident",
        "guardian", "integrity", "vulnerability", "exploit", "pentest",
    ]),
    ("video", [
        "video", "ffmpeg", "youtube", "thumbnail", "shorts", "timelapse",
        "screen recording", "clip", "endscreen", "stack-video", "daily-video",
        "weekly-video", "video-essay", "recording",
    ]),
    ("vault", [
        "vault", "obsidian", "inbox", "triage", "note", "frontmatter",
        "wiki-link", "mirror_id", "mirror_links", "glossary", "compress",
        "read path", "archive",
    ]),
    ("ai-kernel", [
        "dream", "council", "swarm", "calibrate", "cognitive", "evolve",
        "drift", "reflect", "ollama", "llm", "model", "inference",
        "embedding", "student-teacher", "verifier", "ai agent", "brain",
        "mirror seed", "twin",
    ]),
    ("research", [
        "paper", "arxiv", "zenodo", "research", "benchmark", "experiment",
        "prove", "evidence", "citation", "academic", "peer review",
        "breakthrough", "capability",
    ]),
    ("governance", [
        "governance", "contract", "alignment", "sovereignty", "sovereign",
        "killswitch", "policy", "compliance", "audit", "witness",
        "provenance",
    ]),
    ("devops", [
        "deploy", "launchagent", "backup", "health", "service", "daemon",
        "supervisor", "port", "restart", "migrate", "dependency", "smoke",
        "test", "regression", "wire-check", "reaper", "pulse", "status",
        "logs", "device", "cert", "network", "sitemap", "commit",
    ]),
    ("distribution", [
        "viral", "distribute", "bluesky", "mastodon", "indexnow", "seo",
        "aeo", "aio", "llms.txt", "promote", "launch", "newsletter",
        "drip", "funnel", "backlink", "hashtag", "growth", "audience",
        "engagement", "community", "pr ", "press",
    ]),
    ("content", [
        "carousel", "post", "thread", "headline", "hook", "cta",
        "storytell", "brief", "draft", "content", "podcast", "blog",
        "beacon", "brand", "og-image", "quote-card", "tutorial",
        "series", "niche", "evergreen", "trending", "idea",
        "comparison", "behind-scenes", "recap",
    ]),
    ("analytics", [
        "analytics", "metric", "velocity", "cost", "ab-test", "a/b test",
        "optimize", "trend", "performance", "stats", "report", "standup",
        "milestone", "inventory", "changelog",
    ]),
    ("system-ops", [
        "sync", "signal", "bus", "handoff", "pickup", "overnight",
        "morning", "session", "phone-pull", "factory", "ship", "tag",
        "find", "link", "focus", "meta", "history", "snapshot",
        "onboard", "collab", "spec",
    ]),
]


def extract_title(content: str, filename: str) -> str:
    """Extract title from the first # heading line."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            # Format: "# /name — Title" or "# Title"
            heading = line[2:].strip()
            # Remove the /name prefix if present
            match = re.match(r"^/\S+\s*[—–-]\s*(.+)$", heading)
            if match:
                return match.group(1).strip()
            return heading
    # No heading found — use first non-empty line as title
    for line in content.splitlines():
        line = line.strip()
        if line:
            # Truncate long first-lines
            return line[:120] if len(line) > 120 else line
    return filename


def extract_description(content: str) -> str:
    """Extract first paragraph after the heading (one line)."""
    lines = content.splitlines()
    found_heading = False
    past_blank = False

    for line in lines:
        stripped = line.strip()
        if not found_heading:
            if stripped.startswith("# "):
                found_heading = True
            elif stripped:
                # No heading — first non-empty line IS the description
                return stripped
            continue

        # After heading, skip blank lines to find first paragraph
        if not stripped:
            if not past_blank:
                past_blank = True
                continue
            # Second blank after heading — we've passed the description zone
            continue

        # Skip sub-headings and code blocks
        if stripped.startswith("#") or stripped.startswith("```"):
            continue

        # This is the description paragraph
        return stripped

    return ""


def infer_category(content: str, filename: str) -> str:
    """Infer category from content keywords and filename."""
    searchable = (filename + " " + content).lower()

    best_category = "system-ops"  # default fallback
    best_score = 0

    for category, keywords in CATEGORY_RULES:
        score = sum(1 for kw in keywords if kw in searchable)
        if score > best_score:
            best_score = score
            best_category = category

    return best_category


def has_script_reference(content: str) -> bool:
    """Check if the skill references a bash or python script."""
    patterns = [
        r"python3?\s+\S+\.py",
        r"bash\s+\S+\.sh",
        r"sh\s+\S+\.sh",
        r"\./\S+\.(py|sh)",
        r"~/\S+\.(py|sh)",
        r"\$HOME/\S+\.(py|sh)",
        r"scripts/\S+\.(py|sh)",
    ]
    for pattern in patterns:
        if re.search(pattern, content):
            return True
    return False


def assess_complexity(content: str) -> str:
    """Assess complexity based on number of steps and content length."""
    # Count numbered steps (top-level: "1.", "2.", etc. or "### 1.", "### 2.")
    step_pattern = re.findall(r"(?:^|\n)\s*(?:###?\s*)?\d+\.\s", content)
    num_steps = len(step_pattern)

    # Also consider sub-sections as complexity signal
    sub_sections = len(re.findall(r"^##\s", content, re.MULTILINE))

    # Content length as secondary signal
    line_count = len([l for l in content.splitlines() if l.strip()])

    if num_steps <= 3 and line_count <= 20 and sub_sections <= 1:
        return "simple"
    elif num_steps >= 6 or line_count >= 60 or sub_sections >= 4:
        return "advanced"
    else:
        return "moderate"


def parse_skill(filepath: Path) -> dict:
    """Parse a single skill .md file into a registry entry."""
    content = filepath.read_text(encoding="utf-8")
    name = filepath.stem

    return {
        "name": name,
        "title": extract_title(content, name),
        "description": extract_description(content),
        "category": infer_category(content, name),
        "has_script": has_script_reference(content),
        "complexity": assess_complexity(content),
    }


def build_categories(skills: list) -> dict:
    """Group skills by category with counts."""
    categories = {}
    for skill in skills:
        cat = skill["category"]
        if cat not in categories:
            categories[cat] = {"count": 0, "skills": []}
        categories[cat]["count"] += 1
        categories[cat]["skills"].append(skill["name"])

    # Sort categories by count descending
    return dict(sorted(categories.items(), key=lambda x: -x[1]["count"]))


def main():
    if not SKILLS_DIR.is_dir():
        print(f"Error: skills directory not found at {SKILLS_DIR}", file=sys.stderr)
        sys.exit(1)

    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)

    # Scan and parse all skill files
    skill_files = sorted(SKILLS_DIR.glob("*.md"))
    if not skill_files:
        print("No .md files found in skills/", file=sys.stderr)
        sys.exit(1)

    skills = [parse_skill(f) for f in skill_files]
    skills.sort(key=lambda s: s["name"])

    # Build category index
    categories = build_categories(skills)

    # Write skills.json
    skills_path = REGISTRY_DIR / "skills.json"
    with open(skills_path, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2, ensure_ascii=False)

    # Write categories.json
    categories_path = REGISTRY_DIR / "categories.json"
    with open(categories_path, "w", encoding="utf-8") as f:
        json.dump(categories, f, indent=2, ensure_ascii=False)

    # Summary
    print(f"Registry built: {len(skills)} skills across {len(categories)} categories")
    print(f"  -> {skills_path}")
    print(f"  -> {categories_path}")
    print()
    for cat, data in categories.items():
        print(f"  {cat}: {data['count']} skills")


if __name__ == "__main__":
    main()
