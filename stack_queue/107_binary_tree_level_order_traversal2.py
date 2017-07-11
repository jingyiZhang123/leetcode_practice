"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [(root,0)]
        result = defaultdict(list)

        while stack:
            node, level = stack.pop()
            result[level].append(node.val)
            if node.right: stack.append((node.right, level + 1))
            if node.left: stack.append((node.left, level + 1))

        return [y[1] for y in sorted(result.items(), key=lambda x:-x[0])]









