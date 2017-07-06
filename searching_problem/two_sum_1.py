
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data_len = len(nums)
        if data_len <= 1:
            return []
        need = {}
        for i in range(data_len):
            if nums[i] not in need:
                need[target - nums[i]] = i
            else:
                return [need[nums[i]], i]
        return []

print(Solution().twoSum([3,2,3], 6))
