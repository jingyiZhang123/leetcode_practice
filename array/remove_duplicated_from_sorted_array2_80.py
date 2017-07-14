"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 1
        record_index = 1
        record_num = nums[0]
        record_len = 1
        data_len = len(nums)
        for i in range(1, data_len):
            if nums[i] > record_num:
                record_num = nums[i]
                nums[record_index] = nums[i]
                record_index += 1
                result += 1
                record_len = 1
            elif nums[i] == record_num:
                if record_len < 2:
                    nums[record_index] = nums[i]
                    record_len += 1
                    record_index += 1
                    result += 1


        return result

L = [1,1,1,1,3,3]
result = Solution().removeDuplicates(L)
print(result, L)
