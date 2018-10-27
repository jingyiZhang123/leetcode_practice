"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

# memo = {}
# class Solution(object):
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n not in memo:
#             memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
#         return memo[n]


class Solution(object):
    def climbStairs(self, n):
        memo = [-1 for _ in range(max(n+1, 3))]
        memo[1], memo[2] = 1, 2
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

print(Solution().climbStairs(1))










