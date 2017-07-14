"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummy_node = ListNode(0)
        dummy_node.next = head

        del_node = head
        end_node = head
        prev_node = dummy_node
        for i in range(n-1):
            end_node = end_node.next

        while end_node.next:
            end_node = end_node.next
            del_node = del_node.next
            prev_node = prev_node.next

        prev_node.next = del_node.next
        return dummy_node.next



















