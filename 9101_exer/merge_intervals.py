"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals:
            return []
            
        intervals.sort(key=lambda x:x.start, reverse=True)
        result = []
        result.append(intervals.pop())

        while intervals:
            a = result[-1]
            b = intervals.pop()
            if a.end >= b.start:
                a.end = max(a.end, b.end)
            else:
                result.append(b)

        return result


