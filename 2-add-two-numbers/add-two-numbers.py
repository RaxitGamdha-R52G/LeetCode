# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q=None
        c=0
        while l1!=None or l2!=None:
            if l1 is None:
                p=0
            else:
                p=l1.val
                l1=l1.next
            if l2 is None:
                r=0
            else:
                r=l2.val
                l2=l2.next
            s=p+r+c
            c=s//10 if s>9 else 0
            s%=10
            
            d=ListNode(s)
            if q is None:
                q=d
                g=d
            else:
                g.next=d
                g=g.next
        
        if c>0:
            g.next=ListNode(c)
            g=g.next
        return q
            
            