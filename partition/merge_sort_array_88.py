"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

# simple solution
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         pt1 = pt2 = 0
#         free = modify
#         temp = [nums1[i] for i in range(m)]
#         for i in range(0, m+n):
#             if pt1 >= m:
#                 nums1[i] = nums2[pt2]
#                 pt2 += 1
#             elif pt2 >= n:
#                 nums1[i] = temp[pt1]
#                 pt1 += 1
#             elif temp[pt1] < nums2[pt2]:
#                 nums1[i] = temp[pt1]
#                 pt1 += 1
#             else:
#                 nums1[i] = nums2[pt2]
#                 pt2 += 1

#         return

# better solution
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        pt1 = m-1
        pt2 = n-1
        for i in range(m+n-1, -1, -1):
            if pt1 < 0:
                nums1[i] = nums2[pt2]
                pt2 -= 1
            elif pt2 < 0:
                nums1[i] = nums1[pt1]
                pt1 -= 1
            elif nums1[pt1] > nums2[pt2]:
                nums1[i] = nums1[pt1]
                pt1 -= 1
            else:
                nums1[i] = nums2[pt2]
                pt2 -= 1

l1 = [4,5,6,0,0,0]
l2 = [1,2,3]
Solution().merge(l1, 3, l2,3)
print(l1)














