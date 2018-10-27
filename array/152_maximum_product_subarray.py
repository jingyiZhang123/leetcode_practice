"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur_max = cur_min = max_product = nums[0]
        for i in nums[1:]:
            cur_max,cur_min = max(i, cur_max * i, cur_min * i), min(i, cur_min * i, cur_max * i)
            max_product = max(cur_max, max_product)
        return max_product

print(Solution().maxProduct([-1,-2,-9,-6]))







