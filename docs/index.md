# UVI - UV Init

> The future of Python project templating powered by UV

UVI (UV Init) is a modern Python project generator built around [UV](https://docs.astral.sh/uv/) - the revolutionary package manager that's reshaping the Python ecosystem. It provides a streamlined CLI that generates fully-configured Python projects with best practices and modern development tools already set up.

## Why UVI?

UVI lets you **instantly create production-ready Python projects** with a single command. Every project comes with:

- **[UV](https://docs.astral.sh/uv/) at the core**: 10-100x faster dependency management
- **Modern code quality**: [ruff](https://github.com/charliermarsh/ruff) (with Pylint rules), [mypy](https://mypy.readthedocs.io/), [deptry](https://github.com/shaneholloman/deptry/), and [prettier](https://prettier.io/)
- **CI/CD integration**: [GitHub Actions](https://github.com/features/actions) workflows configured
- **Git hooks**: Automated checks with [pre-commit](https://pre-commit.com/)
- **Testing**: [pytest](https://docs.pytest.org/) and [codecov](https://about.codecov.io/)
- **Documentation**: Generated with [MkDocs](https://www.mkdocs.org/)
- **Publishing**: Automated PyPI publishing through GitHub releases
- **Containerization**: Development and deployment with [Docker](https://www.docker.com/)
- **Dev environments**: Consistent setup with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)
- **Multi-Python testing**: [tox-uv](https://github.com/tox-dev/tox-uv) for all supported Python versions

## Installation

Install UVI using UV (recommended):

```bash
uv tool install uvi
```

Alternative installation methods:

```bash
# Using pipx
pipx install uvi

# Using pip
pip install --user uvi
```

## Usage

Creating a new project couldn't be simpler:

```bash
# Navigate to where you want to create your project
cd ~/projects

# Run UVI
uvi
```

Follow the prompts to configure your project. UVI will:

1. Auto-detect your user information from git or GitHub CLI
2. Generate a complete project structure
3. Set up all the configured tools and infrastructure

Once completed, you'll have a fully functional project ready for development. An example of a project generated with UVI can be found [here](https://github.com/shaneholloman/uvi-example).

> [!NOTE]
> Advanced users can also use Cookiecutter directly with UVI's template. See [Direct Cookiecutter Usage](features/direct-cookiecutter.md) for more details on why both options are available.
