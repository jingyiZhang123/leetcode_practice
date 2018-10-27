"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        diff = [b-a for a,b in zip([0]+prices, prices+[0])][1:-1]
        max_value = diff[0]
        cur_value = diff[0]
        for i in range(1, len(diff)):
            cur_value = diff[i] if diff[i] > (cur_value+diff[i]) else (cur_value+diff[i])
            max_value = max_value if max_value > cur_value else cur_value
        return 0 if max_value <= 0 else max_value

print(Solution().maxProfit([7,1,5,3,6,4]))








