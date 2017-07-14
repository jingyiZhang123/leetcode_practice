"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ? k ? BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder_traversal(self, root):
        if root and self.result is None:
            self.inorder_traversal(root.left)
            self.count -= 1
            if self.count == 0:
                self.result = root.val
            self.inorder_traversal(root.right)



    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        self.count = k
        self.result = None
        self.inorder_traversal(root)
        return self.result


