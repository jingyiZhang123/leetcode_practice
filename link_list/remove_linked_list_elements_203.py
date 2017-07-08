"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur_node = head
        record_node = dummy_node
        while cur_node:
            next_node = cur_node.next
            if cur_node.val != val:
                record_node.next = cur_node
                record_node = record_node.next
            cur_node = next_node
        record_node.next = None
        return dummy_node.next







