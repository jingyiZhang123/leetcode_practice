"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

"""

class Solution(object):
    def is_palindrome(self, string):
        for i in range(len(string) // 2):
            if string[i] != string[-(i+1)]:
                return False
        else:
            return True

    def _partition(self, soFar, rest):
        if not rest:
            self.result.append(soFar)
            return

        for i in range(0, len(rest)):
            next = rest[:i+1]
            if self.is_palindrome(next):
                remaining = rest[i+1:]
                self._partition(soFar+[next], remaining)

    def partition(self, s):
        if not s:
            return []
        self.result = []
        self._partition([], s)
        return self.result


print(Solution().partition("amanaplanacanalpanama"))







