"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# easy solution
class Solution(object):
    def _postorderTraversal(self, root):
        if root:
            self._postorderTraversal(root.left)
            self._postorderTraversal(root.right)
            self.result.append(root.val)


    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self._postorderTraversal(root)
        return self.result

# iterative solution
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = [(root, 'ADD')]
        result = []

        while stack:
            node, command = stack.pop()
            if command == 'RESULT':
                result.append(node.val)
            elif command == 'ADD':
                stack.append((node, 'RESULT'))
                if node.right: stack.append((node.right, 'ADD'))
                if node.left: stack.append((node.left, 'ADD'))
        return result








