# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next:
            p = head
            while p and p.next:
                r = p
                q = p.next
                while q and q.next :
                    r = q
                    q = q.next
                r.next = None
                q.next = p.next
                p.next = q
                p = p.next.next