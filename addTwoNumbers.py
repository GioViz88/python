# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        ans = ListNode(0,None)
        h = ans
        leftover = 0
        def get_val(l):
            return l.val if l else 0
        
        while l1 or l2:
            h.next = ListNode(0,None)
            h = h.next
            add_l1_l2_leftover = get_val(l1)+get_val(l2)+leftover
            val = add_l1_l2_leftover%10
            leftover = (add_l1_l2_leftover-val)//10
            h.val = val
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if leftover > 0:
            h.next = ListNode(leftover,None)
        return ans.next
