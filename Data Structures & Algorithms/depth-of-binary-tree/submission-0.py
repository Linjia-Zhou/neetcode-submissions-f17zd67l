# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        left = self.maxDepth(root.left) # getting the height of the left branch
        right = self.maxDepth(root.right) # getting the height of the right branch
        
        return 1 + max(left, right)