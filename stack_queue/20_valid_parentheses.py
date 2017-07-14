"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {']':'[', ')':'(', '}':'{'}
        for i in s:
            if i in '[{(':
                stack.append(i)
            elif i in brackets:
                if not stack:
                    return False
                b = stack.pop()
                if b != brackets[i]:
                    return False
        if stack:
            return False
        return True

print(Solution().isValid("()[]{}"))




