# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        
        prev = None
        curr = head
        for _ in range(k):
            nex_t = curr.next
            curr.next = prev
            prev = curr
            curr = nex_t
        
        head.next = self.reverseKGroup(curr,k)
        head = prev
        return head
        