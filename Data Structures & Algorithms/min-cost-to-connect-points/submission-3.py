import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # use prim's algorithm to form a MST
        # start at a node, we know we need to connect all nodes (since we're creating a tree)
        # then, we should connect the closest node to the starting node
        # now we have 2 nodes in our tree
        # find the next closest node that will connect to either of the 2 nodes
        # and so on...
        ans = 0
        visited = set()
        min_heap = [(0, 0)] # [distance, index]

        while len(visited) < len(points):
            dist, i = heapq.heappop(min_heap)
            
            if i in visited: continue
            else: visited.add(i)

            ans += dist # we added this node to visited, so we're gonna use it
            xi, yi = points[i]

            for j in range(len(points)):
                if i == j: continue
                if j not in visited: 
                    xj, yj = points[j]
                    i_to_j = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (i_to_j, j))
        
        return ans




