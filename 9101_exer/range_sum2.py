class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        left = float('Inf')
        right = float('-Inf')
        n = len(nums)
        
        for i in range(n):
            left = min(left, nums[i])
            right = max(right, nums[i])


        while right-left > 0:
            
            mid = (right-left)/2
            print(left, right, mid)

            sumAi = [0 for _ in range(n + 1)]
            for i in range(n):
                sumAi[i+1] = sumAi[i] + nums[i] - mid
            
            preMin = 0
            sumMax = float('-Inf')
            for i in range(k, n+1):
                sumMax = max(sumMax, sumAi[i] - preMin)
                preMin = min(preMin, sumAi[i-k+1])
            

            if(sumMax>0):
                left = mid
            else:
                right = mid

        
        return left


print(Solution().maxAverage([1,12,-5,-6,50,3], 3))