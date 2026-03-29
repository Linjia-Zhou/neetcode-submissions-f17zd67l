import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # trying to find a minimum path in the grid --> minheap?
        # within that minimum path, return the maximum value

        min_heap = [(grid[0][0], 0, 0)] # (value, i, j)
        path = []
        visited = set() # set of (i, j)
        ROWS, COLS = len(grid), len(grid[0])

        while min_heap:
            val, i, j = heapq.heappop(min_heap)
            path.append(val)

            if i == ROWS - 1 and j == COLS - 1: break
            
            if (i, j) in visited: continue
            visited.add((i, j))

            if i < ROWS - 1:
                heapq.heappush(min_heap, (grid[i+1][j], i+1, j))
            if i > 0:
                heapq.heappush(min_heap, (grid[i-1][j], i-1, j))
            
            if j < COLS - 1:
                heapq.heappush(min_heap, (grid[i][j+1], i, j+1))
            if j > 0:
                heapq.heappush(min_heap, (grid[i][j-1], i, j-1))
            
        return max(path)
        



