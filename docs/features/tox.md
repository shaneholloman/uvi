# Testing with Tox and uv

This project integrates [tox-uv](https://github.com/tox-dev/tox-uv) to leverage uv's fast, reliable package management for testing. When `tox` is set to `"y"`, your project will use tox with uv for all test environments and dependency management.

## Setup

1. Create and activate a virtual environment:

   ```bash
   uv venv
   .venv/Scripts/activate  # On Windows
   ```

2. Install all dependencies (including tox, tox-uv, and test dependencies):

   ```bash
   uv sync
   ```

Note: The project's test dependencies (pytest, pytest-cov, mypy, pyyaml) are automatically installed in each tox environment.

If you need to recreate the virtual environment:

```bash
Remove-Item -Recurse -Force .venv  # On Windows
rm -rf .venv                       # On Unix
uv venv
uv sync
```

The integration with uv means:

- Faster environment creation
- More reliable dependency resolution
- Consistent package management across development and testing

## What Tox Does

- Creates isolated virtual environments
- Tests package installation
- Runs tests against multiple Python versions
- Executes linting and formatting checks
- Validates package builds

## Running Tox

Basic usage:

```bash
uv run tox
```

Run specific environments:

```bash
uv run tox -e py310  # Run tests for Python 3.10
uv run tox -e py311  # Run tests for Python 3.11
```

## Python Version Compatibility

By default, the project is tested with Python `3.10`, `3.11`, `3.12`, and `3.13`.

Testing for compatibility with different Python versions is automatically done in the CI/CD pipeline:

- On every pull request
- On merges to main
- On each release

## When to Use Tox

- Before pushing code changes
- To verify package works across Python versions
- Running complete test suite in clean environments
- Executing all quality checks in one command

## Customizing Python Versions

To test compatibility with additional Python versions:

1. Add versions to `tox.ini`
2. Update the workflows in `.github`
