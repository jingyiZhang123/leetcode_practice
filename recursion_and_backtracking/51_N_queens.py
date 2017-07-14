"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""

class Solution(object):
    def _solve(self, n, index, row):
        if index == n:
            self.result.append(row[:])
            return

        for i in range(n):
            if not self.col[i] and not self.dia1[index+i] and not self.dia2[index-i+n-1]:
                row.append(i)
                self.col[i] = True
                self.dia1[index+i] = True
                self.dia2[index-i+n-1] = True
                self._solve(n, index + 1, row)
                self.col[i] = False
                self.dia1[index+i] = False
                self.dia2[index-i+n-1] = False
                row.pop()


    def solveNQueens(self, n):
        self.result = []
        self.col = [False for _ in range(n)]
        self.dia1 = [False for _ in range(2*n - 1)]
        self.dia2 = [False for _ in range(2*n - 1)]
        self._solve(n, 0, [])
        boards = [[['.' for j in range(n)] for i in range(n)] for k in range(len(self.result))]
        for i in range(len(self.result)):
            for j in range(n):
                boards[i][j][self.result[i][j]] = 'Q'
                boards[i][j] = ''.join(boards[i][j])

        return boards

print(Solution().solveNQueens(4))













