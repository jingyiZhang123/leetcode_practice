"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        if not nums: return []

        data_len = len(nums)
        appeared = [False for _ in range(data_len+1)]
        for i in nums:
            appeared[i] = True
        return [x for x in range(1, data_len+1) if not appeared[x]]


print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))






