"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        prev_node = dummy_node
        cur_node = head
        while cur_node and cur_node.next:
            next_node = cur_node.next
            temp = next_node.next

            next_node.next = cur_node
            cur_node.next = temp
            prev_node.next = next_node

            prev_node = cur_node
            cur_node = cur_node.next
        return dummy_node.next














