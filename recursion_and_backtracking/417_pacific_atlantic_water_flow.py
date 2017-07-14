"""
Given an m x n matrix of non-negative integers representing height of each unit cell in a continent, Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one height equal or lower.

Find  list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

"""
class Solution(object):
    def inArea(self, i, j, height, width):
        return 0 <= i < height and 0 <= j < width
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        width, height = len(matrix[0]), len(matrix)
        Pacific_stack = [(0, x) for x in range(width)] + [(x, 0) for x in range(height)]
        Atlantic_stack = [(height-1, x) for x in range(width)] + [(x, width-1) for x in range(height)]

        Pacific = set()
        Atlantic = set()

        while Pacific_stack:
            point = Pacific_stack.pop()
            if point in Pacific: continue
            Pacific.add(point)
            i, j = point
            new_i, new_j = i + 0, j + 1
            if self.inArea(new_i, new_j, height, width) and matrix[new_i][new_j] >= matrix[i][j]:
                Pacific_stack.append((new_i, new_j))
            new_i, new_j = i + 0, j - 1
            if self.inArea(new_i, new_j, height, width) and matrix[new_i][new_j] >= matrix[i][j]:
                Pacific_stack.append((new_i, new_j))
            new_i, new_j = i + 1, j + 0
            if self.inArea(new_i, new_j, height, width) and matrix[new_i][new_j] >= matrix[i][j]:
                Pacific_stack.append((new_i, new_j))
            new_i, new_j = i - 1, j + 0
            if self.inArea(new_i, new_j, height, width) and matrix[new_i][new_j] >= matrix[i][j]:
                Pacific_stack.append((new_i, new_j))

        while Atlantic_stack:
            point = Atlantic_stack.pop()
            if point in Atlantic: continue
            Atlantic.add(point)
            i, j = point
            new_i, new_j = i + 0, j + 1
            if self.inArea(new_i, new_j, height, width) and matrix[new_i][new_j] >= matrix[i][j]:
                Atlantic_stack.append((new_i, new_j))
            new_i, new_j = i + 0, j - 1
            if self.inArea(new_i, new_j, height, width) and matrix[new_i][new_j] >= matrix[i][j]:
                Atlantic_stack.append((new_i, new_j))
            new_i, new_j = i + 1, j + 0
            if self.inArea(new_i, new_j, height, width) and matrix[new_i][new_j] >= matrix[i][j]:
                Atlantic_stack.append((new_i, new_j))
            new_i, new_j = i - 1, j + 0
            if self.inArea(new_i, new_j, height, width) and matrix[new_i][new_j] >= matrix[i][j]:
                Atlantic_stack.append((new_i, new_j))

        return list(Atlantic & Pacific)




grid = [[1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]]
print(Solution().pacificAtlantic(grid))














