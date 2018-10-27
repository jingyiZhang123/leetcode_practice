class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
        def to_base3(n):

            result = 0
            power = 0
            while n:
                temp = n % 3
                n //= 3
                result += (temp * (3**power))
                power += 1
  
            return result
        
        def xor3(a, b):
            result = 0
            power = 0
            while a or b:
                aa = a % 3
                bb = b % 3
                
                cc = (aa + bb) % 3
                result += (cc * (3 ** power))
                
                power += 1                
                a //= 3
                b //= 3
            return result
        for i in range(len(A)):
            A[i] = to_base3(A[i])
        
        print(A[i])
        for i in range(len(A) - 1, 0, -1):
            A[i-1] = xor3(A[i], A[i-1])
        
        return A[0]
        
print(Solution().singleNumberII([1,1,2,3,3,3,2,2,4,1]))