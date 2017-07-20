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
        if not nums: return []
        record_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if record_index != i:
                    nums[record_index], nums[i] = nums[i], nums[record_index]
                record_index += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)










