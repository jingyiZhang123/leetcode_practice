class Solution:
    """
    @param a: a positive integer
    @return: the smallest positive integer whose multiplication of each digit equals to a
    """
    def smallestFactorization(self, a):
        result = []
        for _ in range(10):
            if a == 1:
                break
            for i in range(9, 1, -1):
                if a / i == a // i:
                    a //= i
                    result.append(i)
                    break
            else:
                if not result:
                    return 0
                a *= result.pop()
        else:
            return 0
        return int(''.join(str(x) for x in reversed(result)))

print(Solution().smallestFactorization(11))