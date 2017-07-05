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
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        data_len = len(nums)
        lp = 0
        rp = data_len - 1
        result = 0
        while lp <= rp:
            if nums[rp] == val:
                rp -= 1
                result += 1
            else:
                if nums[lp] == val:
                    nums[lp], nums[rp] = nums[rp], nums[lp]
                    result += 1
                    rp -= 1
                lp += 1

        return data_len - result


L = [3,2,2,3]
L = [1]
result = Solution().removeElement(L, 1)
print(result, L)
