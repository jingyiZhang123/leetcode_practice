class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def change_dir(self):
        if self.di == 0 and self.dj == 1:
            self.di = 1
            self.dj = 0
        elif self.di == 1 and self.dj == 0:
            self.di = 0
            self.dj = -1
        elif self.di == 0 and self.dj == -1:
            self.di = -1
            self.dj = 0
        else:
            self.di = 0
            self.dj = 1
    
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        self.di = 0
        self.dj = 1
        
        width = len(matrix[0])
        height = len(matrix)
        visited = [[False for _ in range(width)] for _ in range(height)]
        num_rest = width * height 
        result = []
        i = j = 0
        while num_rest:
            if 0 <= i < height and 0 <= j < width and not visited[i][j]:
                visited[i][j] = True
                num_rest -= 1
                result.append(matrix[i][j])
            
            ii = i + self.di
            jj = j + self.dj
            if not num_rest:
                break
            while not (0 <= ii < height and 0 <= jj < width and not visited[ii][jj]):
                #print(ii, jj, self.di, self.dj, i , j)
                self.change_dir()
                ii = i + self.di
                jj = j + self.dj
            i = ii
            j = jj
        return result

                
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
