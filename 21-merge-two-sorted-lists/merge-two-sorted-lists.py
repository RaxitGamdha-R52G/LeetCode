# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=None

        while list1!=None or list2!=None:
            q=list1 if list1 is not None else "__"
            p=list2 if list2 is not None else "__"
            if (q=="__" ) or (p!="__" and p.val<=q.val):
                Node=p
                list2=list2.next
            else:
                Node=q
                list1=list1.next
            if list3==None:
                list3=Node
                list3_e=Node
            else:
                list3_e.next=Node
                list3_e=list3_e.next
        
        return list3

                
        