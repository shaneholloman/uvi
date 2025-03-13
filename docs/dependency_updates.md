# Dependency Updates

## Current Dependencies vs Latest Versions

| Package | Current Version | Latest Version | Update Needed |
|---------|----------------|----------------|---------------|
| cookiecutter | 2.6.0 | 2.6.0 | No |
| build | 1.2.2.post1 | 1.2.2.post1 | No |
| deptry | 0.21.2 | 0.23.0 | Yes |
| mkdocs-material | 9.5.49 | 9.6.7 | Yes |
| mkdocstrings[python] | 0.27.0 | 0.29.0 | Yes |
| mypy | 1.14.1 | 1.15.0 | Yes |
| pre-commit | 4.0.1 | 4.1.0 | Yes |
| pytest | 8.3.4 | 8.3.5 | Yes |
| pytest-cookies | 0.7.0 | 0.7.0 | No |
| pytest-cov | 6.0.0 | 6.0.0 | No |
| ruff | 0.9.10 | 0.9.10 | No |
| tox-uv | 1.17.0 | 1.25.0 | Yes |
| twine | 6.0.1 | 6.1.0 | Yes |

## Transitive Dependencies with Updates Available

| Package | Current Version | Latest Version |
|---------|----------------|----------------|
| jinja2 | 3.1.5 | 3.1.6 |
| certifi | 2024.12.14 | 2025.1.31 |
| pygments | 2.18.0 | 2.19.1 |
| types-setuptools | 75.6.0.20241223 | 76.0.0.20250313 |
| babel | 2.16.0 | 2.17.0 |
| pymdown-extensions | 10.13 | 10.14.3 |
| mkdocs-autorefs | 1.2.0 | 1.4.1 |
| griffe | 1.5.4 | 1.6.0 |
| identify | 2.6.4 | 2.6.9 |
| virtualenv | 20.28.1 | 20.29.3 |
| filelock | 3.16.1 | 3.17.0 |
| coverage[toml] | 7.6.10 | 7.6.12 |
| tox | 4.23.2 | 4.24.2 |
| cachetools | 5.5.0 | 5.5.2 |
| pyproject-api | 1.8.0 | 1.9.0 |
| uv | 0.5.14 | 0.6.6 |
| more-itertools | 10.5.0 | 10.6.0 |
| pkginfo | 1.12.0 | 1.12.1.2 |
| nh3 | 0.2.20 | 0.2.21 |

## Update Plan

1. Update all direct dependencies to their latest versions
2. Run tests to ensure everything still works correctly
3. Commit the changes with a clear message about the version updates
