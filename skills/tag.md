# /tag — Tag Management

Manage Vault tags per Part XXIV. List tags, check for duplicates, add to registry.

## Arguments

`/tag` — List all tags and counts
`/tag check` — Check for duplicates and inconsistencies
`/tag add [tag-name]` — Register a new tag
`/tag find [tag-name]` — Find all files with a tag

## Steps

### List Tags
1. **Extract All Tags from Frontmatter**
```bash
grep -rh "^tags:" ~/MirrorDNA-Vault/ 2>/dev/null | sed 's/tags://g' | tr ',' '\n' | tr -d '[]"' | sed 's/^ *//;s/ *$//' | sort | uniq -c | sort -rn
```

2. **Check Tag Registry**
```bash
cat ~/MirrorDNA-Vault/tag_registry.md 2>/dev/null || echo "No tag registry found"
```

### Check for Issues
1. **Find Duplicate/Similar Tags**
Look for:
- Case variants (e.g., `Sovereignty` vs `sovereignty`)
- Plural variants (e.g., `spec` vs `specs`)
- Hyphen variants (e.g., `mirror-dna` vs `mirrordna`)

2. **Find Unregistered Tags**
Tags used in files but not in the registry.

3. **Find Unused Registered Tags**
Tags in registry but used nowhere.

### Add Tag
1. **Check if Exists**
```bash
grep -i "[tag-name]" ~/MirrorDNA-Vault/tag_registry.md 2>/dev/null
```

2. **Add to Registry**
```bash
echo "- **[tag-name]**: [auto-generated description]" >> ~/MirrorDNA-Vault/tag_registry.md
```

### Find by Tag
1. **Search Frontmatter**
```bash
grep -rl "tags:.*[tag-name]" ~/MirrorDNA-Vault/ 2>/dev/null
```

## Output

```
⟡ Tag Report

Top Tags:
  sovereignty (12 files)
  infrastructure (8 files)
  spec (6 files)
  active-project (5 files)

Issues:
  ⚠ Case mismatch: "Sovereignty" vs "sovereignty" (3 files)
  ⚠ Unregistered: "new-tag" used in 2 files

Total: [N] unique tags across [N] files
Registry: [N] registered tags
```
