# python-template
Base python template repository to use as a starting point for Python projects.

## Getting Started

1. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/).
1. Decide what type of project needs to be created [`uv` projects](https://docs.astral.sh/uv/guides/projects/#project-structure)
    - Run the necessary `uv init` command for that project - e.g. `uv init --lib`
1. Copy the default values `ruff`, `mypy`, `pytest`, and `coverage` into `./pyproject.toml`
    - Run the following if you dont want to make any changes to defaults `echo ./pyproject.toml.bak >> ./pyproject.toml`
1. Install dependencies `uv add --dev pre-commit ruff mypy pytest pytest-cov`
1. Install `pre-commit` hooks `uv run pre-commit install`
1. Start writing code

## Code Quality

This template comes with pre-configured options to use [`ruff`](https://docs.astral.sh/ruff) for linting and formatting of code.

Format wise this performs very similarly to `black` and the lint rules are meant to be a collection of `flake8` plugins. All these settings can be configured in [`pyproject.toml`](./pyproject.toml) - check out the opinionated defaults in [`pyproject.toml.bak`](./pyproject.toml.bak).

### Pre-commit

Code quality is upheld by using git's pre-commit hooks - a python package of [`pre-commit`](https://pre-commit.com). By installing these, the linting formatting and static analysis tools that are pre-configured will be run on every commit. And to escape them on a specific commit, one can `git commit -m "hacky commit" --no-verify`

## Changelog

The `CHANGELOG.md` is maintained by a tool [`changie`](https://changie.dev) which helps in quickly creating fragments from CLI and then making a nicely formatted CHANGELOG for each version.

Some common workflows would be:

```bash
## Add a changelog fragment
changie new
# Type of change ...
# contents of change...
# Author of change ...
git add .changes
git commit -m "add changelog fragment"
git push

## Create a release
changie merge auto --dry-run
# inspect version output etc
changie merge auto
changie batch
git add .
git commit -m "release VERSION"
```

## Dependencies and Virtualenv

Use [uv](https://docs.astral.sh/uv/) for fast dependency resolution and python version management.

This repository has a preset of using Python3.12 (see [`.python-version`](./.python-version))

To change this to another Python version, use `uv python pin <VERSION>` which accepts alternate Python versions like PyPy.

### Virtualenv

`uv` follows the PEP-405 virtualenv directive - so all dependencies will install in `.venv` by default. To activate the virtualenv, `source ~/.venv/bin/activate` for Unix machines.

### Adding dependencies

Dependencies are split into two types for uv - necessary and development. Development ones are only necessary for developers as additional tooling in maintaining the code - i.e. test frameworks (`pytest`). Necessary dependencies would be packages used in the main source code - i.e. `numpy`.

To add a necessary dependency: `uv add <PACKAGE>`

To add a development dependency: `uv add --dev <PACKAGE>`

## GitHub Actions CI

This repository includes 3 CI actions out of the box - inside the `.github` directory:

1. `changelog.yaml` - fails if Pull Requests don't contribute a CHANGELOG fragment.
1. `pre-commit.yaml` - Fails if a commit doesn't match configured style and format conventions.
1. `tests.yaml` - Runs `pytest` and reports about failures.

### After cloning

Depending on your choice of naming scheme (and `git` version) the following actions may need to be done to avoid misconfiguration failures.

1. `changelog.yaml` - Change the name of your default branch for comparing CHANGELOG fragments.