"""
find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]
"""


class Solution(object):
    def _combine(self, soFar, rest, length, target):
        l = len(soFar)
        s = sum(soFar)
        if s == target and l == length:
            self.result.append(soFar)
            return
        if s > target or l > target or not rest:
            return

        for i in range(len(rest)):
            next = rest[i]
            remaining = rest[i+1:]
            self._combine(soFar+[next], remaining, length, target)

    def combinationSum3(self, k, n):
        self.result = []
        self._combine([], list(range(1,10)), k, n)
        return self.result

print(Solution().combinationSum3(3,9))



