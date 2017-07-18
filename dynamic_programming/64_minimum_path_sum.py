"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution(object):
    def InArea(self, point):
        return 0 <= point[0] < self.height and 0 <= point[1] < self.width

    def minPathSum(self, grid):
        if not grid:
            return 0
        self.width, self.height = len(grid[0]), len(grid)
        for i in range(self.height):
            for j in range(self.width):
                new_i, new_j = i - 1, j
                res1 = (grid[i][j] + grid[new_i][new_j]) if self.InArea((new_i, new_j)) else None
                new_i, new_j = i, j - 1
                res2 = (grid[i][j] + grid[new_i][new_j]) if self.InArea((new_i, new_j)) else None
                if res1 is not None and res2 is not None:
                    grid[i][j] = min(res1, res2)
                else:
                    if not res1 and not res2:
                        grid[i][j] = grid[i][j]
                    elif not res1:
                        grid[i][j] = res2
                    else:
                        grid[i][j] = res1
        return grid[self.height-1][self.width-1]

print(Solution().minPathSum([[0]]))
