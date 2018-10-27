"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        data_len = len(nums)
        lis = [1 for _ in range(data_len)]

        for i in range(1, data_len):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
                # lis[i] = max(lis[i], lis[j]+(1 if nums[i]>nums[j] else 0))

        return max(lis)

print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        num_len = len(nums)
        dp = [1 for _ in range(num_len)]
        for i in range(num_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))















