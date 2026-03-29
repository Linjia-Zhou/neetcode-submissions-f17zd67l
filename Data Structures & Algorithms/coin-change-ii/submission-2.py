class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} # (index, current sum): count (eventually this is the answer)

        def dfs(i, a):
            # base cases
            if a == amount: return 1
            if i == len(coins) or a > amount: return 0
            if (i, a) in memo: return memo[(i, a)]
            
            # recursive case
            memo[(i, a)] = dfs(i, a+coins[i]) + dfs(i+1, a)
            return memo[(i, a)]

        return dfs(0, 0)

            

            

            
