"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
"""

from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # O(n^2) solution
        num_points = len(points)
        result = 0
        for i in range(num_points):
            temp = defaultdict(int)
            for j in range(num_points):
                if i == j:
                    continue
                distance = ((points[i][0]-points[j][0]) ** 2) + \
                            ((points[i][1]-points[j][1]) ** 2)
                temp[distance] += 1
            for each_pair in temp.values():
                if each_pair >= 2:
                    result += (each_pair * (each_pair - 1))
        return result


print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))












