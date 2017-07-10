"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy_node = ListNode(0)
        dummy_node.next = head
        record_node = dummy_node
        cur_node = head

        while cur_node and cur_node.next:
            next_node = cur_node.next
            if next_node.val != cur_node.val:
                record_node.next = cur_node
                record_node = cur_node
                cur_node = next_node
            else:
                while cur_node.next and cur_node.val == cur_node.next.val:
                    cur_node = cur_node.next
                cur_node = cur_node.next
                record_node.next = cur_node

        return dummy_node.next








