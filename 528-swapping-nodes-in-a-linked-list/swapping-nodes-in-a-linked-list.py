# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front=None
        last=None
        p=q=head

        for i in range(k-1):
            p=p.next
        front=p
        while(p.next!=None):
            p=p.next
            q=q.next
        last= q
        front.val,last.val=last.val,front.val
        return head