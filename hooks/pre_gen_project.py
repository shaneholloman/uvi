"""Pre-generation script for cookiecutter template.

Validates project name and slug to ensure they conform to Python module naming conventions
before project generation proceeds.
"""

from __future__ import annotations

import re
import sys

PROJECT_NAME_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
# Get value from cookiecutter
PROJECT_NAME = "{{cookiecutter.project_name}}"

if not re.match(PROJECT_NAME_REGEX, PROJECT_NAME):
    print(
        f"ERROR: The project name {PROJECT_NAME} is not a valid Python module name. "
        "Please do not use a _ and use - instead"
    )
    # Exit to cancel project
    sys.exit(1)

PROJECT_SLUG_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
# Get value from cookiecutter
PROJECT_SLUG = "{{cookiecutter.project_slug}}"

if not re.match(PROJECT_SLUG_REGEX, PROJECT_SLUG):
    print(
        f"ERROR: The project slug {PROJECT_SLUG} is not a valid Python module name. "
        "Please do not use a - and use _ instead"
    )
    # Exit to cancel project
    sys.exit(1)
