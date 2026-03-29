class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (i, t): count
        # i: index
        # t: sum we can reach from index
        # count: number of ways we can reach target from (i, t)

        def dfs(i, t):
            # print(f'i: {i}, t: {t}, memo: {memo}')
            if i == len(nums):
                if t == target:
                    # print('base case: target found')
                    return 1
                else:
                    return 0
                
            if (i, t) in memo: 
                # print('base case: (i, t) in memo')
                return memo[(i, t)]

            memo[(i, t)] = dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
            
            return memo[(i, t)]

        return dfs(0, 0)
