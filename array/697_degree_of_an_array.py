
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {x:[0, -1, -1] for x in nums}
        max_n = -1
        for i, v in enumerate(nums):
            counter[v][0] += 1
            if counter[v][1] == -1:
                counter[v][1] = i
            counter[v][2] = i
            
            if max_n < counter[v][0]:
                max_n = counter[v][0]
        counter = {x:y[2]-y[1] for x,y in counter.items() if y[0] == max_n}
        
        print(counter)
        return min(counter.values()) + 1
        

aa = Solution().findShortestSubArray([1,2,2,3,1])
print(aa)