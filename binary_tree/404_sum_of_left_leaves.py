"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _sum(self, root, result, is_left):
        if not root:
            return result
        if not root.left and not root.right:
            return (result + root.val) if is_left else result

        return self._sum(root.left, result, True) + self._sum(root.right, result, False)


    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        return self._sum(root.left, 0, True) + self._sum(root.right, 0, False)

















