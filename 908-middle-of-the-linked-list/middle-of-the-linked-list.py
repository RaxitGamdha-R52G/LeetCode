# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p=head
        q=head.next
        while q != None:
            if q.next and q.next.next :
                q = q.next.next
            else:
                break
            p=p.next
        return p.next
        