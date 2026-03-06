# /contract — Create Work Contract for Digital Coworkers

Create, list, or manage typed work contracts for the digital coworker runtime.

## Arguments

`/contract create <objective> --assign <role> [--budget N] [--handoff <role>]`
`/contract list [--status queued|active|completed]`
`/contract status <contract_id>`

## Steps

1. **Create**: Generate a WorkContract JSON with:
   - contract_id (uuid)
   - type (build_module, review, verify, deploy, architect)
   - owner: Paul
   - assigned_to: architect|builder|critic|verifier|operator
   - objective
   - constraints (time_budget, token_budget, allowed_tools)
   - success_criteria
   - handoff_to (next role in chain)
   - status: queued

2. **Save** to `~/MirrorDNA-Vault/01_ACTIVE/DigitalCoworkers/runtime/contracts/`

3. **List**: Read contracts index, filter by status, show summary table

4. **Status**: Read specific contract, show progress and handoff chain

## Contract Chain Pattern
```
Paul intent → Architect (scope) → Builder (implement) → Critic (review) → Verifier (test) → Operator (deploy)
```
