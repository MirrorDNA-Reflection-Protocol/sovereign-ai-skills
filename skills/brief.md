# /brief — Generate Sovereign Briefing

Scan HN, tech news, and crypto signals. Format per the Sovereign Brief pattern.

## Steps

1. **Scan Sources**
Fetch headlines and top stories from:
- Hacker News (top/new)
- Tech news (major announcements)
- Crypto signals (BTC, ETH, SOL prices + major moves)
- AI news (model releases, policy changes)

2. **Filter for Relevance**
Prioritize stories relevant to:
- Sovereign infrastructure / self-hosting
- AI developments (models, APIs, open source)
- Crypto / DeFi / on-chain
- Privacy / security
- Paul's active projects (from bus state)

3. **Check Vault for Context**
```bash
# See what Paul is currently focused on
~/.mirrordna/bin/bus read 2>/dev/null | head -10
```

4. **Format Brief**
```bash
DATE=$(date +%Y-%m-%d)
cat > ~/MirrorDNA-Vault/Content/briefs/sovereign-brief-${DATE}.md << EOF
---
id: BRIEF-${DATE}
title: "Sovereign Brief — ${DATE}"
type: brief
created: $(date -u +%Y-%m-%dT%H:%M:%SZ)
status: active
---

# ⟡ Sovereign Brief — ${DATE}

## Signal
[Top 3-5 stories that matter, with one-line commentary each]

## AI
[AI developments — model releases, benchmarks, policy]

## Crypto
[Market snapshot + notable moves]

## Infrastructure
[Self-hosting, privacy, security news]

## Relevant to Current Work
[Stories that connect to Paul's active projects/interests]

## Action Items
- [ ] [Things worth investigating further]
- [ ] [Opportunities to act on]

---
*Generated via /brief — $(date '+%H:%M')*
EOF
```

5. **Commit**
```bash
cd ~/MirrorDNA-Vault && git add -A && git commit -m "⟡ Sovereign Brief ${DATE} — via Claude Code"
```

## Output

```
⟡ Sovereign Brief — [date]

Signal:
  1. [headline] — [one-line take]
  2. [headline] — [one-line take]
  3. [headline] — [one-line take]

AI: [key development]
Crypto: BTC $[price] | ETH $[price] | [notable move]
Infra: [key story]

Action items: [N]
Saved: ~/MirrorDNA-Vault/Content/briefs/sovereign-brief-[date].md
```
