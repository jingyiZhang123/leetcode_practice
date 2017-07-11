"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ? k ? number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


from collections import defaultdict
from queue import PriorityQueue
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        info = defaultdict(int)
        for i in nums:
            info[i] += 1
        # return [x[0] for x in sorted(info.items(), key=lambda x:-x[1])[:k]]
        q = PriorityQueue()
        for val, freq in info.items():
            if q.qsize() >= k:
                temp = q.get()
                new_elem = temp if temp[0] > freq else (freq, val)
                q.put(new_elem)
            else:
                q.put((freq, val))
        result = []
        while not q.empty():
            result.append(q.get()[1])
        return list(reversed(result))

class Solution(object):
    def topKFrequent(self, nums, k):


print(Solution().topKFrequent([1,1,2,2,3,3,1,3,3], 3))








