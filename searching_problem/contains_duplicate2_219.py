"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        data_len = len(nums)
        if data_len <= 1:
            return False
        head = 0
        tail = -1
        lexicon = set()
        for i in range(data_len):
            if nums[i] in lexicon:
                return True
            lexicon.add(nums[i])
            if len(lexicon) >= k + 1:
                lexicon.remove(nums[i-k])
        return False



print(Solution().containsNearbyDuplicate([1,2], 2))













