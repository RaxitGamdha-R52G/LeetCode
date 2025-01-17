# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        self.prev = None

        def traverse(root):
            if not root:
                return
            
            traverse(root.right)
            traverse(root.left)

            root.right = self.prev
            root.left = None
            self.prev = root

        traverse(root)    