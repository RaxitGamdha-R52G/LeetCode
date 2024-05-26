# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        p=None
        q=head
        while q!= None:
            if q.val == val:
                if p is not None:
                    p.next = q.next
                else:
                    head = head.next
                q=q.next
            else:
                p=q
                q=q.next
        
        return head



        