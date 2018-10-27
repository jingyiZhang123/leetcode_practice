class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        def helper(path, rest, result):
            if not rest:
                self.counter += 1
                if all(path[i] == result[i] for i in range(len(result))):
                    self.result = self.counter
                return 
            for i in range(len(rest)):
                cur_index = len(path)
                if rest[i] != result[cur_index]:
                    temp = 1
                    for x in range(2, len(rest)):
                        temp *= x
                    self.counter += (temp)
                    continue
                else:
                    helper(path+[rest[i]], rest[:i]+rest[i+1:], result)

        sortA = sorted(A)
        self.counter = 0
        self.result = 0
        helper([], sortA, A)
        return self.result


print(Solution().permutationIndex([10,9,8,7,6,5,4,3,2,1]))
print(Solution().permutationIndex([2,1,4]))