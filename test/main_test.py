"""Behavioral tests for the maximum-profit application entrypoint."""

from pathlib import Path
import subprocess
import sys

from examples import main as app


def test_main_prints_sample_prices_and_profit(capsys):
    """Capture stdout and check the complete sample output."""
    app.main()
    assert capsys.readouterr().out == (
        "Prices: [7, 1, 5, 3, 6, 4]\nMaximum profit: 5\n"
    )


def test_main_returns_none(capsys):
    """Run the entrypoint and check its documented None return value."""
    assert app.main() is None


def test_main_passes_chronological_sample_to_max_profits(monkeypatch, capsys):
    """Record calls with a stub and verify one call with the sample prices."""
    calls = []

    def record_prices(prices):
        """Record the supplied prices and return a constant stub profit."""
        calls.append(prices.copy())
        return 5

    monkeypatch.setattr(app, "max_profits", record_prices)
    app.main()
    assert calls == [[7, 1, 5, 3, 6, 4]]


def test_main_prints_profit_returned_by_algorithm(monkeypatch, capsys):
    """Substitute a distinct profit to ensure the printed result is computed."""
    monkeypatch.setattr(app, "max_profits", lambda prices: 42)
    app.main()
    assert "Maximum profit: 42\n" in capsys.readouterr().out


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
    assert result.stdout == "Prices: [7, 1, 5, 3, 6, 4]\nMaximum profit: 5\n"
    assert result.stderr == ""
