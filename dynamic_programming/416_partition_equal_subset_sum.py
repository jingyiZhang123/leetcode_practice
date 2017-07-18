"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets
"""

class Solution(object):
    # nums[从0到index]能否填充一个容量为C的背包
    def tryPartition(self, nums, index, C):
        if C == 0:
            return True
        if C < 0 or index < 0:
            return False
        if (index, C) in self.memo:
            return self.memo[(index, C)]
        self.memo[(index, C)] = self.tryPartition(nums, index-1, C) or self.tryPartition(nums, index-1, C - nums[index])
        return self.memo[(index, C)]

    def canPartition(self, nums):
        self.memo = {}
        s = sum(nums)
        if s % 2 != 0: return False
        return self.tryPartition(nums, len(nums) - 1, s // 2)

class Solution(object):
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        n = len(nums)
        c = s // 2
        dp = [False for _ in range(c+1)]
        for i in range(c+1):
            dp[i] = True if nums[0] == i else False

        for i in range(1, n):
            for j in range(c, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[c]




print(Solution().canPartition([1,5,11,5]))



















