"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution(object):
    def _comb(self, soFar, rest, target):
        s = sum(soFar)
        if s > target:
            return
        if s == target:
            self.result.append(soFar)
        if not rest:
            return
        for i in range(len(rest)):
            if i > 0 and rest[i] == rest[i-1]:
                continue
            next = rest[i]
            remaining = rest[i+1:]
            self._comb(soFar+[next], remaining, target)

    def combinationSum2(self, candidates, target):

        candidates.sort()
        self.result = []
        self._comb([], candidates, target)
        return self.result











