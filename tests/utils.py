"""Utility functions for testing cookiecutter template generation.

Provides helper functions for YAML validation, directory context management,
and file content checking.
"""

from __future__ import annotations

import os
from contextlib import contextmanager
from pathlib import Path

import yaml


def is_valid_yaml(path: str | Path) -> bool:
    """Validate if a file contains valid YAML content.

    Args:
        path: Path to the YAML file to validate

    Returns:
        bool: True if file exists and contains valid YAML, False otherwise
    """
    path = Path(path)

    if not path.is_file():
        print(f"File does not exist: {path}")
        return False

    try:
        with path.open("r", encoding="utf-8") as file:
            yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Invalid YAML file: {path} - Error: {e}")
        return False
    except OSError as e:
        print(f"Error reading file: {path} - Error: {e}")
        return False

    return True


@contextmanager
def run_within_dir(path: str):
    """Context manager to temporarily change working directory.

    Args:
        path: Directory path to temporarily change to
    """
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def file_contains_text(file: str, text: str) -> bool:
    """Check if a file contains specific text.

    Args:
        file: Path to the file to check
        text: Text to search for in the file

    Returns:
        bool: True if text is found in file, False otherwise
    """
    with open(file, encoding="utf-8") as f:
        return f.read().find(text) != -1
