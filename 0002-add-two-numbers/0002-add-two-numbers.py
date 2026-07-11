# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            # Agar list khatam ho gayi ho, value 0 lenge
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total = val1 + val2 + carry

            # Current digit
            digit = total % 10

            # Next addition ke liye carry
            carry = total // 10

            # Answer list mein new node add karna
            current.next = ListNode(digit)
            current = current.next

            # Dono lists mein aage badhna
            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return dummy.next
        