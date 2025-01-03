# `uvi` uv init

[![Build status](https://img.shields.io/github/actions/workflow/status/shaneholloman/uvi/main.yml?branch=main)](https://github.com/shaneholloman/uvi/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/shaneholloman/uvi/blob/main/pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://shaneholloman.github.io/uvi/)
[![License](https://img.shields.io/github/license/shaneholloman/uvi)](https://img.shields.io/github/license/shaneholloman/uvi)

This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development, testing, and deployment. It supports the following features:

> This project 'works' but is far from perfect!

See todos: [TODO.md](./TODO.md)

- [uv](https://docs.astral.sh/uv/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), [deptry](https://github.com/shaneholloman/deptry/) and [prettier](https://prettier.io/)
- Publishing to [PyPI](https://pypi.org) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [tox-uv](https://github.com/tox-dev/tox-uv)
- Containerization with [Docker](https://www.docker.com/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

## Docs

- [Docs](https://shaneholloman.github.io/uvi/)

## Installation & Usage

> For both methods follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project.

### Method 1: Using the CLI tool (Recommended)

Install the `uvi` tool globally:

```bash
uv tool install uvi
```

```bash
# or using pip
pip install uvi
```

Then navigate to the directory where you want to create your project and run:

```bash
uvi
```

### Method 2: Using Cookiecutter directly

Alternatively, you can use cookiecutter directly:

```bash
uvx cookiecutter https://github.com/shaneholloman/uvi.git
# or if you don't have uv installed:
pip install cookiecutter
cookiecutter https://github.com/shaneholloman/uvi.git
```
