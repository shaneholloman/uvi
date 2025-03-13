# Publishing to PyPI

## Version 0.4.0+ Updates

This document has been updated with the latest publishing workflow information.

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

### Prerequisites

- You must have write access to the GitHub repository
- PyPI project must have trusted publishing configured for this repository or a PYPI_API_TOKEN secret configured
- All code changes must be committed and pushed to the main branch

#### Setting Up Trusted Publishing (Recommended)

For maximum security, you can set up trusted publishing in PyPI:

1. Go to your PyPI project: <https://pypi.org/project/uvi/>
2. Navigate to "Manage" > "Publishing"
3. Add a new publisher:
   - Select "GitHub Actions"
   - Enter repository name: `shaneholloman/uvi`
   - Set workflow name: `release.yml`
   - Choose environment: leave blank for regular repos

#### Alternative: GitHub Secret for PyPI Token

A PYPI_API_TOKEN secret has been added to the repository as a fallback mechanism:

1. The token is stored securely in GitHub repository secrets
2. It will only be used if trusted publishing fails
3. No need to add or modify this token unless it expires

### Steps to Publish a New Release

1. **Update Version Numbers**:

   - Update the version in `pyproject.toml` under the `[project]` section
   - Update the version in `uvi/__init__.py` (`__version__ = "x.y.z"`)
   - Commit and push these changes to the main branch

2. **Create a New Release on GitHub**:

   - Go to <https://github.com/shaneholloman/uvi/releases>
   - Click "Draft a new release"
   - Create a new tag matching your version (e.g., `v0.4.0`)
   - Set the title to the version number (e.g., "UVI 0.4.0")
   - Write detailed release notes describing the changes
   - Click "Publish release"

3. **Monitor GitHub Actions Workflow**:
   - The workflow will automatically start when the release is published
   - You can monitor progress at <https://github.com/shaneholloman/uvi/actions>
   - The workflow includes three jobs:
     - Test: Runs pytest to verify package functionality
     - Deploy Docs: Updates documentation on GitHub Pages
     - Deploy PyPI: Builds and publishes the package to PyPI

### What the Workflow Does

The GitHub Actions workflow will automatically:

- Run tests to verify the package
- Build the package using UV
- Try to publish to PyPI using trusted publishing (primary method)
- Fall back to token-based publishing if trusted publishing isn't set up
- Deploy the documentation to GitHub Pages

The workflow is designed to be resilient, with a dual publishing approach that works whether trusted publishing is set up or not.

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
