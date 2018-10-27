"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])


print(Solution().findMin([5,1,2,3,4]))


class Solution2(object):
    def partition(self, arr, left, right):
        
        pivot = arr[left]
        j = left

        for i in range(left + 1, right + 1):
            if arr[i] < pivot:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[left], arr[j] =  arr[j], arr[left]
        
        return j

    def helper(self, arr, left, right, rank):
        if left >= right:
            return arr[left]
        p = self.partition(arr, left, right)
        
        if p == rank:
            return arr[p]
        elif p > rank:
            return self.helper(arr, left, p - 1, rank)
        else:
            return self.helper(arr, p + 1, right, rank)

    def findMin(self, nums):
        n = len(nums)
        if n % 2 != 0:
            return self.helper(nums, 0, n - 1, n // 2)
        else:
            return (self.helper(nums, 0, n - 1, n // 2) + self.helper(nums, 0, n - 1, n // 2 - 1)) / 2


print(Solution2().findMin([3,1, 2]))
