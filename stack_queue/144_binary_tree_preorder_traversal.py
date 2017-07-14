"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution
class Solution(object):
    def _preorderTraversal(self, root):
        if root:
            self.result.append(root.val)
            self._preorderTraversal(root.left)
            self._preorderTraversal(root.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self._preorderTraversal(root)
        return self.result

# iterative solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

# more generic iterative solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [(root, 'ADD'), (root, 'RESULT')]
        result = []
        while stack:
            node, command = stack.pop()
            if command == 'RESULT':
                result.append(node.val)
            elif command == 'ADD':
                if node.right:
                    stack.append((node.right, 'ADD'))
                    stack.append((node.right, 'RESULT'))
                if node.left:
                    stack.append((node.left, 'ADD'))
                    stack.append((node.left, 'RESULT'))

        return result


















