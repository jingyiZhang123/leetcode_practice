
result = []
def _bag(soFar, rest, C):
    global result
    s = sum(x[0] for x in soFar)
    if not rest:
        if s <= C:
            result.append(sum(x[1] for x in soFar))
        return

    for i in range(len(rest)):
        next = rest[i]
        remaining = rest[i+1:]
        _bag(soFar+[next], remaining, C)


def bag(w, v, C):
    w_v = list(zip(w,v))
    _bag([], w_v, C)
    # global result
    return max(result)
print(bag([1,2,3,1], [6,10,12,5], 5))
memo = {}
def _bag(w, v, cur, c):
    if cur >= len(w) or c < 0:
        return 0

    if (cur, c) in memo:
        return memo[(cur, c)]

    res = _bag(w, v, cur+1, c)
    if w[cur] <= c:
        res = max(res, v[cur] + _bag(w, v, cur+1, c-w[cur]))
    memo[(cur, c)] = res
    return res


def bag(w, v, C):
    return _bag(w, v, 0, C)
print(bag([1,2,3,1], [6,10,12,5], 5))


def bag(w, v, C):
    num_items = len(w)
    dp = [[-1 for j in range(C+1)] for i in range(num_items)]
    for j in range(C + 1):
        dp[0][j] = v[0] if w[0] <= j else 0

    for i in range(1, num_items):
        for j in range(C + 1):
            dp[i][j] = dp[i-1][j]
            if w[i] <= j:
                dp[i][j] = max(dp[i][j], v[i] + dp[i-1][j-w[i]])
    return dp[num_items-1][C]
print(bag([1,2,3,1], [6,10,12,5], 5))

def bag(w, v, C):
    num_items = len(w)
    current = [-1 for j in range(C+1)]
    next = [-1 for j in range(C+1)]
    for j in range(C + 1):
        current[j] = v[0] if w[0] <= j else 0

    for i in range(1, num_items):
        for j in range(C + 1):
            next[j] = current[j]
            if w[i] <= j:
                next[j] = max(next[j], v[i] + current[j-w[i]])
        current, next = next, [-1 for j in range(C+1)]
    return current[-1]
print(bag([1,2,3,1], [6,10,12,5], 5))

def bag(w, v, C):
    num_items = len(w)
    dp = [[-1 for j in range(C+1)] for i in range(2)]
    for j in range(C + 1):
        dp[0][j] = v[0] if w[0] <= j else 0

    for i in range(1, num_items):
        for j in range(C + 1):
            dp[i%2][j] = dp[(i-1)%2][j]
            if w[i] <= j:
                dp[i%2][j] = max(dp[i%2][j], v[i] + dp[(i-1)%2][j-w[i]])

    return dp[(num_items-1)%2][C]

print(bag([1,2,3,1], [6,10,12,5], 5))














