"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
# solution 1
# from random import randint
# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         data_len = len(nums)
#         self._threeway_sort(nums, 0, data_len - 1)

#     def _threeway_sort(self, arr, left, right):
#         if(left >= right):
#             return

#         lt, gt = self._partition(arr, left, right)

#         self._threeway_sort(arr, left, lt-1)
#         self._threeway_sort(arr, gt, right)

#     def _partition(self, arr, left, right):
#         swap = left + randint(0, (right - left))
#         arr[left], arr[swap] = arr[swap], arr[left]
#         pivat = arr[left]
#         lt = left # [left..lt] < pivat and [lt+1..gt-1] == pivat
#         gt = right + 1 # [gt..right] > pivat

#         i = left + 1
#         while i < gt:
#             if arr[i] < pivat:
#                 arr[lt+1], arr[i] = arr[i], arr[lt+1]
#                 lt += 1
#                 i += 1
#             elif arr[i] > pivat:
#                 gt -= 1
#                 arr[gt], arr[i] = arr[i], arr[gt]
#             else:
#                 i += 1
#         arr[left], arr[lt] = arr[lt], arr[left]
#         return lt, gt

# solution 2:
# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         data_len = len(nums)
#         counter = [0,0,0]
#         for i in nums:
#             counter[i] += 1

#         temp = 0
#         for i in range(0,3):
#             for j in range(temp, temp + counter[i]):
#                 nums[j] = i
#             temp += counter[i]

#solution 3
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        zero = left - 1 #[left..zero] = 0
        two = right + 1 #[two..right] = 2

        i = 0
        while(i < two):
            if nums[i] == 0:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]



L = [0, 1,2,2,0,2,1]
result = Solution().sortColors(L)
print(result, L)









