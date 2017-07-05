"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # non_zero_nums = [x for x in nums if x != 0]
        # for i in range(len(nums)):
        #     nums[i] = 0
        # for i in range(len(non_zero_nums)):
        #     nums[i] = non_zero_nums[i]
        nums_len = len(nums)
        record_pos = 0
        for i in range(nums_len):
            if nums[i]:
                if i != record_pos:
                    nums[record_pos], nums[i] = nums[i], nums[record_pos]
                record_pos += 1


L = [0,1,0,3,12]
Solution().moveZeroes(L)
print(L)
