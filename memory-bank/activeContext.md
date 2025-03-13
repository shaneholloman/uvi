# UVI Active Context

## Current Work Focus

The current focus is on three main improvements:

1. Implementing the ability to prefill the cookiecutter prompts with the user's git username and email. This feature has been successfully implemented using proper implementation workflow.

2. Modernizing the linting system by migrating from Pylint to Ruff with Pylint-equivalent rules. This improves code quality, speeds up linting, and simplifies the development workflow.

3. Planning migration from Tox to Nox for testing. This will provide better UV integration, increased flexibility through Python-native configuration, and a more modern architecture for the testing system.

## Recent Changes

- The project is currently at version 0.5.0
- Updated all dependencies to their latest versions (March 2025)
- Added UV commands to .clinerules file for checking latest package versions
- A memory bank structure has been established to document the project systematically
- Core documentation files have been created to capture project knowledge
- The .clinerules file was updated with comprehensive feature implementation workflow
- Implementation of git user prefill for cookiecutter prompts has been properly verified
- Migrated from Pylint to Ruff with Pylint-equivalent rules
- Removed .pylintrc and updated all related documentation files
- Updated code to follow modern Python best practices for error handling
- Upgraded cookiecutter dependency from 2.1.1 to 2.6.0
- Updated Python target version from 3.9 to 3.10 in the main project
- Ensured dependency version parity between the main project and the template
- Synchronized pre-commit hook versions between the main project and template
- Added Pylint-equivalent rules to the template's Ruff configuration

## Implementation Details: Dependency Updates

### Latest Version Update (March 2025)

- Updated all dev dependencies to their latest versions:
  - pytest: 8.3.5 (from 7.2.0)
  - pre-commit: 4.1.0 (from 2.20.0)
  - pytest-cookies: 0.7.0 (from 0.6.1)
  - tox-uv: 1.25.0 (from 1.11.3)
  - deptry: 0.23.0 (from 0.20.0)
  - mypy: 1.15.0 (from 0.991)
  - pytest-cov: 6.0.0 (from 4.0.0)
  - ruff: 0.9.10 (from 0.6.9)
  - mkdocs-material: 9.6.7 (from 9.0.0)
  - mkdocstrings[python]: 0.29.0 (from 0.19.0)
  - build: 1.2.2.post1 (from 1.0.3)
  - twine: 6.1.0 (from 4.0.2)

- Documented new UV commands for checking latest package versions:

  ```bash
  uv tree --package <package> --outdated  # Check specific package
  uv tree --outdated                     # Check all packages
  ```

- Updated documentation in memory-bank/techContext.md to reflect current versions

## Implementation Details: User Info Prefill

### Previous Behavior (Documented)

- Users had to manually enter their name, email, and GitHub handle every time they created a new project
- The template didn't check for or use local git configuration
- Default values were hardcoded personal information in cookiecutter.json

### New Behavior (Verified)

#### Tiered Information Sources

1. **GitHub CLI (Primary Source)**

   - If available and authenticated, retrieves user profile from GitHub API
   - Provides the most accurate GitHub handle along with name and email
   - Displays a message when using GitHub account info

2. **Git Configuration (Fallback)**

   - If GitHub CLI isn't available, falls back to git config
   - Prioritizes local repository config over global config
   - Tries to extract GitHub handle from GitHub-style emails
   - Displays messages about which values are being used

3. **Generic Defaults (Last Resort)**
   - If neither GitHub nor git is available, uses generic placeholders
   - Ensures users never see someone else's personal information

#### Key Improvements

- Cross-platform command detection (works on Windows, Mac, Linux)
- Proper error handling for all external commands
- Detailed user feedback about information sources
- Maintains the interactive prompt experience
- Clear separation of concerns in the code structure

### Additional Improvements

- Removed hardcoded personal information from config files
- Changed default values to generic placeholders ("Your Name", "<your.email@example.com>")
- Added proper handling for missing/unavailable tools
- Made the implementation OS-agnostic

### Implementation Details

1. Added `get_git_config_value` function to safely retrieve git configuration values

   - Added check to verify git is installed using `shutil.which`
   - Properly handles errors if git command fails or values aren't set
   - Uses `subprocess.check_output` with appropriate error handling

2. Added `get_git_user_info` function to collect user information

   - Gets name from git config user.name
   - Gets email from git config user.email
   - Attempts to extract GitHub handle from email if it follows GitHub patterns

3. Modified main function to:
   - Get git user info before invoking cookiecutter
   - Pass this info as `extra_context` to cookiecutter

### Testing and Verification

1. Documented baseline behavior using actual tool execution
2. Set up test environment with custom git config values
3. Ran the tool with implementation and verified correct behavior
4. Documented improvements and compared before/after experiences

### Technical Considerations Addressed

- Handles cases where git isn't installed by using `shutil.which` to check for git
- Handles cases where git config values aren't set by only including values that exist
- Maintains backward compatibility with previous versions (the tool works exactly the same if git isn't available)
- Does not modify the cookiecutter.json template structure, only prefills values
- Uses proper error handling and follows the project's coding standards
- Passes all linting, type checking, and actual execution tests

## Implementation Details: Linting System Modernization

### Previous System

- Used both Ruff and Pylint for linting
- Pylint provided deeper code analysis
- Pre-commit hooks ran both linters
- Required maintaining two separate configurations

### New System

- Exclusively uses Ruff for all linting needs
- Added Pylint-equivalent rule sets (PLC, PLE, PLR, PLW)
- Removed dependencies on Pylint
- Simplified pre-commit configuration
- Follows Ruff's recommended practices for error handling

### Linting System Improvements

- Faster linting process (Ruff is significantly faster than Pylint)
- Single source of truth for linting rules
- Simplified configuration management
- Consistent code style enforcement
- Better developer experience
- More modern approach to Python linting

### Technical Changes

1. Updated pyproject.toml to include Pylint-equivalent rules
2. Removed Pylint from dependencies and pre-commit hooks
3. Deleted .pylintrc file
4. Updated documentation to reflect the new linting approach
5. Improved exception handling in the codebase to follow Ruff's best practices
6. Resolved inconsistencies between Ruff and Pylint rules

## Next Steps

1. **Highest Priority:** Implement smarter template download behavior to eliminate the re-download prompt
   - Use Cookiecutter's `force_download` parameter with internet connectivity detection
   - If online: Silently pull the latest template version
   - If offline: Use the cached version without prompting
   - Documented in docs/briefs/cli-enhancements.md

2. Implement Tox to Nox migration (detailed plan in docs/briefs/tox-to-nox-migration.md)
3. Fix remaining linting issues in the info/ directory using Ruff
4. Add python_version selection option
5. Consider implementing other CLI enhancements from docs/briefs/cli-enhancements.md
6. Consider implementing Makefile enhancements documented in docs/briefs/makefile-enhancements.md
7. Discuss and develop a strategy for Cookiecutter maintenance concerns documented in docs/briefs/uvi-future-strategy.md
8. Consider implementing other items from the TODO list in future work
9. Version bump and PyPI publish with all improvements

## Planned Implementation: Tox to Nox Migration

### Motivation

- Replace Tox with Nox for testing infrastructure
- Benefit from Python-native configuration offered by Nox
- Better integration with UV (no need for tox-uv plugin)
- More flexible approach to test management

### Migration Strategy

- Develop Noxfile.py with equivalent functionality to current tox.ini
- Run parallel testing to ensure identical results
- Update cookiecutter template to use Nox instead of Tox
- Update documentation and guides
- Remove Tox dependencies once migration is verified successful

### Expected Benefits

- More intuitive test configuration using Python code
- Better code organization through function-based approach
- Direct UV command execution without plugins
- Modern testing architecture aligned with project goals

## Active Decisions

- Keep the implementation simple and focused on local git config
- Don't attempt to fetch GitHub-specific information (like the GitHub handle) at this stage
- Maintain backward compatibility with current usage patterns
- Implement error handling for cases where git isn't available or config values aren't set
- Migrate from Tox to Nox while maintaining feature parity during transition
