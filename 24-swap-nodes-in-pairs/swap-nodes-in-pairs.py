# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p=head
        while p!=None and p.next!= None:
            p.val,p.next.val= p.next.val,p.val
            p=p.next.next
        return head
        