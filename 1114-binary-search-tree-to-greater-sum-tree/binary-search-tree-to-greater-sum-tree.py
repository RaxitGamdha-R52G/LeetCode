# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    b = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            root.right = self.bstToGst(root.right)
            root.val += self.b
            self.b = root.val
            root.left = self.bstToGst(root.left)
        return root
        
        