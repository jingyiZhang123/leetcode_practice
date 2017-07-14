"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lexicon = set()
        lb = 0  # lower bound is 0
        ub = -1 # upper bound is -1 [lb..up]
        datalen = len(s)
        res = 0
        while lb < datalen:
            if ub + 1 < datalen and s[ub+1] not in lexicon:
                ub += 1
                lexicon.add(s[ub])
            else:
                lexicon.remove(s[lb])
                lb += 1
            temp = ub - lb + 1
            res = temp if temp > res else res
        return res


print(Solution().lengthOfLongestSubstring("abcabcbb"))



