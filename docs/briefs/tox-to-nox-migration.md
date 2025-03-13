# Tox to Nox Migration Brief

## Project Context

UVI is a Python project template generator using UV for dependency management, currently using Tox for testing across multiple Python versions (3.10-3.13).

## Migration Plan Summary

### Phase 1: Setup (1-2 hours)

- Install Nox (`uv add nox --dev`)
- Create basic noxfile.py mirroring current tox functionality

### Phase 2: Implementation (3-4 hours)

- Develop complete noxfile.py with all test sessions
- Maintain feature parity with current tox configuration
- Configure Python version matrix (3.10-3.13)

### Phase 3: Parallel Testing (2-3 hours)

- Run both systems to verify identical results
- Fix any discrepancies in behavior

### Phase 4: Template & Documentation (2-3 hours)

- Update cookiecutter template to use noxfile.py
- Update documentation and guides

### Phase 5: Tox Removal (1 hour)

- Remove tox dependencies and files
- Final verification

## Key Benefits

1. **Better UV Integration**: Direct UV command execution without plugins
2. **Increased Flexibility**: Python-native configuration allows for:
   - Programmatic test setup
   - Code reuse between test sessions
   - Conditional testing logic

3. **Modern Architecture**:
   - Function-based approach aligns with Python best practices
   - Cleaner separation of concerns
   - More explicit dependency management

4. **Template Improvement**:
   - Generated projects will use a more modern, flexible testing approach
   - Better alignment with UVI's focus on contemporary Python tools

## Noxfile.py Reference Implementation

```python
import nox

# Configure Nox
nox.options.sessions = ["tests"]
python_versions = ["3.10", "3.11", "3.12", "3.13"]

@nox.session(python=python_versions)
def tests(session):
    """Run the test suite."""
    session.run("uv", "sync", "--python", session.python, external=True)
    session.install("pytest", "pytest-cookies", "pytest-cov", "pyyaml")
    session.run(
        "python", "-m", "pytest", "--doctest-modules", "tests",
        "--cov", "--cov-config=pyproject.toml", "--cov-report=xml"
    )
    session.run("mypy")

@nox.session(python=["3.13"])
def lint(session):
    """Run the linter."""
    session.install("ruff")
    session.run("ruff", "check", ".")

@nox.session(python=["3.13"])
def docs(session):
    """Build the documentation."""
    session.install("mkdocs-material", "mkdocs-github-admonitions-plugin", "mkdocstrings[python]")
    session.run("mkdocs", "build")
```

## Comparative Analysis: Tox vs. Nox for UVI

### Tox Advantages

- Already established in project
- tox-uv plugin integration
- Template consistency
- Familiar to contributors

### Nox Advantages

- Python-native configuration
- Direct UV command execution
- Function-based approach allows better code organization
- More flexible for complex testing scenarios

## Next Steps

1. Start with a minimal noxfile.py focused on core test functionality
2. Verify each Python version works correctly
3. Add specialized test sessions for additional checks
4. Update template once core functionality is proven

Total estimated time: 8-12 hours of development work
