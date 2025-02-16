#! /usr/bin/env bash

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Source cargo environment with error handling
CARGO_ENV="${HOME}/.cargo/env"
if [[ -f "${CARGO_ENV}" ]]; then
    # shellcheck disable=SC1090
    source "${CARGO_ENV}"
else
    export PATH="${HOME}/.cargo/bin:${PATH}"
fi

# Install Dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install --install-hooks
