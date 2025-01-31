# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            rightmost = None
            for i in range(size):
                n = queue.popleft()
                rightmost = n
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            res.append(rightmost.val)
        
        return res