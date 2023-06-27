#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        primes = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)

        turns = 0
        while len(primes) > 0:
            if turns % 2 == 0:
                player = "Maria"
            else:
                player = "Ben"

            selected_prime = primes[0]
            primes = [num for num in primes if num % selected_prime != 0]
            turns += 1

        if turns % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = []
    for n in nums:
        winners.append(play_game(n))

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None