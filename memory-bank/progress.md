# UVI Project Progress

## What Works

1. **Core CLI Functionality**

   - Command-line interface for creating Python projects
   - Integration with cookiecutter templating system
   - Version information display

2. **Project Generation**

   - Complete project structure creation
   - Configuration via interactive prompts
   - Template processing with variable substitution

3. **Features Configuration**

   - GitHub Actions integration
   - PyPI publishing setup
   - Documentation with MkDocs
   - Code quality tools (ruff, mypy, deptry)
   - Testing with pytest and coverage
   - Containerization with Docker
   - Development environments with VSCode devcontainers

4. **Hook System**

   - Pre-generation validation
   - Post-generation cleanup
   - Conditional file removal based on user selections

5. **Documentation**
   - Project setup instructions
   - Feature documentation
   - Prompt arguments explained

## Current Status

- Version 0.3.3 is published and functional
- Basic project generation works reliably
- All advertised features are implemented
- Documentation is in place

## Known Issues

- [x] Automatic prefill of user information implemented (FIXED)
- No check for required tools (gh CLI, uv CLI)
- ~No option to add pylint in prompt arguments~ (Not needed - migrated to Ruff with Pylint-equivalent rules)
- No python_version selection option
- Linting issues in info/ directory (using Ruff)
- Documentation-deploy function in Makefile needs improvement
- No .env file handling

## What's Left to Build

From the TODO list, the following items need to be implemented:

1. **Completed**

   - [x] Implementation of user information prefill for cookiecutter prompts (GitHub CLI + git + fallbacks)

2. **Future Work**
   - [ ] Add trusted PyPI publishing to the project
   - [ ] Ensure project description is printed to the GitHub site repo page
   - [ ] Add checks for gh CLI and uv CLI installation
   - [ ] Fix linting issues in info/ directory using Ruff
   - [x] ~Add pylint option to prompt arguments~ (Obsolete - migrated to Ruff with Pylint-equivalent rules)
   - [ ] Add python_version selection option
   - [ ] Add codemapper option
   - [ ] Add .env file handling capability
   - [ ] Improve docs-deploy function in root Makefile

## Progress Metrics

- Feature completeness: ~85%
- Documentation completeness: ~95%
- Test coverage: Good, with room for improvement
- Code quality: Significantly improved after Ruff migration
