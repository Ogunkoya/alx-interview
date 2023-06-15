#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each amount from 0 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through all possible amounts from 1 to total
    for amount in range(1, total + 1):
        # Iterate through each coin value
        for coin in coins:
            # Check if the coin value is less than or equal to the current amount
            if coin <= amount:
                # Calculate the number of coins needed for the current amount
                num_coins = min_coins[amount - coin] + 1
                # Update the fewest number of coins if it is smaller than the current value
                min_coins[amount] = min(min_coins[amount], num_coins)

    # Return the fewest number of coins needed to meet the total
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]