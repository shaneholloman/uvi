# Template Dependency Parity Brief

## Project Context

UVI is a Python project generator that creates Python projects using UV for dependency management. The template should maintain functional parity with the main project to ensure a consistent "dogfooding" experience.

## Current Status and Issues

- The main UVI project includes dependencies and configurations that are not currently reflected in the template
- Missing configurations can lead to inconsistent behavior between the main project and generated projects
- Users of generated projects may miss out on best practices established in the main project

## Proposed Changes

### Phase 1: MkDocs Github Admonitions Plugin (Complete)

- Add `mkdocs-github-admonitions-plugin>=0.0.3` to the template's dev dependencies
- This enables consistent documentation features between the main project and generated projects

### Phase 2: Ruff Import Configuration (Needed)

- Add the following configuration to template pyproject.toml:

  ```toml
  [tool.ruff.lint.isort]
  required-imports = ["from __future__ import annotations"]
  ```

- This ensures all files include future annotations, maintaining consistent import styling

### Phase 3: Build & Publish Strategy (Analysis)

- Current main project includes `build>=1.2.2.post1` and `twine>=6.1.0` for package building/publishing
- Analysis reveals UV natively supports these operations via:
  - `uv build` - Replaces the build package functionality
  - `uv publish` - Replaces the twine package functionality
- **Recommendation**: Rather than adding these as dependencies, document the use of UV's native capabilities in generated projects

## Implementation Plan

1. Add the ruff isort configuration to the template
2. Update project documentation to highlight UV's native build/publish capabilities
3. Consider adding a new cookiecutter variable to include publishing documentation in README.md
4. Verify the changes with a test project generation

## Benefits

1. **Improved Consistency**: Generated projects will follow the same best practices as the main project
2. **Better Code Quality**: Enforced import style results in more maintainable code
3. **UV-First Approach**: Promoting UV's native capabilities over additional dependencies aligns with the project's philosophy
4. **Reduced Dependency Overhead**: Using built-in UV features instead of adding dependencies simplifies project maintenance

## Summary

This brief proposes maintaining a closer alignment between the UVI main project and its template by:

1. Adding the missing GitHub admonitions plugin dependency (completed)
2. Adding missing ruff import configuration (pending)
3. Leveraging UV's native build/publish capabilities instead of adding dependencies (strategic decision)

These changes support the project's mission of providing a modern, UV-based Python project template with a consistent developer experience.
