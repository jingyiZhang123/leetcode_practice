"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
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
        cur_node = head
        prev_node = None

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        median_node = head
        end_node = head
        while 1:
            if end_node.next:
                end_node = end_node.next
            else:
                next_node = median_node.next
                median_node.next = None
                median_node = next_node
                break

            if end_node.next:
                end_node = end_node.next
            else:
                next_node = median_node.next
                median_node.next = None
                median_node = next_node
                break

            median_node = median_node.next

        l1 = head
        l2 = self._reverse(median_node)

        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True



a  = LinkedList([1,2,1])
Solution().isPalindrome(a.head)
a.print()











