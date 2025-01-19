# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Solution 1
    #     if len(lists) == 0:
    #         return None
    #     elif len(lists) == 1:
    #         return lists[0]
    #     for i in range(len(lists)-1,0,-1):
    #         lists[i-1] = self.List(lists[i],lists[i-1])
    #     return lists[0]


    
    # def List(self,list1,list2):
    #     if not list1:
    #         return list2
    #     if not list2:
    #         return list1
    #     if list1.val < list2.val:
    #         list1.next = self.List(list1.next,list2)
    #         return list1
    #     else:
    #         list2.next = self.List(list1,list2.next)
    #         return list2
        
        # Solution 2
        min_heap = []
        for lst in lists:
            while lst:
                heapq.heappush(min_heap,lst.val)
                lst = lst.next
        
        dummy = ListNode(0)
        temp = dummy

        while min_heap:
            temp.next = ListNode(heapq.heappop(min_heap))
            temp = temp.next
        return dummy.next