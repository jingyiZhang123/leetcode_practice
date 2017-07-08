"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lt_list = []
        gt_eq_list = []
        if not head or not head.next:
            return head
        node = head
        while node:
            next_node = node.next
            if node.val < x:
                lt_list.append(node)
            else:
                gt_eq_list.append(node)
            node = next_node

        dummy_node = ListNode(0)
        node = dummy_node
        for i in range(0, len(lt_list)):
            node.next = lt_list[i]
            node = node.next
        for i in range(0, len(gt_eq_list)):
            node.next = gt_eq_list[i]
            node = node.next
        node.next = None
        return dummy_node.next















