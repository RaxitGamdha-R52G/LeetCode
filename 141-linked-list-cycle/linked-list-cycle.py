# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        p=head
        q=head.next.next
        while  q!=None:
            if p == q :return True
            p=p.next
            if q.next is None:
                return False
            q=q.next.next
        return False
