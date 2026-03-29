from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        p_que, a_que = deque(), deque() # queues for pacific and atlantic
        p_seen, a_seen = set(), set()

        # initialize queues and sets with border values 
        for c in range(COLS):
            p_que.append((0, c))
            p_seen.add((0, c))
        
        for r in range(1, ROWS):
            p_que.append((r, 0))
            p_seen.add((r, 0))

        for c in range(COLS):
            a_que.append((ROWS-1, c))
            a_seen.add((ROWS-1, c))
        
        for r in range(ROWS-1):
            a_que.append((r, COLS-1))
            a_seen.add((r, COLS-1))
        
        # get coordinates of all cells that can flow to current cells in queue
        # at the end, set seen will have all the valid coords that can flow to pacific or atlantic
        def get_coords(que, seen):
            while que:
                r, c = que.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                        que.append((nr, nc))
                        seen.add((nr, nc))
        
        get_coords(p_que, p_seen) # p_seen has all coords that can flow into pacific
        get_coords(a_que, a_seen) # a_seen has all coords that can flow into atlantic

        # return intersection of p_seen and a_seen to get all coords that can flow into both oceans
        return list(p_seen.intersection(a_seen))

