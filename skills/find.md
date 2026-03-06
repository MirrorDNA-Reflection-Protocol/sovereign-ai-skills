# /find — Smart Vault Search

Search the Vault by keyword or topic. Searches by layer priority: Canonical → Active → Reference → Archive.

## Arguments

`/find [keyword or topic]`

Required: search term.

## Steps

1. **Search by Layer Priority**
```bash
# Search in priority order
for layer in 01_CANONICAL 02_ACTIVE 03_REFERENCE 04_ARCHIVE 00_INBOX; do
  echo "=== $layer ==="
  grep -ril "[keyword]" ~/MirrorDNA-Vault/$layer/ 2>/dev/null || echo "  (no matches)"
done
```

2. **Search Filenames**
```bash
find ~/MirrorDNA-Vault -name "*[keyword]*" -type f 2>/dev/null
```

3. **Search Frontmatter Tags**
```bash
grep -rl "tags:.*[keyword]" ~/MirrorDNA-Vault/ 2>/dev/null
```

4. **Rank Results**
For each match, extract:
- File path and layer
- Title from frontmatter
- Matching line/context (first 2 matches)
- Last modified date

5. **Present Results**
Order by: layer priority first, then recency within each layer.

## Output

```
⟡ Vault Search: "[keyword]"

Found [N] matches:

CANONICAL (highest priority):
  1. ~/MirrorDNA-Vault/01_CANONICAL/sovereignty.md
     Title: "Sovereignty Framework"
     Match: "...keyword appears in context..."
     Modified: 2026-01-15

ACTIVE:
  2. ~/MirrorDNA-Vault/02_ACTIVE/current-project.md
     Title: "Current Project Spec"
     Match: "...keyword in context..."
     Modified: 2026-01-20

REFERENCE:
  (no matches)

Use `/read [path]` to follow a read path starting from any result.
```
