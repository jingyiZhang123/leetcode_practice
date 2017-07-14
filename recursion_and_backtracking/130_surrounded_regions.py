"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""
import sys
sys.setrecursionlimit(5000)
class Solution(object):
    def in_area(self, i, j):
        return i >= 0 and i < self.height and j >= 0 and j < self.width

    def _solve(self, board, point):
        i,j = point
        if self.visited[i][j]:
            return
        self.visited[i][j] = True
        self.results.add(point)

        new_i, new_j = i + 0, j + 1
        if self.in_area(new_i, new_j) and not self.visited[new_i][new_j]:
            self._solve(board, (new_i, new_j))

        new_i, new_j = i + 0, j - 1
        if self.in_area(new_i, new_j) and not self.visited[new_i][new_j]:
            self._solve(board, (new_i, new_j))

        new_i, new_j = i + 1, j + 0
        if self.in_area(new_i, new_j) and not self.visited[new_i][new_j]:
            self._solve(board, (new_i, new_j))

        new_i, new_j = i - 1, j + 0
        if self.in_area(new_i, new_j) and not self.visited[new_i][new_j]:
            self._solve(board, (new_i, new_j))


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        self.height = len(board)
        self.width = len(board[0])
        self.visited = [[True if board[i][j] == 'X' else False for j in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            board[i] = [x for x in board[i]]

        self.results = set()
        for i in range(self.height):
            for j in range(self.width):
                if not self.visited[i][j] and (i == 0 or j == 0 or i == self.height-1 or j == self.width - 1):
                    self._solve(board, (i,j))

        for i in range(self.height):
            for j in range(self.width):
                if (i,j) in self.results:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        for i in range(self.height):
            board[i] = ''.join(board[i])
        return

grid = ['XXXX','XOOX','XXOX','XOXX']
Solution().solve(grid)
for i in grid:
    print(i)










