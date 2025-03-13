# Direct Cookiecutter Usage

UVI provides two ways to create new Python projects:

1. Using the `uvi` command (recommended approach)
2. Using Cookiecutter directly with the UVI template

This document explains why both approaches are offered and the benefits of each.

## What UVI's CLI Actually Does

Looking at the implementation, the `uvi` command is essentially a wrapper around Cookiecutter that provides:

1. **User information auto-detection** - It automatically gets user details from:
   - GitHub CLI (if available and authenticated)
   - Git config (local or global)
   - Falls back to generic defaults if needed

2. **Template resolution** - It handles finding the template whether installed as a package or accessed directly

3. **Error handling** - Provides friendly error messages for various failure scenarios

## Why Direct Cookiecutter Usage Makes Sense

### 1. Advanced User Flexibility

Advanced users familiar with Cookiecutter may want more control over the templating process. The direct approach lets them:

- Override specific parameters without going through the UVI CLI
- Use Cookiecutter's advanced features not exposed by the UVI wrapper
- Integrate with their existing Cookiecutter-based workflows

### 2. CI/CD Integration

In continuous integration pipelines, teams might prefer using Cookiecutter directly:

- More predictable for automated environments
- Can be used with pre-defined configuration files
- Easier to parameterize in build scripts

### 3. Availability

There may be environments where:

- Installing the full UVI package isn't feasible
- Users already have Cookiecutter installed
- Dependency conflicts prevent installing UVI

### 4. Educational Value

Showing direct Cookiecutter usage:

- Makes the implementation transparent
- Teaches users about the underlying technology
- Demonstrates how they could create their own templates

### 5. Separation of Concerns

This design respects the separation between:

- **Template content** (what UVI provides)
- **Template usage mechanism** (how it's accessed)

## It's About Options, Not Redundancy

Having both options isn't redundant - it's providing appropriate interfaces for different user needs:

- Casual users get a simplified `uvi` command
- Advanced users get direct Cookiecutter access
- Both access the same high-quality template

The code specifically handles both scenarios, with logic to determine if it's running as an installed package or accessed directly through Cookiecutter.

## How to Use Cookiecutter Directly

As mentioned in the README, you can use Cookiecutter directly with:

```bash
# Still using UV (preferred)
uvx cookiecutter https://github.com/shaneholloman/uvi.git

# Without UV (not recommended)
pip install cookiecutter
cookiecutter https://github.com/shaneholloman/uvi.git
```

This gives you all the power of UVI's templates with the flexibility of Cookiecutter's interface.
