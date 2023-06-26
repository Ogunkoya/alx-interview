#!/usr/bin/python3

def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def getPrimes(n):
        primes = []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= n:
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        return primes

    def canWin(primes, num):
        for prime in primes:
            if num % prime == 0:
                return True
        return False

    winner_count = {'Maria': 0, 'Ben': 0}

    for n in nums:
        primes = getPrimes(n)
        if canWin(primes, n):
            winner_count['Maria'] += 1
        else:
            winner_count['Ben'] += 1

    if winner_count['Maria'] > winner_count['Ben']:
        return 'Maria'
    elif winner_count['Maria'] < winner_count['Ben']:
        return 'Ben'
    else:
        return None