# /scaffold — Scaffold New Project

Create a new project with standard MirrorDNA structure and patterns.

## Arguments

`/scaffold [name] --type [node|python|script|service|vault-spec]`

## Steps

1. **Create Directory** at `~/repos/[name]`
2. **Generate Files** based on type (src, tests, config, .gitignore, README)
3. **Init Git** with first commit
4. **Set Bus Focus** to new project
5. **Log** to ledger

## Output

```
⟡ Scaffolded: [name]

Type: [type]
Location: ~/repos/[name]
Files: [N] created
Git: initialized
Focus set to: [name]
```
