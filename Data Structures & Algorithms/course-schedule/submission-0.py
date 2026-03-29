from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for a, b in prerequisites:
            d[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(course):
            # if we have fully visited course, we know that there is no problem with it
            if states[course] == VISITED: return True

            # this indicates that we have a cycle, which is a problem
            if states[course] == VISITING: return False

            # else, we have not visited this course yet
            states[course] = VISITING

            # check the prereqs (neighbours) of the current course
            for nei in d[course]:
                if not dfs(nei): return False
            
            # if we got through the for loop, that means all prereqs of current course are valid, so current course is valid
            states[course] = VISITED
            return True


        # go through every course and check if it's valid
        for i in range(numCourses):
            # if dfs is not true, then we know there is a problem
            if not dfs(i): return False
        
        return True


