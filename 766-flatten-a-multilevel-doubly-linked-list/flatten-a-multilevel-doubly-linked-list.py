"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.prev = None
        def traverse(node):
            if not node:
                return 
            traverse(node.next)
            traverse(node.child)

            node.next = self.prev
            if self.prev:
                self.prev.prev = node
            node.child = None
            self.prev = node
        
        traverse(head)
        return head