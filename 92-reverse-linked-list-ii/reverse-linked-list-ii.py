# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode('1')
        dummy.next = head
        v=dummy
        count = 0
        p=head
        while p:
            count += 1
            if left <= count <= right:
                
                q = p
                for i in range(left,right):
                    p = p.next
                d=p.next
                
                while p != q:
                    prev = q
                    q = q.next
                    prev.next = d
                    d = prev
                p.next = d
                v.next = p
                break
                
            else:
                v=p
                p=p.next
        return dummy.next