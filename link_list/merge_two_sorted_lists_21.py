"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy_node = ListNode(0)
        node = dummy_node
        l1_node = l1
        l2_node = l2

        while l1_node or l2_node:
            if not l1_node:
                node.next = l2_node
                return dummy_node.next
            elif not l2_node:
                node.next = l1_node
                return dummy_node.next
            elif l1_node.val < l2_node.val:
                node.next = l1_node
                node = node.next
                l1_node = l1_node.next
            else:
                node.next = l2_node
                node = node.next
                l2_node = l2_node.next










