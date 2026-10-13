def binary_search(arr, target):
    """Find a target value in a sequence sorted in ascending order.

    Args:
        arr: Ascending sequence whose elements support comparison with target.
            Assumes O(1) indexing and length access, as provided by a list or
            tuple. The sequence is not sorted, validated, or modified here.
        target: Value to locate in arr.

    Returns:
        The zero-based index of a matching element, or -1 if target is absent
        or arr is empty. If duplicates exist, any matching index may be
        returned; the result is not necessarily the first or last occurrence.

    Logic:
        Keep inclusive start and end indices for the remaining search range.
        Compare the middle element with target. Return its index on equality.
        If it is smaller, search only the right half; otherwise, search only
        the left half. Exclude the middle element when updating either bound
        so each iteration shrinks the range. Return -1 when the range is empty.

    Complexity:
        Worst-case runtime is O(log n) for n = len(arr), assuming O(1) indexing
        and comparisons. An empty sequence takes O(1) time. Auxiliary space
        is O(1) because only the bounds and middle index are stored.
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
