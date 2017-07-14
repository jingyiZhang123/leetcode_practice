"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
from random import randint
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self._find_rank(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def _partition(self, arr, left, right):
        swap = left + randint(0, (right-left))
        arr[left], arr[swap] = arr[swap], arr[left]
        pivot = arr[left]
        lt = left

        for i in range(left + 1, right + 1):
            if arr[i] < pivot:
                lt += 1
                arr[i], arr[lt] = arr[lt], arr[i]
        arr[left], arr[lt] = arr[lt], arr[left]
        return lt


    def _find_rank(self, arr, left, right, target):
        if left >= right:
            return arr[left]

        p = self._partition(arr, left, right)
        cur_rank = p - left + 1
        if cur_rank == target:
            return arr[p]
        elif cur_rank > target:
            return self._find_rank(arr, left, p-1, target)
        else:
            return self._find_rank(arr, p+1, right, target - cur_rank)


print(Solution().findKthLargest([1], 1))











