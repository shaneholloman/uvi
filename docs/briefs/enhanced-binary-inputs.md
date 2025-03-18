# Enhanced Binary Input Handling

## Overview

This enhancement improves the UVI CLI questionnaire interface by allowing more flexible user input options for binary (yes/no) questions. Currently, users must enter exactly `y` or `n` for binary choices, which can lead to frustration when more intuitive responses like `Y`, `N`, `1`, or `2` are rejected.

## Problem Statement

The current UVI CLI uses Cookiecutter's default input handling, which strictly enforces the options defined in `cookiecutter.json`. For binary questions (those with `["y", "n"]` choices), this means:

- Only lowercase `y` or `n` is accepted
- Common variations like uppercase `Y` or `N` are rejected
- Numeric inputs (`1` for yes, `2` for no) - which are intuitive for many CLI users - are not supported
- Each invalid input requires retyping the answer, creating friction in the user experience

## Enhancement Solution

This improvement will extend the input handling for binary questions to accept:

- Case-insensitive letter inputs: `y`, `Y`, `n`, `N`
- Full word inputs: `yes`, `no` (case-insensitive)
- Numeric inputs: `1` (for yes), `2` (for no)
- While maintaining compatibility with the original `y`/`n` format

## Implementation Approach

The implementation will:

1. Create a custom input handler that wraps the Cookiecutter prompts
2. Parse the `cookiecutter.json` configuration to identify binary choice questions
3. For those questions, implement enhanced input validation and normalization
4. Convert all accepted inputs to the standard Cookiecutter format (`y` or `n`)
5. Provide clear error messages when inputs don't match any accepted format

## Technical Details

The enhancement involves creating a custom prompt handler that:

1. Reads the `cookiecutter.json` configuration
2. Identifies binary choice questions (those with `["y", "n"]` options)
3. Processes user input through a flexible parser that normalizes various input formats
4. Builds a complete context dictionary with all user responses
5. Passes this pre-filled context to Cookiecutter with `no_input=True`

For binary questions, input processing will follow this logic:

```python
def process_binary_input(user_input):
    # Normalize input
    normalized = user_input.strip().lower()

    # Check for various affirmative inputs
    if normalized in ('y', 'yes', '1'):
        return 'y'

    # Check for various negative inputs
    if normalized in ('n', 'no', '2'):
        return 'n'

    # If input doesn't match any accepted format, return None
    # to indicate invalid input
    return None
```

## User Experience

With this enhancement, the following scenario becomes possible:

```
? include_github_actions [y/n]: Y        → Accepted (converted to 'y')
? publish_to_pypi [y/n]: 2               → Accepted (converted to 'n')
? deptry [y/n]: yes                      → Accepted (converted to 'y')
? mkdocs [y/n]: NO                       → Accepted (converted to 'n')
```

If the user enters an invalid input, they will receive a clear error message prompting them to try again with one of the accepted formats.

## Alignment with Project Goals

This enhancement supports UVI's commitment to a user-friendly CLI experience by:

1. Reducing friction in the project creation process
2. Following the principle of least surprise by accepting common input formats
3. Maintaining backward compatibility with existing workflows
4. Improving the overall user experience with more intuitive input handling

## Future Considerations

After this enhancement is implemented and tested, potential future improvements could include:

1. Extending similar flexible input handling to other question types
2. Adding color-coded prompts and responses for better visual clarity
3. Implementing input history and tab completion for frequent choices
