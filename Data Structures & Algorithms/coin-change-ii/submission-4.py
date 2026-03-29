class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # claude conversation link explaining this problem: https://claude.ai/share/dc43847d-b6d3-49b8-9324-7889c537003a

        memo = {} # (i, a): count 
        # i → which coin we're currently deciding to use (index into coins)
        # a → the running sum we've accumulated so far
        # aka, (i, a) represents all the possible sums (a_1, a_2,..., a_n) we can generate from index i

        # count → number of ways to reach amount from this exact state

        

        def dfs(i, a):
            if i >= len(coins) or a > amount: return 0
            if a == amount: return 1
            if (i, a) in memo: return memo[(i, a)]

            memo[(i, a)] = dfs(i, a + coins[i]) + dfs(i+1, a)
            return memo[(i, a)]
        
        return dfs(0, 0)
            
            




            
