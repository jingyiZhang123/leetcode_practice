"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        obstacles = set()

        for i in range(height):
            for j in range(width):
                if obstacleGrid[i][j] == 1:
                    obstacles.add((i, j))
        board = [[0 for j in range(width)] for i in range(height)]
        board[0][0] = 1
        for i in range(height):
            for j in range(width):
                if (i,j) in obstacles:
                    board[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        continue
                    top = board[i-1][j] if i-1 >= 0 else 0
                    left = board[i][j-1] if j-1 >= 0 else 0
                    board[i][j] = top + left
        # for i in board:
            # print(i)
        return board[height-1][width-1]

print(Solution().uniquePathsWithObstacles([[1]]))








