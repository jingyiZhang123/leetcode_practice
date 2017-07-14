"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""

class Solution(object):
    def _helper(self, soFar, rest, target):
        s = sum(soFar)
        if s == target:
            self.result.append(soFar)
            return
        if s > target:
            return
        if not rest:
            return

        for i in range(len(rest)):
            next = rest[i]
            remaining = rest[i:]
            self._helper(soFar+[next], remaining, target)


    def combinationSum(self, candidates, target):
        self.result = []
        self._helper([], candidates, target)
        return self.result


print(Solution().combinationSum([2,3,6,7], 7))



