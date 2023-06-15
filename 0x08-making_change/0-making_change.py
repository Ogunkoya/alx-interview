#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
import sys


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be met using the coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total is 0 or less, returns 0.
             If the total cannot be met by any number of coins, returns -1.

    """
    if total <= 0:
        return 0
    table = [sys.maxsize for i in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = table[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    if table[total] == sys.maxsize:
        return -1