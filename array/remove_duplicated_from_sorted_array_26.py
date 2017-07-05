"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 1
        record_index = 1
        record_num = nums[0]
        data_len = len(nums)
        for i in range(1, data_len):
            if nums[i] > record_num:
                record_num = nums[i]
                nums[record_index] = nums[i]
                record_index += 1
                result += 1

        return result

L = [1,1,2]
result = Solution().removeDuplicates(L)
print(result)
