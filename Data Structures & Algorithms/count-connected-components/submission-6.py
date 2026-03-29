from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        d = defaultdict(list)
        visited = set()

        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        
        def dfs(edge):
            for nei in d[edge]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        for edge in range(n):
            if edge not in visited:
                visited.add(edge)
                dfs(edge)
                count += 1

        return count