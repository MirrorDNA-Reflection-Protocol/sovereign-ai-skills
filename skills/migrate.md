# /migrate — Move Notes Between Vault Layers

Move vault notes between layers (INBOX, ACTIVE, SHIPPED, PARKED, REFERENCE, ARCHIVE) with automatic frontmatter update.

## Arguments

`/migrate <file-or-glob> <target-layer>`

Example: `/migrate 00_INBOX/MirrorGate_spec.md 01_ACTIVE/MirrorGate/`

## Steps

1. Read the source file, preserve YAML frontmatter
2. Update `layer` field in frontmatter to match target
3. Update `moved_date` field to today
4. Move file to target directory
5. Update any `[[wiki-links]]` that reference the old path
6. Report: moved from X to Y, N links updated
