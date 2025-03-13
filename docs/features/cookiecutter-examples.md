# Cookiecutter Examples

Practical Cookiecutter Usage Examples

This document provides practical examples of using Cookiecutter directly with UVI, demonstrating the flexibility discussed in [Direct Cookiecutter Usage](direct-cookiecutter.md).

## 1. Creating a Project with Custom Parameters

You can pass parameters directly to Cookiecutter to customize your project without interactive prompts:

```bash
# Create a project with custom parameters
uvx cookiecutter /path/to/uvi --no-input \
  project_name=api-service \
  project_description="API service created with direct cookiecutter" \
  dockerfile=y \
  devcontainer=y
```

This creates a complete project with parameters specified on the command line, ideal for scripting or automation.

## 2. Batch Project Creation

Direct Cookiecutter access enables creating multiple projects in a single operation:

```bash
#!/bin/bash
# create_services.sh - Create multiple microservices from a template
for service in "auth-service" "user-service" "payment-service"; do
  uvx cookiecutter /path/to/uvi --no-input \
    project_name="$service" \
    project_description="Microservice for ${service}" \
    dockerfile=y \
    devcontainer=y
done
```

This script generates three separate projects, each with its own configuration but sharing common settings. Excellent for creating collections of related microservices or libraries.

## 3. CI/CD Pipeline Integration

For CI/CD environments, use something like:

```bash
# In a GitHub Actions workflow
- name: Generate project
  run: |
    uvx cookiecutter https://github.com/shaneholloman/uvi.git --no-input \
      project_name=${{ github.event.repository.name }} \
      project_description="${{ github.event.repository.description }}" \
      include_github_actions=y \
      codecov=y
```

This approach allows generating standardized project templates based on repository metadata.

## 4. Local Template Development

When developing the template itself, use local paths:

```bash
# Use local template for testing changes
uvx cookiecutter /path/to/local/uvi --no-input \
  project_name="test-project" \
  include_github_actions=n
```

This allows for rapid testing of template changes without pushing to a remote repository.

## 5. Creating Projects in Specific Locations

You can specify where the generated project should be created:

```bash
# Output to a specific directory
uvx cookiecutter /path/to/uvi --output-dir ./projects \
  project_name="specific-location"
```

This is useful for organizing multiple generated projects in a structured way.

## Notes on Parameter Formatting

- Boolean values are passed as `y` or `n` (e.g., `dockerfile=y`)
- Strings with spaces need quotes (e.g., `project_description="My Project"`)
- All parameters must match those in cookiecutter.json
- Parameter names are case-sensitive

## Available Parameters

All parameters defined in UVI's cookiecutter.json file:

| Parameter              | Description                        | Example Values                     |
| ---------------------- | ---------------------------------- | ---------------------------------- |
| author                 | Author name                        | "Your Name"                        |
| email                  | Author email                       | "<your.email@example.com>"         |
| author_github_handle   | GitHub username                    | "your-github-handle"               |
| project_name           | Project name                       | "example-project"                  |
| project_slug           | Slug for import (auto-generated)   | "example_project"                  |
| project_description    | Brief description                  | "This is a template repository..." |
| include_github_actions | Add GitHub Actions                 | "y" or "n"                         |
| publish_to_pypi        | Configure PyPI publishing          | "y" or "n"                         |
| deptry                 | Add deptry for dependency checking | "y" or "n"                         |
| mkdocs                 | Add MkDocs documentation           | "y" or "n"                         |
| codecov                | Add code coverage                  | "y" or "n"                         |
| dockerfile             | Add Dockerfile                     | "y" or "n"                         |
| devcontainer           | Add VS Code devcontainer           | "y" or "n"                         |
| open_source_license    | License type                       | "MIT license", "BSD license", etc. |
