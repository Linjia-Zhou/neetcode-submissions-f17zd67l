class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what makes a valid tree?
        # 1. no cycles
        # 2. fully connected

        par = list(range(n))
        rank = [1] * n

        def find(node):
            if par[node] != node:
                return find(par[node])
            
            return par[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2: return False

            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        # failures:
        # if union(n1, n2) finds that n1, n2 have the same parent, then we have found a cycle
        # if len(visited) !=, then graph isn't connected

        for n1, n2 in edges:
            if not union(n1, n2): return False
        
        return len(edges) == n-1