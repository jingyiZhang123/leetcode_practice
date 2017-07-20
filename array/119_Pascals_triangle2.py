"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
"""


class Solution(object):
    def getRow(self, rowIndex):
        result = [1]
        if rowIndex < 1: return result
        for i in range(1, rowIndex+1):
            result = [sum(x) for x in zip([0] + result, result + [0])]
        return result

print(Solution().getRow(3))


