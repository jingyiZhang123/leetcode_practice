"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _sum(self, root, soFar):
        if not root.left and not root.right:
            self.result.append(soFar)
        if root.left:
            self._sum(root.left, soFar + [str(root.left.val)])
        if root.right:
            self._sum(root.right, soFar + [str(root.right.val)])

    def sumNumbers(self, root):
        if not root:
            return 0
        self.result = []
        self._sum(root, [str(root.val)])
        return sum(int(''.join(x)) for x in self.result)














