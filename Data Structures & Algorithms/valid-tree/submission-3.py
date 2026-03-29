from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n-1): return False

        d = defaultdict(list)
        visited = set()

        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        
        def dfs(node, prev):
            if node in visited: return False

            visited.add(node)

            if node not in d: return True # reached the end of the tree (node has no children)

            for nei in d[node]:
                if nei == prev: continue # avoiding double-checking
                if not dfs(nei, node): return False

            return True

        return dfs(0, -1) and len(visited) == n
