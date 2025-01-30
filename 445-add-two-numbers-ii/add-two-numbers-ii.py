# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        p = l1
        while p:
            stack1.append(p.val)
            p = p.next
        
        stack2 = []
        p = l2
        while p:
            stack2.append(p.val)
            p = p.next
        
        prev = None
        carry = 0
        while stack1 or stack2:
            val = 0
            if stack1:
                val += stack1.pop()
            if stack2:
                val += stack2.pop()
            
            val += carry
            carry = val // 10
            val = val % 10

            n = ListNode(val)
            n.next = prev
            prev = n
        

        if carry:
            n = ListNode(carry)
            n.next = prev
            prev = n
        return prev