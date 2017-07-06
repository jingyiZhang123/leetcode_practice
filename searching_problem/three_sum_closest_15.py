"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        data_len = len(nums)
        result = None
        nums.sort()
        min_result = float('Inf')
        for i in range(data_len - 2):
            head = i + 1
            tail = data_len - 1
            while head < tail:
                s = nums[i] + nums[head] + nums[tail]
                diff = abs(s - target)
                if diff < min_result:
                    min_result = diff
                    result = s
                if s == target:
                    return target
                elif s > target:
                    tail -= 1
                else:
                    head += 1

        if min_result == float('Inf'):
            return sum(nums)
        return result

print(Solution().threeSumClosest([1,1,1,0], -100))











