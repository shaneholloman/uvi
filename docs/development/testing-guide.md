# Testing Guide

> Testing and Coverage Guide for UVI Development

## Overview

This guide documents our testing strategy using pytest and code coverage reporting with codecov. It's based on practical experience developing the UVI (uv init) project.

## Project Structure

Our test-related files are organized as follows:

```sh
uvi/
├── uvi/
│   ├── __init__.py     # Package version info (2 lines)
│   └── cli.py          # Main CLI logic (27 lines)
├── tests/
│   ├── __init__.py
│   ├── test_cli.py           # Tests for CLI functionality
│   ├── test_cookiecutter.py  # Tests for template generation
│   └── utils.py              # Helper functions for tests
└── pyproject.toml      # Test and coverage configuration
```

## Running Tests

### Basic Test Run

```bash
pytest
```

### With Coverage

```bash
pytest --cov
```

### Full Test Suite with Coverage Report

```bash
uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml tests
```

## Understanding Test Files

### Test Discovery

- pytest automatically discovers test files matching these patterns:
  - `test_*.py`
  - `*_test.py`
- Functions must be prefixed with `test_`
- Test classes must be prefixed with `Test`

### Our Test Files

1. `test_cli.py`

   - Tests CLI functionality
   - Currently focuses on version display
   - Limited coverage due to interactive nature of CLI

2. `test_cookiecutter.py`

   - Tests template generation
   - Multiple test cases (20+)
   - Doesn't affect main package coverage

3. `utils.py`
   - Helper functions for tests
   - Not a test file (no `test_` prefix)
   - Not included in test discovery

## Coverage Reporting

### Configuration

Coverage settings are in `pyproject.toml`:

```toml
[tool.coverage.run]
branch = true
source = ["uvi"]
parallel = true
concurrency = ["thread", "multiprocessing"]

[tool.coverage.report]
skip_empty = true
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "pass",
    "raise ImportError"
]
```

### Understanding Coverage Reports

Example coverage output:

```sh
Name              Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------
uvi/__init__.py       2      0      0      0   100%
uvi/cli.py           27     17      2      0    34%   45-72
-------------------------------------------------------------
TOTAL                29     17      2      0    39%
```

- Coverage only measures code in the `uvi/` source directory
- Helper files in `tests/` don't affect coverage
- Coverage percentage represents how much source code is executed during tests

### Coverage Metrics Explained

- Stmts: Number of statements
- Miss: Number of statements not executed
- Branch: Number of possible branches (if/else)
- BrPart: Number of partially executed branches
- Cover: Overall coverage percentage
- Missing: Line numbers not covered

## Testing Challenges

### Interactive CLI Testing

- Interactive features are difficult to test
- Mock with caution
- Focus on testing non-interactive parts

### Coverage vs. Functionality

- Lower coverage doesn't necessarily indicate poor quality
- Some code paths (like error handling) are hard to test
- Prioritize reliable tests over coverage percentage

## Best Practices

1. Keep tests focused and independent
2. Use `utils.py` for shared test functionality
3. Don't force coverage of interactive features
4. Document test limitations
5. Run full test suite before committing

## Continuous Integration

Coverage reports are generated during CI runs and can be viewed:

1. In the GitHub Actions output
2. On the codecov dashboard
3. In the generated `coverage.xml` file

Remember that while high coverage is desirable, the reliability and maintainability of tests should take precedence over coverage metrics.
