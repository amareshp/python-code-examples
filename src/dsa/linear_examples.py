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

def max_area(height):
    """Find the most water a container formed by two vertical lines can hold.

    Args:
        height: Sequence of nonnegative integers, where height[i] is the
            height of a vertical line drawn from (i, 0) to (i, height[i]).
            Assumes O(1) indexing and length access, as provided by a list
            or tuple. The input is not modified.

    Returns:
        The largest value of min(height[i], height[j]) * (j - i) over all
        index pairs i < j. Returns 0 when fewer than two lines are given,
        or when every possible container has zero height or width.

    Raises:
        ValueError: If any height is negative.

    Logic:
        Reject negative heights first, since a line cannot extend below the
        x-axis. Then place one pointer at each end of the sequence, giving
        the widest container. At each step, record the area bounded by the
        shorter of the two lines, then move the pointer at the shorter line
        inward. Any other container using that shorter line would be
        narrower and still limited by that line's height, so it cannot hold
        more water and the line can be discarded. When the heights are
        equal, neither line can do better with an inner partner, so moving
        either pointer is safe. The scan stops when the pointers meet, after
        every line has been discarded or paired once.

    Complexity:
        Runtime is O(n), where n = len(height): one pass validates the
        heights and the pointers move toward each other at most n - 1 times,
        assuming O(1) comparisons and arithmetic. Auxiliary space is O(1),
        since only two indices and the best area are stored.
    """
    if any(h < 0 for h in height):
        raise ValueError("heights must be nonnegative")
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


def first_missing_positive(nums):
    """Find the smallest positive integer that does not appear in nums.

    Args:
        nums: Mutable sequence of integers, such as a list. Values may be
            negative, zero, positive, or repeated. Assumes O(1) indexing,
            length access, and item assignment. The input is rearranged in
            place: it keeps the same elements, but their order may change.
            Pass a copy to preserve the original order.

    Returns:
        The smallest integer k >= 1 that is not an element of nums. Returns
        1 for empty input or when 1 is absent, and len(nums) + 1 when every
        integer from 1 to len(nums) is present.

    Logic:
        With n = len(nums), the answer must lie in 1..n + 1, since n values
        can fill at most the positions 1..n. In the first pass, swap each
        value v in 1..n into index v - 1, its home position. Keep swapping
        at index i until it holds a value outside 1..n or a value whose home
        position already contains it. The second check stops duplicates
        from swapping forever. Each swap places a value at its home, where
        it is never moved again, so there are at most n swaps in total.
        In the second pass, the first index i where nums[i] != i + 1 gives
        the missing value i + 1. If every position matches, all of 1..n
        are present and the answer is n + 1.

    Complexity:
        Runtime is O(n), where n = len(nums): each pass visits n positions
        and the swap loop runs at most n times overall, assuming O(1)
        comparisons and item access. Auxiliary space is O(1), since the
        input itself is used as the lookup table.
    """
    min_positive = 1
    max_positive = len(nums)
    for i in range(len(nums)):
        # Move nums[i] to its home index until this slot holds an
        # out-of-range value or a value already present at its home.
        while (min_positive <= nums[i] <= max_positive) and (nums[nums[i] - 1] != nums[i]):
            # Save the home index first, because the swap changes nums[i].
            correct_index = nums[i] - 1
            nums[correct_index], nums[i] = nums[i], nums[correct_index]
    # The first index not holding i + 1 identifies the missing value.
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1
