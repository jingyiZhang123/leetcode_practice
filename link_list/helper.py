
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
    def print(self):
        temp = self
        while temp:
            print(temp.val, '->', end = ' ')
            temp = temp.next
        print()

class LinkedList:
    def __init__(self, L = None, key = lambda x: x):
        self.key = key
        if L is None:
            self.head = None
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next = Node(e)
            node = node.next

    def print(self, separator = ', '):
        '''
        >>> LinkedList(range(4)).print(':')
        0:1:2:3
        >>> LinkedList(range(4)).print('--')
        0--1--2--3
        '''
        if not self.head:
            return
        node = self.head
        print(node.val, end = '')
        node = node.next
        while node:
            print(separator, node.val, sep = '', end = '')
            node = node.next
        print()
