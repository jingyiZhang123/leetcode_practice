"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def _subset(self, soFar, rest):
        self.result.append(soFar)
        if not rest:
            return

        for i in range(len(rest)):
            next = rest[i]
            remaining = rest[i+1:]
            if i > 0 and rest[i] == rest[i-1]:
                continue
            self._subset(soFar+[next], remaining)

    def subsetsWithDup(self, nums):
        nums.sort()
        self.result = []
        self._subset([], nums)
        return self.result

print(Solution().subsetsWithDup([1,2,2]))








