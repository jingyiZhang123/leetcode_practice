"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

from random import randint
class Solution(object):
    def _partition(self, arr, left, right):
        if left >= right:
            return

        rand = left + randint(0, right-left-1)
        arr[left], arr[rand] = arr[rand], arr[left]
        pivat = arr[left]
        less = left # [left .. less) <= pivat

        for i in range(left+1, right+1):
            if arr[i] >= pivat:
                less += 1
                arr[less], arr[i] = arr[i], arr[less]
        arr[left], arr[less] = arr[less], arr[left]
        return less

    def _find_rank(self, nums, left, right, rank):
        if left >= right:
            # print(nums)
            return nums[left]

        p = self._partition(nums, left, right)

        if p == rank:
            # print(nums)
            return nums[p]
        elif p > rank:
            return self._find_rank(nums, left, right-1, rank)
        else:
            return self._find_rank(nums, left+1, right, rank)


    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums = list(set(nums))
        self.data_len = len(nums)
        if self.data_len < 3:
            return max(nums)
        return self._find_rank(nums, 0, self.data_len-1, 2)

print(Solution().thirdMax([1,1,2]))
print(sorted([1,2,3,4,5,6])[-3])







