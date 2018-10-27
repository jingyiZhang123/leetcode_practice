"""
A peak element is an element that is greater than its neighbors.

Given an input array where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [float('-Inf')] + nums + [float('-Inf')]
        data_len = len(nums)
        left, right = 0, data_len - 1

        while True:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid



print(Solution().findPeakElement([2,1,2]))



