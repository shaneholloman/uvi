# UVI Product Context

## Why This Project Exists

UVI was created to address the friction and inconsistency in starting new Python projects. It specifically targets projects that want to use the modern `uv` package manager instead of traditional tools like pip or poetry. The goal is to provide a standardized starting point that incorporates current best practices without requiring developers to manually configure everything from scratch.

## Problems It Solves

1. **Setup Complexity**: Starting a new Python project with proper structure, testing, linting, and documentation requires significant setup time
2. **Tool Integration**: Configuring multiple tools to work together (ruff, mypy, pytest, GitHub Actions, etc.) is complex
3. **Best Practice Adoption**: Many developers struggle to implement all recommended practices for Python projects
4. **Dependency Management**: The shift to using `uv` requires adapting existing patterns and workflows
5. **Consistency**: Projects often lack consistent structure and configurations across teams or even within organizations

## How It Should Work

UVI is designed to be simple and intuitive:

1. Users install the `uvi` CLI tool
2. They run a single command: `uvi`
3. They answer a series of prompts to configure their project
4. A complete project structure is generated with all selected features configured

The template is customizable through prompt arguments that enable/disable various features like GitHub Actions, documentation, Docker support, etc. Each feature is completely configured when enabled, requiring no additional setup.

## User Experience Goals

1. **Simplicity**: Users should be able to generate a project with minimal effort
2. **Discoverability**: Options should be clear and well-documented
3. **Completeness**: Generated projects should be immediately usable
4. **Flexibility**: Users should be able to choose which features they need
5. **Modern**: Incorporate the latest Python best practices and tools
6. **Maintainable**: Projects should be easy to maintain with built-in tooling

## Target Audience

- Python developers looking to start new projects
- Teams wanting consistency in project structure
- Developers interested in adopting the `uv` package manager
- Organizations wanting to standardize their Python development practices
