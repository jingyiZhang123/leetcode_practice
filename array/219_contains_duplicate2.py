"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        start = 0
        data_len = len(nums)
        lexicon = set()
        for i in range(data_len):
            if nums[i] in lexicon:
                return True
            lexicon.add(nums[i])
            if i - start >= k:
                lexicon.remove(nums[start])
                start += 1
        return False


print(Solution().containsNearbyDuplicate([1,2,1], 1))
