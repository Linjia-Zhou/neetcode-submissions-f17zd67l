class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # intuition: what if we popped nums[i] last? 
        # then, we guarantee that max coins is 1 * nums[i] * 1
        # we can also split nums into 2 subproblems --> left subarray and right subarray
        
        # ex. nums = [4, 2, 3, 7]
        # if we assume popping nums[1] last, max coins for the last pop is 2
        # we also guarantee that nums[1] will always be available for coin counting
        # left_array = [1] + [4] = [1, 4]
        # right_array = [3, 7] + [1] = [3, 7, 1]
        # recursively loop through left and right arrays to find max of each if we pop i last


        nums = [1] + nums + [1]

        memo = {} 

        def dfs(l, r):
            if l > r: return 0 # array is empty
            if (l, r) in memo: return memo[(l, r)]

            memo[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1] # popping i last
                coins += dfs(l, i-1) + dfs(i+1, r)
                memo[(l, r)] = max(memo[(l, r)], coins)
            
            return memo[(l, r)]

        return dfs(1, len(nums)-2)

