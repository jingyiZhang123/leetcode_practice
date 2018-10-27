"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: return []
        row = [1]
        result = [row]
        for i in range(numRows-1):
            row = [sum(x) for x in zip([0]+row, row+[0])]
            result.append(row)
        return result

print(Solution().generate(5))
