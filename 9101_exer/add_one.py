class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        result = []
        carry = 1
        while digits or carry:
            if digits:
                d = digits.pop()
            else:
                d = 0
            
            d += carry

            carry = d // 10
            d = d % 10

            result.append(d)
            
        return [x for x in reversed(result)]

print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([9,9,9]))