"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

class Solution(object):
    def _color(self, grid, start_point):
        i,j = start_point
        if i < 0 or i >= self.height or j < 0 or j >= self.width:
            return
        if self.visited[i][j]:
            return
        self.visited[i][j] = True
        self._color(grid, (i, j-1))
        self._color(grid, (i, j+1))
        self._color(grid, (i+1, j))
        self._color(grid, (i-1, j))

    def _num(self, grid):
        for i in range(self.height):
            for j in range(self.width):
                if not self.visited[i][j]:
                    self._color(grid, (i,j))
                    self.result += 1

    def numIslands(self, grid):
        if not grid:
            return 0
        self.width = len(grid[0])
        self.height = len(grid)
        self.visited = [[True for _ in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == '1':
                    self.visited[i][j] = False
        self.result = 0
        self._num(grid)
        return self.result



grid = ['11110','11010','11000','00000']
print(Solution().numIslands(grid))





