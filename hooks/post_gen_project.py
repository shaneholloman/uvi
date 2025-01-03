#!/usr/bin/env python
"""Post-generation script for cookiecutter template.

Handles cleanup and organization of project files based on user configuration choices,
including removal of unused files/directories and proper license file placement.
"""

# pylint: disable=comparison-of-constants
# Disabled because these are cookiecutter template variables, not actual constants

from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove a file from the generated project directory.

    Args:
        filepath: Relative path to the file to be removed
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    """Remove a directory and its contents from the generated project directory.

    Args:
        filepath: Relative path to the directory to be removed
    """
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def move_file(filepath: str, target: str) -> None:
    """Move/rename a file within the generated project directory.

    Args:
        filepath: Current relative path of the file
        target: New relative path for the file
    """
    os.rename(
        os.path.join(PROJECT_DIRECTORY, filepath),
        os.path.join(PROJECT_DIRECTORY, target),
    )


def should_remove_release_workflow() -> bool:
    """Check if the release workflow file should be removed.

    Returns:
        bool: True if the file should be removed, False otherwise
    """
    no_mkdocs = "{{cookiecutter.mkdocs}}" != "y"
    no_pypi = "{{cookiecutter.publish_to_pypi}}" == "n"
    return no_mkdocs and no_pypi


if __name__ == "__main__":  # pylint: disable=comparison-of-constants
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if should_remove_release_workflow():
            remove_file(".github/workflows/on-release-main.yml")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    if "{{cookiecutter.open_source_license}}" == "MIT license":
        move_file("LICENSE_MIT", "LICENSE")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "BSD license":
        move_file("LICENSE_BSD", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "ISC license":
        move_file("LICENSE_ISC", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "Apache Software License 2.0":
        move_file("LICENSE_APACHE", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "GNU General Public License v3":
        move_file("LICENSE_GPL", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "Not open source":
        remove_file("LICENSE_GPL")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
