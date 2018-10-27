
class Solution(object):
    def calculate(self, A):
        n = len(A)
        opt_suf = [1 for x in A]
        opt_sum = [x for x in A]

        for i in range(1, n):
            if(opt_sum[i] < opt_sum[i-1] + opt_sum[i]):
                opt_sum[i] = opt_sum[i-1] + opt_sum[i]
                opt_suf[i] = opt_suf[i-1] + 1
        print(opt_sum)
        print(opt_suf)
        return None



arr = [-2, -3, 4, -1, -2, 1, 5, -3]
ret = Solution().calculate(arr)

print(ret)
