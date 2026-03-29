class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (index, buying/selling): max_profit

        def dfs(i, buying):
            if i >= len(prices): return 0
            if (i, buying) in dp: return dp[(i, buying)]

            if buying:
                buy = dfs(i+1, False) - prices[i]
                nothing = dfs(i+1, True)
                dp[(i, buying)] = max(buy, nothing)
            else:
                sell = dfs(i+2, True) + prices[i]
                nothing = dfs(i+1, False)
                dp[(i, buying)] = max(sell, nothing)
            
            return dp[(i, buying)]
        
        return dfs(0, True)


            
            

        

            