"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        max_water = tail * min(height[head], height[tail])
        while head < tail:
            if height[head] <= height[tail]:
                head += 1
            else:
                tail -= 1
            temp = (tail-head) * min(height[head], height[tail])
            max_water = temp if temp > max_water else max_water

        return max_water

print(Solution().maxArea([2,3,10,5,7,8,9]))
