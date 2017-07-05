"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        head = 0
        tail = len(s) - 1
        s = [x for x in s]
        while head < tail:
            while head < tail and s[head] not in "aeiouAEIOU":
                head += 1
            while head < tail and s[tail] not in "aeiouAEIOU":
                tail -= 1
            s[head], s[tail] = s[tail], s[head]
            head += 1; tail -= 1
        return ''.join(s)













