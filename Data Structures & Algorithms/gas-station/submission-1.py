class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def dfs(i, fuel):
            if start == 3:
                print(f'i: {i}, fuel: {fuel}')
            # base cases
            if i == len(gas): return start
            if fuel < 0: return -1
            if i == len(gas) - 1:
                if fuel >= 0: return start
                else: return -1
            
            # recursive cases
            return dfs(i+1, fuel + dummy_gas[i+1] - dummy_cost[i+1])
        
        for i in range(len(gas)):
            dummy_gas = gas[i:] + gas[:i]
            dummy_cost = cost[i:] + cost[:i]
            print(f'dummy_gas: {dummy_gas}, dummy_cost: {dummy_cost}')
            start = i
            ans = dfs(0, dummy_gas[0] - dummy_cost[0])
            print(f'start: {start}, ans: {ans}')
            if ans != -1: return ans
        
        return -1