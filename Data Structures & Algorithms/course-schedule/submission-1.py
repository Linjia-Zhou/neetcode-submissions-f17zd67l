from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        for a, b in prerequisites:
            d[a].append(b)

        # check for cycle
        def dfs(course) -> bool:
            if states[course] == VISITED: return True
            if states[course] == VISITING: return False

            states[course] = VISITING

            for prereq in d[course]:
                if not dfs(prereq): return False
            
            states[course] = VISITED
            return True


        for course in range(numCourses):
            if not dfs(course): return False
        
        return True

