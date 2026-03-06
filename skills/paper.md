# /paper — Generate Research Paper from System Capabilities

Turn shipped capabilities into publishable research artifacts.

## Arguments

`/paper <topic> [--format arxiv|zenodo|blog]`

## Steps

1. **Read FACTS.md** — mandatory before any publishable writing
```bash
cat ~/.mirrordna/FACTS.md
```

2. **Gather evidence** from the system:
   - SHIPLOG entries related to the topic
   - Benchmark data from `~/.mirrordna/health/benchmarks.jsonl`
   - Proof artifacts from `~/.mirrordna/proofs/`
   - Witness chain entries as provenance
   - Calibration data as performance evidence

3. **Draft paper structure**:
   - Abstract (what we built, why it matters)
   - Architecture (how it works — from actual code, not memory)
   - Evaluation (benchmarks, metrics — from actual data)
   - Related work (what exists, how ours differs)
   - Conclusion

4. **Write draft** to `~/MirrorDNA-Vault/Papers/<topic>_draft.md`

5. **Run verification**
```bash
python3 ~/.mirrordna/scripts/verify_claims.py ~/MirrorDNA-Vault/Papers/<topic>_draft.md
```

6. **Fix any flagged claims**

7. **DO NOT PUBLISH** — papers require Paul's explicit approval

## Output Format
```
PAPER DRAFT — [topic]
  Format: [arxiv|zenodo|blog]
  Claims: [N] verified, [N] flagged
  Path: ~/MirrorDNA-Vault/Papers/[topic]_draft.md
  Status: DRAFT — awaiting Paul's review
```
