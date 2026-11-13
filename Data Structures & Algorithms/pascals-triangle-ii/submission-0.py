class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]

        # arr = [1 for _ in range(rowIndex + 1)]
        
        # don't ever need to change index 0 or index -1 in arr
        # arr = [1, 1, 1, 1]

        # 0: [1]
        # 1: [1, 1]
        # 2: [1, 2, 1]
        # 3: [1, 3, 3, 1]

        ans = [1, 1]
        row = 2

        while row <= rowIndex:
            temp = [1 for _ in range(row + 1)]

            for i in range(1, row):
                temp[i] = ans[i-1] + ans[i]
            
            ans = temp[:]
            row += 1
        
        return ans




            