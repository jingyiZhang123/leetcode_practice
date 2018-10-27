class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        if n == 1:
            return nums
        ii = n - 1
        for ii in range(n - 1, 0, -1):
            i = ii - 1
            if nums[i] < nums[ii]:
                j = n - 1
                while nums[i] >= nums[j]:
                    j -= 1
                
                nums[i], nums[j] = nums[j], nums[i]
                nums = nums[:i+1] + list(reversed(nums[i+1:]))
                
                return nums
        
        return sorted(nums)


print(Solution().nextPermutation([1, 3 ,2]))


