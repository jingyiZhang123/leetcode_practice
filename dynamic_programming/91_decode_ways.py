"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

memo = {}
class Solution(object):
    def _solve(self, s):
        str_len = len(s)
        if str_len == 1 and s[0] != '0': return 1
        if str_len == 0: return 1

        result = 0
        if s in memo:
            return memo[s]

        for i in range(min(2, len(s))):
            if int(s[:i+1]) > 26 or (s[:i+1][0]=='0'):
                continue
            result += self._solve(s[i+1:])
        memo[s] = result
        return result

    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        return self._solve(s)



class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if s[i-2:i] < "27" and s[i-2:i] > "09":
                dp[i] += dp[i-2]

        return dp[len(s)]


print(Solution().numDecodings("11235"))















