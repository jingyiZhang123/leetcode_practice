"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lexicon = set()
        for i in range(len(nums)):
            if nums[i] in lexicon:
                return True
            lexicon.add(nums[i])
        return False
