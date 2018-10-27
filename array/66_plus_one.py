"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        result = int(''.join([str(x) for x in digits])) + 1
        return [int(x) for x in str(result)]

class Solution(object):
    def plusOne(self, digits):
        carrier = 1
        for i in range(len(digits)-1, -1, -1):
            carrier, digits[i] = divmod(digits[i]+carrier, 10)
        if carrier:
            digits = [1] + digits
        return digits

print(Solution().plusOne([0]))






