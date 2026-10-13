# Function documentation

Functions should have docstrings that explain:

- **Purpose:** What the function does.
- **Parameters:** What each parameter represents, including any constraints or assumptions.
- **Return values:** What the function returns, including special cases such as `None`.
- **Implementation logic:** How the function works, describing the algorithm and key steps clearly enough to make the implementation easy to understand.
- **Runtime complexity:** Include Big O notation where practical, such as O(1) or O(n). Define the input size variables used and explain relevant assumptions.

# Tests

- Keep pytest tests in the project-root `test/` directory.
- Name each test file after its source module using `<source_stem>_test.py`, for example `linear_examples_test.py` for `src/dsa/linear_examples.py`.
- Aim for about five test functions per source module with executable behavior. Package `__init__.py` files that contain only documentation do not need separate tests.
- Use parameterization to cover normal cases, boundary conditions, missing results, duplicates, zeros, and negative values where relevant. Cover every public function in a module.
- Assert observable behavior and documented guarantees, including input preservation and printed output where relevant. Avoid tests tied to internal implementation steps.
- Give tests concise docstrings describing the behavior and how it is checked. Detailed parameter, return-value, and complexity documentation is primarily for application functions.
- Pytest discovery is configured in `pyproject.toml` with `testpaths = ["test"]`, `python_files = ["*_test.py"]`, and `pythonpath = ["src"]`.
- Pytest is a development dependency. Run `uv sync --group dev` to install it and `uv run pytest` from the project root to run the suite. Run the relevant tests after code changes and the full suite before completing work.
