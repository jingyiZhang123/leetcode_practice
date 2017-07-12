"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# stack solution
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        stack = [(root, [str(root.val)])]
        result = []
        while stack:
            node, path = stack.pop()
            if node.left: stack.append((node.left, path+[str(node.left.val)]))
            if node.right: stack.append((node.right, path+[str(node.right.val)]))
            if not node.left and not node.right:
                result.append(path)

        result = ['->'.join(x) for x in result]
        return result

class Solution(object):
    def _path(self, root, soFar):
        if not root.left and not root.right:
            self.result.append(soFar)
            return
        if root.left: self._path(root.left, soFar+[str(root.left.val)])
        if root.right: self._path(root.right, soFar+[str(root.right.val)])

    def binaryTreePaths(self, root):
        if not root:
            return []
        self.result = []
        self._path(root, [str(root.val)])
        result = ['->'.join(x) for x in self.result]
        return result





















