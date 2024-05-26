# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        count = 0
        p=head
        while p != None:
            count += 1
            p=p.next
        if k> count :
            k=k%count
        for i in range(k):
            p=head
            q=None
            temp=None
            while p.next != None:
                q=p
                p=p.next
            temp = p
            q.next=None
            temp.next=head
            head=temp
        return head


        