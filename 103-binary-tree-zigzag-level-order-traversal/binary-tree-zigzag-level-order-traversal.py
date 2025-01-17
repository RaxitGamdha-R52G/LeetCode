# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root])

        count = 0
        while queue:
            level_size = len(queue)
            level_nodes = []

            for n in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if count % 2 == 0:
                result.append(level_nodes)
            else:
                result.append(level_nodes[::-1])
            count += 1
        
        return result
            
        