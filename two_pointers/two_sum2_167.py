"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pt1 = 0
        pt2 = len(numbers)-1
        while pt1 < pt2:

            s = numbers[pt1] + numbers[pt2]
            if s == target:
                return [pt1+1, pt2+1]
            elif s > target:
                pt2 -= 1
            else:
                pt1 += 1
        return [None, None]
















