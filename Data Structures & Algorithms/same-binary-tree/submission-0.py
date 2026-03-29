# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bal = True

        if not p and not q: 
            bal = True
            return bal

        if (p and not q) or (q and not p): 
            bal = False
            return bal

        if p.val != q.val: 
            bal = False
            return bal
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return bal

