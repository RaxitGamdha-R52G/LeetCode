# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=q=head
        for i in range(n):
            p=p.next

        if q.next==p and p==None:
            return None
        elif p==None and q==head:
            head=head.next
        else:
            while(p.next!=None):
                p=p.next
                q=q.next
            q.next=q.next.next
        return head