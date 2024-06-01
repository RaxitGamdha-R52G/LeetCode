# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        nodes = []
        p=head
        while p:
            nodes.append(p.val)
            p=p.next
        
        return self.BST(nodes)
        
    
    def BST(self,arr):
        if arr == []:
            return None
        left = 0
        right = len(arr)
        mid = (left+right) //2
        root = TreeNode(arr[mid])
        root.left = self.BST(arr[:mid])
        if len(arr)>2:
            root.right = self.BST(arr[mid+1:])
        return root
            