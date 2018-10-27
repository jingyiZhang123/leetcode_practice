class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        grid = [[x if x != '0' else 0 for x in line] for line in grid]
        print(grid)
        height = len(grid)
        width = len(grid[0])

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 'E':
                    for k in range(i-1, -1, -1):
                        if grid[k][j] == 'W':
                            break
                        elif isinstance(grid[k][j], int):
                            grid[k][j] += 1
                    for k in range(i+1, height):
                        if grid[k][j] == 'W':
                            break
                        elif isinstance(grid[k][j], int):
                            grid[k][j] += 1
                    for k in range(j-1, -1, -1):
                        if grid[i][k] == 'W':
                            break
                        elif isinstance(grid[i][k], int):
                            grid[i][k] += 1
                    for k in range(j+1, width):
                        if grid[i][k] == 'W':
                            break
                        elif isinstance(grid[i][k], int):
                            grid[i][k] += 1
        
        result = 0
        for i in grid:
            for j in i:
                if isinstance(j, int) and j > result:
                    result = j
        return result
        
print(Solution().maxKilledEnemies(["0E00","E0WE","0E00"]))