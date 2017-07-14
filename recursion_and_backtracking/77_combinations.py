"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""



class Solution(object):
    def _combine(self, soFar, rest, target):
        l = len(soFar)
        if l == target:
            self.result.append(soFar)
            return
        if not rest:
            return

        for i in range(len(rest) - target + l + 1):
            next = rest[i]
            remaining = rest[i+1:]
            self._combine(soFar+[next], remaining, target)



    def combine(self, n, k):
        nums = list(range(1,n+1))
        self.result = []
        self._combine([], nums, k)
        return self.result


print(Solution().combine(4,2))
