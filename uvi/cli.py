"""UVI CLI - Python Project Generator.

This module provides the command-line interface for UVI (uv init),
a Python project template generator that creates pre-configured projects
optimized for the uv package manager. It uses cookiecutter to streamline
the creation of new Python projects with modern best practices and tooling pre-configured.

Features:
    - Generates a complete Python project structure
    - Configures modern development tools (pytest, tox, pre-commit)
    - Sets up documentation (MkDocs)
    - Includes CI/CD pipelines
    - Configures code coverage reporting
    - Adds Docker support
    - Implements UV package management

Usage:
    uvi [--version]

The CLI will interactively prompt for project configuration options unless
--no-input is specified. It uses either a local template (when installed as
a package) or fetches from the GitHub repository.

Example:
    $ uvi  # Launches interactive project creation
    $ uvi --version  # Displays the current version
"""

from __future__ import annotations

import argparse
import os
import sys

from cookiecutter.main import cookiecutter

from . import __version__


def main() -> None:
    """Create a new Python project using the uvi template."""
    parser = argparse.ArgumentParser(description="Create a new Python project using uvi template")
    parser.add_argument("--version", action="version", version=f"uvi {__version__}")
    parser.parse_args()
    try:
        # When installed as a package, use the local template
        if os.path.exists(os.path.join(os.path.dirname(__file__), "..", "cookiecutter.json")):
            template = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        # When used directly via cookiecutter, use the GitHub repo
        else:
            template = "https://github.com/shaneholloman/uvi.git"

        # Run cookiecutter with the template
        cookiecutter(
            template,
            no_input=False,  # Enable interactive prompts
            overwrite_if_exists=False,  # Don't overwrite existing projects
        )
    except OSError as e:
        print(f"File system error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Invalid configuration: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:  # pylint: disable=broad-except
        # Keep a broad exception handler as a last resort for unexpected errors,
        # but explicitly acknowledge it with a pylint disable comment
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
