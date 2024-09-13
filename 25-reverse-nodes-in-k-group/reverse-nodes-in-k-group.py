# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k<2:
            return head
        dummy = ListNode("_")
        dummy.next = head
        p = dummy
        r = head
        count = 0
        q = r
        while q != None:
            if count == k-1:
                jp = r
                prev = r
                r = r.next
                for i in range(k-1):
                    temp = r
                    r = r.next
                    temp.next = prev
                    prev = temp
                p.next = prev
                p = jp
                jp.next = r
                q = r

                count = 1
            else:
                count += 1
            if q:
                q = q.next
        return dummy.next 