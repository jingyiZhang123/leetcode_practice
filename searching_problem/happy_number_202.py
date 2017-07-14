"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        calculated = set([n])
        each_num = [int(x) for x in str(n)]
        result = sum(x**2 for x in each_num)
        if result == 1:
            return True
        while result not in calculated:
            calculated.add(result)
            result = sum(int(x)**2 for x in str(result))
            if result == 1:
                return True
        else:
            return False
print(Solution().isHappy(20))












