"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _sum(self, root, target, soFar):
        if not root.left and not root.right and target == 0:
            self.result.append(soFar)
        if root.left:
            self._sum(root.left, target - root.left.val, soFar + [root.left.val])
        if root.right:
            self._sum(root.right, target - root.right.val, soFar + [root.right.val])

    def pathSum(self, root, sum):
        if not root:
            return []
        self.result = []
        self._sum(root, sum - root.val, [root.val])
        return self.result










