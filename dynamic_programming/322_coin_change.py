"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        min_coin = [amount+1 for _ in range(amount+1)]
        min_coin[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    min_coin[i] = min(min_coin[i], min_coin[i - coin] + 1)

        return min_coin[amount] if min_coin[amount] != amount + 1 else -1

print(Solution().coinChange([2], 3))













