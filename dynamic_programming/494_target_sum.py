"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""


class Solution(object):
    def _solve(self, nums, index, target):
        if index >= len(nums):
            return 1 if not target else 0
        if (index, target) in self.memo:
            return self.memo[(index, target)]
        self.memo[(index, target)] = self._solve(nums, index+1, target - nums[index]) + self._solve(nums, index+1, target + nums[index])
        return self.memo[(index, target)]

    def findTargetSumWays(self, nums, S):
        self.memo = {}
        return self._solve(nums, 0, S)


class Solution(object):
    def findTargetSumWays(self, nums, S):

        return self._solve(nums, 0, S)


print(Solution().findTargetSumWays([1,1,1,1,1], 3))

















