"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""




class Solution(object):
    def _rob(self, soFar, rest):
        if not rest:
            self.result.append(sum(soFar))
            return

        for i in range(len(rest)):
            next = rest[i]
            remaining = rest[i+2:]
            self._rob(soFar+[next], remaining)


    def rob(self, nums):
        if not nums:
            return 0
        self.result = []
        self._rob([], nums)
        return max(self.result)

class Solution(object):
    #考虑抢劫houses[index..hourses.size())这个范围内的所有房子
    def tryRob(self, houses, index):
        if index >= len(houses):
            return 0

        if self.memo[index] != -1:
            return self.memo[index]
        result = 0
        for i in range(index, len(houses)):
            result = max(result, houses[i] + self.tryRob(houses, i + 2))
        self.memo[index] = result
        return result

    def rob(self, nums):
        self.memo = [-1 for _ in range(len(nums) + 1)]
        return self.tryRob(nums, 0)


class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0

        # n = len(nums)
        # dp = [-1 for _ in range(n)]
        # dp[n-1] = nums[n-1]
        # for i in range(n-2, -1, -1):
        #     for j in range(i, n):
        #         dp[i] = max(dp[i], nums[j] + (dp[j+2] if j+2<n else 0))

        n = len(nums)
        dp = [-1 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            for j in range(i, -1, -1):
                dp[i] = max(dp[i], nums[j] + (dp[j-2] if j-2>=0 else 0))

        return dp[n-1]

print(Solution().rob([3,4,1,7]))








