#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""



def isWinner(x, nums):
    """
    Determines the winner of the Prime Game based on the number of rounds played and the list of numbers provided.

    Args:
        x (int): The number of rounds to be played in the game.
        nums (list): A list of numbers.

    Returns:
        str or None: 
            - If x <= 0 or nums is None, returns None.
            - If x is not equal to the length of nums, returns None.
            - If there is a winner, returns the name of the winner ("Ben" or "Maria").
            - If there is no winner, returns None.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Removes multiples of primes from the given list.

    Args:
        ls (list): The list from which multiples of primes will be removed.
        x (int): The prime number whose multiples are to be removed from the list.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break