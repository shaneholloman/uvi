# `uvi` - UV Init: The Future of Python Project Templating

[![Build status](https://img.shields.io/github/actions/workflow/status/shaneholloman/uvi/main.yml?branch=main)](https://github.com/shaneholloman/uvi/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/shaneholloman/uvi/blob/main/pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://shaneholloman.github.io/uvi/)
[![License](https://img.shields.io/github/license/shaneholloman/uvi)](https://img.shields.io/github/license/shaneholloman/uvi)

UVI (UV Init) is a modern Cookiecutter template built around [UV](https://docs.astral.sh/uv/) - the revolutionary Python package manager that's reshaping the Python ecosystem. This tool generates fully-configured Python projects with best practices and modern development tools already set up.

## Why UV is the Way Forward

UV represents the future of Python dependency management:

- **Blazing Fast**: UV is up to 10-100x faster than traditional tools
- **Reliable and Deterministic**: Produces perfectly reproducible environments
- **Modern Architecture**: Built in Rust with best practices from the ground up
- **Complete Solution**: Handles all Python packaging needs in one tool

This project fully embraces UV's philosophy - we're not just using UV, **we're built around it**.

> [!IMPORTANT]
> This project 'works' but is far from perfect!

See todos: [TODO.md](./TODO.md)

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

## Documentation

- [Full Documentation](https://shaneholloman.github.io/uvi/)

## Installation & Usage

> After installation, follow the prompts to configure your project. A new directory containing your project will be created. Navigate into this directory and follow the `README.md` instructions to complete setup.

### The UV Way (Recommended)

Install the `uvi` tool using UV:

```bash
# Using UV - "This is the way"
uv tool install uvi
```

### Legacy Installation Methods

While we strongly recommend using UV, these alternatives are available:

```bash
# Using pipx
pipx install uvi
```

```bash
# Using pip
pip install --user uvi
```

To create your new project, navigate to your desired directory and run:

```bash
uvi
```

### Direct Cookiecutter Usage

For advanced users, you can use cookiecutter directly:

```bash
# Still using UV (preferred)
uvx cookiecutter https://github.com/shaneholloman/uvi.git

# Without UV (not recommended)
pip install cookiecutter
cookiecutter https://github.com/shaneholloman/uvi.git
```

## The UV Advantage in Generated Projects

Projects created with UVI are fully configured to leverage UV's advantages:

- **Fast dependency installation**: `uv sync` installs dependencies in seconds
- **Reproducible environments**: Lock files ensure consistent builds across machines
- **Simplified workflow**: Single command for environment setup
- **Future-ready**: Your project starts with tomorrow's best practices today
