"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        head = 0
        tail = len(s)-1
        while head < tail:
            while head < tail and not s[head].isalnum():
                head += 1
            while head < tail and not s[tail].isalnum():
                tail -= 1
            if s[tail].lower() != s[head].lower():
                return False
            head += 1
            tail -= 1
        return True


print(Solution().isPalindrome(""))



















