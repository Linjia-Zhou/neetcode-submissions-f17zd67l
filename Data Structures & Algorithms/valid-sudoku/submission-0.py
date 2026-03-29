from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # key = number in sudoku
        # value = index of number in board
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        # ROWS TO DICT
        for i, row in enumerate(board): # i = index of row, row = nested list in board
            for j, num in enumerate(row): # j = index of number in row, num = number in row
                # print(f"row: {i} col: {j} number: {num}")
                if num == '.':
                    continue
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)

                if num in cols[j]:
                    return False
                else:
                    cols[j].add(num)

                box_i = i // 3
                box_j = j // 3
                key = (box_i, box_j)

                if num in boxes[key]:
                    return False
                else:
                    boxes[key].add(num)
                
        return True


        
                
        
        


