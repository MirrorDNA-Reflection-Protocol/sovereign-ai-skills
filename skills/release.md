# /release — Create Release

Full release cycle: tag, generate notes, publish via GitHub.

## Arguments

`/release [version]` — e.g., `1.2.0`
`/release [version] --draft` — draft release
`/release [version] --prerelease` — mark as pre-release

## Steps

1. **Verify Clean State** — check for uncommitted changes
2. **Get Last Tag** — `git describe --tags --abbrev=0`
3. **Generate Release Notes** — categorize commits since last tag
4. **Update Version Files** — package.json, pyproject.toml, Cargo.toml
5. **Commit Version Bump**
6. **Create Tag** — `git tag -a "v[version]"`
7. **Push Tag and Commits**
8. **Create GitHub Release** — `gh release create`
9. **Log to Ledger**

## Output

```
⟡ Released: v[version]

Tag: v[version]
Commits: [N] since [last tag]
URL: [github release url]

Release Notes:
  Features: [N]
  Fixes: [N]
  Changes: [N]
```
