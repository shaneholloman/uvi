# `uvi` - UV Init: The Future of Python Project Generation

[![Build status](https://img.shields.io/github/actions/workflow/status/shaneholloman/uvi/main.yml?branch=main)](https://github.com/shaneholloman/uvi/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/shaneholloman/uvi/blob/main/pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://shaneholloman.github.io/uvi/)
[![License](https://img.shields.io/github/license/shaneholloman/uvi)](https://img.shields.io/github/license/shaneholloman/uvi)

UVI (UV Init) is a modern Python project generator built around [UV](https://docs.astral.sh/uv/) - the high-performance Python package manager that's reshaping the Python ecosystem. This tool creates fully-configured Python projects with best practices and modern development tools already set up.

## TLDR

```sh
uvi # follow prompts
uv run mkdocs serve # start your documentation server
```

## Why UV is the Way Forward

UV represents the future of Python dependency management:

- **Blazing Fast**: UV is up to 10-100x faster than traditional tools
- **Reliable and Deterministic**: Produces perfectly reproducible environments
- **Modern Architecture**: Built in Rust with best practices from the ground up
- **Complete Solution**: Handles all Python packaging needs in one tool

This project is designed with UV as its foundation - UV is integrated into every aspect of the project architecture.

> [!IMPORTANT]
> This project 'works' but it's not done yet!

See Progress: [progress](./memory-bank/progress.md)

## Features

- **[UV](https://docs.astral.sh/uv/) at the core**: The foundation of our dependency management approach
- **UV-powered testing**: Compatibility testing with [tox-uv](https://github.com/tox-dev/tox-uv)
- **Modern code quality**: [ruff](https://github.com/charliermarsh/ruff) (including Pylint-equivalent rules), [mypy](https://mypy.readthedocs.io/en/stable/), [deptry](https://github.com/shaneholloman/deptry/), and [prettier](https://prettier.io/)
- **CI/CD integration**: Workflows with [GitHub Actions](https://github.com/features/actions)
- **Git hooks**: Automated checks with [pre-commit](https://pre-commit.com/)
- **Testing**: Framework with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- **Documentation**: Generated with [MkDocs](https://www.mkdocs.org/)
- **Publishing**: Easy PyPI publishing through GitHub releases
- **Containerization**: Development and deployment with [Docker](https://www.docker.com/)
- **Dev environments**: Consistent setup with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

## Pre-configured GitHub Workflows

Projects created with UVI come with production-ready GitHub workflows:

- **Comprehensive CI Pipeline**: Runs quality checks, tests, and type checking with a single workflow
- **Multi-Python Testing**: Automatically verifies compatibility with Python 3.9-3.13 using matrix builds
- **Documentation CI**: Validates that your MkDocs documentation builds successfully
- **Code Coverage**: Seamlessly integrated with Codecov for visibility into test coverage
- **Optimized Performance**: Pre-configured caching for dependencies and pre-commit to speed up CI runs
- **Custom GitHub Actions**: Includes reusable custom actions for Python environment setup
- **Conditional Features**: Workflows adapt based on your project configuration (MkDocs, Codecov, etc.)

All workflows use the latest stable Ubuntu runners and leverage UV for consistent, fast dependency installation.

## UVI's Self-Consistent Philosophy

UVI embodies a fundamentally consistent approach. The same technology, patterns, and workflows used to build UVI itself are automatically provided in every project UVI generates:

- **Consistent Toolchain**: The UV-powered build process that makes UVI lightning-fast is the same one your projects inherit
- **Shared Infrastructure**: The GitHub Actions workflows, pre-commit hooks, and testing frameworks aren't bolt-ons - they're the same ones UVI relies on
- **Inherited DNA**: When we improve UVI's internal architecture, your next project automatically benefits

This creates a consistent workflow:

1. **You install UVI** (one simple command)
2. **You run UVI** (answer a few prompts)
3. **You get a project** with the same capabilities, performance, and reliability as UVI itself

The value of UVI is in this consistency - generated projects benefit from the same technical foundations that power UVI itself.

## Documentation

- [Full Documentation](https://shaneholloman.github.io/uvi/)

## Installation & Usage

Install `uvi` using UV - this is the only supported method:

```bash
uv tool install uvi
```

Then run it to create your project:

```bash
uvi
```

The generated project will provide clear instructions in its README for next steps.

## Project Benefits

Projects created with UVI inherit significant advantages:

- **Fast dependency installation**: `uv sync` installs dependencies in seconds
- **Reproducible environments**: Lock files ensure consistent builds across machines
- **Simplified workflow**: Single command for environment setup
- **Future-ready**: Your project starts with tomorrow's best practices today

## Acknowledgments

UVI builds upon [Cookiecutter](https://github.com/cookiecutter/cookiecutter), the powerful project templating engine. We're grateful to the Cookiecutter team and the broader Python packaging community whose work makes tools like UVI possible.
