"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        temp = root
        queue = deque([temp])

        while queue:
            level = len(queue)
            prev = Node(0)
            for i in range(level ):
                node = queue.popleft()
                
                prev.next = node
                prev = prev.next

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            prev.next = None
        
        return root
        
        