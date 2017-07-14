
class Solution(object):
    def _putQueen(self, n, cur_row):
        if cur_row == n:
            self.result += 1
            return

        for i in range(n):
            if self.col_available[i] and self.diag1_available[cur_row+i] and self.diag2_available[cur_row-i+n-1]:
                self.col_available[i] = False
                self.diag1_available[cur_row+i] = False
                self.diag2_available[cur_row-i+n-1] = False
                self._putQueen(n, cur_row + 1)
                self.col_available[i] = True
                self.diag1_available[cur_row+i] = True
                self.diag2_available[cur_row-i+n-1] = True



    def totalNQueens(self, n):
        self.result = 0
        self.col_available = [True for _ in range(n)]
        self.diag1_available = [True for _ in range(n*2-1)]
        self.diag2_available = [True for _ in range(n*2-1)]

        self._putQueen(n, 0)
        return self.result


print(Solution().totalNQueens(8))
