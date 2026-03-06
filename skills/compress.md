# /compress — Identify Compression Candidates

Find version chains, topic clusters, and redundant notes in the Vault. Draft compression nodes to consolidate.

## Arguments

`/compress [layer] [--execute]`

Default: scan all layers, report only. With `--execute`, create compression nodes.

## Steps

1. **Scan for Version Chains**
```bash
# Find files with version suffixes (v1, v2, _old, _new, _draft, _final)
find ~/MirrorDNA-Vault -name "*v[0-9]*" -o -name "*_old*" -o -name "*_new*" -o -name "*_draft*" -o -name "*_final*" 2>/dev/null
```

2. **Scan for Topic Clusters**
Read file titles and tags across layers. Identify groups of 3+ files covering the same topic.

3. **Scan for Near-Duplicates**
Check for files with:
- Same title, different locations
- >80% content overlap
- Same tags/topics but different layers

4. **Score Candidates**
| Criterion | Score |
|-----------|-------|
| Version chain >2 files | HIGH |
| Topic cluster >3 files | MEDIUM |
| Near-duplicate pair | HIGH |
| Same-tag cluster >5 | LOW |

5. **Draft Compression Nodes** (if --execute)
For each HIGH candidate:
```bash
cat > ~/MirrorDNA-Vault/[layer]/[compressed-name].md << EOF
---
id: [new-id]
title: "[Compressed topic]"
layer: [layer]
created: $(date +%Y-%m-%d)
compressed_from: [list of source files]
status: active
---
# [Topic] — Compressed Node

[Merged content from all source files]

## Source Files
[List original files with dates]

## Compression Notes
[What was merged, what was dropped, why]
EOF
```

6. **Move Originals to Archive**
```bash
for file in [source-files]; do
  mv "$file" ~/MirrorDNA-Vault/04_ARCHIVE/compressed/
done
```

## Output

```
⟡ Compression Analysis

Version Chains: [N] found
  - sovereignty-v1.md → sovereignty-v2.md → sovereignty-v3.md
  - [more chains]

Topic Clusters: [N] found
  - "inference" (4 files across Active/Reference)
  - [more clusters]

Near-Duplicates: [N] found
  - file-a.md ≈ file-b.md (92% overlap)

Recommended: [N] compressions would reduce [X] files to [Y]
Run `/compress --execute` to create compression nodes.
```
