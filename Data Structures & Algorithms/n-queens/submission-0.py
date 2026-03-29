class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.'] * n for _ in range(n)]
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                ans.append(copy)
                return
            
            for c in range(n):
                if (r+c in posDiag) or (r-c in negDiag) or (c in cols):
                    # this means the current square is not valid for queen placement
                    continue 
                
                board[r][c] = 'Q'
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backtrack(r+1)

                board[r][c] = '.'
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        backtrack(0)
        return ans