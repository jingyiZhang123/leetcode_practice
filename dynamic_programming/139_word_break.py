"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""



class Solution(object):
    def wordBreak(self, s, wordDict):
        str_len = len(s)
        dp = [False for _ in range(str_len)]
        wordDict = set(wordDict)

        for i in range(str_len):
            for word in wordDict:
                if i+1 >= len(word):
                    if s[:i+1] in wordDict or (dp[i-len(word)] and s[i-len(word)+1:i+1] == word):
                        dp[i] = True
                        break

        return dp[str_len-1]

s = "acccbccb"
dict1 = ["cc","bc","ac","ca"]
print(Solution().wordBreak(s, dict1))















