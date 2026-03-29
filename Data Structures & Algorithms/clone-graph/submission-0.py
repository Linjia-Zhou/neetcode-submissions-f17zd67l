"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        o_to_n = {} # map old nodes to new nodes, ex. {1:1, 2:2, 3:3}
        stk = [node] # nodes we need to add to o_to_n
        visited = set()
        visited.add(node)

        # building o_to_n
        while stk:
            n = stk.pop()
            o_to_n[n] = Node(val=n.val)

            for nei in n.neighbors:
                if nei not in visited:
                    stk.append(nei)
                    visited.add(nei)
        
        # connecting new nodes together
        for old_node, new_node in o_to_n.items(): # key-value pairs
            for nei in old_node.neighbors:
                new_nei = o_to_n[nei] # remember to copy new Node (value), not the old Node (key)
                new_node.neighbors.append(new_nei)
        
        return o_to_n[node]
        


            