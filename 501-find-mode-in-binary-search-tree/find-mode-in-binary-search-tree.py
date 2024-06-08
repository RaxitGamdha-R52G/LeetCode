# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def findNode(root):

            d=[]
            if not root:
                return d
            d.append(root.val)
            d.extend(findNode(root.left))
            d.extend(findNode(root.right))
            return d
        
        arr= findNode(root)
        mode = float('-inf')
        l = []
        for i in set(arr):
            d = arr.count(i)
            if d > arr.count(mode):
                mode = i
                l = [i]
            elif d == arr.count(mode):
                l.append(i)
        return l

            