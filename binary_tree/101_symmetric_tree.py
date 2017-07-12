"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution
class Solution(object):
    def _is_symmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            return self._is_symmetric(left.left, right.right) and self._is_symmetric(left.right, right.left)
        else:
            return False


    def isSymmetric(self, root):
        if not root:
            return True
        return self._is_symmetric(root.left, root.right)

# iterative solution
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()
            if (left and not right) or (not left and right):
                return False
            if left and right and left.val != right.val:
                return False
            if left and right:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
        return True


















