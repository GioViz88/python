# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        # Move fast pointer n steps ahead
        for i in range(0, n):
            if fast.next is None:
                # If n is equal to the number of nodes, delete the head node
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next
        # Loop until fast node reaches to the end
        # Now we will move both slow and fast pointers
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        # Delink the nth node from last
        if slow.next is not None:
            slow.next = slow.next.next
        return head