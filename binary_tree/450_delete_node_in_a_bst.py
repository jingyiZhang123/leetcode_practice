"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _minimum(self, root):
        if not root.left:
            return root
        return self._minimum(root.left)

    def _remove_min(self, root):
        if not root.left:
            return root.right
        root.left = self._remove_min(root.left)
        return root

    def contains(self, root, key):
        if not root:
            return False
        if key < root.val:
            return self.contains(root.left, key)
        elif key > root.val:
            return self.contains(root.right, key)
        else:
            return True


    def _remove(self, root, key):
        if not root:
            return

        if key < root.val:
            root.left = self._remove(root.left, key)
        elif key > root.val:
            root.right = self._remove(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                delNode = root
                successor = self._minimum(delNode.right)
                successor.right = self._remove_min(delNode.right)
                successor.left = delNode.left
                return successor
        return root

    def deleteNode(self, root, key):
        if not root:
            return
        if not self.contains(root, key):
            return root
        return self._remove(root, key)






















