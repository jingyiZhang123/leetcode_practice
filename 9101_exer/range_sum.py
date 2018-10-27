class Solution:
    """
    @param nums: a list of integers
    @param lower: a integer
    @param upper: a integer
    @return: return a integer
    """
    def countRangeSum(self, nums, lower, upper):
        def mergesort(data, lower, upper, left, right):
            if right - left <= 1:
                return 0
            mid = (left + right) // 2
            lb = ub = mid
            count = 0
            count = mergesort(data, lower, upper, left, mid) + mergesort(data, lower, upper, mid, right)
            for i in range(left, mid):
                

        n = len(nums)
        sums = [0 for _ in range(n + 1)]
        for i in range(n):
            sums[i+1] = sums[i] + nums[i]
        return mergesort(nums, lower, upper, 0, n + 1)
