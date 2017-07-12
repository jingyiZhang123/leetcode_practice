"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _height(self, root):
        if not root:
            return 0
        return max(self._height(root.left), self._height(root.right)) + 1

    def isBalanced(self, root):
        if not root:
            return True
        left_height = self._height(root.left)
        right_height = self._height(root.right)

        return abs(left_height - right_height) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)
























