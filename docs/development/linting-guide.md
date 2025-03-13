# Linting Guide

> Linting Strategy Guide for UVI Development

## Overview

This guide documents our linting approach using Ruff as our primary linter. Ruff is a fast, modern Python linter that includes Pylint-equivalent rules for comprehensive code quality checks.

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
  # Pylint-equivalent rules
  "PLC", # pylint-convention
  "PLE", # pylint-error
  "PLR", # pylint-refactor
  "PLW", # pylint-warning
]
ignore = [
  # LineTooLong
  "E501",
  # DoNotAssignLambda
  "E731",
]
```

## Running Linters

### Development Checks

```bash
# Check code
ruff check .

# Fix auto-fixable issues
ruff check --fix .

# Format code
ruff format .
```

### Pre-commit Integration

Our `.pre-commit-config.yaml` configuration:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: "v0.6.3"
    hooks:
      - id: ruff
        args: [--exit-non-zero-on-fix, --config=pyproject.toml]
        exclude: ^{{cookiecutter.project_name}}
      - id: ruff-format
        args: [--config=pyproject.toml]
        exclude: ^{{cookiecutter.project_name}}
```

## Linting Strategy

### Why Ruff?

1. **Comprehensive Coverage**

   - Includes most functionality from tools like Flake8, Black, isort, pyupgrade, etc.
   - Incorporates Pylint-equivalent rules for deeper code analysis
   - Detects security issues, antipatterns, and complexity issues

2. **Performance**

   - Extremely fast execution (written in Rust)
   - Efficient for CI/CD pipelines
   - Quick developer feedback

3. **Modern Features**
   - Auto-fix capabilities for many issues
   - Type annotation checks
   - Pre-commit integration
   - Built-in formatter

### What Ruff Catches

- Import sorting and organization
- Code style and formatting issues
- Type annotation problems
- Security vulnerabilities
- Unused imports and variables
- Complex code and high cyclomatic complexity
- Documentation issues
- And much more!

## Best Practices

1. **Development Workflow**

   - Run Ruff frequently during development
   - Use Ruff's auto-fix capability (`ruff check --fix`)
   - Format code with `ruff format`
   - Address all warnings before committing

2. **Issue Resolution**

   - Fix issues immediately during development
   - Use proper exception handling instead of noqa directives
   - Document necessary suppressions (rare cases only)

3. **Configuration Management**
   - Keep Ruff rules up to date
   - Minimize rule suppressions
   - Document why rules are ignored when necessary

## Recommended IDE Setup

For the best development experience:

1. **VS Code**

   - Install the Ruff extension
   - Configure auto-formatting on save
   - Enable lint-on-save

2. **PyCharm/IntelliJ**
   - Use the Ruff plugin
   - Configure auto-formatting

## CI Integration

Ruff runs in CI:

1. Checks all code for issues
2. Verifies formatting standards
3. Must pass for PR approval

## Future Considerations

1. Stay current with Ruff updates

   - Ruff is actively developed
   - New rules and features are added regularly
   - Update to newer versions as available

2. Regular Review
   - Reassess linting strategy periodically
   - Update rules as project needs change
   - Consider new tools as they emerge
