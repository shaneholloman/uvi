# Linting Strategy Guide for UVI Development

## Overview

This guide documents our dual-linter approach using Ruff as our primary linter and Pylint as a secondary linter. While Ruff is fast and catches most issues, Pylint provides additional checks that complement Ruff's capabilities.

## Linter Configuration

### Ruff Configuration

Our Ruff settings in `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py39"
line-length = 120
fix = true

[tool.ruff.lint]
select = [
  # flake8-2020
  "YTT",
  # flake8-bandit
  "S",
  # flake8-bugbear
  "B",
  # flake8-builtins
  "A",
  # flake8-comprehensions
  "C4",
  # flake8-debugger
  "T10",
  # flake8-simplify
  "SIM",
  # isort
  "I",
  # mccabe
  "C90",
  # pycodestyle
  "E", "W",
  # pyflakes
  "F",
  # pygrep-hooks
  "PGH",
  # pyupgrade
  "UP",
  # ruff
  "RUF",
  # tryceratops
  "TRY",
]
ignore = [
  # LineTooLong
  "E501",
  # DoNotAssignLambda
  "E731",
]
```

### Pylint Configuration

Our minimal `.pylintrc`:

```ini
[format]
max-line-length=120
```

## Running Linters

### Fast Development Checks (Ruff)

```bash
# Check code
ruff check .

# Fix auto-fixable issues
ruff check --fix .
```

### Deep Analysis (Pylint)

```bash
# Run on specific files
pylint uvi/cli.py

# Run on whole package
pylint uvi
```

### Pre-commit Integration

Our `.pre-commit-config.yaml` runs both:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: "v0.6.3"
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  - repo: https://github.com/PyCQA/pylint
    rev: "v3.0.3"
    hooks:
      - id: pylint
```

## Linting Strategy

### Why Both Linters?

1. **Ruff** (Primary Linter)

   - Extremely fast execution
   - Catches most common issues
   - Auto-fixes many problems
   - Used during active development

2. **Pylint** (Secondary Linter)
   - More thorough analysis
   - Catches complex issues
   - Better type checking
   - Run before commits/PRs

### Common Issues Unique to Each

#### Ruff Catches

- Import sorting
- Simple code style issues
- Basic type annotations
- Common security issues
- Unused imports

#### Pylint Catches

- Complex code flows
- Deeper variable usage analysis
- Advanced type checking
- Possible design problems
- Documentation completeness

## Best Practices

1. **Development Workflow**

   - Run Ruff frequently during development
   - Use Ruff's auto-fix capability
   - Run Pylint before committing
   - Address Pylint warnings thoughtfully

2. **Issue Resolution**

   - Fix Ruff issues immediately (they're usually straightforward)
   - Review Pylint warnings carefully (they might indicate design issues)
   - Document any necessary linter suppressions

3. **Configuration Management**
   - Keep Ruff rules up to date
   - Minimize Pylint suppressions
   - Document why rules are disabled

## CI Integration

Both linters run in CI:

1. Ruff runs first (fast feedback)
2. Pylint runs after (deeper analysis)
3. Both must pass for PR approval

## Trade-offs and Decisions

### Why Keep Pylint?

- Catches issues Ruff misses
- Better for complex code analysis
- Stronger typing checks
- More thorough documentation checks

### Why Use Ruff?

- Much faster execution
- Good auto-fix capabilities
- Active development
- Growing rule set

## Future Considerations

1. Monitor Ruff's development

   - May be able to reduce Pylint usage as Ruff grows
   - Watch for new rules that could replace Pylint checks

2. Regular Review
   - Reassess linting strategy quarterly
   - Update rules as project needs change
   - Consider new tools as they emerge
