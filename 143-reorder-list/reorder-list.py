# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next
        
        p = head
        i = 0
        j = len(arr)-1
        while i<=j:
            if i != j:
                p.val = arr[i]
                p = p.next
            p.val = arr[j]
            p = p.next
            i += 1
            j -= 1
        