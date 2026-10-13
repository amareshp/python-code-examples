"""Behavioral tests for binary search on ascending sequences."""

import pytest

from dsa.search_examples import binary_search


@pytest.mark.parametrize("target,expected", [(2, 0), (11, 2), (15, 3)])
def test_binary_search_finds_targets(target, expected):
    """Check that first, interior, and last targets return their indices."""
    assert binary_search([2, 7, 11, 15], target) == expected


@pytest.mark.parametrize(
    "numbers,target", [([], 0), ([2, 7, 11, 15], 1),
                       ([2, 7, 11, 15], 10), ([2, 7, 11, 15], 20)]
)
def test_binary_search_returns_minus_one_when_absent(numbers, target):
    """Check empty input and targets below, within, or above the value range."""
    assert binary_search(numbers, target) == -1


def test_binary_search_accepts_any_matching_duplicate():
    """Verify a duplicate match without requiring its first or last index."""
    numbers = [-3, 2, 2, 2, 8]
    index = binary_search(numbers, 2)
    assert 0 <= index < len(numbers)
    assert numbers[index] == 2


@pytest.mark.parametrize("target,expected", [(5, 0), (4, -1), (6, -1)])
def test_binary_search_handles_singleton(target, expected):
    """Check both matching and absent targets for a one-element list."""
    assert binary_search([5], target) == expected


def test_binary_search_preserves_input():
    """Search negative values and confirm their original order is preserved."""
    numbers = [-8, -3, 0, 4]
    assert binary_search(numbers, -3) == 1
    assert numbers == [-8, -3, 0, 4]
