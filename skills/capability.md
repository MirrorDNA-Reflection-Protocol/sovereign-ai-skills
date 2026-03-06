# /capability — System Capability Matrix

Generate a complete matrix of what the system can and cannot do. Find capability gaps.

## Steps

1. **Enumerate capabilities by domain**:

   **Cognition** (kernel primitives):
   - Identity: LOAD_IDENTITY, VERIFY_IDENTITY, INTEND
   - Knowledge: RETRIEVE, EXPAND_GRAPH, LINK_NODE, SEARCH, MESH
   - Reasoning: REASON, EVALUATE, REFLECT, SIMULATE, ANTICIPATE
   - Learning: LEARN, DREAM, OBSERVE, CALIBRATE, REMEMBER, TEMPORAL_RETRIEVE
   - Creative: COMPOSE, TRANSFORM
   - Safety: PERMISSION_CHECK, HALT, CONSCIENCE, NUDGE, WITNESS, VERIFY_CHAIN
   - Social: EMPATHIZE

   **Infrastructure** (LaunchAgents):
   - Monitoring, healing, heartbeat, sentinels, reapers, snapshots

   **Content** (skills):
   - Create, publish, distribute, analyze, optimize

   **Devices** (mesh):
   - OnePlus, Pixel, Red Mac, MacBook Air

2. **Rate each capability**:
   - `shipped`: working in production
   - `wired`: exists but not battle-tested
   - `stub`: skeleton only
   - `missing`: doesn't exist yet

3. **Identify strategic gaps**: what's the highest-value missing capability?

4. **Write matrix** to `~/.mirrordna/health/capability_matrix.json`

## Output Format
```
CAPABILITY MATRIX — [date]
  Domain          Shipped  Wired  Stub  Missing  Coverage
  Cognition       22       4      2     0        96%
  Infrastructure  35       8      3     2        90%
  Content         25       10     5     3        80%
  Devices         3        1      0     1        75%
  Security        5        2      1     3        64%

  Top gaps: [list 5 highest-value missing capabilities]
```
