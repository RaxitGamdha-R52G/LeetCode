# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        l_d = self.depth(root.left)
        r_d = self.depth(root.right)
        if abs(l_d-r_d) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self,root):
        if not root:
            return 0
        l_d = self.depth(root.left)
        r_d = self.depth(root.right)
        return 1 + max(l_d,r_d)
        
        
        