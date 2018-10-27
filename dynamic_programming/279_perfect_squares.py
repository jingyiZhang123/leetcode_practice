"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""


class Solution(object):
    def generate_candi(self, n):
        result = []
        for i in range(1, n):
            if i * i > n:
                break
            result.append(i*i)
        return result

    def numSquares(self, n):
        candi = self.generate_candi(n)
        memo = [n+1 for i in range(n+1)]
        memo[0] = 0
        memo[1] = 1

        for i in range(2, n+1):
            for j in candi:
                if i >= j:
                    memo[i] = min(memo[i], memo[i-j] + 1)
        return memo[n]


print(Solution().numSquares(12))












