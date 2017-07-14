"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from helper import *

class Solution(object):
    def _reverse(self, head, tail):
        if not head or not head.next:
            return head
        cur_node = head
        prev_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node

            prev_node = cur_node
            cur_node = next_node
            if prev_node == tail:
                break

        return prev_node


    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        record_node = dummy_node

        begin_node = head
        end_node = head

        while end_node:
            for i in range(k-1):
                end_node = end_node.next
                if not end_node:
                    record_node.next = begin_node
                    return dummy_node.next
            next_start = end_node.next if end_node else end_node

            record_node.next = self._reverse(begin_node, end_node)
            record_node = begin_node

            begin_node = next_start
            end_node = next_start

        return dummy_node.next


a  = LinkedList([1,2,3,4,5,6])
a = Solution().reverseKGroup(a.head, 3)
a.print()










