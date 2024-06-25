# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        b = nums.index(max(nums))
        root = TreeNode(nums[b])
        if b != len(nums)-1:
            root.right = self.constructMaximumBinaryTree(nums[b+1:])
        root.left = self.constructMaximumBinaryTree(nums[:b])
        return root         