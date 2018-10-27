"""
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        num_house = len(nums)
        without_first = nums[1:]
        without_last = nums[:-1]
        dp_first = [-1 for _ in range(num_house - 1)]
        dp_last = [-1 for _ in range(num_house - 1)]

        dp_first[0] = without_first[0]
        dp_last[0] = without_last[0]

        for i in range(1, len(dp_first)):
            for j in range(i, -1, -1):
                dp_first[i] = max(dp_first[i], without_first[j] + (dp_first[j-2] if j-2>=0 else 0))

        for i in range(1, len(dp_last)):
            for j in range(i, -1, -1):
                dp_last[i] = max(dp_last[i], without_last[j] + (dp_last[j-2] if j-2>=0 else 0))


        return max(dp_first[-1], dp_last[-1])



