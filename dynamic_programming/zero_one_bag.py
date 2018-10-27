"""
经典0-1背包问题
F(n, C) 考虑将n个物品放进容量为C的背包，使其价值最大
F(i, c)   #i个物品，放入容量为小c的背包使其价值最大
        选择1. = F(i-1, c) 对来的这第i的物品不管不问，认为其是没用的
        选择2. = v(i) + F(i-1, c-w(i)) 把i这个物品，放入背包中

        在这两者中选择一个最大值
        => F(i,c) = max(F(i-1, c), v(i) + F(i-1, c-w(i)))
"""

memo = {}
#考虑从0到index这些物品，来填充容积为小c的背包
def bestValue(w, v, index, c):
    if index < 0 or c <= 0:
        return 0

    if (index, c) in memo:
        return memo[(index, c)]
    res = bestValue(w, v, index - 1, c)
    if c >= w[index]:
        res = max(v[index] + bestValue(w, v, index - 1, c - w[index]), res)
    memo[(index,c)] = res
    return res

def knapsack01(weights, values, capacity):
    return bestValue(weights, values, len(weights)-1, capacity)

def knapsack01(w, v, C):
    if not w or not v or len(w) != len(v):
        return 0
    n = len(w)
    dp = [[-1 for j in range(C+1)] for i in range(n)]

    for j in range(C+1):
        dp[0][j] = v[0] if j >= w[0] else 0

    for i in range(1, n):
        for j in range(0, C+1):
            dp[i][j] = dp[i-1][j]
            if j >= w[i]:
                dp[i][j] = max(dp[i][j], v[i] + dp[i-1][j-w[i]])

    return dp[n-1][C]


print(knapsack01([1,2,3], [6,10,12], 5))












