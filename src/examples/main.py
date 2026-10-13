from dsa.linear_examples import first_missing_positive


def main():
    """Run the first-missing-positive demonstration and print each result.

    Takes no parameters and returns None. Print two sample integer lists and
    the smallest positive integer missing from each, passing copies to
    first_missing_positive so the printed samples are not rearranged.
    Runtime and auxiliary space are O(1) for these fixed-size sample inputs.
    """
    for numbers in ([3, 4, -1, 1], [1, 2, 3]):
        print(f"Numbers: {numbers}")
        print(f"First missing positive: {first_missing_positive(numbers.copy())}")


if __name__ == "__main__":
    main()
