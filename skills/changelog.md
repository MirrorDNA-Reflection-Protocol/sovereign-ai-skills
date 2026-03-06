# /changelog — Generate Changelog

Analyze git history between tags/dates and produce a categorized changelog.

## Arguments

`/changelog` — changes since last tag
`/changelog [tag1..tag2]` — between two tags
`/changelog [date]` — since date
`/changelog --save` — write to CHANGELOG.md

## Steps

1. **Determine Range**
```bash
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
```

2. **Get Commits**
```bash
git log $RANGE --pretty=format:"%h|%s|%an|%ad" --date=short
```

3. **Categorize** — Added, Changed, Fixed, Removed, Refactored, Docs, Tests

4. **Format as Changelog**

5. **If --save, write to CHANGELOG.md and commit**

## Output

```
⟡ Changelog: [range]

## [Unreleased] — [date]

### Added
- [commit] ([hash])

### Fixed
- [commit] ([hash])

Stats: [N] commits, [N] files, [contributors]
```
