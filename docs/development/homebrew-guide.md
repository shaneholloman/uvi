# Making uvi Available via Homebrew

This guide outlines the process of making `uvi` available through Homebrew, both via a personal tap and through Homebrew Core.

## Option 1: Submit to Homebrew Core (Recommended)

### 1. Prepare Formula

```ruby
class Uvi < Formula
  include Language::Python::Virtualenv

  desc "Python cookiecutter application for creating uv-managed projects"
  homepage "https://github.com/shaneholloman/uvi"
  url "https://api.github.com/repos/shaneholloman/uvi/releases/latest", headers: ["Accept: application/vnd.github.v3+json"]
  license "MIT"
  head "https://github.com/shaneholloman/uvi.git", branch: "main"

  depends_on "python@3.12"
  depends_on "uv"

  on_linux do
    depends_on "pkg-config" => :build
  end

  resource "cookiecutter" do
    url "https://pypi.org/pypi/cookiecutter/json"
    regex(/latest_version": "([^"]+)"/)
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/uvi", "--version"
  end
end
```

### 2. Submit to Homebrew Core

1. Fork the [Homebrew Core repository](https://github.com/Homebrew/homebrew-core)
2. Create a new branch: `git checkout -b add-uvi`
3. Add your formula to `Formula/u/uvi.rb`
4. Test locally:
   ```bash
   brew test-bot --only-formulae uvi
   ```
5. Create a Pull Request

## Option 2: Personal Tap

### 1. Create Homebrew Tap Repository

1. Create a new GitHub repository named `homebrew-tools`
2. Clone it locally:
   ```bash
   git clone git@github.com:shaneholloman/homebrew-tools.git
   cd homebrew-tools
   ```

3. Add the formula file:
   ```bash
   mkdir -p Formula
   # Copy the formula from above into Formula/uvi.rb
   ```

### 2. Automated Updates Workflow

Create `.github/workflows/update-formula.yml`:

```yaml
name: Update Formula

on:
  repository_dispatch:
    types: [uvi-release]
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to update to (leave empty for latest)'
        required: false

jobs:
  update-formula:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          
      - name: Get package info
        id: package
        run: |
          VERSION=${{ github.event.inputs.version || github.event.client_payload.version }}
          URL="https://files.pythonhosted.org/packages/source/u/uvi/uvi-${VERSION}.tar.gz"
          curl -L -o uvi.tar.gz "$URL"
          SHA=$(sha256sum uvi.tar.gz | cut -d' ' -f1)
          echo "version=${VERSION}" >> $GITHUB_ENV
          echo "url=${URL}" >> $GITHUB_ENV
          echo "sha=${SHA}" >> $GITHUB_ENV
          
      - name: Update formula
        run: |
          sed -i "s|url.*|url \"${{ env.url }}\"|" Formula/uvi.rb
          sed -i "s|sha256.*|sha256 \"${{ env.sha }}\"|" Formula/uvi.rb
          
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v6
        with:
          commit-message: "feat: update uvi to ${{ env.version }}"
          title: "Update uvi to ${{ env.version }}"
          body: |
            Updates uvi formula to version ${{ env.version }}
            
            - URL: ${{ env.url }}
            - SHA256: ${{ env.sha }}
          branch: update-uvi
          delete-branch: true
```

### 3. Trigger Updates

Add to your main `uvi` repository's release workflow:

```yaml
  update-homebrew:
    needs: [publish]  # Assuming you have a publish job
    runs-on: ubuntu-latest
    steps:
      - name: Trigger formula update
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.WORKFLOW_TOKEN }}
          repository: shaneholloman/homebrew-tools
          event-type: uvi-release
          client-payload: '{"version": "${{ github.ref_name }}"}'
```

### 4. Installation Instructions

Users can install via:

```bash
# Add tap (one-time)
brew tap shaneholloman/tools

# Install uvi
brew install uvi
```

## Required Actions

1. **For Homebrew Core**:
   - [ ] Get current PyPI package URL
   - [ ] Calculate SHA256
   - [ ] Submit PR to Homebrew Core
   - [ ] Address reviewer feedback

2. **For Personal Tap**:
   - [ ] Create homebrew-tools repository
   - [ ] Set up GitHub Actions workflow
   - [ ] Add WORKFLOW_TOKEN secret
   - [ ] Update release workflow in main repository
   - [ ] Test installation process

## Notes

- The personal tap approach gives you more control but requires users to add your tap
- Homebrew Core is preferred for wider distribution
- Both approaches can be maintained simultaneously
- Update automation only works with the personal tap approach
