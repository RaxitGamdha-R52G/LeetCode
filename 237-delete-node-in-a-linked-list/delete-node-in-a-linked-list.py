# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
            prev = node
            node = node.next
            while node.next:
                prev.val = node.val
                prev = node
                node = node.next
            prev.val = node.val
            prev.next = None

        