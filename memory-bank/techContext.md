# UVI Technical Context

## Technologies Used

### Core Dependencies

- **Python**: 3.10+ (supports 3.10, 3.11, 3.12, 3.13)
- **Cookiecutter**: Template engine for project generation
- **UV**: Modern Python package manager used for dependency management

### Development Dependencies

- **Ruff**: Fast Python linter and formatter
- **Pylint**: Static code analyzer
- **MyPy**: Static type checking
- **Pytest**: Testing framework
- **Pre-commit**: Git hook framework
- **Tox-UV**: Testing against multiple Python versions with UV
- **MkDocs**: Documentation generator
- **Deptry**: Dependency checking tool

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

### Development Dependencies

The project uses several development dependencies:

```python
dev = [
  "pylint>=3.0.0",
  "pytest>=7.2.0",
  "pre-commit>=2.20.0",
  "pytest-cookies>=0.6.1",
  "tox-uv>=1.11.3",
  "deptry>=0.20.0",
  "mypy>=0.991",
  "pytest-cov>=4.0.0",
  "ruff>=0.6.9",
  "mkdocs-material>=9.0.0",
  "mkdocstrings[python]>=0.19.0",
  "build>=1.0.3",
  "twine>=4.0.2",
]
```

### Build System

- Uses setuptools for packaging (build-backend = "setuptools.build_meta")
