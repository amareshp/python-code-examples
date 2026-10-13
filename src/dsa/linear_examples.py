def max_profits(prices):
    """Find the maximum profit from at most one buy followed by one sell.

    Args:
        prices: Finite numeric prices in chronological order, with each entry
            representing one time step. The input is not modified. Prices
            must support comparison and subtraction; their validity is not
            checked by this function.

    Returns:
        The largest nonnegative difference between a later selling price and
        an earlier buying price. Returns 0 for empty input, a single price,
        or when no profitable transaction exists. Returns only the profit,
        not the buy and sell indices.

    Logic:
        Start with zero profit and an infinite minimum price. Scan the prices
        once, updating the minimum price seen so far at each step. Subtract
        that minimum from the current price to compute the potential profit,
        then keep the larger of this profit and the best previous profit.
        Updating the minimum first lets the current price produce a zero
        profit, but a positive profit always uses an earlier buying price.
        This preserves chronological order without examining every pair.

    Complexity:
        Runtime is O(n), where n is the number of prices, assuming O(1)
        comparisons and arithmetic. Auxiliary space is O(1), since only
        the running minimum price and maximum profit are stored.
    """
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

def product_of_array_except_self(nums):
    """Return the product of all other elements for each input position.

    Args:
        nums: Sequence of numbers supporting multiplication, including zeros
            and negative values. Assumes O(1) indexing and length access,
            as provided by a list or tuple. The input is not modified.
            Floating-point products follow normal rounding behavior.

    Returns:
        A new list of the same length as nums, where result[i] is the product
        of every input element except nums[i]. Empty input returns []. A
        single-element input returns [1], since the product of no elements
        is 1. With exact arithmetic on finite values, one zero means only
        that zero's position can have a nonzero product; multiple zeros mean
        all results are zero.

    Logic:
        Initialize the result list and both running products to 1. In the
        left-to-right pass, multiply each result slot by left_product before
        multiplying left_product by the current input value. Each slot then
        contains the product of elements strictly to its left. In the
        right-to-left pass, multiply each slot by right_product before
        multiplying right_product by the current input value. Combining the
        left and right products excludes the current element. This uses two
        passes without division or separate prefix and suffix arrays.

    Complexity:
        Runtime is O(n), where n = len(nums), assuming O(1) multiplication,
        indexing, and length access. Auxiliary space is O(1) beyond the O(n)
        output list. Large integer products can increase multiplication cost
        and the memory needed to store each product.
    """
    left_product = 1
    right_product = 1
    result = [1] * len(nums)
    for i in range(len(nums)):
        result[i] *= left_product
        left_product *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result
