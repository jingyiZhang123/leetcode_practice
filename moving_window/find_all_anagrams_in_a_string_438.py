"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        datalen = len(s)
        p_len = len(p)
        if not s or datalen < p_len:
            return []
        lexicon = [0 for _ in range(256)]
        ref = [0 for _ in range(256)]
        for i in range(p_len):
            ref[ord(p[i])] += 1
            lexicon[ord(s[i])] += 1
        result = []
        if ref == lexicon:
            result.append(0)
        for i in range(1, datalen - p_len + 1):
            lexicon[ord(s[i-1])] -= 1
            lexicon[ord(s[i+p_len-1])] += 1
            if lexicon == ref:
                result.append(i)

        return result

print(Solution().findAnagrams("cbaebabacd", "abc"))




















