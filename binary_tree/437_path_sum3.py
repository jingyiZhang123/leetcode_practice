"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _sum(self, root, target):
        if not root:
            return 0
        result = 0
        if root.val == target:
            result += 1
        result += self._sum(root.left, target - root.val)
        result += self._sum(root.right, target - root.val)
        return result


    def pathSum(self, root, sum):
        if not root:
            return 0
        result = self._sum(root, sum)
        result += self.pathSum(root.left, sum)
        result += self.pathSum(root.right, sum)
        return result

class Solution(object):
    def _sum(self, root, target, soFar):
        if sum(soFar) == target:
            self.result += 1
        if not root.left and not root.right:
            return
        if root.left:
            self._sum(root.left, target, soFar+[root.left.val])
        if root.right:
            self._sum(root.right, target, soFar+[root.right.val])

    def _pathSum(self, root, target):
        if not root:
            return 0
        self._sum(root, target, [root.val])
        if root.left: self._pathSum(root.left, target)
        if root.right: self._pathSum(root.right, target)


    def pathSum(self, root, sum):
        if not root:
            return 0

        self.result = 0
        self._pathSum(root, sum)
        return self.result
















