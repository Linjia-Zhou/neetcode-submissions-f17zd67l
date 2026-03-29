from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        ans = []
        queue = deque([root])

        while queue:
            rightMost = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    rightMost = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightMost: ans.append(rightMost.val)
            
        return ans














        '''
        ans = []

        def rightTraverse(root):
            if not root: return []
            
            ans.append(root.val)

            if (not root.right) and (root.left):
                return rightTraverse(root.left)

            return rightTraverse(root.right)
        
        rightTraverse(root)
        return ans
        '''



        