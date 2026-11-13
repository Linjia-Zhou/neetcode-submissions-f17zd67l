class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]

        ans = [1, 1]
        row = 2

        while row <= rowIndex:
            temp = ans[:] + [1]

            for i in range(1, row):
                temp[i] = ans[i-1] + ans[i]
            
            ans = temp[:]
            row += 1
        
        return ans




            