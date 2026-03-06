# /spec — Draft a New Spec Document

Create a scaffolded spec with frontmatter, sections, and verification checklist.

## Arguments

`/spec [name]`

Required: spec name/title.

## Steps

1. **Generate Metadata**
```bash
ID="SPEC-$(date +%Y%m%d)-$(date +%H%M)"
FILENAME="spec-$(echo '[name]' | tr ' ' '-' | tr '[:upper:]' '[:lower:]').md"
```

2. **Create Spec**
```bash
cat > ~/MirrorDNA-Vault/02_ACTIVE/$FILENAME << EOF
---
id: $ID
title: "[name]"
type: spec
layer: active
created: $(date -u +%Y-%m-%dT%H:%M:%SZ)
author: Paul Desai
status: draft
version: 0.1
tags: [spec]
---

# ⟡ SPEC: [Name]

## Overview
[What this spec defines and why it exists]

## Motivation
[Why this is needed — problem statement]

## Requirements
### Must Have
- [ ] [Requirement 1]
- [ ] [Requirement 2]

### Should Have
- [ ] [Requirement 3]

### Nice to Have
- [ ] [Requirement 4]

## Design
### Architecture
[High-level design]

### Components
[Key components and their roles]

### Data Flow
[How data moves through the system]

## Implementation Plan
1. [Phase 1]
2. [Phase 2]
3. [Phase 3]

## Constraints
- [Technical constraints]
- [Resource constraints]
- [Timeline constraints]

## Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Plan] |

## Verification Checklist
- [ ] Requirements are testable
- [ ] Design covers all requirements
- [ ] Implementation plan is actionable
- [ ] Risks are identified and mitigated
- [ ] Reviewed by Paul

## Changelog
- $(date +%Y-%m-%d): Initial draft (claude_code)

---
*Generated via /spec*
EOF
```

3. **Commit**
```bash
cd ~/MirrorDNA-Vault && git add -A && git commit -m "⟡ Spec: [name] — via Claude Code"
```

## Output

```
⟡ Spec Created

Name: [name]
ID: SPEC-20260127-1430
File: ~/MirrorDNA-Vault/02_ACTIVE/spec-[name].md
Status: Draft v0.1

Sections scaffolded: Overview, Motivation, Requirements, Design,
  Implementation Plan, Constraints, Risks, Verification

Fill in the sections and run `/audit` to verify completeness.
```
