"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        data_len = len(nums)
        print(nums)
        result = []
        for i in range(0, data_len-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            head = i+1
            tail = data_len - 1
            while head < tail:
                s = nums[head] + nums[tail]
                if s == target:
                    temp = [nums[i], nums[head], nums[tail]]
                    result.append(temp)
                    while head < tail and nums[head] == nums[head+1]:
                        head += 1
                    while head < tail and nums[tail] == nums[tail-1]:
                        tail -= 1
                    head += 1
                    tail -= 1
                elif s > target:
                    tail -= 1
                else:
                    head += 1

        return result

print(Solution().threeSum([-2,0,0,2,2]))












