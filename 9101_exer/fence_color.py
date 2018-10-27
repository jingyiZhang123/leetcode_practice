class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        opt = [None for _ in range(n)]
        opt[0] = k
        opt[1] = k * k
        for i in range(2, n):
            opt[i] = opt[i-2] * (k-1) + opt[i-1] * (k-1)
        
        return opt[n-1]


        


print(Solution().numWays(3, 2))

