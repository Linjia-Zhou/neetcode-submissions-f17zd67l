class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list) # {node: [(distance, neighbour node)]}

        for u, v, d in times:
            edges[u].append((d, v))
        
        min_heap = [(0, k)] # (aggregate distance, node)
        visited = set()
        ans = 0

        while min_heap:
            curr_d, node = heapq.heappop(min_heap)
            
            if node in visited:
                continue

            visited.add(node)
            ans = max(ans, curr_d)

            for d, nei in edges[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (curr_d + d, nei))
            
            
        if len(visited) == n: return ans
        else: return -1


        
