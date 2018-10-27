class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return
        
        self.dp = [None for _ in range(len(nums))]
        self.dp[0] = nums[0]

        for i in range(1, len(nums)):
            self.dp[i] = nums[i] + self.dp[i - 1]

        return
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if  i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i-1]
        


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)
print(param_1)
param_1 = obj.sumRange(2,5)
print(param_1)
param_1 = obj.sumRange(0,5)
print(param_1)