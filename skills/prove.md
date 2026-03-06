# /prove — Generate Proof of Capability

Generate verifiable evidence that a claimed capability actually works. For papers, demos, and credibility.

## Arguments

`/prove <capability>`

Example: `/prove conscience-loop`, `/prove self-healing`, `/prove witness-chain`

## Steps

1. **Identify the claim** — what exactly are we proving?

2. **Design the test** — a reproducible demonstration:
   - For conscience-loop: run DREAM → CALIBRATE → CONSCIENCE → show nudge output
   - For self-healing: kill a service, show MirrorPulse auto-restarts it
   - For witness-chain: show chain integrity, verify hashes
   - For temperature-as-architecture: show same prompt at temp 0.0 vs 0.7
   - For sovereign-infra: show all services running locally, no cloud calls

3. **Execute the test** — capture output as evidence

4. **Generate proof artifact**:
   - Timestamped output log
   - Hash of the evidence (witness chain entry)
   - Screenshot if visual
   - JSON proof object with claim, test, result, evidence_hash

5. **Save proof** to `~/.mirrordna/proofs/PROOF-<capability>-<date>.json`

6. **Register in witness chain** via WITNESS primitive

## Output Format
```
PROOF OF CAPABILITY — [capability]
  Claim: [what we're proving]
  Test: [what we did]
  Result: [VERIFIED / FAILED]
  Evidence: [hash]
  Witness entry: [seq #]
  Artifact: [path]
```
