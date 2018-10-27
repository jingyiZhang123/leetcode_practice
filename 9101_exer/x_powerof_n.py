class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n <= 2:
            return x ** n

        isOdd = (n & 1 == 1)
        n = n - 1 if isOdd else n
        result = self.myPow(x, n >> 1)
        result *= result
        if isOdd: # odd
            result *= x
        return result

print(Solution().myPow(2,10))
