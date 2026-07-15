from typing import List, Optional
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        min_heap = []

        # Har non-empty list ka first node heap mein daalo
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, index, node))

        dummy = ListNode()
        current = dummy

        while min_heap:
            value, index, node = heapq.heappop(min_heap)

            # Smallest node merged list mein add karo
            current.next = node
            current = current.next

            # Usi list ka next node heap mein daalo
            if node.next:
                heapq.heappush(
                    min_heap,
                    (node.next.val, index, node.next)
                )

        return dummy.next