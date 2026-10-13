"""Behavioral tests for the linear-scan array examples."""

import pytest

from dsa.linear_examples import (
    first_missing_positive,
    max_area,
    max_profits,
    product_of_array_except_self,
)


@pytest.mark.parametrize(
    "prices,expected",
    [([7, 1, 5, 3, 6, 4], 5), ([1, 2, 3, 4], 3),
     ([2, 4, 1], 2), ([1, 5, 2, 8], 7), ([1.5, 2.0, 1.0, 3.5], 2.5)],
)
def test_max_profits_finds_best_single_transaction(prices, expected):
    """Check profit, buy-before-sell order, and input preservation per case."""
    original = prices.copy()
    assert max_profits(prices) == expected
    assert prices == original


@pytest.mark.parametrize("prices", [[], [5], [7, 6, 4, 3, 1], [3, 3, 3]])
def test_max_profits_returns_zero_without_profitable_trade(prices):
    """Check that insufficient or unprofitable prices produce zero profit."""
    assert max_profits(prices) == 0


@pytest.mark.parametrize(
    "numbers,expected",
    [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 2, -3], [-6, 3, -2]),
     ([1.5, 2.0, 4.0], [8.0, 6.0, 3.0])],
)
def test_product_except_self_multiplies_other_entries(numbers, expected):
    """Check integer and float products in a new list without mutating input."""
    original = numbers.copy()
    result = product_of_array_except_self(numbers)
    assert result == expected
    assert result is not numbers
    assert numbers == original


@pytest.mark.parametrize(
    "numbers,expected", [([0, 2, 3], [6, 0, 0]), ([2, 0, 3], [0, 6, 0]),
                         ([2, 3, 0], [0, 0, 6]), ([0, 2, 0], [0, 0, 0])]
)
def test_product_except_self_handles_zeros(numbers, expected):
    """Check single zeros at each position and multiple-zero inputs."""
    assert product_of_array_except_self(numbers) == expected


@pytest.mark.parametrize(
    "numbers,expected", [([], []), ([5], [1]), ([0], [1]), ([2, 3], [3, 2])]
)
def test_product_except_self_handles_short_inputs(numbers, expected):
    """Check the empty-product convention and the smallest nontrivial pair."""
    assert product_of_array_except_self(numbers) == expected


@pytest.mark.parametrize(
    "heights,expected",
    [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([4, 3, 2, 1, 4], 16),
     ([1, 2, 1], 2), ([2, 3, 4, 5, 18, 17, 6], 17), ((1, 1), 1)],
)
def test_max_area_finds_largest_container(heights, expected):
    """Check the best container area and that the input is not modified."""
    original = list(heights)
    assert max_area(heights) == expected
    assert list(heights) == original


@pytest.mark.parametrize("heights", [[], [5], [0]])
def test_max_area_returns_zero_with_fewer_than_two_lines(heights):
    """Check that inputs without a pair of lines hold no water."""
    assert max_area(heights) == 0


@pytest.mark.parametrize(
    "heights,expected",
    [([0, 0], 0), ([0, 5, 0], 0), ([0, 5, 0, 5, 0], 10), ([0, 0, 0, 7], 0)],
)
def test_max_area_handles_zero_heights(heights, expected):
    """Check that zero-height lines bound containers holding no water."""
    assert max_area(heights) == expected


@pytest.mark.parametrize(
    "heights,expected",
    [([4, 4, 4, 4], 12), ([3, 1, 3], 6), ([1, 2, 3, 4, 5], 6),
     ([5, 4, 3, 2, 1], 6)],
)
def test_max_area_handles_duplicates_and_monotonic_heights(heights, expected):
    """Check equal-height ties and strictly increasing or decreasing lines."""
    assert max_area(heights) == expected


@pytest.mark.parametrize("heights", [[-1, 2], [3, -4, 5], [-1, -1]])
def test_max_area_rejects_negative_heights(heights):
    """Check that a ValueError is raised for any negative line height."""
    with pytest.raises(ValueError):
        max_area(heights)


@pytest.mark.parametrize(
    "numbers,expected",
    [([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1), ([1, 2, 0], 3),
     ([2, 3, 4], 1), ([5, 1, 3, 2], 4)],
)
def test_first_missing_positive_finds_smallest_absent_value(numbers, expected):
    """Check gaps at the start, middle, and among out-of-range values."""
    assert first_missing_positive(numbers) == expected


@pytest.mark.parametrize(
    "numbers,expected",
    [([1], 2), ([2, 1], 3), ([1, 2, 3], 4), ([4, 3, 2, 1, 5], 6)],
)
def test_first_missing_positive_returns_next_after_full_range(numbers, expected):
    """Check that len(nums) + 1 is returned when 1..len(nums) are present."""
    assert first_missing_positive(numbers) == expected


@pytest.mark.parametrize(
    "numbers,expected",
    [([1, 1], 2), ([2, 2], 1), ([3, 3, 1], 2), ([1, 1, 2, 2], 3),
     ([7, 7, 7], 1)],
)
def test_first_missing_positive_handles_duplicates(numbers, expected):
    """Check that repeated values terminate and do not count as extra values."""
    assert first_missing_positive(numbers) == expected


@pytest.mark.parametrize(
    "numbers", [[], [0], [-1], [0, 0], [-3, -2, -1], [-1, 0, 2]],
)
def test_first_missing_positive_returns_one_without_one(numbers):
    """Check empty, zero, and negative inputs where 1 is missing."""
    assert first_missing_positive(numbers) == 1


@pytest.mark.parametrize(
    "numbers", [[3, 4, -1, 1], [2, 2, 0, -5], [1, 2, 3]],
)
def test_first_missing_positive_keeps_same_elements(numbers):
    """Check that in-place rearranging neither adds nor removes elements."""
    original = sorted(numbers)
    first_missing_positive(numbers)
    assert sorted(numbers) == original
