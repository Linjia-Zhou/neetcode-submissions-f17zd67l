class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom-up approach
        coins.sort()
        dp = [0] * (amount+1) # need amount+1 b/c we want to include 0 as well

        for i in range(1, amount + 1): # looping through dp, finding min coins for 0, 1, 2, 3, etc.
            minn = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0: # since coins is sorted, this means all remaining values are too big
                    break
                
                minn = min(minn, 1 + dp[diff]) # need to add one since we're using a coin here (diff = i - coin)

            dp[i] = minn
        
        if dp[amount] < float('inf'): return dp[amount]
        else: return -1


        


        