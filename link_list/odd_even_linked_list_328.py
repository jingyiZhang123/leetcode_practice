"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd_head = head
        even_head = head.next

        odd_node = head
        even_node = head.next
        node = head.next.next

        is_odd = True
        while node:
            next_node = node.next
            if is_odd:
                odd_node.next = node
                odd_node = odd_node.next
            else:
                even_node.next = node
                even_node = even_node.next
            is_odd = not is_odd
            node = next_node

        odd_node.next = even_head
        even_node.next = None
        return odd_head

















