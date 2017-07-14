"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""


class Solution(object):
    def is_palindrome(self, string):
        return string == string[::-1]

    def _min_cut(self, soFar, rest):
        if not rest:
            self.result.append(soFar)
            return

        for i in range(1,len(rest)+1):
            next = rest[:i]
            if self.is_palindrome(next):
                remaining = rest[i:]
                self._min_cut(soFar+[next], remaining)


    def minCut(self, s):
        if not s:
            return 0
        self.result = []
        self._min_cut([], s)

        return min(len(x) for x in self.result) - 1

print(Solution().minCut('aab'))




