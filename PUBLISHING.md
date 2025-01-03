# Publishing to PyPI

> WIP!

This document outlines two methods for publishing the `uvi` package to PyPI.

## Important: Version Management

Before publishing (either method), always update the version in `pyproject.toml`:

```toml
[project]
name = "uvi"
version = "x.y.z"  # Update this version number
```

## Method 1: Automated Publishing via GitHub Actions (Recommended)

This repository is configured to automatically publish to PyPI when a new release is created on GitHub using trusted publishing.

1. Ensure your changes are committed and pushed to the main branch
2. **IMPORTANT**: Update the version in `pyproject.toml` (see Version Management above)
3. Create a new release on GitHub:
   - Go to <https://github.com/shaneholloman/uvi/releases>
   - Click "Draft a new release"
   - Create a new tag (e.g., v0.1.0)
   - Write release notes
   - Click "Publish release"
4. The GitHub Actions workflow will automatically:
   - Build the package
   - Publish to PyPI using trusted publishing
   - Deploy the documentation

## Method 2: Manual Publishing

If you need to publish manually, follow these steps:

1. **IMPORTANT**: Update the version in `pyproject.toml` (see Version Management above)

2. Ensure dev dependencies are installed and pre-commit hooks are set up:

   ```bash
   uv sync
   uv run pre-commit install
   uv run pre-commit run -a --show-diff-on-failure
   ```

3. Build the package using uvx:

   ```bash
   uvx --from build pyproject-build --installer uv
   ```

   This creates distribution files in the `dist/` directory.

4. Upload to PyPI using uvx:

   ```bash
   uvx twine upload --verbose dist/*
   ```

   You'll need to provide your PyPI username and password.

## Verifying the Publication

After publishing (either method), verify the package is available:

1. Check the PyPI page: <https://pypi.org/project/uvi/>
2. Try installing it (or upgrade to latest version):

   ```bash
   uv tool install uvi  # fresh install
   uv tool install --force uvi  # force reinstall to latest version
   ```

## Notes

- The automated GitHub Actions method uses PyPI's trusted publishing feature, which is more secure than using API tokens
- For manual publishing, you'll need a PyPI account with appropriate permissions
