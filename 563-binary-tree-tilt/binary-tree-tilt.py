# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        d = 0
        v = 0
        if root:
            l_d = self.bsum(root.left)
            r_d = self.bsum(root.right)
            d = abs(l_d - r_d)
            v = self.findTilt(root.left) + self.findTilt(root.right)

        return  d + v
    
    def bsum(self,root):
        d = 0
        v = 0
        if root:
            d = root.val
            v = self.bsum(root.left) + self.bsum(root.right)
        return d + v
            
        