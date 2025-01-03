# Dependency Management with uv

The generated repository uses [uv](https://docs.astral.sh/uv/) for fast, reliable Python package management. When you create your repository using this cookiecutter template, a uv environment is pre-configured in `pyproject.toml`.

## Adding Dependencies

To add project-specific dependencies:

```bash
uv add <package>
```

## Common Commands

### Installing Dependencies

```bash
uv sync
```

This command:

- Installs all dependencies from pyproject.toml
- Creates/updates uv.lock with exact versions
- Use when setting up a new environment or after adding new dependencies

### Reproducible Installations

```bash
uv sync --frozen
```

This command:

- Installs exact versions from uv.lock
- Ensures consistent environments across machines
- Use for production deployments or team synchronization

### Updating Dependencies

To update all dependencies to their latest compatible versions:

1. Remove the lock file:

   ```bash
   rm uv.lock
   ```

2. Sync dependencies:

   ```bash
   uv sync
   ```

This will:

- Fetch latest compatible versions
- Create a new lock file
- Install updated packages

### Running Commands

You can run commands within your virtual environment:

```bash
uv run python -m pytest
```

## When to Use Each Command

- `uv sync`:

  - Setting up new development environment
  - After adding new dependencies
  - When you want to update to latest compatible versions

- `uv sync --frozen`:
  - Deploying to production
  - Ensuring team has identical dependencies
  - After pulling changes with new uv.lock
