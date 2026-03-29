from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # find all UNSURROUNDED cells and change them to "T" (temporary)
        for r in range(ROWS):
            for c in range(COLS):
                # check if we are at a bordering cell
                if board[r][c] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    dfs(r, c)
        
        # now that we have found all unsorrounded cells and changed them to "T", 
        # we guarantee that any remaining O's must be surrounded
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O': board[r][c] = 'X'
                if board[r][c] == 'T': board[r][c] = 'O'
