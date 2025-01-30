# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        
        if not head or not head.next:
            return head
        p = head  

        while p and p.next:
            q = p.next  
            val = gcd(p.val, q.val)
            new_node = ListNode(val)
            new_node.next = q
            p.next = new_node
            p = q
        
        return head