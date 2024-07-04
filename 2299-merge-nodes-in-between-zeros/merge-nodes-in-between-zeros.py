# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        d = dummy
        p = head
        q = head.next
        s = 0
        while q !=None:
            if q.val == 0:
                d.next = ListNode(s)
                s = 0
                p = q
                d = d.next
            else:
                s+= q.val
            q = q.next
        return dummy.next
        