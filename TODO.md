# TODO

- [ ] move from tox to nox
- [x] fully commit to ruff by removing other linters and formatters
- [ ] comment extra styles in the mkdocs.yml conf
- [ ] add possibility to use an org instead of a user account for github
- [ ] use git user name and email in the project to prefill the cookiecutter prompts
- [ ] Add trusted pypi publishing to the project
- [ ] Ensure project description is printed to the github site repo page
- [ ] Ensure user has gh cli installed
- [ ] Ensure user has uv cli installed
- [ ] `info/` dir code needs proper ruff linting fixes!
- [ ] ~Pylint is included in this project but the option to add it is not available in the prompt arguments~ (Resolved: Replaced by Ruff with Pylint-equivalent rules)
- [ ] Add python_version option
- [ ] Add codemapper option. This would add codemapper to the project deps in case the user wants to use it.
- [ ] Consider adding how to handle .env files in the project. Could be handy to have a prompt argument that ask for repo secrets and add them via gh cli.
- [ ] Improve the docs-deploy function in our root MakeFile.
