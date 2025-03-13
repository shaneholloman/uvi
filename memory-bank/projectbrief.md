# UVI Project Brief

## Project Definition

UVI (UV Init) is a modern Cookiecutter template for Python projects that integrates with the UV package manager. It provides a CLI tool that generates pre-configured Python projects with best practices and modern development tools already set up.

## Core Requirements

1. Provide a simple command-line interface for creating new Python projects
2. Utilize cookiecutter for project templating
3. Integrate UV for dependency management
4. Include modern code quality tools (ruff with Pylint-equivalent rules, mypy)
5. Support testing with pytest and code coverage
6. Offer documentation generation with MkDocs
7. Enable CI/CD workflows with GitHub Actions
8. Support containerization with Docker and devcontainers
9. Make publishing to PyPI straightforward

## Project Goals

- Simplify the initial setup of Python projects
- Enforce best practices for Python development
- Reduce the friction of adopting modern tools
- Provide a standardized but configurable project structure
- Support multiple Python versions (3.10, 3.11, 3.12, 3.13)

## Scope

- Command-line tool for project generation
- Template with configurable options
- Documentation on features and usage
- Supporting scripts for project maintenance

## Current Priorities

- ✅ Implement git user details prefilling for cookiecutter prompts
- ✅ Migrate from Pylint to Ruff with Pylint-equivalent rules
- Fix remaining linting issues in the info/ directory
- Address remaining items in the TODO.md file
