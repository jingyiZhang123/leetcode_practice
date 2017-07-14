"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in nums1:
            dict1[i] += 1
        for i in nums2:
            dict2[i] += 1

        result = []

        for k,v in dict2.items():
            if k in dict1:
                for i in range(min(dict1[k], v)):
                    result.append(k)
        return result


print(Solution().intersect([1,2,2,1], [2,2]))















