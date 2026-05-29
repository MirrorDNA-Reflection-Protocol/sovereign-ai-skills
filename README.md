# Sovereign AI Skills

**153 production-tested skill definitions for autonomous AI agent operations -- system governance, self-healing, observability, content pipelines, and lifecycle management.**

[![License: MIT](https://img.shields.io/badge/license-MIT-grey.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-153-0a66c2.svg)](skills/)

---

Sovereign AI Skills is an infrastructure library for running governed AI systems from the command line. Each skill is a structured job profile for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Anthropic's CLI agent) -- not a prompt template, but a complete workflow definition with steps, verification criteria, and output format.

Install the skills, and commands like `/forensic`, `/calibrate`, `/evolve`, and `/council` become available as first-class operations in your agent.

## Architecture

```
+-----------------------------------------------------------------+
|  Operator                                                       |
+-----------------------------------------------------------------+
         |
         v
+-----------------------------------------------------------------+
|  Claude Code + 153 Skills (this repository)                     |
|  /forensic  /calibrate  /evolve  /council  /prove  ...         |
+-----------------------------------------------------------------+
         |
         v
+-----------------------------------------------------------------+
|  Cognitive Kernel (28 primitives)                                |
|                                                                  |
|  15 deterministic (temp 0.0)   identity, search, verify         |
|   6 creative     (temp 0.7)   dream, compose, simulate          |
|   7 blended      (temp 0.3)   conscience, learn, anticipate     |
+-----------------------------------------------------------------+
         |
         v
+-----------------------------------------------------------------+
|  Self-Healing Infrastructure                                     |
|  Detect --> Diagnose --> Heal --> Learn --> Report               |
|  Evolving fix playbook: patterns that work are retained         |
+-----------------------------------------------------------------+
         |
         v
+-----------------------------------------------------------------+
|  Runtime                                                         |
|  Local inference (Ollama)  |  Automation scripts  |  Agents     |
+-----------------------------------------------------------------+
```

## Skill Categories

### System Operations (22 skills)

Infrastructure management, diagnostics, and deployment.

| Skill | Purpose |
|-------|---------|
| `/forensic` | Full 10-layer system scan: services, network, kernel, integrity, infra, deps, vault, security, continuity, drift |
| `/benchmark` | Quantitative performance benchmarks tracked over time |
| `/regression` | Detect performance regressions against baselines |
| `/wire-check` | Verify all AI components are connected end-to-end |
| `/calibrate` | Self-benchmarking with grade (A-F), trend, and recommendations |
| `/drift` | Detect configuration drift across sources of truth |
| `/promote` | Promote script to managed service (LaunchAgent + registry) |
| `/retire` | Gracefully disable a service (stop, archive, update registry) |
| `/health` | Service health check |
| `/smoke` | End-to-end smoke tests |
| `/deploy` | Deploy LaunchAgents |
| `/killswitch` | Emergency stop for all agents |

### Intelligence and Self-Improvement (9 skills)

Autonomous evaluation, adversarial testing, and capability tracking.

| Skill | Purpose |
|-------|---------|
| `/evolve` | Self-improvement cycle: calibrate, identify weaknesses, fix |
| `/adversarial` | Red team self-testing |
| `/prove` | Generate verifiable proof that a capability works |
| `/experiment` | Controlled A/B experiments on system behavior |
| `/council` | Multi-perspective review (architect, critic, operator) |
| `/dream` | Autonomous self-improvement engine |
| `/reflect` | Meta-analysis of own performance |
| `/capability` | System capability matrix with coverage scores |
| `/breakthrough` | Track and generate novel capabilities |

### Governance and Continuity (14 skills)

Session management, handoffs, witness chain, and compliance.

| Skill | Purpose |
|-------|---------|
| `/incident` | Post-mortem generator from failure data |
| `/replay` | Reconstruct sessions from witness chain |
| `/contract` | Work contracts for digital coworkers |
| `/onboard` | Generate context pack for new agents |
| `/handoff` | Write handoff for next agent |
| `/pickup` | Continue from last handoff |
| `/standup` | Morning standup |
| `/sync` | Synchronize state across all clients |
| `/bus` | Memory bus operations |

### Build and Ship (10 skills)

Version control, testing, release management.

| Skill | Purpose |
|-------|---------|
| `/commit` | Smart commit with semantic message |
| `/ship` | Commit, push, and mark complete |
| `/pr` | Create pull request |
| `/release` | Create release |
| `/test` | Run tests |
| `/review` | Review changes |
| `/scaffold` | Scaffold new project |
| `/spec` | Draft specification document |

### Content, Distribution, and Analytics (55 skills)

Content creation, SEO, syndication, growth tracking, and audience analysis across text, video, and social formats. Includes skills for newsletters, carousels, video essays, YouTube SEO, A/B testing, and funnel analysis.

See the full catalog in [`skills/`](skills/).

### Knowledge Management (12 skills)

Vault operations, search, compression, and research.

| Skill | Purpose |
|-------|---------|
| `/find` | Smart vault search |
| `/audit` | Vault health audit |
| `/triage` | Auto-triage inbox |
| `/compress` | Identify compression candidates |
| `/research` | Deep research |
| `/migrate` | Move notes between vault layers |

### Lifecycle (8 skills)

Staleness detection, archival, backup, and process management.

| Skill | Purpose |
|-------|---------|
| `/decay` | Check staleness thresholds |
| `/reaper` | Staleness reaper with auto-archive |
| `/backup` | Vault backup operations |
| `/cognitive` | Cognitive dashboard |

## Key Concepts

**Temperature-as-Architecture.** Each cognitive kernel primitive declares its execution mode -- deterministic, creative, or blended. Temperature is a structural decision made at design time, not a parameter tuned at call time.

**Witness Chain.** SHA-256 hash-chain providing cryptographic provenance for every AI session. Each session links to its predecessor, creating an auditable lineage.

**Conscience Loop.** A feedback cycle -- `DREAM -> CALIBRATE -> CONSCIENCE -> INJECT -> ACT -> WITNESS` -- where the system evaluates its own behavior and adjusts before the next action.

**Self-Healing Playbook.** The infrastructure layer (MirrorPulse) follows a `Detect -> Diagnose -> Heal -> Learn -> Report` pattern. Fix patterns that succeed are retained and reused.

**Compaction Survival.** Distilled checkpoints that survive context window compression, ensuring continuity across long-running agent sessions.

## Installation

```bash
git clone https://github.com/MirrorDNA-Reflection-Protocol/sovereign-ai-skills.git
cd sovereign-ai-skills

# Copy all skills into Claude Code's command directory
cp skills/*.md ~/.claude/commands/

# Skills are now available as /skill-name in Claude Code
```

Most skills reference a `~/.mirrordna/` directory structure for state, configuration, and logs. The skill patterns and workflow definitions are transferable to any agent infrastructure -- adapt the paths to your environment.

### Automated Installation

```bash
./install.sh
```

The install script copies skills to the Claude Code commands directory and validates the installation.

## Repository Structure

```
sovereign-ai-skills/
  skills/          153 skill definitions (.md files)
  scripts/         Build and registry tooling
  registry/        Skill metadata (categories.json, skills.json)
  marketplace/     Public skill index
  docs/            Additional documentation
  llms.txt         Machine-readable project summary
  install.sh       Automated installer
```

## Compliance

See [COMPLIANCE.md](COMPLIANCE.md) for control mappings against the EU AI Act, SOC 2 Type II, and ISO 27001:2022.

## Security

To report a vulnerability, see [SECURITY.md](SECURITY.md). Do not use public GitHub issues for security reports.

## License

MIT

---

Built by [Active Mirror](https://activemirror.ai) -- governed AI for institutional work.
