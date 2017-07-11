"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(nlogn)
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        lists = [x for x in lists if x]
        if not lists:
            return

        for each_head in lists:
            node = each_head
            while node:
                heapq.heappush(heap, (node.val, node))
                node = node.next

        new_head = heapq.heappop(heap)[1]
        node = new_head
        while heap:
            node.next = heapq.heappop(heap)[1]
            node = node.next
        node.next = None
        return new_head

# O(nlogk)
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        lists = [x for x in lists if x]
        if not lists:
            return

        num_heads = len(lists)
        heads = [x for x in lists]
        for each_head in heads:
            heapq.heappush(heap, (each_head.val, each_head))

        dummy_head = ListNode(0)
        node = dummy_head
        while heap:
            temp = heapq.heappop(heap)[1]
            node.next = temp
            temp = temp.next
            node = node.next
            if temp: heapq.heappush(heap, (temp.val, temp))

        node.next = None
        return dummy_head.next










