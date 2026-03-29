# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if curr_root > p, then we know curr_root can't be ancestor of p
        # same as q
        lca = root
        if lca.val == p.val:
            return p
        if lca.val == q.val:
            return q

        if (p.val > lca.val and q.val < lca.val) or (p.val < lca.val and q.val > lca.val):
            return lca

        if (p.val < lca.val) and (q.val < lca.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        if (p.val > lca.val) and (q.val > lca.val):
            return self.lowestCommonAncestor(root.right, p, q)
        
        






        
