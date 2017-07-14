"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def _permute(self, soFar, rest):
        if not rest:
            self.result.append(soFar)
            return

        for i in range(len(rest)):
            next = rest[i]
            if i > 0 and rest[i] == rest[i-1]:
                continue
            remaining = rest[:i] + rest[i+1:]
            self._permute(soFar+[next], remaining)

    def permuteUnique(self, nums):
        nums.sort()
        self.result = []
        self._permute([], nums)
        return self.result



print(Solution().permuteUnique([1,1,2]))






