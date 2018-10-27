"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        data_len = len(nums)
        target = data_len // 2

        info = defaultdict(int)
        for i in nums:
            info[i] += 1
        return [k for k,v in info.items() if v > target][0]





