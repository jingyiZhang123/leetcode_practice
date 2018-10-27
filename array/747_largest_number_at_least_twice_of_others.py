class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_index = 0
        max_value = nums[0]
        max_expect = max_value * 2

        found = True
        for i in range(1, n):
            
            if nums[i] >= max_expect:
                found = True
                max_index = i
                max_value = nums[i]
                max_expect = max_value * 2

            elif nums[i] > max_value and nums[i] < max_expect:
                found = False
                max_index = i
                max_value = nums[i]
                max_expect = max_value * 2
                
            elif nums[i] < max_value and nums[i] * 2 > max_value:
                found = False
            

        return max_index if found else -1

a = Solution().dominantIndex([0,0,3,2])
print(a)

