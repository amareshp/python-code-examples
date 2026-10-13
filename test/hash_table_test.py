"""Behavioral tests for the two-sum algorithm."""

import pytest

from dsa.hash_table import two_sum


@pytest.mark.parametrize(
    "numbers,target,expected",
    [([2, 7, 11, 15], 9, (0, 1)), ([-3, 4, 3], 0, (0, 2)),
     ([1.5, 2.5], 4.0, (0, 1))],
)
def test_two_sum_finds_pair(numbers, target, expected):
    """Check that each supplied input yields the expected pair of indices."""
    assert two_sum(numbers, target) == expected


@pytest.mark.parametrize("numbers,target", [([3, 3], 6), ([0, 0], 0)])
def test_two_sum_uses_distinct_entries_for_duplicates(numbers, target):
    """Verify equal values can pair when they occupy distinct positions."""
    assert two_sum(numbers, target) == (0, 1)


@pytest.mark.parametrize(
    "numbers,target", [([], 0), ([3], 6), ([1, 2, 3], 10)]
)
def test_two_sum_returns_none_when_pair_is_absent(numbers, target):
    """Check empty, singleton, and unmatched inputs return None."""
    assert two_sum(numbers, target) is None


@pytest.mark.parametrize("target", [9, 100])
def test_two_sum_prints_inputs(target, capsys):
    """Use captured stdout to verify inputs print even when no pair exists."""
    two_sum([2, 7], target)
    assert capsys.readouterr().out == f"Numbers: [2, 7]\nTarget sum: {target}\n"


def test_two_sum_preserves_input():
    """Compare the list to its original values after finding a pair."""
    numbers = [2, 7, 11, 15]
    two_sum(numbers, 9)
    assert numbers == [2, 7, 11, 15]
