from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))

                if grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0: return fresh_count
        
        while queue and fresh_count > 0:
            queue_size = len(queue)

            # we want to process all rotten oranges at current minute --> aka, we need to process every single pair in the current queue
            for _ in range(queue_size):
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
                
            # only increment minutes if we rotted something (aka queue is not empty)
            # we only add to queue if we successfully rotted a fruit, so if queue is empty, it means we didn't rot any fruit
            if queue: minutes += 1
        
        return minutes if fresh_count == 0 else -1
        
                