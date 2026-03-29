class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(r, c, i):
            # base cases (aka, returning True/False)
            # reached end of word, return True
            if i == len(word):
                return True
            
            # 4 cases where we return False
            if (r < 0 or c < 0 or # index out of bounds
                r >= ROWS or c >= COLS or # index out of bounds
                board[r][c] != word[i] or # letter in board does not match word[i]
                (r, c) in path # already visited this cell
            ):
                return False
            
            # recursive case
            # if we reached this step, it means board[r][c] is a match
            path.add((r, c))
            
            # checking all 4 adjacent cells
            # if any of these is a match, then res will be True
            res = (backtrack(r, c+1, i+1) or
                backtrack(r, c-1, i+1) or
                backtrack(r+1, c, i+1) or
                backtrack(r-1, c, i+1)
            )

            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0): return True
        
        return False

            

