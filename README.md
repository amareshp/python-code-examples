# python-code-examples

Application source code lives under `src`. The entrypoint is
`src/examples/main.py`, and algorithms live in `src/dsa`.

```text
src/
├── dsa/
│   ├── __init__.py
│   ├── hash_table.py
│   ├── linear_examples.py
│   └── search_examples.py
└── examples/
    ├── __init__.py
    └── main.py
test/
├── hash_table_test.py
├── linear_examples_test.py
├── main_test.py
└── search_examples_test.py
```

Requires Python 3.14 or newer. Run uv commands from the `python-code-examples`
project root. Run the application with uv:

```sh
uv run python-code-examples
```

Or run the entrypoint as a module:

```sh
uv run python -m examples.main
```

The sample calls `max_profits([7, 1, 5, 3, 6, 4])` and prints the prices
and maximum profit `5` (buy at `1`, sell later at `6`). The function allows
at most one transaction and returns `0` when no profitable transaction exists.

## Tests

Install the development dependencies and run the pytest suite from the project root:

```sh
uv sync --group dev
uv run pytest
```

Run a single module's tests with:

```sh
uv run pytest test/linear_examples_test.py
```

Each source module with executable behavior has a matching `<source_stem>_test.py`
file with five test functions. Parameterized cases cover additional inputs,
including empty and singleton lists, missing results, duplicates, zeros, negative
numbers, input preservation, and entrypoint output. The package `__init__.py`
files contain only documentation and have no separate tests.

Pytest discovery and the `src` import path are configured in `pyproject.toml`.

## Virtual environment after a folder rename

If your terminal still has the old environment activated, run `deactivate` first.
From the renamed project root, recreate the environment and install dependencies:

```sh
uv venv --clear --prompt python-code-examples .venv
uv sync --group dev
source .venv/bin/activate
```

`VIRTUAL_ENV` should now point to the `.venv` inside `python-code-examples`.
Activation is optional for `uv run`, but a terminal with the old environment
activated must be deactivated or switched to the new environment to remove
the mismatch warning.

In PyCharm, select `python-code-examples/.venv/bin/python` as the project
interpreter if it still references the old project folder.
