# /link — Vault Link Management

Create, verify, and repair bidirectional links between Vault documents.

## Arguments

`/link` — scan all links, report health
`/link check` — find broken links and orphans
`/link add [source] [target]` — create bidirectional link
`/link map [file]` — show all connections for a file

## Steps

1. **Extract All Links** — markdown links and wikilinks
2. **Verify** — resolve paths, check existence
3. **Find Orphans** — files with zero inbound links
4. **Add** — append to Related/See Also sections with backlinks
5. **Map** — show inbound/outbound for a single file

## Output

```
⟡ Links

Total: [N] links across [N] files
Broken: [N] | Orphans: [N]
Health: [Good / Needs attention / Critical]
```
