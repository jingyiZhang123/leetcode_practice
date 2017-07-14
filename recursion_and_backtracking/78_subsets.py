"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def _subsets(self, soFar, rest):
        self.result.append(soFar)
        if not rest: return
        for i in range(len(rest)):
            self._subsets(soFar+[rest[i]], rest[i+1:])

    def subsets(self, nums):
        self.result = []
        self._subsets([], nums)
        return self.result

print(Solution().subsets([1,2,3]))




