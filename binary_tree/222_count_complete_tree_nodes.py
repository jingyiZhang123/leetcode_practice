"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        left, right = root.left, root.right
        left_height = right_height= 0
        while left:
            left = left.left
            left_height += 1
        while right:
            right = right.right
            right_height += 1
        if left_height == right_height:
            return 2**(left_height + 1) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)























