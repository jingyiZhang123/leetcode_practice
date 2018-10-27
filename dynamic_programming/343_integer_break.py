"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""



class Solution(object):
    def _solve(self, soFar, rest):
        if soFar:
            m = 1
            for i in soFar:
                m *= i
            m *= rest
            self.result = m if m > self.result else self.result
        if rest == 0:
            return
        for i in range(1, rest):
            next = i
            remaining = rest - i
            self._solve(soFar+[next], remaining)

    def integerBreak(self, n):
        self.result = 0
        self._solve([], n)
        return self.result


class Solution(object):
    def _solve(self, n):
        if n == 1:
            return 1
        result = -1

        if self.memo[n] != -1:
            return self.memo[n]
        for i in range(1, n):
            result = max(i * self._solve(n-i), result, i * (n-i))
        self.memo[n] = result
        return result

    def integerBreak(self, n):
        self.memo = [-1 for _ in range(n+1)]
        return self._solve(n)


class Solution(object):
    def integerBreak(self, n):
        # memo[i]表示将数字i分割（至少两部分）后得到的最大乘积
        memo = [-1 for _ in range(n+1)]
        memo[1] = memo[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                memo[i] = max(memo[i], j*(i-j), j*memo[i-j])

        return memo[n]




print(Solution().integerBreak(10))















