class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        paths = collections.defaultdict(list)

        for start, finish in tickets:
            paths[start].append(finish)
        
        print(paths)
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


        '''
        ans, q = [], deque(['JFK']) # must start at JFK
        # start = 'JFK'
        visited = set()

        while q:
            curr_airport = q.popleft()
            ans.append(curr_airport)

            for airport in sorted(paths[curr_airport]):
                if (curr_airport, airport) not in visited:
                    q.append(airport)

                visited.add((curr_airport, airport)) # this may need to be moved somewhere else
            
            # when do i know to append to ans? 
            # feel like i need another loop or data structure or smt

        # paths = {HOU: [JFK], SEA: [JFK], JFK: [SEA, HOU]}
        # curr_airport = SEA
        # visited = ((JFK, HOU), (JFK, SEA), (HOU, JFK), (SEA, JFK))
        # q = [JFK]
        # ans = [JFK, HOU, SEA, JFK]
        '''

