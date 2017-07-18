"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""

class Solution(object):
    def _solve(self, soFar, rest, target):
        s = sum(soFar)
        r = sum(rest)
        if s == target:
            return 1
        if s > target:
            return 0

        if (s, r) in self.memo:
            return self.memo[(s,r)]
        result = 0
        for i in range(len(rest)):
            next = rest[i]
            result += self._solve(soFar+[next], rest, target)
        self.memo[(s,r)] = result
        return result

    def combinationSum4(self, nums, target):
        if not nums:
            return 0
        self.memo = {}
        return self._solve([], nums, target)

print(Solution().combinationSum4([1,2],4))

class Solution(object):
    def _solve(self, nums, index, sofar):
        if sofar == self.target:
            return 1
        if index >= len(nums) or sofar > self.target:
            return 0

        if (index, sofar) in self.memo:
            return self.memo[(index, sofar)]

        result = 0
        for i in range(len(nums)):
            result += self._solve(nums, i, sofar + nums[i])
        self.memo[(index, sofar)] = result
        return result

    def combinationSum4(self, nums, target):
        if not nums:
            return 0
        self.memo = {}
        self.target = target
        return self._solve(nums, 0, 0)

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        nums.sort()
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i-num]
        return dp[target]


print(Solution().combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],10))
# print(Solution().combinationSum4([4,2,1], 32))













