"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""



class Solution(object):
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        board = [[0 for j in range(n)] for i in range(m)]
        for i in range(n):
            board[0][i] = 1
        for i in range(m):
            board[i][0] = 1

        for i in range(1, m):
            for j in range(1,n):
                board[i][j] = board[i-1][j] + board[i][j-1]
        return board[m-1][n-1]


print(Solution().uniquePaths(0,1))




