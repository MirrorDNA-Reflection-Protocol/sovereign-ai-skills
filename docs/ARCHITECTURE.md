# Architecture — How the Skill System Works

## Skill Anatomy

Every skill in this library follows the same pattern:

```markdown
# /skill-name — One-Line Description

Context about when and why to use this skill.

## Arguments
What parameters the skill accepts.

## Steps
1. Concrete bash commands or actions
2. Each step has verification
3. Results feed into the next step

## Output Format
Exactly what the output looks like.
```

## Skill Categories by Job Function

Think of each skill as a **job profile** — the complete description of a role in an AI operating system:

| Job Function | Example Skills | Human Equivalent |
|-------------|---------------|-----------------|
| SRE | `/forensic`, `/pulse`, `/smoke` | Site Reliability Engineer |
| DevOps | `/deploy`, `/promote`, `/retire` | DevOps Engineer |
| Security | `/adversarial`, `/cert`, `/guardian` | Security Engineer |
| QA | `/benchmark`, `/regression`, `/test` | Quality Assurance |
| Research | `/experiment`, `/prove`, `/paper` | Research Scientist |
| Product | `/capability`, `/breakthrough`, `/evolve` | Product Manager |
| Content | `/draft`, `/storytell`, `/thread` | Content Creator |
| Analytics | `/analytics`, `/growth`, `/funnel` | Data Analyst |
| Ops | `/incident`, `/replay`, `/onboard` | Operations Manager |

## The Cognitive Kernel

Skills invoke primitives on the cognitive kernel. Each primitive has a **mode**:

- **Deterministic** (temp 0.0): `EVALUATE`, `SEARCH`, `VERIFY_IDENTITY`, `RETRIEVE`, `REFLECT`, `LINK_NODE`, `PERMISSION_CHECK`, `HALT`, `MESH`, `REMEMBER`, `TEMPORAL_RETRIEVE`, `CALIBRATE`, `WITNESS`, `VERIFY_CHAIN`, `OBSERVE` — same input always produces same output
- **Creative** (temp 0.7): `REASON`, `SIMULATE`, `EXPAND_GRAPH`, `DREAM`, `COMPOSE`, `TRANSFORM` — exploration and generation
- **Blended** (temp 0.3): `CONSCIENCE`, `NUDGE`, `LEARN`, `ANTICIPATE`, `EMPATHIZE`, `INTEND`, `OBSERVE` — informed by both structure and intuition

This isn't a parameter choice. It's **architecture** — the system knows which cognitive tasks need precision and which need exploration.

## Self-Improvement Loop

```
/calibrate → identifies weaknesses
/evolve → proposes and applies fixes
/benchmark → measures improvement
/regression → catches degradation
/breakthrough → tracks novelty
/prove → generates evidence
/paper → publishes findings
```

This loop runs autonomously. The system gets better without being asked.
