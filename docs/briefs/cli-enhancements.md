# UVI Enhancement Ideas

This document logs proposed enhancements to the UVI command-line interface to provide more flexibility and improved user experience.

## Current CLI Limitations

The current UVI CLI implementation offers minimal command-line options (only `--version`), while providing significant value through its automatic user information detection. However, it lacks some of the flexibility available when using Cookiecutter directly.

## Proposed Enhancements

### High-Value Additions

#### 1. Quick/Silent Mode

```bash
uvi --quick   # or --silent or --simple
```

Only prompts for the project name and uses sensible defaults for everything else:

- Auto-detects user information (as it already does)
- Enables all features (GitHub Actions, PyPI publishing, deptry, MkDocs, codecov, Docker, devcontainer)
- Uses MIT license (most permissive common license)
- Generates a default description like "A Python package for [project_name]"

**User Experience Example:**

```sh
$ uvi --quick
Detecting user information...
Using information from GitHub account: username
Enter project name: my-awesome-project
Creating project with all features enabled...
Project created successfully!
```

#### 2. Configuration Profiles

```bash
# Create a minimalist project with just the basics
uvi --profile minimal

# Create a data science focused project
uvi --profile datascience

# Create a web application project
uvi --profile webapp
```

Each profile would have different default selections for features that make sense for that type of project.

#### 3. Non-Interactive Mode

```bash
uvi --no-input [parameters]
```

Allow for scripted/automated project creation, passing values directly rather than through interactive prompts. Essential for CI/CD pipelines or batch operations.

#### 4. Parameter Overrides

```bash
uvi --param project_name=myproject --param dockerfile=y
```

Allow specifying individual template parameters directly via CLI, useful for overriding specific values without answering all prompts.

#### 5. Output Directory Control

```bash
uvi --output-dir /path/to/projects
```

Specify where the generated project should be placed, rather than always using the current directory.

#### 6. Configuration Files

```bash
uvi --config my-config.json
```

Support loading parameter values from a configuration file, enabling standardized project creation across a team.

#### 7. Template Saving/Replay

```bash
# Save configuration
uvi --save-config my-python-service.json

# Use saved configuration
uvi --replay my-python-service.json
```

Save configurations for reuse, allowing consistent recreation of similar projects.

### Medium-Value Additions

#### 8. Template Customization

```bash
uvi --template https://github.com/user/custom-template.git
```

Allow specifying an alternative template source, enabling organization-specific templates.

#### 9. Preview Mode

```bash
uvi --dry-run
```

Show what would be generated without actually creating files, useful for validation.

#### 10. Verbosity Control

```bash
uvi --quiet
uvi --verbose
```

Control the amount of output during project generation.

#### 11. Overwrite Protection Toggle

```bash
uvi --overwrite-if-exists
```

Allow overwriting existing directories when needed.

#### 12. Parameter Listing

```bash
uvi --list-parameters
```

Display all available parameters and their defaults without starting project creation.

## Implementation Considerations

Adding these options would require:

1. Extending the argument parser in `main()`
2. Passing appropriate parameters to the Cookiecutter function
3. Maintaining backward compatibility
4. Updating documentation

Most of these could be implemented as direct passes to Cookiecutter's API, making implementation relatively straightforward while significantly enhancing the UVI CLI's flexibility.

## Priority Recommendations

Based on user feedback and enhancement value, the following features are recommended as priority implementations:

### Highest Priority

1. **Smarter Template Download Behavior** - Eliminate the annoying re-download prompt

   ```bash
   # Current behavior: Always asks if you want to re-download the template
   # Improved behavior: Automatically use latest if online, use cached if offline
   ```

   This would use Cookiecutter's `force_download` parameter with internet connectivity detection to:
   - If online: Silently pull the latest template version
   - If offline: Use the cached version without prompting

   Implementation would involve checking internet connectivity and setting the appropriate Cookiecutter parameters:

   ```python
   try:
       # Try to connect to a reliable site
       requests.get("https://pypi.org", timeout=1)
       # Online - force download latest
       force_download = True
   except requests.RequestException:
       # Offline - use cached version without asking
       force_download = False

   cookiecutter(
       template,
       force_download=force_download,
       # other params...
   )
   ```

### High Priority

- **Quick/Silent Mode** - Provides immediate value for common use cases
- **Parameter Overrides** - Offers flexibility without complexity
- **Non-Interactive Mode** - Essential for automation
- **Configuration Profiles** - Streamlines workflow for different project types

These enhancements would significantly improve the user experience while maintaining the simplicity that makes UVI valuable.
