# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        x = lambda a,b: f"{a}->{b}"
        
        def dfs(root):
            arr = []
            if root:
                path = str(root.val)
                if root.left:
                    arr += [x(path,i) for i in dfs(root.left)]
                if root.right:
                    arr += [x(path,i) for i in dfs(root.right)]
                if not (root.left or root.right):
                    arr.append(path)
            return arr
        return dfs(root)
        