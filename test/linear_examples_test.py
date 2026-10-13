"""Behavioral tests for maximum profit and product except self."""

import pytest

from dsa.linear_examples import max_profits, product_of_array_except_self


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
