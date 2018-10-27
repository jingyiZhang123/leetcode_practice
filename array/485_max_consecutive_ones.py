"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_cn = cur_cn = 0
        for i in nums:
            if i:
                cur_cn += 1
                max_cn = cur_cn if cur_cn > max_cn else max_cn
            else:
                cur_cn = 0
        return max_cn






