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
        arr = [root]
        i = 0
        level = 0
        no_of_nodes = 1
        prev = -1
        while arr:
            d = arr[i]
            no_of_nodes -= 1
            if not d:
                arr.append(None)
                arr.append(None)
            else:
                arr.append(d.left)
                arr.append(d.right)
            if no_of_nodes == 0:
                if level % 2 == 0:
                    row = arr[prev + 1:prev + 2**level + 1]
                else:
                    row = arr[prev + 2**level : prev : -1]
                temp = []
                for node in row:
                    if node:
                        temp.append(node.val)
                result.append(temp)
                prev = i
                level += 1
                no_of_nodes = 2**level
                if not any(arr[i+1:]):
                    break
            i += 1
        
        return result
            
        