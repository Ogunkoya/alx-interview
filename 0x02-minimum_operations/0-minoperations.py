#!/usr/bin/python3

def minOperations(n):
    '''
    method that calculates the fewest number of operations needed 
    to result in exactly n H characters in the file
    '''

    if n == 1:
        return 0
    
    # Find smallest prime factors
    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i

    return n