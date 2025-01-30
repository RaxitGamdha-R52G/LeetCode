# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
        nums = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8]

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            val = curr.val << 1
            prev.val += carry[val]
            curr.val = nums[val]
            prev = curr
            curr = curr.next
        
        return head if dummy.val == 0 else dummy
        