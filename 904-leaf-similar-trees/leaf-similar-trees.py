# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def root_leaf(root):
            result=[]
            if root :
                if  not root.left and not root.right:
                    return [root.val]
                result.extend(root_leaf(root.left))
                result.extend(root_leaf(root.right))
            return result
        
        root1_leaves = root_leaf(root1)
        root2_leaves = root_leaf(root2)

        return root1_leaves == root2_leaves