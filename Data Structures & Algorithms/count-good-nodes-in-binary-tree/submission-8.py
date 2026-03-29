# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def helper(r, curr_max):
            if not r: 
                return self.count

            if r.val >= curr_max: 
                self.count += 1
                curr_max = r.val
                
            return helper(r.left, curr_max) and helper(r.right, curr_max)
        
        return helper(root, root.val)
