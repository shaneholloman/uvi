# UVI Makefile Ideas

This document provides suggestions for enhancing UVI's Makefile based on a comparison with Cookiecutter's Makefile. These enhancements would provide additional developer conveniences and improve the development workflow.

## Current Makefile Strengths

UVI's current Makefile already includes several excellent features:

- Integration with GitHub CLI for documentation deployment
- Sophisticated bake targets with pre-built options
- Comprehensive code quality checks (lock file consistency, pre-commit, mypy, deptry)
- Modern tooling integration (UV throughout)
- Well-documented target descriptions
- Clear separation of concerns

## Proposed Enhancements

### 1. More Granular Clean Targets

Cookiecutter provides multiple specialized clean targets that give developers fine-grained control:

```makefile
.PHONY: clean-tox
clean-tox: ## Remove tox testing artifacts
 @echo "+ $@"
 @rm -rf .tox/

.PHONY: clean-coverage
clean-coverage: ## Remove coverage reports
 @echo "+ $@"
 @rm -rf htmlcov/
 @rm -rf .coverage
 @rm -rf coverage.xml

.PHONY: clean-pytest
clean-pytest: ## Remove pytest cache
 @echo "+ $@"
 @rm -rf .pytest_cache/

.PHONY: clean-docs-build
clean-docs-build: ## Remove local docs
 @echo "+ $@"
 @rm -rf docs/_build

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
 @echo "+ $@"
 @find . -type d -name '__pycache__' -exec rm -rf {} +
 @find . -type f -name '*.py[co]' -exec rm -f {} +
 @find . -name '*~' -exec rm -f {} +

.PHONY: clean
clean: clean-build clean-pyc clean-tox clean-coverage clean-pytest clean-docs-build
```

UVI could benefit from similar granular targets, including a master `clean` target that combines all cleaning operations.

### 2. Test Coverage Viewing

Add a target to generate and automatically open coverage reports:

```makefile
.PHONY: coverage
coverage: ## Generate and view coverage report
 @echo "Generating coverage report"
 @uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=html
 @uv run python -c "import webbrowser, os; webbrowser.open('file://' + os.path.abspath('htmlcov/index.html'))"
```

This would make it easier for developers to inspect coverage results after running tests.

### 3. Multi-Python Version Testing

While UVI uses tox for multi-version testing, the Makefile could provide an easy shortcut:

```makefile
.PHONY: test-all
test-all: ## Test with all supported Python versions
 @echo "Testing with all supported Python versions"
 @uv run tox
```

### 4. Separate Distribution Formats

Currently, UVI combines sdist and wheel building. Separating these could provide more flexibility:

```makefile
.PHONY: sdist
sdist: clean-build ## Build source distribution
 @echo "Creating source distribution"
 @uvx --from build pyproject-build --sdist --installer uv
 @ls -l dist

.PHONY: wheel
wheel: clean-build ## Build wheel
 @echo "Creating wheel distribution"
 @uvx --from build pyproject-build --wheel --installer uv
 @ls -l dist
```

### 5. Documentation Improvements

Add targets for different documentation workflows:

```makefile
.PHONY: docs-build
docs-build: ## Build documentation locally
 @echo "Building documentation"
 @uv run mkdocs build

.PHONY: docs-serve
docs-serve: ## Serve documentation for local development
 @echo "Serving documentation at http://localhost:8000"
 @uv run mkdocs serve

.PHONY: docs-check
docs-check: ## Check documentation for issues
 @echo "Checking documentation"
 @uv run mkdocs build -s
```

### 6. Dev Environment Setup

Make it easier to set up consistent development environments:

```makefile
.PHONY: dev-setup
dev-setup: ## Set up development environment
 @echo "Setting up development environment"
 @uv sync
 @uv run pre-commit install
 @echo "Development environment ready"
```

### 7. Dependency Management

Add targets for managing and analyzing dependencies:

```makefile
.PHONY: deps-update
deps-update: ## Update dependencies
 @echo "Updating dependencies"
 @uv tree --outdated

.PHONY: deps-check
deps-check: ## Check for outdated dependencies
 @echo "Checking for outdated dependencies"
 @uv tree --outdated
```

## Implementation Considerations

1. **Compatibility**: These enhancements should maintain compatibility with existing targets
2. **Platform Independence**: Ensure commands work across different operating systems
3. **Documentation**: Each new target should include clear documentation comments
4. **UV Integration**: Continue to leverage UV for all Python operations

## Priority Recommendations

Based on development workflow impact, the following enhancements are recommended as priorities:

1. **Clean Targets**: More granular clean operations would immediately improve developer experience
2. **Coverage Viewing**: Directly visualizing test coverage would encourage better testing practices
3. **Dependency Management**: Simplifying dependency updates would help maintain project health
4. **Dev Environment Setup**: Making development setup more consistent would help contributors

These enhancements would further improve UVI's development workflow while maintaining the project's commitment to modern Python practices and tooling.
