"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution(object):
    def canJump(self, nums):
        # can = [False for _ in range(len(nums))]
        # can[0] = True
        # for i in range(1, len(nums)):
        #     for j in range(i-1, -1, -1):
        #         if can[j] and j + nums[j] >= i:
        #             can[i] = True
        #             break
        # return can[-1]
        if not nums:
            return 0
        nums_len = len(nums)
        max_dis= nums[0]
        for i in range(1, nums_len):
            if i > max_dis:
                return False
            max_dis = max(max_dis, nums[i]+i)
        return True












