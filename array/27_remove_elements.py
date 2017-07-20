"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        if not nums: return 0

        data_len = len(nums)
        start, end = 0, data_len - 1
        result = 0
        while start <= end:
            if nums[end] == val:
                end -= 1
                result += 1
            else:
                if nums[start] == val:
                    nums[start], nums[end] = nums[end], nums[start]
                    end -= 1
                    result += 1
                start += 1
        return data_len - result

print(Solution().removeElement([1], 1))


