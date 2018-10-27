class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    def divisble(self, a, b):
        
        result = (a / b == a // b) or (b / a == b // a)
            
        return result
    
    def helper(self, arr, rest):
        if not rest:
            self.result += 1
            return
        
        for i in range(len(rest)):
            cur_elem_i = len(arr) + 1
            if self.divisble(rest[i], cur_elem_i):
                new_arr = arr + [rest[i]]
                remaining = rest[:i] + rest[i+1:]
                self.helper(new_arr, remaining)

    def countArrangement(self, N):
        self.result = 0
        
        self.helper([], [x for x in range(1, N+1)])
        return self.result
    
print(Solution().countArrangement(12))


