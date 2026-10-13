from dsa.linear_examples import max_profits


def main():
    """Run the maximum-profit demonstration and print its inputs and result.

    Takes no parameters and returns None. Pass chronological sample prices
    to max_profits and print the maximum profit from one transaction.
    Runtime and auxiliary space are O(1) for this fixed-size sample input.
    """
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices}")
    print(f"Maximum profit: {max_profits(prices)}")


if __name__ == "__main__":
    main()
