#!/usr/bin/python3
"""
Module to find least change needed
"""


def makeChange(coins, total):
    """
    Function to determine the min number of coins needed to equal
    sum of a given total amount.
    Args:
        coins (list): List containing coin denominations (integers > 0)
        total (int): Target amount to make change for
    Returns:
        int: Min number of coins needed, -1 if impossible,
        0 if total <= 0
    """

    if total <= 0:
        return 0
    if not coins:
        return -1

    coins_needed = [total + 1] * (total + 1)
    coins_needed[0] = 0

    for amount in range(1, total + 1):

        for coin in coins:
            if coin <= amount:

                coins_needed[amount] = min(
                        coins_needed[amount],
                        coins_needed[amount - coin] + 1
                        )

    return -1 if coins_needed[total] > total else coins_needed[total]
