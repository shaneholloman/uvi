# Test coverage with codecov

Code coverage is a tool used to identify lines of code in a software project that have not been tested. It is often expressed as a percentage of the number of lines tested divided by the total number of lines in the codebase. For example, a code coverage of 91% means that 91% of the codebase has been tested, leaving 9% untested. The tool helps developers ensure that all parts of the code are tested, improving the overall quality of the software.

If `codecov` is set to `"y"`, `pytest-cov` is added as a development dependency,
and `make test` will run the tests and output a coverage report as `coverage.xml`.
If `include_github_actions` is set to `"y"`, coverage tests with [codecov](https://about.codecov.io/) are added to the CI/CD pipeline. To enable this, sign up at [codecov.io](https://about.codecov.io/) with your GitHub account.
Additionally, a `codecov.yaml` file is created, with the following defaults:

```yaml
# Badge color changes from red to green between 70% and 100%
# PR pipeline fails if codecov falls with 1%

coverage:
  range: 70..100
  round: down
  precision: 1
  status:
    project:
      default:
        target: auto
        threshold: 1%

# Ignoring Paths
# --------------
# which folders/files to ignore
ignore:
  - "foo/bar.py"
```

If `codecov` is set to `"n"`, `pytest-cov` is not added to the development dependencies and the github actions won't produce a coverage report.
