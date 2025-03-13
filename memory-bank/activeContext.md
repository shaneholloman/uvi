# UVI Active Context

## Current Work Focus

The current focus is implementing the ability to prefill the cookiecutter prompts with the user's git username and email. This is one of the items from the TODO list, aimed at improving the user experience by reducing repetitive input.

## Recent Changes

- The project is currently at version 0.3.3
- A memory bank structure has been established to document the project systematically
- Core documentation files have been created to capture project knowledge

## Implementation Details: Git User Prefill

### Current Behavior

- Currently, users must manually enter their name, email, and GitHub handle every time they create a new project
- The template doesn't check for or use local git configuration

### Target Behavior

- The CLI should read git configuration using the `git config` command
- It should extract user.name and user.email values
- These values should be used to prefill the corresponding fields in the cookiecutter prompts
- The prefill should be optional and users should still be able to change the values

### Implementation Approach

1. Modify `uvi/cli.py` to get git user details before invoking cookiecutter
2. Use subprocess to run git config commands
3. Create a context dictionary with default values from git
4. Pass this context to cookiecutter's `extra_context` parameter

### Technical Considerations

- Need to handle cases where git isn't installed
- Need to handle cases where git config values aren't set
- Should maintain backward compatibility with previous versions
- Should not modify the cookiecutter.json template structure

## Next Steps

1. Implement the git user prefill feature in the CLI
2. Test the implementation with various scenarios
3. Update documentation to reflect the new capability
4. Consider implementing other items from the TODO list in future work

## Active Decisions

- Keep the implementation simple and focused on local git config
- Don't attempt to fetch GitHub-specific information (like the GitHub handle) at this stage
- Maintain backward compatibility with current usage patterns
- Implement error handling for cases where git isn't available or config values aren't set
