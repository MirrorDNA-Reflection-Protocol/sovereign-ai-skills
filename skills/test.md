# /test — Run Tests

Auto-detect test framework, run suite, report pass/fail, suggest fixes for failures.

## Arguments

`/test [path]` — run tests for a specific file/directory
`/test` — detect and run all tests for current project
`/test --coverage` — include coverage report

## Steps

1. **Detect Framework**
```bash
ls package.json pytest.ini setup.cfg pyproject.toml Cargo.toml go.mod Makefile 2>/dev/null
```

| File | Command |
|------|---------|
| package.json (jest/vitest) | `npm test` |
| pytest.ini / pyproject.toml | `pytest -v` |
| Cargo.toml | `cargo test` |
| go.mod | `go test ./...` |
| Makefile | `make test` |

2. **Check Bus for Focused Project**
```bash
~/.mirrordna/bin/bus read 2>/dev/null | grep -i focus
```

3. **Run Tests**
```bash
[framework-specific command] 2>&1
```

4. **Parse Results** — extract passed/failed/skipped counts and failure details

5. **If Failures** — read test file + source, identify mismatch, suggest fix

## Output

```
⟡ Tests: [project]

Framework: [detected]
Results: [N] passed, [N] failed, [N] skipped

Failures:
  ✗ test_name (file:line)
    Expected: [value]
    Got: [value]
    Fix: [suggestion]
```
