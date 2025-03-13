# UVI System Patterns

## System Architecture

UVI uses a layered architecture with the following components:

```mermaid
flowchart TD
    CLI[CLI Interface] --> Template[Template System]
    Template --> Hooks[Generation Hooks]
    Template --> Content[Project Structure]
```

### Core Components

1. **CLI Interface (uvi/cli.py)**

   - Entry point for user interaction
   - Parses command-line arguments
   - Invokes cookiecutter with the appropriate template

2. **Template System**

   - Uses cookiecutter for templating
   - Configuration defined in cookiecutter.json
   - Handles variable substitution

3. **Generation Hooks**

   - Pre-generation validation (hooks/pre_gen_project.py)
   - Post-generation cleanup (hooks/post_gen_project.py)
   - Conditional file removal based on user choices

4. **Project Structure**
   - Template files in {{cookiecutter.project_name}}/
   - Configurable components based on user selections

## Key Technical Decisions

1. **Cookiecutter as Template Engine**

   - Mature, widely-used templating system
   - Supports pre/post generation hooks
   - Handles complex templating requirements

2. **UV for Dependency Management**

   - Modern, fast Python package manager
   - Better performance than pip/poetry
   - Core focus of the generated projects

3. **CLI-First Approach**

   - Simple command-line interface
   - No complex GUI or web interface
   - Focus on developer experience

4. **Explicit Configuration**
   - All options clearly defined in prompts
   - No hidden defaults or magic
   - User in control of all features

## Design Patterns in Use

1. **Template Method Pattern**

   - Hooks define the skeleton of operations
   - Concrete implementations determined by user choices

2. **Factory Pattern**

   - Creates project structure based on configuration
   - Different "products" (features) based on user input

3. **Command Pattern**

   - CLI executes a series of operations
   - Encapsulates all the logic needed to perform actions

4. **Decorator Pattern**
   - Configuration options add or remove features
   - Base project enhanced with optional components

## Testing Architecture

The testing infrastructure is a key component of both UVI itself and the generated projects.

### Current Pattern: Tox

```mermaid
flowchart TD
    Tox[Tox] --> EnvCreate[Create Virtual Environments]
    EnvCreate --> EnvPy310[Python 3.10]
    EnvCreate --> EnvPy311[Python 3.11]
    EnvCreate --> EnvPy312[Python 3.12]
    EnvCreate --> EnvPy313[Python 3.13]
    EnvPy310 & EnvPy311 & EnvPy312 & EnvPy313 --> UVSync[UV Sync Dependencies]
    UVSync --> RunTests[Run Test Suite]
    RunTests --> Coverage[Generate Coverage]
    RunTests --> TypeChecking[Type Checking]
```

- Configuration-based via tox.ini
- Declarative environment specification
- Integration with GitHub Actions via gh-actions section
- Uses tox-uv plugin for UV integration

### Planned Pattern: Nox

```mermaid
flowchart TD
    Nox[Noxfile.py] --> Sessions[Define Sessions]
    Sessions --> TestSession[Test Sessions]
    Sessions --> LintSession[Lint Sessions]
    Sessions --> DocsSession[Docs Sessions]
    TestSession --> Py310Test[Python 3.10 Tests]
    TestSession --> Py311Test[Python 3.11 Tests]
    TestSession --> Py312Test[Python 3.12 Tests]
    TestSession --> Py313Test[Python 3.13 Tests]
    Py310Test & Py311Test & Py312Test & Py313Test --> UVSync[UV Sync]
    UVSync --> RunTests[Run Test Suite]
```

- Python-native configuration via noxfile.py
- Programmatic session definition with explicit dependency management
- Direct UV integration without plugins
- Enhanced flexibility through Python functions

## Component Relationships

```mermaid
flowchart TD
    subgraph User Interaction
        CLI[CLI Tool]
        Prompts[Interactive Prompts]
    end

    subgraph Generation Process
        Pre[Pre-Generation Hook]
        Template[Template Processing]
        Post[Post-Generation Hook]
    end

    subgraph Output
        Project[Generated Project]
    end

    CLI --> Prompts
    Prompts --> Pre
    Pre --> Template
    Template --> Post
    Post --> Project
```

## File Structure

- `uvi/` - Package containing the CLI tool
- `hooks/` - Pre/post generation scripts
- `{{cookiecutter.project_name}}/` - Template for generated projects
- Configuration files (cookiecutter.json, pyproject.toml, etc.)

## Processing Flow

1. User runs `uvi` command
2. CLI parses arguments and invokes cookiecutter
3. Cookiecutter presents interactive prompts
4. Pre-generation hook validates inputs
5. Template is processed with user selections
6. Post-generation hook cleans up based on choices
7. Final project is generated in the filesystem
