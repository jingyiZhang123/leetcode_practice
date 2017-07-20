"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]: return 0
        if target > nums[-1]: return len(nums)
        if target == nums[-1]: return len(nums) - 1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return end


print(Solution().searchInsert([1,3,5,6], 2))















