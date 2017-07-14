"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        head = 0
        tail = -1
        cur_sum = 0
        data_len = len(nums)
        min_len = data_len + 1
        while head < data_len:
            if tail+1 < data_len and cur_sum < s:
                tail += 1
                cur_sum += nums[tail]
            else:
                cur_sum -= nums[head]
                head += 1
            if cur_sum >= s:
                min_len = min(min_len, tail - head + 1)

        if min_len == data_len + 1:
            return 0
        return min_len






