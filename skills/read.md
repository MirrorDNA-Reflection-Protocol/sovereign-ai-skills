# /read — Follow a Read Path

Load and present a Vault read path — a curated sequence of documents for understanding a topic.

## Arguments

`/read [path-name]`

If no argument, list available read paths. If argument provided, load and present the sequence.

## Steps

### If No Argument — List Paths
1. **Find Read Path Definitions**
```bash
find ~/MirrorDNA-Vault -name "read-path-*.md" -o -name "READ_PATH_*.md" -o -name "*_read_path.md" 2>/dev/null
```

2. **Also Check Index**
```bash
cat ~/MirrorDNA-Vault/read_paths.md 2>/dev/null || echo "No read path index found"
```

3. **List Available**
```
⟡ Available Read Paths:

1. sovereignty — Core identity framework (5 docs)
2. infrastructure — MirrorDNA tech stack (8 docs)
3. [more paths]

Usage: /read sovereignty
```

### If Argument — Load Path
1. **Find Path Definition**
```bash
grep -ril "[path-name]" ~/MirrorDNA-Vault/ 2>/dev/null | head -5
```

2. **Extract Document Sequence**
Read the path definition file. Extract ordered list of documents.

3. **Load Each Document**
For each document in sequence:
- Read the file
- Extract title, summary/first paragraph
- Note connections to next document

4. **Present as Guided Reading**
```
⟡ Read Path: [name]

[1/N] sovereignty-core.md
  "The sovereignty framework establishes..."
  Key concepts: [list]
  → Continues to: sovereignty-practice.md

[2/N] sovereignty-practice.md
  "Applying sovereignty means..."
  Key concepts: [list]
  → Continues to: sovereignty-tools.md

[current position indicator]
```

## Output

```
⟡ Read Path: [name]
Documents: [N] in sequence
Estimated reading: [brief/moderate/deep]

[Present first document, offer to continue]
```
