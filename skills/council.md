# /council — Multi-Perspective Review Council

Spawn 3 parallel review agents with different perspectives to evaluate a document, codebase, architecture, or idea. The council provides brutally honest feedback from multiple angles.

## Arguments

`/council [path-or-topic] [type]`

- `path-or-topic`: File path, directory, or description of what to review
- `type` (optional): `paper`, `code`, `architecture`, `idea`, `product` — defaults to auto-detect

## Steps

### 1. Identify the Target

Read the target document/code. Determine what type of review is needed.

### 2. Spawn 3 Parallel Review Agents

Launch 3 Task agents simultaneously, each with a different reviewer persona:

**For `paper` type:**
- **Academic Reviewer** — Conference peer reviewer (NeurIPS/ICML tier). Checks: novelty, rigor, experimental validity, writing, missing references. Returns: Accept/Weak Accept/Borderline/Weak Reject/Reject.
- **Practitioner Reviewer** — Senior engineer at a top AI lab. Checks: practical relevance, scalability, implementation gaps, competitive positioning. Returns: Would I cite this? Would I use this?
- **Adversarial Reviewer** — Hostile critic. Tries to tear it apart. Checks: is this marketing? Is the evidence real? What's circular? What's decorative? Returns: what survives scrutiny.

**For `code` type:**
- **Security Reviewer** — Red team lead. Checks: injection vectors, auth gaps, data exposure, supply chain, OWASP top 10.
- **Architecture Reviewer** — Principal engineer. Checks: separation of concerns, scalability, coupling, error handling, tech debt.
- **User Reviewer** — End user/developer who has to work with this. Checks: DX, docs, naming, discoverability, footguns.

**For `architecture` type:**
- **Systems Reviewer** — Distributed systems engineer. Checks: failure modes, consistency, latency, observability, recovery.
- **Security Reviewer** — Threat modeler. Checks: attack surface, trust boundaries, data flow, privilege escalation.
- **Product Reviewer** — Technical PM. Checks: does this solve the right problem? What's overengineered? What's missing?

**For `idea` or `product` type:**
- **Bull Case** — Strongest argument FOR. What makes this great? What's the moat?
- **Bear Case** — Strongest argument AGAINST. What kills this? What's the fatal flaw?
- **Operator Case** — Practical next steps. What would it take to make this work? What's the MVP?

### 3. Synthesize Results

After all 3 agents return, produce a synthesis:

1. **Consensus points** — What all 3 agree on (strongest signals)
2. **Divergence** — Where reviewers disagree (interesting tensions)
3. **Survival test** — What claims/code/ideas survive all 3 reviews
4. **Top fixes** — Prioritized list of improvements, ordered by impact

### 4. Report

```
COUNCIL REVIEW — [target name]

Reviewers: [Academic | Practitioner | Adversarial]

| | Reviewer 1 | Reviewer 2 | Reviewer 3 |
|---|---|---|---|
| Score | ... | ... | ... |
| Strongest point | ... | ... | ... |
| Biggest gap | ... | ... | ... |

Consensus:
  - [What all 3 agree on]

What Survives:
  - [Claims/code that hold up under all 3 lenses]

Top Fixes (by impact):
  1. [Most impactful fix]
  2. [Second most impactful]
  3. [Third most impactful]
```

### 5. Write Deliberation File (for Cognitive Dashboard)

After synthesis, write the results to `~/.mirrordna/council/` so the dashboard picks it up:

```bash
mkdir -p ~/.mirrordna/council
```

Write file: `~/.mirrordna/council/DELIB-YYYY-MM-DD-HHMM.md`

```markdown
---
topic: [target name]
type: [paper|code|architecture|idea|product]
reviewers: [Reviewer 1 name, Reviewer 2 name, Reviewer 3 name]
date: [ISO timestamp]
---

# Council: [target name]

## Scores
| | [R1] | [R2] | [R3] |
|---|---|---|---|
| Score | ... | ... | ... |
| Strongest | ... | ... | ... |
| Biggest gap | ... | ... | ... |

## Consensus
- [point 1]
- [point 2]

## What Survives
- [surviving claim/code 1]
- [surviving claim/code 2]

## Top Fixes
1. [fix 1]
2. [fix 2]
3. [fix 3]
```

This file is auto-discovered by the Cognitive Dashboard's Council panel (panel 12).

## Notes

- All 3 reviewers run in parallel (Task agents with subagent_type=general-purpose)
- Each reviewer gets the full document/code — no summaries
- Reviewers are instructed to be brutally honest, not encouraging
- The synthesis is the most valuable part — it's where signal emerges from noise
- For papers: reviewers check related work, methodology, claims vs evidence
- For code: reviewers actually read the implementation, not just the README
- The deliberation file feeds the Cognitive Dashboard — council results show in the terminal UI
