"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max3 = [float('-Inf'), float('-Inf'), float('-Inf')]
        min2 = [float('Inf'), float('Inf')]

        for i in nums:
            if i > max3[2]: max3 = [max3[1], max3[2], i]
            elif i > max3[1]: max3 = [max3[1], i, max3[2]]
            elif i > max3[0]: max3 = [i, max3[1], max3[2]]

            if i < min2[0]: min2 = [i, min2[0]]
            elif i < min2[1]: min2 = [min2[0], i]

        print(max3, min2)
        return max(max3[0] * max3[1] * max3[2], max3[2] * min2[0] * min2[1])


print(Solution().maximumProduct([-4,-3,-2,-1,60]))





