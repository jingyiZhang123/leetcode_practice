"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        num_points = len(points)
        max_num = 0
        for i in range(num_points):
            record = defaultdict(int)
            num_sp = 0
            for j in range(num_points):
                if i == j:
                    continue
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    num_sp += 1
                elif points[j].x == points[i].x:
                    gradient = 99999
                    gradient = round(gradient, 3)
                    record[gradient] += 1
                else:
                    gradient = (points[j].y - points[i].y)*1.0 / (points[j].x - points[i].x)
                    gradient = round(gradient, 3)
                    record[gradient] += 1
            if record:
                temp = max(record.values()) + num_sp
            else:
                temp = num_sp

            max_num = temp if temp > max_num else max_num

        return max_num + 1

print(Solution().maxPoints([[0,0]]))
