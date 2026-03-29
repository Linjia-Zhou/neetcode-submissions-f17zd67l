from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def helper(root, check):
            if root.val >= check: self.count += 1
            
            if root.left: helper(root.left, max(check, root.val))

            if root.right: helper(root.right, max(check, root.val))

        helper(root, root.val)
        return self.count


                    
