# Example Pytest Suite

I wanted to explore adding snapshot and benchmark testing to a library. While the _library_ is not very mature or useful, it does give us enough to do these standard things

## What are these Tests

- Snapshot testing is comparing the output of a function call to itself from a previous version. Usually helpful when comparing something visually, it can also just guarantee that the function behaves the same without having a test with an **EXACT** value that it needs to match. In my mind, this makes sense for even JSON objects - we might care that a produced document is still the same but don't want to write out checking every attribute of said object.

- Benchmark testing is to compare runtimes of a code with analagous hardware in a performance focused test. This can help degradations in algorithm implementations that should be a O(log n) runtime but slows to a O(n).

## Chosen Libraries

- For snapshot testing, [`insta`](https://insta.rs/) from the Rust ecosystem seemed really cool. A similar looking API for pytest was [`pytest-insta`](https://github.com/vberlier/pytest-insta). Just takes adds in a fixture, that you assert equality against.
- For benchmarking, [`pytest-benchmark`](https://pytest-benchmark.readthedocs.io/en/stable/index.html) seemed like the de-facto go to. The only odd thing to show for demonstration is that the benchmarks are unique per platform, Python version and architecture. So if your setup is different than mine, will have to make a reference benchmark before messing around in the code.


## Getting Started

1. Clone this repository `git clone https://github.com/rhyn0/example-pytest-suite.git
1. Enter into the directory and setup the virtualenv. I suggest uv `cd example-pytest-suite && uv sync --all-extras`
1. Run `pytest`. This should create the reference benchmark for the test suite in a folder inside `test/benchmark/.benchmark`.
    - This might have cause an Error, if so go into `pyproject.toml` and comment out line 110 for one run.
1. Try messing with the benchmarked function `src/example_pytest_suite/sorts/merge.py`.
    - Make it slower rather than making it wrong. Maybe a `time.sleep` ?
1. Run the benchmarks again `pytest --benchmark-only` Should notice a that the timing metrics are worse than before, and depending on how much slower might emit a failing exit code.

Now try making the snapshot testing fail:

1. Edit the tested function inside `src/example_pytest_suite/formats/iterable.py`
    - Add a space or another new line possibly.
1. Run `pytest` and should see that the snapshots are failing.
1. If you run the test selectively, with `--insta review` flag, it should give you an interactive accept/deny CLI tool.


### Other nice things

#### Code Quality

This template comes with pre-configured options to use [`ruff`](https://docs.astral.sh/ruff) for linting and formatting of code.

Format wise this performs very similarly to `black` and the lint rules are meant to be a collection of `flake8` plugins. All these settings can be configured in [`pyproject.toml`](./pyproject.toml) - check out the opinionated defaults in [`pyproject.toml.bak`](./pyproject.toml.bak).

##### Pre-commit

Code quality is upheld by using git's pre-commit hooks - a python package of [`pre-commit`](https://pre-commit.com). By installing these, the linting formatting and static analysis tools that are pre-configured will be run on every commit. And to escape them on a specific commit, one can `git commit -m "hacky commit" --no-verify`

##### Changelog

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
