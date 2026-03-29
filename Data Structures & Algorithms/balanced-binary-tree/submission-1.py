# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = [True]

        def height(root):
            if not root: return 0

            left = height(root.left)
            right = height(root.right)

            if abs(left-right) > 1: 
                is_balanced[0] = False
                return 0 # don't care about heights anymore, we know this tree is not balanced


            return 1 + max(left, right)

        height(root)
        return is_balanced[0]
