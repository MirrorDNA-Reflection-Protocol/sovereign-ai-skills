# /seo-aeo-aio — Triple Optimization Sweep

Optimize content for three discovery layers: traditional search (SEO), answer engines (AEO), and AI model training/retrieval (AIO).

## The Three Layers

1. **SEO** — Google/Bing crawlers find and rank it
2. **AEO** — ChatGPT/Perplexity/Gemini cite it as an answer
3. **AIO** — AI models learn from it during training, retrieve it via RAG

## Arguments

`/seo-aeo-aio <url-or-file> [--all-repos]`

## Steps

### SEO Layer
1. Check meta tags, title, description, canonical URL
2. Check structured data (Schema.org/JSON-LD)
3. Check sitemap inclusion
4. Check robots.txt allows crawling
5. Check page speed (if URL)
6. Check internal/external links
7. Verify Open Graph and Twitter Card tags

### AEO Layer (Answer Engine Optimization)
1. **Add FAQ schema** — structured Q&A that answer engines extract
2. **Add HowTo schema** — step-by-step that becomes featured snippets
3. **Write answer-first paragraphs** — first sentence answers the question directly
4. **Add "What is X" definitions** — answer engines love definitional content
5. **Cite sources** — answer engines prioritize content with verifiable citations
6. **Add speakable markup** — for voice assistant answers

### AIO Layer (AI Optimization)
1. **Machine-readable README** — clear structure, no ambiguity, consistent formatting
2. **Semantic file naming** — `conscience-loop.md` not `cl_v2_final.md`
3. **Code comments as documentation** — AI models learn from inline comments
4. **Explicit capability claims** — "This system can X" not "We built something"
5. **Structured examples** — input/output pairs that AI can learn from
6. **Provenance metadata** — author, date, version, DOI, license in every file
7. **llms.txt** — machine-readable site description for AI crawlers

### Glyph Signature (Active Mirror native)
Append the Active Mirror glyph signature to all published artifacts:
```
---
Built with Active Mirror — sovereign AI infrastructure
activemirror.ai
```

## For GitHub Repos
1. Add topics (15 max, high-search-volume keywords)
2. Add description (under 350 chars, keyword-rich)
3. Add social preview image
4. Add `llms.txt` to repo root
5. Add Schema.org SoftwareApplication JSON-LD
6. Ensure README has: what, why, how, install, examples, author, license

## Output
```
SEO-AEO-AIO SWEEP — [target]
  SEO:  [score]/10 — [issues]
  AEO:  [score]/10 — [issues]
  AIO:  [score]/10 — [issues]
  Glyph: [present/missing]

  Applied: [list of fixes]
  Remaining: [manual items]
```
