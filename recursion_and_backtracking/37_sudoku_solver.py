
class Solution(object):
    def isValid(self, board, point, value):
        i, j = point
        for k in range(9):
            if k != j and board[i][k] == value:
                return False
        for k in range(9):
            if k != i and board[k][j] == value:
                return False

        for ii in range(i//3*3, i//3*3+3):
            for jj in range(j//3*3, j//3*3+3):
                if ii != i and jj != j and board[ii][jj] == value:
                    return False

        return True


    def solve(self, board):
        if self.solved:
            return
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for val in range(1, 10):
                        if self.isValid(board, (i, j), val):
                            board[i][j] = val
                            self.solve(board)
                            if self.solved:
                                return
                            board[i][j] = 0
                    return
        self.solved = True

    def solveSudoku(self, board):
        for i in range(9):
            board[i] = [int(x) if x != '.' else 0 for x in board[i]]
        self.solved = False
        self.solve(board)
        for i in range(9):
            board[i] = ''.join([str(x) for x in board[i]])

grid = ["53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79"]

for i in range(len(grid)):
    if i % 3 == 0:
        print('----------------------')
    for j in range(len(grid[0])):
        if j % 3 == 0:
            print('|',end='')
        print(grid[i][j],end=' ')
    print('|')
print('----------------------')

Solution().solveSudoku(grid)
for i in range(len(grid)):
    if i % 3 == 0:
        print('----------------------')
    for j in range(len(grid[0])):
        if j % 3 == 0:
            print('|',end='')
        print(grid[i][j],end=' ')
    print('|')
print('----------------------')




