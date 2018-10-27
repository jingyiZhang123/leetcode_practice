"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        data_len = len(nums)
        min_len = data_len
        start = end = 0
        cur_sum = nums[0]
        while start < data_len:
            if cur_sum >= s:
                min_len = min(min_len, end-start+1)
            if cur_sum < s and end + 1 < data_len:
                end += 1
                cur_sum += nums[end]
            else:
                cur_sum -= nums[start]
                start += 1

        return min_len

print(Solution().minSubArrayLen([2,3,1,2,4,3], 7))


