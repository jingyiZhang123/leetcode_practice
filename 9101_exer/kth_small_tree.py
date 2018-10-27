"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def _mid_traverse(self, root, target):
        if self.result is not None:
            return
        
        if root is not None:
            self._mid_traverse(root.left, target)
            self.counter += 1
            if self.counter == target:
                self.result = self.val
            self._mid_traverse(root.right, target)


    def kthSmallest(self, root, k):
        # write your code here
        self.counter = 0
        self.result = None
        self._mid_traverse(root, k)
        return self.result