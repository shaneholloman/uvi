.PHONY: bake
bake: ## bake without inputs and overwrite if exists.
	@uv run cookiecutter --no-input . --overwrite-if-exists

.PHONY: bake-with-inputs
bake-with-inputs: ## bake with inputs and overwrite if exists.
	@uv run cookiecutter . --overwrite-if-exists

.PHONY: bake-and-test-deploy
bake-and-test-deploy: ## For quick publishing to uvi-example to test GH Actions
	@rm -rf uvi-example || true
	@uv run cookiecutter --no-input . --overwrite-if-exists \
		author="Shane Holloman" \
		email="shaneholloman@gmail.com" \
		github_author_handle=shaneholloman \
		project_name=uvi-example \
		project_slug=uvi_example
	@cd uvi-example; uv sync && \
		git init -b main && \
		git add . && \
		uv run pre-commit install && \
		uv run pre-commit run -a || true && \
		git add . && \
		uv run pre-commit run -a || true && \
		git add . && \
		git commit -m "init commit" && \
		git remote add origin git@github.com:shaneholloman/uvi-example.git && \
		git push -f origin main


.PHONY: install
install: ## Install the virtual environment
	@echo "Creating virtual environment"
	@uv sync

.PHONY: check
check: ## Run code quality tools.
	@echo "Checking lock file consistency with 'pyproject.toml'"
	@uv lock --locked
	@echo "Linting code: Running pre-commit"
	@uv run pre-commit run -a
	@echo "Static type checking: Running mypy"
	@uv run mypy
	@echo "Checking for obsolete dependencies: Running deptry"
	@uv run deptry .

.PHONY: test
test: ## Test the code with pytest.
	@echo "Testing code: Running pytest"
	@uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

.PHONY: build
build: clean-build ## Build wheel file
	@echo "Creating wheel file"
	@uvx --from build pyproject-build --installer uv

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "Removing build artifacts"
	@uv run python -c "import shutil; import os; shutil.rmtree('dist') if os.path.exists('dist') else None"

.PHONY: publish
publish: ## Publish a release to PyPI.
	@echo "Publishing: Dry run."
	@uvx --from build pyproject-build --installer uv
	@echo "Publishing."
	@uvx twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@uv run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@uv run mkdocs serve

.PHONY: check-gh-cli
check-gh-cli: ## Check if GitHub CLI is installed
	@where gh >nul 2>&1 || ( \
		echo Error: GitHub CLI (gh^) is not installed. Please install it first: && \
		echo Windows (with winget^): winget install GitHub.cli && \
		echo Windows (with scoop^): scoop install gh && \
		echo macOS: brew install gh && \
		echo Linux: See https://github.com/cli/cli/blob/trunk/docs/install_linux.md && \
		exit /b 1 \
	)
	@git rev-parse --git-dir >nul 2>&1 || ( \
		echo Error: Not in a git repository && \
		exit /b 1 \
	)
	@git remote get-url origin >nul 2>&1 || ( \
		echo Error: No git remote 'origin' configured && \
		exit /b 1 \
	)
	@gh auth status >nul 2>&1 || ( \
		echo Error: Not logged in to GitHub. Please run 'gh auth login' first && \
		exit /b 1 \
	)

.PHONY: docs-deploy doc-deploy
docs-deploy: check-gh-cli ## Deploy documentation to GitHub Pages (only deploys if changes detected)
	@powershell -Command " \
		$$remote = git remote get-url origin; \
		if ($$remote -match 'github.com[:/]([^/]+)/([^/.]+)') { \
			$$owner = $$matches[1]; \
			$$repo = $$matches[2]; \
			$$fullRepo = \"$$owner/$$repo\"; \
			Write-Host \"Detected repository: $$fullRepo\"; \
			Write-Host \"Building documentation...\"; \
			uv run mkdocs build; \
			Write-Host \"Checking for changes...\"; \
			if (Test-Path .git/refs/heads/gh-pages) { \
				$$current = git rev-parse gh-pages; \
				git checkout gh-pages --quiet; \
				$$diff = git diff --quiet HEAD site/ 2>$$null; \
				if ($$LASTEXITCODE -eq 1) { \
					Write-Host \"Changes detected, deploying...\"; \
					Write-Host \"Checking GitHub Pages configuration...\"; \
					$$pages = gh api --method GET /repos/$$fullRepo/pages 2>$$null; \
					if (!$$pages) { \
						Write-Host \"Enabling GitHub Pages...\"; \
						gh api --method PUT /repos/$$fullRepo/pages --field source='{\"branch\":\"gh-pages\",\"path\":\"/\"}' >$$null; \
						Write-Host \"GitHub Pages enabled successfully\"; \
					}; \
					uv run mkdocs gh-deploy --quiet; \
					Write-Host \"Documentation deployed successfully.\"; \
				} else { \
					Write-Host \"No changes detected in documentation.\"; \
				}; \
				git checkout - --quiet; \
			} else { \
				Write-Host \"First deployment, setting up GitHub Pages...\"; \
				gh api --method PUT /repos/$$fullRepo/pages --field source='{\"branch\":\"gh-pages\",\"path\":\"/\"}' >$$null; \
				uv run mkdocs gh-deploy --quiet; \
				Write-Host \"Documentation deployed successfully.\"; \
			}; \
			Write-Host \"You can view your documentation at: https://$$owner.github.io/$$repo/\"; \
		} else { \
			Write-Host \"Error: Could not detect repository information from git remote\" -ForegroundColor Red; \
			exit 1; \
		}"

doc-deploy: docs-deploy  # Alias for docs-deploy

.PHONY: help
help:
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
