"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        data_len = len(nums)
        k %= data_len
        if not k: return

        temp = nums[data_len-k:] + nums[:-k]

        for i in range(data_len):
            nums[i] = temp[i]

a = [1,2,3,4]
print(Solution().rotate(a, 1))
print(a)


