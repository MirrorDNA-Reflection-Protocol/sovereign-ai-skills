# /glossary — Vault Glossary Management

Look up or add glossary terms for the MirrorDNA vocabulary.

## Arguments

`/glossary [term]` — Look up a term
`/glossary add [term]: [definition]` — Add a new term

## Steps

### Look Up Term
1. **Find Glossary File**
```bash
GLOSSARY=$(find ~/MirrorDNA-Vault -name "glossary*" -o -name "Glossary*" -o -name "GLOSSARY*" | head -1)
echo "$GLOSSARY"
```

2. **Search for Term**
```bash
grep -i -A 3 "[term]" "$GLOSSARY" 2>/dev/null
```

3. **Also Search Vault for Usage**
```bash
grep -ril "[term]" ~/MirrorDNA-Vault/01_CANONICAL/ ~/MirrorDNA-Vault/02_ACTIVE/ 2>/dev/null | head -5
```

4. **Present Definition + Context**
```
⟡ Glossary: [term]

Definition: [from glossary]
Also known as: [aliases if any]

Used in:
  - [file1.md] — "[context snippet]"
  - [file2.md] — "[context snippet]"
```

### Add Term
1. **Check for Duplicates**
```bash
grep -i "^## [term]" "$GLOSSARY" 2>/dev/null || grep -i "^- \*\*[term]\*\*" "$GLOSSARY" 2>/dev/null
```

2. **Append to Glossary**
```bash
cat >> "$GLOSSARY" << EOF

## [term]
[definition]
*Added: $(date +%Y-%m-%d) by claude_code*
EOF
```

3. **Commit**
```bash
cd ~/MirrorDNA-Vault && git add -A && git commit -m "⟡ Glossary: added [term] — via Claude Code"
```

## Output

```
⟡ Glossary Updated

Added: [term]
Definition: [definition]
File: [glossary path]
```
