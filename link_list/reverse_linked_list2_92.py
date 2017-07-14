"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ? m ? n ? length of list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy_node = ListNode(0)
        dummy_node.next = head
        prev_node = dummy_node
        for i in range(m-1):
            prev_node = prev_node.next

        reverse = None
        node = prev_node.next
        for i in range(n-m+1):
            next_node = node.next
            node.next = reverse
            reverse = node
            node = next_node

        prev_node.next.next = node
        prev_node.next = reverse

        return dummy_node.next













