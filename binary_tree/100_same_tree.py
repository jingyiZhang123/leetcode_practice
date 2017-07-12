"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""


class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False

