class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return -1
        
        sum_left = 0
        sum_right = sum(nums[1:])

        for i in range(n):
            #print(sum_left, sum_right)
            if sum_left != sum_right:
                sum_left += nums[i]
                if i + 1 >= n:
                    sum_right = 0
                else:
                    sum_right -= nums[i + 1]
            else:
                return i
            
        return -1

aa = Solution().pivotIndex([-1,-1,-1,-1,-1,-1])
print(aa)