# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p=head.next
        q=head
        while p != None:
            if q.val == p.val:
                q.next= p.next
            else:
                q = q.next
            p = p.next
        q.next = None
        return head
            

        