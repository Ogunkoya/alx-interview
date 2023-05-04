#!/usr/bin/python3

def minOperations(n):
    '''
    method that calculates the fewest number of operations needed 
    to result in exactly n H characters in the file
    '''

    if n == 1:
        return 0
    
    
    for index in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n / index)) + index

    return n