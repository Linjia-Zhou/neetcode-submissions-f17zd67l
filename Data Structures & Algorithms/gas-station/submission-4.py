class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def dfs(i, fuel):
            # base cases
            if i == len(gas) - 1:
                if fuel >= 0: return start
                else: return -1
            if fuel < 0: return -1
            
            # recursive cases
            return dfs(i+1, fuel + dummy_gas[i+1] - dummy_cost[i+1])
        
        for i in range(len(gas)):
            dummy_gas = gas[i:] + gas[:i]
            dummy_cost = cost[i:] + cost[:i]
            start = i
            ans = dfs(0, dummy_gas[0] - dummy_cost[0])
            if ans != -1: return ans
        
        return -1