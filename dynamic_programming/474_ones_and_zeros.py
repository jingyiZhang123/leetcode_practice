"""
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

"""

# m: num of 0
# n: num of 1
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def zeros_ones(string):
            num_zero = num_one = 0
            for i in string:
                if i == '0': num_zero += 1
                else: num_one += 1
            return num_zero, num_one

        num_str = len(strs)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for z,o in [zeros_ones(s) for s in strs]:
            for zz in range(m, -1, -1):
                for oo in range(n, -1, -1):
                    if zz >= z and oo >= o:
                        dp[zz][oo] = max(dp[zz][oo], dp[zz-z][oo-o] + 1)
        return dp[m][n]









