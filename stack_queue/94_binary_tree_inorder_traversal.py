"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# easy recursive solution
class Solution(object):
    def _inorderTraversal(self, root):
        if root:
            self._inorderTraversal(root.left)
            self.result.append(root.val)
            self._inorderTraversal(root.right)


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self._inorderTraversal(root)
        return self.result

# iterative solution
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []

        stack = [(root, 'ADD')]
        result = []

        while stack:
            node, command = stack.pop()
            if command == 'RESULT':
                result.append(node.val)
            elif command == 'ADD':
                if node.right:
                    stack.append((node.right, 'ADD'))
                stack.append((node, 'RESULT'))
                if node.left:
                    stack.append((node.left, 'ADD'))

        return result





















