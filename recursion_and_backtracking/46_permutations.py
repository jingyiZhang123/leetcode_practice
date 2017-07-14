"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def _permute(self, soFar, rest):
        if not rest:
            self.result.append(soFar)
            return

        for i in range(len(rest)):
            next = rest[i]
            remaining = rest[:i] + rest[i+1:]
            self._permute(soFar+[next], remaining)



    def permute(self, nums):
        self.result = []
        self._permute([], nums)
        return self.result


