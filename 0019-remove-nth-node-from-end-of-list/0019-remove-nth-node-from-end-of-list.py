from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        fast = dummy
        slow = dummy

        # Create a gap of n nodes
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next