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
import json
import os
import shutil
import subprocess
import sys
from typing import Any

from cookiecutter.main import cookiecutter

from . import __version__


def _try_command_run(command: str, arg: str) -> bool:
    """Try to run a command with a given argument to check if it's available.

    Args:
        command: The command to check
        arg: The argument to pass to the command (e.g., "--version")

    Returns:
        True if the command is available, False if it raised an exception
    """
    # These subprocess calls are safe as they only use parameters
    # controlled by our code, not user input
    try:
        subprocess.run(  # noqa: S603
            [command, arg],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except (subprocess.SubprocessError, FileNotFoundError):
        # Command not available or execution failed
        return False
    else:
        # If we get here without exception, command is available
        return True


def is_command_available(command: str) -> bool:
    """Check if a command is available in the system.

    Works cross-platform by first using shutil.which, then trying to run the command.

    Args:
        command: The command to check (e.g., "git", "gh")

    Returns:
        True if the command is available, False otherwise
    """
    # Try using shutil.which first (most reliable cross-platform approach)
    if shutil.which(command):
        return True

    # Try with --version flag (most commands support this)
    if _try_command_run(command, "--version"):
        return True

    # Final attempt with --help flag
    return _try_command_run(command, "--help")


def get_github_user_info() -> dict[str, str] | None:
    """Get user information from GitHub CLI.

    Attempts to retrieve user information from GitHub API using the GitHub CLI.

    Returns:
        Dict containing user information from GitHub, or None if unavailable
    """
    if not is_command_available("gh"):
        print("GitHub CLI not found. Consider installing it for better integration.")
        return None

    # Check if user is authenticated with GitHub
    try:
        # The gh command is a fixed string, not user input
        result = subprocess.run(  # noqa: S603
            ["gh", "auth", "status"],  # noqa: S607
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode != 0:
            print("GitHub CLI found but not authenticated. Run 'gh auth login' to set up.")
            return None

        # Get user information from GitHub API
        try:
            # The gh command is a fixed string, not user input
            user_json = subprocess.check_output(  # noqa: S603
                ["gh", "api", "user"],  # noqa: S607
                stderr=subprocess.DEVNULL,
                text=True,
            )
            user_data: dict[str, Any] = json.loads(user_json)

            # Extract relevant information
            context = {}
            if user_data.get("name"):
                context["author"] = user_data["name"]
            if user_data.get("email"):
                context["email"] = user_data["email"]
            if user_data.get("login"):
                context["author_github_handle"] = user_data["login"]

            if context:
                print(f"Using information from GitHub account: {user_data.get('login', 'unknown')}")
                return context
        except (subprocess.SubprocessError, json.JSONDecodeError) as e:
            print(f"Error getting GitHub user data: {e}")
            return None
    except subprocess.SubprocessError:
        return None

    return None


def _try_git_config(key: str, scope: str) -> str | None:
    """Try to get a git config value from specified scope.

    Args:
        key: The git config key (e.g., "user.name")
        scope: The scope to use ("--local" or "--global")

    Returns:
        The config value if found, None otherwise
    """
    # Attempt to get git config value
    try:
        cmd = ["git", "config", scope, "--get", key]
        value = subprocess.check_output(  # noqa: S603
            cmd,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Return None if command fails or git isn't available
        return None
    else:
        # Return the value if it's not empty, None otherwise
        return value if value else None


def get_git_config_value(key: str, local: bool = True) -> str | None:
    """Get a value from git config.

    Args:
        key: The git config key to get (e.g., "user.name")
        local: Whether to get the local repository config (True) or
               global config (False)

    Returns:
        The git config value if found, None otherwise
    """
    # Check if git is available
    if not is_command_available("git"):
        return None

    # Try with the primary scope first
    primary_scope = "--local" if local else "--global"
    value = _try_git_config(key, primary_scope)
    if value:
        return value

    # If primary scope fails, try the alternate scope
    alternate_scope = "--global" if local else "--local"
    return _try_git_config(key, alternate_scope)


def get_git_user_info() -> dict[str, str]:
    """Get user information from git config.

    Attempts to retrieve user name and email from git configuration.
    Falls back to generic defaults if values cannot be retrieved.

    Returns:
        Dict containing user info with git values prioritized over generic defaults
    """
    # Generic defaults that will be used if git config is not available
    context = {"author": "Your Name", "email": "your.email@example.com", "author_github_handle": "your-github-handle"}

    if not is_command_available("git"):
        print("Git not found. Using generic defaults.")
        return context

    # First try local config, then fall back to global
    print("Using git configuration for user details.")

    # Get user name from git config (try local first, then global)
    name_local = get_git_config_value("user.name", local=True)
    if name_local:
        context["author"] = name_local
        print(f"Using local git name: {name_local}")
    else:
        # Try global config
        name_global = get_git_config_value("user.name", local=False)
        if name_global:
            context["author"] = name_global
            print(f"Using global git name: {name_global}")

    # Get user email from git config (try local first, then global)
    email_local = get_git_config_value("user.email", local=True)
    if email_local:
        context["email"] = email_local
        print(f"Using local git email: {email_local}")
    else:
        # Try global config
        email_global = get_git_config_value("user.email", local=False)
        if email_global:
            context["email"] = email_global
            print(f"Using global git email: {email_global}")

    # Try to extract GitHub handle from email (simple heuristic)
    email = context["email"]
    if email and (email.endswith("@github.com") or email.endswith("@users.noreply.github.com")):
        handle = email.split("@", maxsplit=1)[0]
        context["author_github_handle"] = handle
        print(f"Extracted GitHub handle from email: {handle}")

    return context


def get_user_info() -> dict[str, str]:
    """Get user information from various sources.

    Uses a tiered approach:
    1. Try GitHub CLI first for best results
    2. Fall back to git config if GitHub isn't available
    3. Use generic defaults as a last resort

    Returns:
        Dict containing user information from the best available source
    """
    # Try GitHub CLI first
    github_info = get_github_user_info()
    if github_info:
        return github_info

    # Fall back to git config
    return get_git_user_info()


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

        # Get user information from the best available source
        context = get_user_info()

        # Run cookiecutter with the template and prefilled values
        cookiecutter(
            template,
            no_input=False,  # Enable interactive prompts
            overwrite_if_exists=False,  # Don't overwrite existing projects
            extra_context=context,  # Prefill with user info
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
    except (subprocess.SubprocessError, json.JSONDecodeError) as e:
        print(f"External process or data error: {e}", file=sys.stderr)
        sys.exit(1)
    except (ImportError, ModuleNotFoundError) as e:
        print(f"Missing module error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Keep a broad exception handler as a last resort for truly unexpected errors
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
