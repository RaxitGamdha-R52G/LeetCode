# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        p = head
        q = head.next.next

        while q and q.next:
            p = p.next
            q = q.next.next
        p.next = p.next.next

        return head

        