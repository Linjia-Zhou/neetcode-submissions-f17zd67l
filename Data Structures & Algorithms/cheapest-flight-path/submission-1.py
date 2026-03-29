import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # solve this layer by layer
        # calculate how much it costs to go from A --> B when k = 1 (one stop)
        # then how much it costs when k = 2 (two stops), and so on
        # this works b/c we guarantee to calculate minimum for one stop
        # then use this minimum to calculate minimum for two stops, and so on

        # we also need to go layer by layer b/c we need to make sure that we don't accidentally 
        # calculate A --> B --> C in one iteration
        # then, we wouldn't be calculating the number of stops accurately
        
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1): # calculate cost to reach destination for every layer/stop
            tmpPrices = prices.copy()

            for s, d, p in flights: # s=source, d=destination, p=price
                if prices[s] == float('inf'): continue # haven't processed this source yet

                tmpPrices[d] = min(tmpPrices[d], prices[s] + p)
            
            prices = tmpPrices
        
        return -1 if prices[dst] == float('inf') else prices[dst]

        




