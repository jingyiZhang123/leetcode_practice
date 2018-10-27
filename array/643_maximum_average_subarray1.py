"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000]
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        data_len = len(nums)
        start, end = 0, k-1
        max_value = sum(nums[start:end+1])
        cur_value = max_value
        while end+1 < data_len:
            cur_value = cur_value - nums[start] + nums[end+1]
            max_value = cur_value if max_value < cur_value else max_value
            start += 1
            end += 1

        return max_value*1.0 / k

print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))











