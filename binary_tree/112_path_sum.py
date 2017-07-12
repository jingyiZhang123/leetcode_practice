"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: DFS
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, val = stack.pop()
            if val == sum and not node.left and not node.right:
                return True
            if node.left: stack.append((node.left, node.left.val + val))
            if node.right: stack.append((node.right, node.right.val + val))
        else:
            return False

# Solution 2: recursion:
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        left_has = False
        right_has = False
        if root.left:
            left_has = self.hasPathSum(root.left, sum - root.val)
        if root.right:
            right_has = self.hasPathSum(root.right, sum - root.val)
        return left_has or right_has


# Solution 3: recursion:
class Solution(object):
    def _has_path_sum(self, root, sum):
        if not root.left and not root.right:
            return root.val == sum
        if root.left and self._has_path_sum(root.left, sum-root.val):
            return True
        if root.right and self._has_path_sum(root.right, sum-root.val):
            return True
        return False

    def hasPathSum(self, root, sum):
        if not root:
            return False
        return self._has_path_sum(root, sum)

# Solution 4: recursion:
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root: return False
        if not root.right and not root.left: return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)




