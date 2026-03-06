# /experiment — Run Controlled Experiments

Design and run A/B experiments on system behavior. Track hypothesis, method, results.

## Arguments

`/experiment <hypothesis>`

Example: `/experiment "blended mode at 0.3 produces better conscience nudges than 0.5"`

## Steps

1. **Define experiment**:
   - Hypothesis: what we expect
   - Control: current behavior
   - Treatment: proposed change
   - Metric: how we measure success
   - Duration: how long to run

2. **Set up experiment**:
   - Create experiment record in `~/.mirrordna/experiments/EXP-<date>-<seq>.json`
   - Configure the treatment (e.g., change a temperature, swap a prompt)
   - Ensure we can measure the metric

3. **Run both conditions**:
   - Control: run with current settings, capture output
   - Treatment: run with changed settings, capture output

4. **Compare results**:
   - Quantitative: metric values for control vs treatment
   - Qualitative: output quality assessment

5. **Record results** in experiment file

6. **Decision**: adopt treatment, reject, or extend experiment

## Safety
- Never experiment on production services without Paul's approval
- Kernel experiments use the SIMULATE primitive (sandboxed)
- Always revert treatment if results are worse

## Output Format
```
EXPERIMENT — EXP-[date]-[seq]
  Hypothesis: [statement]
  Control: [description] → [metric value]
  Treatment: [description] → [metric value]
  Result: [CONFIRMED / REJECTED / INCONCLUSIVE]
  Decision: [adopt / reject / extend]
```
