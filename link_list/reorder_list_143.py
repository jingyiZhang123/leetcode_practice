"""
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from helper import *
class Solution(object):
    def _reverse(self, head):
        if not head or not head.next:
            return head
        prev_node = None
        cur_node = head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        medien_node = head
        end_node = head
        while True:
            if not end_node.next:
                next_node = medien_node.next
                medien_node.next = None
                medien_node = next_node
                break
            else:
                end_node = end_node.next

            if not end_node.next:
                next_node = medien_node.next
                medien_node.next = None
                medien_node = next_node
                break
            else:
                end_node = end_node.next

            medien_node = medien_node.next

        node = head
        l1 = head
        l2 = self._reverse(medien_node)
        is_l1 = False
        while l1 or l2:
            if is_l1:
                l2 = l2.next
                node.next = l1
                node = node.next
                is_l1 = not is_l1
            else:
                l1 = l1.next
                node.next = l2
                node = node.next
                is_l1 = not is_l1



a  = LinkedList([1,2,3,4])
Solution().reorderList(a.head)
a.print()













