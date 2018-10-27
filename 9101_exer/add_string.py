class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        result = 0
        num1 = [int(x) for x in reversed(num1)]
        num2 = [int(x) for x in reversed(num2)]
        len1 = len(num1)
        len2 = len(num2)

        i = 0
        carry = 0
        while i < len1 or i < len2:
            temp = 0
            if i < len1:
                temp += num1[i]
            if i < len2:
                temp += num2[i]
            
            temp += carry
            carry = temp // 10
            temp %= 10
            
            result += (temp * (10 ** i))
            i += 1
        return result
print(Solution().addStrings("123","45"))
