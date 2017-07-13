from collections import deque,defaultdict
from copy import deepcopy

def NodePrint(node):
    if node:
        print('{}'.format(node.key), end='->')

class Node(object):
    """docstring for Node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def _insert(self, root, key, value):
        if not root:
            self.count += 1
            return Node(key, value)

        if key == root.key:
            root.value = value
        elif key < root.key:
            root.left = self._insert(root.left, key, value)
        else:
            root.right = self._insert(root.right, key, value)
        return root

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _search(self, root, key):
        if not root:
            return None
        if root.key == key:
            return root.value
        elif key > root.key:
            return self._search(root.right, key)
        else:
            return self._search(root.left, key)

    def search(self, key):
        if not self.root:
            return None
        return self._search(self.root, key)

    def _preorder_traversal(self, root, func):
        if not root:
            return
        func(root)
        self._preorder_traversal(root.left, func)
        self._preorder_traversal(root.right, func)

    def preorder_traversal(self, func):
        self._preorder_traversal(self.root, func)

    def _inorder_traversal(self, root, func):
        if not root:
            return
        self._inorder_traversal(root.left, func)
        func(root)
        self._inorder_traversal(root.right, func)

    def inorder_traversal(self, func):
        self._inorder_traversal(self.root, func)

    def _postorder_traversal(self, root, func):
        if not root:
            return
        self._postorder_traversal(root.left, func)
        self._postorder_traversal(root.right, func)
        func(root)

    def postorder_traversal(self, func):
        self._postorder_traversal(self.root, func)

    def level_traversal(self, func):
        if not self.root:
            return
        stack = [(self.root, 0)]
        levels = defaultdict(list)
        while stack:
            node, level = stack.pop()
            levels[level].append(node)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        for level, nodes in sorted(levels.items()):
            print('level %s'%level)
            for node in nodes:
                func(node)

    def _remove_min(self, root):
        if not root.left:
            self.count -= 1
            return root.right
        root.left = self._remove_min(root.left)
        return root

    def remove_min(self):
        if self.root:
            self.root = self._remove_min(self.root)

    def _remove_max(self, root):
        if not root.right:
            self.count -= 1
            return root.left
        root.right = self._remove_max(root.right)
        return root

    def remove_max(self):
        if not self.root:
            return
        self.root = self._remove_max(self.root)


    def remove_max_iter(self):
        if not self.root:
            return self.root
        parent = None
        target = self.root
        while target.right:
            parent = target
            target = target.right
        if parent:
            parent.right = target.left
        else:
            self.root = target.left

        self.count -= 1
        return self.root


    def remove_min_iter(self):
        if not self.root:
            return self.root
        parent = None
        node = self.root
        while node.left:
            parent = node
            node = node.left
        if parent:
            parent.left = node.right
        else:
            self.root = node.right
        self.count -= 1
        return self.root

    # def _remove(self, root, key):
    #     if not root:
    #         return
    #     if key < root.key:
    #         root.left = self._remove(root.left, key)
    #     elif key > root.key:
    #         root.right = self._remove(root.right, key)
    #     else: # key == root.key => remove this node
    #         if not root.left:
    #             self.count -= 1
    #             return root.right
    #         elif not root.right:
    #             self.count -= 1
    #             return root.left
    #         else:
    #             delNode = root
    #             successor = deepcopy(self._minimum(delNode.right))
    #             successor.right = self._remove_min(delNode.right)
    #             successor.left = delNode.left
    #             return successor
    #     return root
    def _remove(self, root, key):
        if not root:
            return
        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)
        else: # key == root.key => remove this node
            if not root.left:
                self.count -= 1
                return root.right
            elif not root.right:
                self.count -= 1
                return root.left
            else:
                delNode = root
                predecessor = self._maximum(delNode.left)
                predecessor.left = self._remove_max(delNode.left)
                predecessor.right = delNode.right
                return predecessor
        return root


    def remove(self, key):
        if not self.root:
            return
        self.root = self._remove(self.root, key)

    def _minimum(self, root):
        if not root.left:
            return root
        return self._minimum(root.left)

    def mininum(self):
        if not self.root:
            return
        return self._minimum(self.root)

    def _maximum(self, root):
        if not root.right:
            return root
        return self._maximum(root.right)

    def maximum(self):
        if not self.root:
            return
        return self._maximum(self.root)







from random import randint, seed
seed(0)
btree = BinarySearchTree()
rand = [randint(0,100) for _ in range(10)]
print(rand)
for i in rand:
    btree.insert(i, i*10)

print(btree.search(100))
# btree.preorder_traversal(NodePrint)
print(btree.mininum().key)
print(btree.maximum().key)
print('-----------------------------------')
btree.inorder_traversal(NodePrint)
print()
# print('-----------------------------------')
# btree.postorder_traversal(NodePrint)
print('-----------------------------------')
# btree.level_traversal(NodePrint)

# for _ in range(5):
#     btree.remove_max()
#     btree.inorder_traversal(NodePrint)
#     print()
#     btree.remove_min()
#     btree.inorder_traversal(NodePrint)
#     print()

btree.remove(51)
btree.remove(53)
btree.remove(97)
btree.remove(5)
btree.remove(100)
btree.inorder_traversal(NodePrint)
print()
print('----------------------------------')









