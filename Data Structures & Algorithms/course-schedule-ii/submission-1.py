from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        for a, b in prerequisites:
            d[a].append(b)

        ans = []
        UNVISITED, VISITING, VISITED = 0, 1, 2

        states = [UNVISITED] * numCourses

        def dfs(course):
            if states[course] == VISITED: 
                return True
            if states[course] == VISITING: 
                return False

            states[course] = VISITING

            for prereq in d[course]:
                if not dfs(prereq): 
                    return False
            
            states[course] = VISITED
            ans.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return ans
