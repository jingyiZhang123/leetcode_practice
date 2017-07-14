"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # head = 0
        # tail = len(s) - 1
        # s = [x for x in s]
        # while head < tail:
        #     if s[head] != s[tail]:
        #         s[head], s[tail] = s[tail], s[head]
        #     head += 1; tail -= 1;

        # return ''.join(s)
        return s[::-1]

print(Solution().reverseString("hello"))
