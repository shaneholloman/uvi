# UVI Technical Context

## Technologies Used

### Core Dependencies

- **Python**: 3.10+ (supports 3.10, 3.11, 3.12, 3.13)
- **Cookiecutter**: 2.6.0 - Template engine for project generation
- **UV**: 0.6.6 - Modern Python package manager used for dependency management

### Development Dependencies

- **Ruff**: 0.9.10 - Fast Python linter and formatter (includes Pylint-equivalent rules)
- **MyPy**: 1.15.0 - Static type checking
- **Pytest**: 8.3.5 - Testing framework
- **Pre-commit**: 4.1.0 - Git hook framework
- **Tox-UV**: 1.25.0 - Testing against multiple Python versions with UV
- **MkDocs-Material**: 9.6.7 - Documentation generator with Material theme
- **MkDocstrings**: 0.29.0 - API documentation generator
- **Deptry**: 0.23.0 - Dependency checking tool

### Generated Project Technologies

The template can generate projects with the following configurable technologies:

- **GitHub Actions**: CI/CD workflows
- **Docker**: Containerization
- **VSCode Devcontainers**: Development environments
- **Codecov**: Code coverage reporting
- **MkDocs**: Documentation with Material theme

## Development Setup

### Requirements

- Python 3.10 or higher
- Git (for version control and user information)
- UV installed for dependency management

### Local Development

1. Clone the repository
2. Install dependencies with UV: `uv sync`
3. Install pre-commit hooks: `pre-commit install`
4. Run tests: `pytest`
5. Check code quality: `make check`

### Testing

- Unit tests are in the `tests/` directory
- Use pytest for running tests
- Use tox-uv for testing against multiple Python versions

## Technical Constraints

### Python Version Compatibility

- Requires Python 3.10+
- Generated projects are set up to work with Python 3.10, 3.11, 3.12, and 3.13

### Package Management

- Designed around UV for dependency management
- Not compatible with traditional requirements.txt-based workflows
- Generated projects use modern pyproject.toml configuration

### User Environment

- Assumes git is available for version control
- May need GitHub CLI for certain GitHub operations
- Requires command-line environment (not GUI-based)

## Dependencies

### Direct Dependencies

- **cookiecutter**: Template system for project generation

### Development Dependencies Specification

The project uses several development dependencies:

```python
dev = [
  # Pylint has been replaced by Ruff with Pylint-equivalent rules
  "pytest>=8.3.5",
  "pre-commit>=4.1.0",
  "pytest-cookies>=0.7.0",
  "tox-uv>=1.25.0",
  "deptry>=0.23.0",
  "mypy>=1.15.0",
  "pytest-cov>=6.0.0",
  "ruff>=0.9.10",
  "mkdocs-material>=9.6.7",
  "mkdocstrings[python]>=0.29.0",
  "build>=1.2.2.post1",
  "twine>=6.1.0",
]
```

### Build System

- Uses setuptools for packaging (build-backend = "setuptools.build_meta")
