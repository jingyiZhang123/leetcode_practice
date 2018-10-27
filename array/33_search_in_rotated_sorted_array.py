"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

print(Solution().search([3,5,1], 1))

from math import factorial

def pick(a,b):
    return factorial(a)//(factorial(a-b) * factorial(b))

num_people = 40
result = 0
# print(pick(num_people, ) * (0.1**i) * (0.9**(num_people-i)))
for i in range(11, num_people+1):
    result += pick(num_people, i) * (0.1**i) * (0.9**(num_people-i))

print(result)

# import matplotlib.pyplot as plt
# plt.plot([735, 6317, 16123], [7.46,6.935,5.6377])
# plt.xlabel('Distance (kM)')
# plt.ylabel('Ratio between RTT and shortest possible time')
# plt.show()

print('--------------------')
n = 2
s = 0
a = 255
for i in range(1, n+1):
    s += a**i
    # print(format(s, '04x'))
    # input()
print(s)
print(format(s, '04x'), '!!!!!!!')
# print(2**20)

num = 250
den = 50
from fractions import gcd
print(gcd(num, den),'!!!')

a = num
b = den

c = 1

while 1:
    if a == 0:
        print(b*c, '??')
        break
    if b == 0:
        print(a*c, '??')
        break
    if a % 2 == 0 and b % 2 == 0:
        a = a//2
        b = b//2
        c = c*2
    elif a % 2 == 0:
        a = a // 2
    elif b % 2 == 0:
        b = b // 2
    else:
        tempa, tempb = a, b
        a = abs(tempa - tempb)//2
        b = min(tempa, tempb)


# a = num
# b = den
# while a != b:
#     if b > a:
#         a,b = b,a
#     if b == 0:
#         print(a,'???')
#         break
#     a %= b
#     print(format(a, '02x'), format(b, '02x'))
#     input()

# else:
#     print(a,'???')

# a,b = divmod(num,den)
# print(a,b)

# cur = prev = den
# while num >= den:
#     print(format(num, '02x'), format(den,'02x'),\
#      format(cur, '02x'), format(prev, '02x'))
#     # input()
#     if cur >= num:
#         num -= prev
#         cur = prev = den
#     else:
#         prev = cur
#         cur *= 2

# print(num)
# 105 >= 8
# 105
# 8
# 16
# 32
# prev 64
# cur 128

# rem = 41
# 41 >= 8
# 41
# 8
# 16
# 32

# 9 >= 8
# rem = 9
# 9
# 8

# 9 < 8
# rem = 1


