def two_sum(
    numbers: list[int | float], target_sum: int | float
) -> tuple[int, int] | None:
    """Find two distinct entries whose values add up to the target sum.

    Args:
        numbers: List of integers or floats to search. Duplicate values are
            allowed, and the list is not modified. Floating-point matching
            uses exact dictionary key equality, without a rounding tolerance.
        target_sum: Desired sum of the two entries.

    Returns:
        A tuple of zero-based indices (earlier_index, current_index) for the
        first match found while scanning from left to right. Returns None
        if no pair exists, including for lists with fewer than two entries.

    Logic:
        Print the input list and target sum before searching. Scan the list
        once, keeping a dictionary that maps each previously seen value to
        its most recent index. For each number, compute the complement as
        target_sum - number. If the complement is in the dictionary, return
        its stored index and the current index. Otherwise, store the current
        number and index, then continue. Checking before storing prevents an
        entry from being paired with itself while allowing duplicate values
        at different indices. Return None after exhausting the list.

    Complexity:
        Expected runtime is O(n), where n is the length of numbers, assuming
        O(1) arithmetic and average O(1) dictionary lookups and insertions.
        Worst-case runtime is O(n^2) if hash collisions make dictionary
        operations O(n). Auxiliary space is O(n) for the dictionary. Printing
        also takes time proportional to the length of the formatted inputs.
    """
    print(f"Numbers: {numbers}")
    print(f"Target sum: {target_sum}")

    seen: dict[int | float, int] = {}
    for index, number in enumerate(numbers):
        complement = target_sum - number
        if complement in seen:
            return seen[complement], index
        seen[number] = index

    return None
