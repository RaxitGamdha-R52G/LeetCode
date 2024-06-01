# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p=head
        q = head.next
        v= ListNode('1')
        v.next = head
        r = v
        while q:
            flag=0
            while q and p.val == q.val:
                q = q.next
                flag = 1
            if flag:
                r.next = q
            else:
                r=p
            p=q
            if q:
                q=q.next

        return v.next