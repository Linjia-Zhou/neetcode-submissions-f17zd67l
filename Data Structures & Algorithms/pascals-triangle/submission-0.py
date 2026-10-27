class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(numRows - 1):
            curr = [1 for _ in range(len(ans[i]) + 1)]

            for j in range(1, len(curr) - 1):
                curr[j] = ans[i][j-1] + ans[i][j]
            
            ans.append(curr)
        
        return ans



