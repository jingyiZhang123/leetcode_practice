"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

from collections import deque
class Solution(object):
    def generate_list(self, n):
        result = []
        for i in range(n+1):
            if i * i > n:
                break
            result.append(i * i)
        return result[::-1]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        candi = self.generate_list(n)
        if n in candi:
            return 1
        stack = deque([(x, 1) for x in candi])
        calculated = set()
        while stack:
            val, level = stack.pop()
            for i in candi:
                s = val + i
                if s not in calculated:
                    calculated.add(s)
                    if s == n:
                        return level + 1
                    if s < n:
                        stack.appendleft((s, level + 1))

print(Solution().numSquares(7135))




