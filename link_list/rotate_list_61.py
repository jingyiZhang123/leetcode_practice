"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy_node = ListNode(0)
        dummy_node.next = head

        prev_node = dummy_node
        start_node = head
        end_node = head

        ll_len = 0
        temp = head
        while temp:
            temp = temp.next
            ll_len += 1
        k = k % ll_len

        for i in range(k):
            end_node = end_node.next

        if not end_node:
            return head
        while end_node.next:
            end_node = end_node.next
            start_node = start_node.next

        end_node.next = head
        dummy_node.next = start_node.next
        start_node.next = None

        return dummy_node.next













