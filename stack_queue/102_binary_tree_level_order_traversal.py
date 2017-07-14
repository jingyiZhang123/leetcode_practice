"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1
from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [(root, 0)]
        result = defaultdict(list)
        while stack:
            node, level = stack.pop()
            if node.right: stack.append((node.right, level + 1))
            if node.left: stack.append((node.left, level + 1))
            result[level].append(node.val)

        return result.values()

# solution 2

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = [[root.val]]
        parent = [root]
        while parent:
            children = []
            for node in parent:
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            if children:
                result.append([x.val for x in children])
            parent = children

        return result







