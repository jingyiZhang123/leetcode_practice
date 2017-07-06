"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = dict()
        str_len = len(s)
        for i in range(str_len):
            if s[i] not in mapping:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]
            else:
                if mapping[s[i]] != t[i]:
                    return False
        else:
            return True


print(Solution().isIsomorphic("foo", "bar"))










