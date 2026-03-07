# /glyph — AI-Native Signature & Provenance Mark

Apply the Active Mirror glyph signature to artifacts. The glyph is our machine-readable + human-readable identity mark — it goes on everything we publish.

## The Glyph System

Three layers of identity marking:

### 1. Human-Readable Glyph
```
--- Built with Active Mirror | activemirror.ai
```
Goes at the bottom of: social posts, blog articles, README files, papers, thread endings.

### 2. Machine-Readable Provenance (JSON-LD)
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Active Mirror",
  "author": {"@type": "Person", "name": "Paul Desai", "url": "https://activemirror.ai"},
  "applicationCategory": "Sovereign AI Infrastructure",
  "operatingSystem": "macOS",
  "url": "https://activemirror.ai"
}
```
Embedded in HTML pages, GitHub README, llms.txt.

### 3. Witness Hash (Cryptographic)
```
witness: sha256:<hash> | seq:<N> | chain:intact
```
Optional. Added to papers, proofs, and high-value artifacts. Links to the witness chain.

## Arguments

`/glyph <target> [--all-repos] [--type human|machine|witness|all]`

## Steps

1. **For a file**: append human-readable glyph signature at the bottom
2. **For a repo**: add glyph to README.md footer + JSON-LD to any HTML
3. **For --all-repos**: scan all public repos, add glyph where missing
4. **For --type witness**: also record in witness chain via WITNESS primitive

## Output Format
```
GLYPH APPLIED — [target]
  Human: [added/already present]
  Machine: [added/already present]
  Witness: [recorded seq #N / skipped]
```
