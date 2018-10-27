class Solution:
    def removeBoxesSub(self, boxes, i, j, k, dp):
        if i > j:
            return 0
        if dp[i][j][k] > 0:
            return dp[i][j][k]
        
        
        res = (k + 1) * (k + 1) + self.removeBoxesSub(boxes, i + 1, j, 0, dp)
        
        for m in range(i+1, j + 1):
            if boxes[i] == boxes[m]:
                res = max(res, self.removeBoxesSub(boxes, i + 1, m - 1, 0, dp) + self.removeBoxesSub(boxes, m, j, k + 1, dp))
            
        dp[i][j][k] = res
        return res

    """
    @param boxes: List[int]
    @return: return an integer
    """
    def removeBoxes(self, boxes):
        n = len(boxes)
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return self.removeBoxesSub(boxes, 0, n - 1, 0, dp)

    

                    
    

print(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))
