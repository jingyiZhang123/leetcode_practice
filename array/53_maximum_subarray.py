"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        if not nums: return 0
        max_sum = cur_sum = nums[0]
        for i in nums[1:]:
            cur_sum = i if (i > cur_sum+i) else cur_sum+i
            max_sum = cur_sum if cur_sum > max_sum else max_sum
        return max_sum
