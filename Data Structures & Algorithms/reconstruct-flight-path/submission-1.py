class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        paths = collections.defaultdict(list)

        for start, finish in tickets:
            paths[start].append(finish)
        
        ans = ['JFK']

        def dfs(start):
            if len(ans) == len(tickets) + 1: # found a valid path
                return True
            
            if start not in paths:
                return False

            for i, nei in enumerate(paths[start]):
                paths[start].pop(i)
                ans.append(nei)

                if dfs(nei): return True

                paths[start].insert(i, nei)
                ans.pop()
            
            return False
        
        dfs('JFK')
        return ans