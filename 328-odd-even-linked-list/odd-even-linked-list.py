# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        p1 = head
        p2 = head.next
        odd = p1
        even = p2

        while p1 and p2 and p2.next:
            p1.next  = p2.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        
        p1.next = even
        return odd