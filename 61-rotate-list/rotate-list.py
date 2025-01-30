# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if head is None or head.next is None:
        #     return head
        # count = 0
        # p=head
        # while p != None:
        #     count += 1
        #     p=p.next
        # if k> count :
        #     k=k%count
        # for i in range(k):
        #     p=head
        #     q=None
        #     temp=None
        #     while p.next != None:
        #         q=p
        #         p=p.next
        #     temp = p
        #     q.next=None
        #     temp.next=head
        #     head=temp
        # return head

        p = head
        count = 0
        while p:
            p = p.next
            count += 1
        
        if (count ==0):
            return None
        k = k %count
        if (k == 0):
            return head
        
        p = head
        for i in range(k):
            p = p.next
        
        q = head
        while p.next:
            q = q.next
            p = p.next
        temp = q.next
        q.next = None
        p = head
        head = temp
        while temp.next:
            temp = temp.next
        temp.next = p
        return head
        

        