"""Behavioral tests for the first-missing-positive application entrypoint."""

from pathlib import Path
import subprocess
import sys

from examples import main as app

EXPECTED_OUTPUT = (
    "Numbers: [3, 4, -1, 1]\nFirst missing positive: 2\n"
    "Numbers: [1, 2, 3]\nFirst missing positive: 4\n"
)


def test_main_prints_samples_and_results(capsys):
    """Capture stdout and check the complete sample output."""
    app.main()
    assert capsys.readouterr().out == EXPECTED_OUTPUT


def test_main_returns_none(capsys):
    """Run the entrypoint and check its documented None return value."""
    assert app.main() is None


def test_main_passes_both_samples_to_first_missing_positive(monkeypatch, capsys):
    """Record calls with a stub and verify one call per sample, in order."""
    calls = []

    def record_numbers(numbers):
        """Record the supplied numbers and return a constant stub result."""
        calls.append(numbers.copy())
        return 1

    monkeypatch.setattr(app, "first_missing_positive", record_numbers)
    app.main()
    assert calls == [[3, 4, -1, 1], [1, 2, 3]]


def test_main_prints_result_returned_by_algorithm(monkeypatch, capsys):
    """Substitute a distinct result to ensure the printed value is computed."""
    monkeypatch.setattr(app, "first_missing_positive", lambda numbers: 42)
    app.main()
    assert capsys.readouterr().out.count("First missing positive: 42\n") == 2


def test_main_runs_as_module():
    """Launch the module in a subprocess and verify successful sample output."""
    result = subprocess.run(
        [sys.executable, "-m", "examples.main"],
        cwd=Path(__file__).resolve().parents[1] / "src",
        capture_output=True,
        text=True,
        check=True,
        timeout=10,
    )
    assert result.stdout == EXPECTED_OUTPUT
    assert result.stderr == ""
