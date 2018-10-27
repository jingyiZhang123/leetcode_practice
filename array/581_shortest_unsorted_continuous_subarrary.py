"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
       [4,-2, 4, 2, -1, 6]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        data_len = len(nums)
        start = -1
        end = -2
        min_value = nums[-1]
        max_value = nums[0]

        for i in range(data_len):
            max_value = max(max_value, nums[i])
            min_value = min(min_value, nums[-(i+1)])
            if nums[i] < max_value:
                end = i
            if nums[-(i+1)] > min_value:
                start = data_len-1-i
        return end - start + 1


print(Solution().findUnsortedSubarray([1,3,2,3,3]))

# class test(object):
#     """docstring for test"""
#     def __init__(self, L):
#         self.index = 0
#         self.data_len = len(L)
#         self.L = L

#     def __iter__(self):
#         while self.index < self.data_len:
#             yield self.L[self.index]
#             self.index += 1
#         raise StopIteration
#     def __str__(self):
#         return str(self.L)

# a = test([1,2,3,4,5])
# for i in a:
#     print(a)
#     a.L.remove(i)
#     a = test([1,2,3,4,5])












