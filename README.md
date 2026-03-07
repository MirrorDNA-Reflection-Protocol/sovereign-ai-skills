# Sovereign AI Skills — 144 Claude Code Commands for Autonomous AI Operations

A complete skill library for running a sovereign AI operating system from the command line. Built by [Paul Desai](https://activemirror.ai) as part of the [Active Mirror](https://activemirror.ai) project — a sovereign AI infrastructure running entirely on a Mac Mini M4 with zero cloud dependencies.

**144 skills. 184 backing scripts. 83 automated agents. One machine.**

## What This Is

Every skill is a `/command` for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Anthropic's CLI agent). Drop them in `~/.claude/commands/` and they become invocable with `/skill-name`.

These aren't toy prompts. Each skill is a job profile — a complete workflow with steps, verification, and output format. They represent every job a sovereign AI system needs to do, organized by domain:

## Skill Categories

### System Operations (22 skills)
| Skill | What it does |
|-------|-------------|
| `/forensic` | Full 10-layer deep system scan (services, network, kernel, integrity, infra, deps, vault, security, continuity, drift) |
| `/benchmark` | Quantitative performance benchmarks tracked over time |
| `/regression` | Detect performance regressions against baselines |
| `/wire-check` | Verify all AI components are connected end-to-end |
| `/calibrate` | Self-benchmarking with grade (A-F), trend, and recommendations |
| `/drift` | Detect configuration drift across all sources of truth |
| `/promote` | Promote script to managed service (LaunchAgent + registry) in one step |
| `/retire` | Gracefully disable a service (stop, archive, update registry) |
| `/device` | Device mesh status dashboard |
| `/cert` | SSL certificate expiry monitor |
| `/inventory` | Complete system inventory (scripts, agents, skills, ports, repos, models) |
| `/cost` | API spend and resource tracking |
| `/dependency` | Package and vulnerability audit (brew, pip, npm) |
| `/health` | Service health check |
| `/status` | Quick status (bus, inbox, git, queues) |
| `/pulse` | Self-healing infrastructure check |
| `/smoke` | End-to-end smoke tests |
| `/services` | Service management |
| `/deploy` | Deploy LaunchAgents |
| `/killswitch` | Emergency stop all agents |
| `/emergency` | Emergency triage protocol |
| `/network` | Network diagnostics |

### Intelligence & Self-Improvement (9 skills)
| Skill | What it does |
|-------|-------------|
| `/evolve` | Self-improvement cycle: calibrate, identify weaknesses, fix |
| `/breakthrough` | Track and generate novel capabilities |
| `/capability` | System capability matrix with coverage scores |
| `/prove` | Generate verifiable proof that a capability works |
| `/experiment` | Controlled A/B experiments on system behavior |
| `/adversarial` | Red team self-testing |
| `/dream` | Run the Dream Engine (autonomous self-improvement) |
| `/reflect` | Meta-analysis of own performance |
| `/council` | Multi-perspective review (architect, critic, operator) |

### Build & Ship (10 skills)
| Skill | What it does |
|-------|-------------|
| `/commit` | Smart commit with semantic message |
| `/ship` | Commit, push, and mark complete |
| `/pr` | Create pull request |
| `/release` | Create release |
| `/scaffold` | Scaffold new project |
| `/test` | Run tests |
| `/review` | Review changes |
| `/factory` | Visual orchestration demo |
| `/swarm` | Multi-agent swarm coordination |
| `/spec` | Draft specification document |

### Content Creation (18 skills)
| Skill | What it does |
|-------|-------------|
| `/draft` | Draft content for publishing |
| `/paper` | Generate research paper from system capabilities |
| `/storytell` | Narrative content generator |
| `/hook` | Generate viral video hooks |
| `/headline` | Generate headlines and titles |
| `/cta` | Generate call-to-action variants |
| `/idea` | Generate content ideas |
| `/carousel` | Social media carousel |
| `/quote-card` | Quotable image cards |
| `/behind-scenes` | Behind-the-scenes content |
| `/evergreen` | Create evergreen content |
| `/comparison` | Create comparison content |
| `/challenge` | Coding challenge content |
| `/newsletter` | Weekly newsletter |
| `/community-post` | YouTube community post |
| `/thread` | Turn build log into social thread |
| `/note` | Quick capture to inbox |
| `/brief` | Sovereign briefing generator |

### Video Production (10 skills)
| Skill | What it does |
|-------|-------------|
| `/daily-video` | Compile daily build log video |
| `/weekly-video` | Weekly recap video |
| `/shorts` | Generate YouTube Shorts from recordings |
| `/clip` | AI-powered highlight clipper |
| `/timelapse` | Coding timelapse |
| `/video-essay` | AI-narrated video essay |
| `/podcast` | Extract podcast audio |
| `/tutorial` | Extract tutorial from build log |
| `/stack-video` | Generate "My Stack" video |
| `/endscreen` | Optimize end screens |

### Distribution & SEO (15 skills)
| Skill | What it does |
|-------|-------------|
| `/auto-publish` | Syndicate content to all platforms |
| `/distribution` | Full distribution pipeline |
| `/launch` | Content launch sequence |
| `/drip` | Drip content publisher |
| `/beacon` | Manage blog |
| `/seo-syndication` | SEO and content syndication |
| `/repurpose` | Repurpose content across formats |
| `/remix` | Remix old content |
| `/schedule` | Optimal content schedule |
| `/content-calendar` | Content calendar management |
| `/sitemap` | Regenerate sitemaps |
| `/schema` | Add structured data / Schema.org |
| `/meta` | Optimize page meta tags |
| `/youtube-seo` | AI-native YouTube SEO |
| `/og-image` | Generate Open Graph images |

### Analytics & Growth (12 skills)
| Skill | What it does |
|-------|-------------|
| `/analytics` | Cross-platform analytics |
| `/growth` | Growth metrics dashboard |
| `/velocity` | Content velocity tracker |
| `/funnel` | Content funnel analysis |
| `/engagement` | Engagement booster |
| `/ab-test` | A/B test video titles and thumbnails |
| `/viral-audit` | Viral readiness audit |
| `/trending` | Find trending topics |
| `/niche-down` | Niche analysis and positioning |
| `/audience` | Audience research and personas |
| `/compete` | Analyze competitor channels |
| `/hashtag` | Research optimal hashtags |

### Knowledge Management (12 skills)
| Skill | What it does |
|-------|-------------|
| `/find` | Smart vault search |
| `/read` | Follow a guided read path |
| `/audit` | Vault health audit |
| `/triage` | Auto-triage inbox |
| `/compress` | Identify compression candidates |
| `/link` | Vault link management |
| `/tag` | Tag management |
| `/glossary` | Glossary management |
| `/migrate` | Move notes between vault layers |
| `/focus` | Set current project focus |
| `/inbox-zero` | Clear all pending items |
| `/research` | Deep research |

### Governance & Continuity (14 skills)
| Skill | What it does |
|-------|-------------|
| `/incident` | Post-mortem generator from failure data |
| `/replay` | Reconstruct sessions from witness chain |
| `/contract` | Work contracts for digital coworkers |
| `/onboard` | Generate context pack for new agents |
| `/handoff` | Write handoff for next agent |
| `/pickup` | Continue from last handoff |
| `/standup` | Morning standup |
| `/overnight` | Queue background agent tasks |
| `/signal` | Send notification via sovereign notification service |
| `/morning-push` | Send morning briefing to devices |
| `/phone-pull` | Pull and triage files from mobile |
| `/sync` | Synchronize state across all clients |
| `/bus` | Memory bus operations |
| `/history` | Session history |

### Branding & Visibility (11 skills)
| Skill | What it does |
|-------|-------------|
| `/brand` | Brand consistency checker |
| `/collab` | Find collaboration opportunities |
| `/backlink` | Backlink strategy |
| `/milestone` | Celebrate and share milestones |
| `/recap` | Weekly/monthly content recap |
| `/changelog` | Generate changelog |
| `/thumbnail` | AI-generate video thumbnails |
| `/demo` | Mobile app demo orchestration |
| `/snapshot` | System snapshot |
| `/optimize` | Full content optimization sweep |
| `/guardian` | Mirror Guardian integrity check |

### Lifecycle (8 skills)
| Skill | What it does |
|-------|-------------|
| `/decay` | Check staleness thresholds |
| `/reaper` | Staleness reaper (auto-archive) |
| `/backup` | Vault backup operations |
| `/logs` | View service logs |
| `/ffmpeg-reaper` | Kill zombie FFmpeg processes |
| `/cognitive` | Cognitive dashboard |
| `/research-agents` | Run intelligence sweep |
| `/release` | Create release |

## The Architecture Behind It

These skills are the interface layer of a sovereign AI stack:

```
You (human)
  |
  v
Claude Code + 141 Skills (this repo)
  |
  v
Cognitive Kernel (28 primitives, temperature-as-architecture)
  |-- 15 deterministic (temp 0.0): identity, search, verify
  |-- 6 creative (temp 0.7): dream, compose, simulate
  |-- 7 blended (temp 0.3): conscience, learn, anticipate
  |
  v
14 Substrates (conscience, witness, dream, calibrate, ...)
  |
  v
Self-Healing Infrastructure (MirrorPulse)
  |-- Detect -> Diagnose -> Heal -> Learn -> Report
  |-- Self-learning playbook (evolves fix patterns)
  |
  v
184 Scripts + 83 LaunchAgents + 5 Ollama Models
  |
  v
Mac Mini M4 (24GB, sovereign, no cloud required)
```

### Novel Concepts

- **Temperature-as-Architecture**: Each kernel primitive declares its mode (deterministic/creative/blended). Temperature isn't a parameter — it's a structural decision.
- **Conscience Loop**: `DREAM -> CALIBRATE -> CONSCIENCE -> INJECT -> ACT -> WITNESS` — the system evaluates its own behavior and nudges itself.
- **Witness Chain**: Cryptographic SHA256 hash-chain providing provenance for every AI session.
- **Compaction Survival**: Distill checkpoints that survive context window compression.
- **Self-Healing Playbook**: MirrorPulse learns which fixes work and evolves its repair patterns.

## Installation

```bash
# Clone
git clone https://github.com/MirrorDNA-Reflection-Protocol/sovereign-ai-skills.git

# Copy skills to Claude Code
cp sovereign-ai-skills/skills/*.md ~/.claude/commands/

# Now you can use /forensic, /benchmark, /evolve, etc. in Claude Code
```

Most skills assume a MirrorDNA-style directory structure at `~/.mirrordna/`. Adapt paths for your setup. The skill patterns are transferable to any sovereign AI infrastructure.

## Who Built This

**Paul Desai** — Building sovereign AI infrastructure at [Active Mirror](https://activemirror.ai). 8 published papers. 57 repos. Zero cloud dependencies.

- [activemirror.ai](https://activemirror.ai) — Main site
- [beacon.activemirror.ai](https://beacon.activemirror.ai) — Blog
- [Publications](https://github.com/MirrorDNA-Reflection-Protocol/publications)

## License

MIT
