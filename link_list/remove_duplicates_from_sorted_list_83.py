"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        node = head
        record_node = node
        appeared = set()
        appeared.add(node.val)
        while node.next:
            next_node = node.next
            if next_node.val not in appeared:
                appeared.add(next_node.val)
                record_node.next = next_node
                record_node = next_node
            node = next_node
        record_node.next = None
        return head












