# UVI Project Development Reference

## Commands

- **Build/Install**: `uv sync`
- **Lint**: `uv run pre-commit run -a` or `uv run ruff check .`
- **Typecheck**: `uv run mypy`
- **Test (all)**: `uv run python -m pytest --cov --cov-config=pyproject.toml tests`
- **Test (single)**: `uv run python -m pytest tests/test_file.py::TestClass::test_function -v`
- **Full Check**: `make check` (lint, typecheck, dependency check)
- **Run Tests**: `make test`
- **Build Package**: `make build`
- **Generate Docs**: `make docs`

## Code Style Guidelines

- **Imports**: Add `from __future__ import annotations` first, group by stdlib/third-party/local
- **Type Annotations**: Required for all functions, follow PEP 484
- **Line Length**: 120 characters max
- **Documentation**: Google-style docstrings with Args/Returns sections
- **Naming**: snake_case for variables/functions, UPPER_CASE for constants
- **Error Handling**: Catch specific exceptions first, use descriptive error messages
- **Formatting**: Uses ruff for auto-formatting, pylint for deeper analysis
- **Functions**: Small, focused with single responsibilities
- **Testing**: pytest with coverage reporting, focus on reliability over coverage percentage

## Dependencies

uv for package management, ruff/pylint for linting, mypy for type checking, pytest for testing
